# Partitioning for Non ODP entities

In Apache Spark, partitioning refers to the way data is divided and distributed across the worker nodes in a cluster for parallel processing. Each partition is a logical chunk of data that can be processed independently by a task. Partitioning is a fundamental concept in Spark that directly impacts performance, scalability, and resource utilization. AWS Glue jobs use Spark's partitioning mechanism to divide the dataset into smaller chunks (partitions) that can be processed in parallel across the cluster's worker nodes. Note that partitioning is not applicable for ODP entities.

For more details, see [AWS Glue Spark and PySpark jobs](spark_and_pyspark.md "spark_and_pyspark.md").

**Prerequisites**

An SAP OData’s Object you would like to read from. You will need the object/EntitySet name. For example: `/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder` .

**Example**

```
sapodata_read = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder"
    }, transformation_ctx=key)
```

## Partitioning Queries

### Field Based partitioning

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently. Integer, Date and DateTime fields support field-based partitioning in the SAP OData connector.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field.

For any field whose data type is DateTime, the Spark timestamp format used in Spark SQL queries is accepted.

Examples of valid values:
`"2000-01-01T00:00:00.000Z"`

- `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: number of partitions.
- `PARTITION_BY`: the type partitioning to be performed, `FIELD` to be passed in case of Field based partitioning.

**Example**

```
sapodata= glueContext.create_dynamic_frame.from_options(
    connection_type="sapodata",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "/sap/opu/odata/sap/SEPM_HCM_SCENARIO_SRV/EmployeeSet",
        "PARTITION_FIELD": "validStartDate"
        "LOWER_BOUND": "2000-01-01T00:00:00.000Z"
        "UPPER_BOUND": "2020-01-01T00:00:00.000Z"
        "NUM_PARTITIONS": "10",
        "PARTITION_BY": "FIELD"
    }, transformation_ctx=key)
```

### Record Based partitioning

The original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

Record-based partitioning is only supported for non-ODP entities, as pagination in ODP entities is supported through the next token/skip token.

- `PARTITION_BY`: the type partitioning to be performed. `COUNT` is to be passed in case of record-based partitioning.

**Example**

```
sapodata= glueContext.create_dynamic_frame.from_options(
    connection_type="sapodata",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "/sap/opu/odata/sap/SEPM_HCM_SCENARIO_SRV/EmployeeSet",
        "NUM_PARTITIONS": "10",
        "PARTITION_BY": "COUNT"
    }, transformation_ctx=key)
```
