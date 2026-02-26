# Real-time Data Engineering Challenge 🚀

This repository contains an end-to-end data pipeline solution using a **Medallion Architecture** (Bronze, Silver, Gold).

## 🛠 Tech Stack
- Source DBs: PostgreSQL & MongoDB
- Streaming: Kafka & Debezium (CDC)
- Warehouse: ClickHouse
- Orchestration: Apache Airflow
- Environment: Kubernetes (K8s)

## 🏗 Pipeline Flow
1. CDC: Debezium tracks changes in Postgres and Mongo.
2. Streaming: Changes are published to Kafka topics.
3. Ingestion: ClickHouse Kafka Engine consumes raw data.
4. Transformation: Materialized Views transform raw data into Silver & Gold layers.
5. Orchestration: Airflow schedules final data quality checks.

## 🚀 How to Run
1. Apply K8s Manifests: `kubectl apply -f k8s/`
2. Deploy Connectors: ```bash
   curl -X POST -H "Content-Type: application/json" --data @connectors/postgres-connector.json http://localhost:8083/connectors
