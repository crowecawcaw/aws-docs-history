# Set up metrics

To monitor the HBase Master, you can set up Amazon CloudWatch Agent to collect specific metrics.

1. **Setting Up HBase Master Metrics** – To monitor the HBase Master, you can set up Amazon CloudWatch Agent to collect specific metrics. Here’s a configuration example
   to track Master assignment manager activities:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "emr-hbase-master-metrics",
        "Properties": {
          "Hadoop:service=HBase,name=Master,sub=AssignmentManager": "AssignFailedCount,AssignSubmittedCount",
          "otel.metric.export.interval": "30000"
        },
        "Configurations": []
      }
    ]
  }
]
```

In this setup:

    * We specify the MBean (`Hadoop:service=HBase,name=Master,sub=AssignmentManager`) to collect metrics like `AssignFailedCount`
     and `AssignSubmittedCount`.
    * We set the interval to collect these metrics every 30 seconds (30000 milliseconds).

2. **Setting Up HBase Region Server Metrics** – To monitor HBase Region Servers, configure the CloudWatch Agent
   as follows:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "emr-hbase-region-server-metrics",
        "Properties": {
          "Hadoop:service=HBase,name=RegionServer,sub=IPC": "numActiveHandler,numActivePriorityHandler",
          "otel.metric.export.interval": "30000"
        },
        "Configurations": []
      }
    ]
  }
]
```

This configuration:

    * Monitors active handlers on the Region Server (`numActiveHandler`, `numActivePriorityHandler`).
    * Uses a 30-second interval for metric collection.

3. **Setting Up HBase REST Server Metrics** – For monitoring the HBase REST interface, you can use the
   following configuration:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "emr-hbase-rest-server-metrics",
        "Properties": {
          "Hadoop:service=HBase,name=REST": "successfulPut,successfulScanCount",
          "otel.metric.export.interval": "30000"
        },
        "Configurations": []
      }
    ]
  }
]
```

In this example, the CloudWatch Agent collects metrics about successful PUT operations and scan counts every 30 seconds. 4. **Setting Up HBase Thrift Server Metrics** – To monitor the HBase Thrift Server, you can configure metrics with a
configuration like the following:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "emr-hbase-thrift-server-metrics",
        "Properties": {
          "Hadoop:service=HBase,name=Thrift,sub=ThriftOne": "BatchGet_max,BatchGet_mean",
          "otel.metric.export.interval": "30000"
        },
        "Configurations": []
      }
    ]
  }
]
```

This setup tracks the maximum and mean times for batch GET operations on the Thrift server.
