from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# 1. إعدادات الـ DAG
default_args = {
    'owner': 'Khalid_DE',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'khalid_pipeline_orchestration',
    default_args=default_args,
    description='Orchestrating Data from Silver to Gold in ClickHouse',
    schedule_interval='@hourly', # تشغيل كل ساعة
    catchup=False
) as dag:

    # 2. مهمة التأكد من اتصال ClickHouse
    check_clickhouse = BashOperator(
        task_id='check_clickhouse_connectivity',
        bash_command='clickhouse-client -q "SELECT 1"'
    )

    # 3. مهمة نقل البيانات للطبقة الذهبية (Aggregations)
    refresh_gold_users = BashOperator(
        task_id='refresh_user_stats_gold',
        bash_command="""
        clickhouse-client -q "
        INSERT INTO default.gold_user_stats 
        SELECT 
            toDate(now()) as event_date,
            count(user_id) as total_users
        FROM default.silver_users;"
        """
    )

    # 4. ترتيب المهام
    check_clickhouse >> refresh_gold_users
