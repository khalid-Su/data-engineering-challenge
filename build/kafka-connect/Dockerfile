FROM quay.io/strimzi/kafka:0.46.0-kafka-4.0.0
USER root:root
RUN mkdir -p /opt/kafka/plugins/debezium
# تحميل موصلات Debezium المتوافقة
RUN curl https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/2.7.3.Final/debezium-connector-postgres-2.7.3.Final-plugin.tar.gz | tar xz -C /opt/kafka/plugins/debezium && \
    curl https://repo1.maven.org/maven2/io/debezium/debezium-connector-mongodb/2.7.3.Final/debezium-connector-mongodb-2.7.3.Final-plugin.tar.gz | tar xz -C /opt/kafka/plugins/debezium
USER 1001
