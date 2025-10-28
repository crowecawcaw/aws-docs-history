# Using Apache Hudi with Apache Flink

Apache Hudi is an open-source data management framework with record-level operations such as insert, update, upsert, and delete that
you can use to simplify data management and data pipeline development. When combined with efficient data management in Amazon S3,
Hudi lets you ingest and update data in real time. Hudi maintains metadata of all of the operations that you run
on the dataset, so all of the actions remain atomic and consistent.

Apache Hudi is available on Amazon EMR on EKS with Apache Flink with Amazon EMR releases 7.2.0 and higher. See the following
steps to learn how to get started and submit Apache Hudi jobs.

## Submit an Apache Hudi job

See the following steps to learn how to submit an Apache Hudi job.

1. Create an AWS Glue database named `default`.

```
aws glue create-database --database-input "{\"Name\":\"default\"}"
```

2. Follow the [Flink Kubernetes Operator SQL Example](https://github.com/apache/flink-kubernetes-operator/tree/main/examples/flink-sql-runner-example "https://github.com/apache/flink-kubernetes-operator/tree/main/examples/flink-sql-runner-example") to build the `flink-sql-runner.jar` file.
3. Create a Hudi SQL script like the following.

```
CREATE CATALOG hudi_glue_catalog WITH (
'type' = 'hudi',
'mode' = 'hms',
'table.external' = 'true',
'default-database' = 'default',
'hive.conf.dir' = '/glue/confs/hive/conf/',
'catalog.path' = 's3://`<hudi-example-bucket>`/FLINK_HUDI/warehouse/'
);

USE CATALOG hudi_glue_catalog;
CREATE DATABASE IF NOT EXISTS hudi_db;
use hudi_db;

CREATE TABLE IF NOT EXISTS hudi-flink-example-table(
    uuid VARCHAR(20),
    name VARCHAR(10),
    age INT,
    ts TIMESTAMP(3),
    `partition` VARCHAR(20)
)
PARTITIONED BY (`partition`)
WITH (
  'connector' = 'hudi',
  'path' = 's3://`<hudi-example-bucket>`/hudi-flink-example-table',
  'hive_sync.enable' = 'true',
  'hive_sync.mode' = 'glue',
  'hive_sync.table' = 'hudi-flink-example-table',
  'hive_sync.db' = 'hudi_db',
  'compaction.delta_commits' = '1',
  'hive_sync.partition_fields' = 'partition',
  'hive_sync.partition_extractor_class' = 'org.apache.hudi.hive.MultiPartKeysValueExtractor',
  'table.type' = 'COPY_ON_WRITE'
);

EXECUTE STATEMENT SET
BEGIN

INSERT INTO hudi-flink-example-table VALUES
    ('id1','Alex',23,TIMESTAMP '1970-01-01 00:00:01','par1'),
    ('id2','Stephen',33,TIMESTAMP '1970-01-01 00:00:02','par1'),
    ('id3','Julian',53,TIMESTAMP '1970-01-01 00:00:03','par2'),
    ('id4','Fabian',31,TIMESTAMP '1970-01-01 00:00:04','par2'),
    ('id5','Sophia',18,TIMESTAMP '1970-01-01 00:00:05','par3'),
    ('id6','Emma',20,TIMESTAMP '1970-01-01 00:00:06','par3'),
    ('id7','Bob',44,TIMESTAMP '1970-01-01 00:00:07','par4'),
    ('id8','Han',56,TIMESTAMP '1970-01-01 00:00:08','par4');

END;
```

4. Upload your Hudi SQL script and the `flink-sql-runner.jar` file to an S3 location.
5. In your `FlinkDeployments` YAML file, set `hudi.enabled` to `true`.

```
spec:
  flinkConfiguration:
    hudi.enabled: "true"
```

6. Create a YAML file to run your configuration. This example file is named `hudi-write.yaml`.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: hudi-write-example
spec:
  flinkVersion: v1_18
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    hudi.enabled: "true"
  executionRoleArn: "`<JobExecutionRole>`"
  emrReleaseLabel: "emr-7.10.0-flink-latest"
  jobManager:
    highAvailabilityEnabled: false
    replicas: 1
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    jarURI: local:///opt/flink/usrlib/flink-sql-runner.jar
    args: ["/opt/flink/scripts/hudi-write.sql"]
    parallelism: 1
    upgradeMode: stateless
  podTemplate:
    spec:
      initContainers:
        - name: flink-sql-script-download
          args:
            - s3
            - cp
            - s3://`<s3_location>`/hudi-write.sql
            - /flink-scripts
          image: amazon/aws-cli:latest
          imagePullPolicy: Always
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
            - mountPath: /flink-scripts
              name: flink-scripts
        - name: flink-sql-runner-download
          args:
            - s3
            - cp
            - s3://`<s3_location>`/flink-sql-runner.jar
            - /flink-artifacts
          image: amazon/aws-cli:latest
          imagePullPolicy: Always
          resources: {}
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          volumeMounts:
            - mountPath: /flink-artifacts
              name: flink-artifact
      containers:
        - name: flink-main-container
          volumeMounts:
            - mountPath: /opt/flink/scripts
              name: flink-scripts
            - mountPath: /opt/flink/usrlib
              name: flink-artifact
      volumes:
        - emptyDir: {}
          name: flink-scripts
        - emptyDir: {}
          name: flink-artifact
```

7. Submit a Flink Hudi job to the [Flink Kubernetes operator](jobruns-flink-kubernetes-operator.md "jobruns-flink-kubernetes-operator.md").

```
kubectl apply -f hudi-write.yaml
```
