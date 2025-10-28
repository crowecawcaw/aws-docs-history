# Integrating with Amazon CloudWatch

Session Manager supports integration with Amazon CloudWatch for Brokers running on Amazon EC2 instances, and also
Brokers running on on-premises hosts.

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you
run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you
can measure for your resources and applications. For more information, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

You can configure the Session Manager Broker to send the following metric data to Amazon CloudWatch:

- `Number of DCV servers`—The number of DCV servers managed
  by the Broker.
- `Number of ready DCV servers`—The number of DCV servers
  that are in the `READY` state managed by the Broker.
- `Number of DCV sessions`—The number of DCV sessions managed
  by the Broker.
- `Number of DCV console sessions`—The number of DCV console
  sessions managed by the Broker.
- `Number of DCV virtual sessions`—The number of DCV virtual sessions
  managed by the Broker.
- `Heap memory used`—The amount of heap memory used by the
  Broker.
- `Off-heap memory used`—The amount of off-heap memory used by the
  Broker.
- `Describe sessions request time`—The amount of time taken to
  complete DescribeSessions API requests.
- `Delete sessions request time`—The amount of time taken to
  complete DeleteSessions API requests.
- `Create sessions request time`—The amount of time taken to
  complete CreateSessions API requests.
- `Get session connection data request time`—The amount of time
  taken to complete GetSessionConnectionData API requests.
- `Update session permissions sequest time`—The amount of time
  taken to complete UpdateSessionPermissions API requests.

###### To configure the Broker to send metric data to the Amazon CloudWatch

1. Open `/etc/dcv-session-manager-broker/session-manager-broker.properties` using
   your preferred text editor and do the following:
   - Set `enable-cloud-watch-metrics` to `true`
   - For `cloud-watch-region`, specify the Region in which to collect the metric
     data.

   ###### Note

   If your Broker is running on an Amazon EC2 instance, this parameter is optional. The Region is
   automatically retrieved from the Instance Metadata Service (IMDS). If you are
   running the Broker on an on-premises host, this parameter is mandatory.

2. Stop and restart the Broker.

```
`$`  sudo systemctl stop dcv-session-manager-broker
```

```
`$`  sudo systemctl start dcv-session-manager-broker
```

The Broker host must also have permission to call the `cloudwatch:PutMetricData`
API. AWS credentials can be retrieved using one of the supported credential retrieval
techniques. For more information, see [Supplying and Retrieving AWS
Credentials](../../../sdk-for-java/v2/developer-guide/credentials.md "../../../sdk-for-java/v2/developer-guide/credentials.md").
