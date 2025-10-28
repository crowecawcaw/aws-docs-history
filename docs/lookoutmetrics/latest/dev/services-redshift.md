Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Using Amazon Redshift with Lookout for Metrics

You can use Amazon Redshift as a datasource for an Amazon Lookout for Metrics detector. With Amazon Redshift, you can choose columns to monitor
(_measures_) and columns that segment measure values (dimensions). The detector monitors the
values in these columns to find anomalies in your data.

###### Important

Lookout for Metrics can only connect to databases in a subset of Availability Zones in some Regions. The following Availability Zones
are supported.

######

- **US East (N. Virginia)** – `use1-az1`,`use1-az4`,
  `use1-az6`
- **US West (Oregon)** – `usw2-az1`, `usw2-az2`,
  `usw2-az3`
- **Asia Pacific (Tokyo)** – `apne1-az1`,
  `apne1-az2`, `apne1-az4`
- **Other Regions** – All Availability Zones.
  Availability Zone names such as `us-west-2a` are aliases for zone IDs that vary by account. To see
  which names map to which IDs in your account, visit the [EC2 dashboard](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2")
  in the AWS Management Console.

To use an Amazon Redshift data warehouse with Lookout for Metrics, the table must have a timestamp column that is
defined as the _sort key_. Amazon Redshift uses the sort key to store data
on disk and construct plans that exploit the way that the data is stored. For more information,
see [Working with sort keys](../../../redshift/latest/dg/t_Sorting_data.md "../../../redshift/latest/dg/t_Sorting_data.md") in the Amazon Redshift
Database Developer Guide.

You also need an AWS Secrets Manager secret for the detector. The secret must have the database password and have a name that starts with `AmazonLookoutMetrics-`.

The detector imports data at the end of each interval. You configure an **offset** to allow
time after an interval ends for all data to be written. For example, if you choose an offset of 30 seconds, the
detector waits 30 seconds after the end of each interval before reading data for that interval.

Before you configure the dataset, you need to know the following information.

######

- **DB identifier** – The unique identifier of the DB instance or cluster.
  For example, `mysql-dbi` or `ld1xmplvzghgn47`.
- **Database name** – The software-level database name. For example,
  `mydb`.
- **Table name** – The name of the table. For example,
  `events`.
- **Column names** – The names of columns that contain timestamps,
  measures, and dimensions.
- **Subnets** – The virtual private cloud (VPC) subnets where the detector
  creates network interfaces to connect to the database. For example,
  `subnet-0752xmpl92bf2e4b7`.
- **Security group** – A VPC security group that allows traffic to the
  database. For example, `sg-0f92xmplfbad0bc95`.
- **Secret name** – The name of an AWS Secrets Manager secret that the detector uses
  to retrieve the database password. For example, `AmazonLookoutMetrics-mysqldbi`.
- **Secret ID** – The ID of the secret, for generating a service role that
  can access it. For example, `AmazonLookoutMetrics-mysqldbi-Nxmplo`.

###### To create an Amazon Redshift dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add dataset**.
4. Choose **Amazon Redshift**.
5. Follow the instructions to create the datasource.
   To configure metrics in Lookout for Metrics, you choose columns to be measures and dimensions. Each measure is a column with a
   numerical value that you want to monitor for anomalies. Each dimension is a column with a string value that segments
   the measure(s). A metric in Lookout for Metrics is a combination of a measure value and a dimension value, aggregated within an
   interval. For example, _average availability in Colorado_, or _maximum temperature in
   furnace 17_.

The detector reads new data from Amazon Redshift periodically, by querying records with timestamps in the most recently
completed interval. If it detects any anomalies in the metrics for the interval, it records an anomaly and sends
[anomaly alerts](detectors-alerts.md "detectors-alerts.md"), if configured.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies.
For a five minute interval, the training process takes approximately one day. Training time varies
[depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart "gettingstarted-quotas.md#gettingstarted-quotas-coldstart").

###### Note

When you add an Amazon Redshift dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md "permissions-service.md") with permission to use the database secret and monitor Amazon Redshift resources. Lookout for Metrics also creates
up to two [elastic network interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md"), which
allow it to connect to your VPC to access your database. When you delete the detector, Lookout for Metrics deletes the network
interfaces.

For more information about Amazon Redshift, see [Getting started with
Amazon Redshift](../../../redshift/latest/gsg/getting-started.md "../../../redshift/latest/gsg/getting-started.md") in the Amazon Redshift Getting Started Guide.

###### Sections

- [Sample IAM policies](#services-redshift-samplepolicies "#services-redshift-samplepolicies")

## Sample IAM policies

The GitHub repository for this guide provides [sample IAM policies](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies "https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies")
that you can use as reference for developing service roles. You can use a single role that grants permission for
both importing data and sending alerts by combining the applicable policies.

###### Example [datasource-redshift.json](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-redshift.json "https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-redshift.json") –

Monitor and access an Amazon Redshift cluster

The second sample policy shows how to grant the detector permission to connect to a cluster across accounts.
The account with the cluster (Account B) must be in the same organization and share its subnet with the account
that contains the detector (`AccountA`).

###### Example [datasource-redshift-xaccount.json](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-redshift-xaccount.json "https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-redshift-xaccount.json") – Cross-account access

```
        ...
        {
            "Action": [
                "ec2:CreateNetworkInterface"
            ],
            "Resource": [
                "arn:aws:ec2:${Region}:${AccountA}:network-interface/*",
                "arn:aws:ec2:${Region}:${AccountA}:security-group/*",
                "arn:aws:ec2:${Region}:${AccountB}:subnet/${SubnetId}"
            ],
            "Effect": "Allow"
        },
        ...
```

For more information, see [Working with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the
_Amazon VPC User Guide_.
