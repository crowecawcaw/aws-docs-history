# Manually add CloudWatch as a data

source

###### To manually add the CloudWatch data source

1. In the Grafana console side menu, hover over the **Configuration** (gear) icon, and then choose **Data Sources**.
2. Choose **Add data source**.
3. Choose the **CloudWatch** data source. If necessary, you
   can start typing `CloudWatch` in the search box to help
   you find it.

## CloudWatch settings

The following CloudWatch settings apply.

| Name                           | Description                                                                                                                                                                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`                         | The data source name. This is how you see the data<br>source in panels and queries.                                                                                                                                                                                                                               |
| `Default`                      | Designates the data source to be pre-selected for<br>new panels.                                                                                                                                                                                                                                                  |
| `Default Region`               | Set the Region in the query editor. Can be changed<br>on per-query basis.                                                                                                                                                                                                                                         |
| `Namespaces of Custom Metrics` | Specifies the CloudWatch namespaces of custom metrics.<br>Can include multiple namespaces, separated by<br>commas.                                                                                                                                                                                                |
| `Auth Provider`                | Specifies the provider to get<br>credentials.                                                                                                                                                                                                                                                                     |
| `Assume Role Arn`              | Specifies the Amazon Resource Name (ARN) of the<br>role to assume.                                                                                                                                                                                                                                                |
| `External ID`                  | (Optional) Specifies the external ID. Use if you<br>are assuming a role in another AWS account that has<br>been created with an external ID.                                                                                                                                                                      |
| `Timeout`                      | Configure the timeout specifically for CloudWatch Logs<br>queries.                                                                                                                                                                                                                                                |
| `X-Ray trace links`            | To automatically add links in your logs when the<br>log contains the `@xrayTraceId` field, link<br>an X-Ray data source in the \*_X-Ray trace<br>link_<br>• section of the data source<br>configuration. You must already have an [X-Ray data source](x-ray-data-source.md "x-ray-data-source.md")<br>configured. |

### Authentication

To enable authentication between Amazon Managed Grafana and CloudWatch, you can use the
Amazon Managed Grafana console to quickly create the policies and permissions that
are needed. Alternatively, you can manually set up authentication using
some of the same methods that you would on a self-managed Grafana
server.

To use Amazon Managed Grafana data source configuration to quickly set up the
policies, follow the steps in [Use AWS data source
configuration to add CloudWatch as a data source](adding-CloudWatch-AWS-config.md "adding-CloudWatch-AWS-config.md").

To set up the permissions manually, use one of the methods in the
following section.

#### AWS

credentials

There are three different authentication methods available.

- **AWS SDK Default**—
  Uses the permissions defined in the role that is attached to
  your workspace. For more information, see [Customer-managed permissions](AMG-manage-permissions.md#AMG-customer-managed "AMG-manage-permissions.md#AMG-customer-managed").
- **Access and secret
  key**— Corresponds to the AWS SDK for Go
  `StaticProvider`. Uses the given access key
  ID and secret key to authenticate. This method doesn’t have
  any fallbacks, and will fail if the provided key pair
  doesn’t work.

#### IAM

roles

Currently, all access to CloudWatch is done server-side by the Grafana
backend using the official AWS SDK. If you choose the
_AWS SDK Default_ authentication method,
and your Grafana server is running on AWS, you can use IAM roles
to handle authentication automatically.

For more information, see [IAM
roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

#### IAM

policies

Grafana needs permissions granted through IAM to be able to read
CloudWatch metrics and EC2 tags, instances, and Regions. You can attach
these permissions to IAM roles and use the built-in Grafana
support for assuming roles.

The following code example shows a minimal policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowReadingMetricsFromCloudWatch",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetInsightRuleReport"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadingLogsFromCloudWatch",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:GetLogGroupFields",
 "logs:StartQuery",
 "logs:StopQuery",
 "logs:GetQueryResults",
 "logs:GetLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadingTagsInstancesRegionsFromEC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeRegions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadingResourcesForTags",
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*"
 },
 {
 "Sid": "AllowReadingAcrossAccounts",
 "Effect": "Allow",
 "Action": [
 "oam:ListSinks",
 "oam:ListAttachedLinks"
 ],
 "Resource": "*"
 }
 ]
}`

```

#### Assuming a role

The `Assume Role ARN` field allows you to specify
which IAM role to assume, if any. If you keep this blank, the
provided credentials are used directly and the associated role or
user should have the required permissions. If this field is not
blank, the provided credentials are used to perform an
`sts:AssumeRole` call.
