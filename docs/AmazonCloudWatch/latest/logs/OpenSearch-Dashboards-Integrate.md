# Step 1: Create the integration with OpenSearch Service

The first step is creating the integration with OpenSearch Service, which you need to do only once.
Creating the integration will create the following resources in your account.

- **[An OpenSearch Service time series collection](../../../opensearch-service/latest/developerguide/serverless-collections.md "../../../opensearch-service/latest/developerguide/serverless-collections.md")** without
  high availability.

A collection is a set of OpenSearch Service _indexes_ that work together
to support a workload.

- **Two security policies** for the collection. One defines the
  encryption type, which is either with a customer managed AWS KMS key or a service
  owned key. The other policy defines network access, allowing the OpenSearch Service
  application to access the collection. For more information, see [Encryption of data at rest for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/encryption-at-rest.md "../../../opensearch-service/latest/developerguide/encryption-at-rest.md").
- **[An OpenSearch Service data access policy](../../../opensearch-service/latest/developerguide/serverless-data-access.md "../../../opensearch-service/latest/developerguide/serverless-data-access.md")** that defines who can
  access data in the collection.
- **[An
  OpenSearch Service direct query data source](../../../opensearch-service/latest/developerguide/direct-query-s3.md "../../../opensearch-service/latest/developerguide/direct-query-s3.md")** with CloudWatch Logs defined as
  the source.
- **[An OpenSearch Service
  application](../../../opensearch-service/latest/developerguide/application.md "../../../opensearch-service/latest/developerguide/application.md")** with the name `aws-analytics`.
  The application will be configured to allow the creation of a workspace. If an
  application named `aws-analytics` already exists, it will be updated
  to add this collection as a data source.
- **[A OpenSearch Service
  workspace](../../../opensearch-service/latest/developerguide/application.md "../../../opensearch-service/latest/developerguide/application.md")** that will host the dashboards and allows
  everyone who has been granted access to read from the workspace.

###### Topics

- [Required permissions](#OpenSearch-Dashboards-Perms "#OpenSearch-Dashboards-Perms")
- [Create the integration](#OpenSearch-Dashboards-Procedure "#OpenSearch-Dashboards-Procedure")

## Required permissions

To create the integration, you must be signed on to an account that has the
**CloudWatchOpenSearchDashboardsFullAccess** managed IAM
policy or equivalent permissions, shown here. You must also have these permissions
to delete the integration, create, edit, and delete dashboards, and to refresh the
dashboard manually.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "CloudWatchOpenSearchDashboardsIntegration",
 "Effect": "Allow",
 "Action": [
 "logs:ListIntegrations",
 "logs:GetIntegration",
 "logs:DeleteIntegration",
 "logs:PutIntegration",
 "logs:DescribeLogGroups",
 "opensearch:ApplicationAccessAll",
 "iam:ListRoles",
 "iam:ListUsers"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchLogsOpensearchReadAPIs",
 "Effect": "Allow",
 "Action": [
 "aoss:BatchGetCollection",
 "aoss:BatchGetLifecyclePolicy",
 "es:ListApplications"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsOpensearchCreateServiceLinkedAccess",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/opensearchservice.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "opensearchservice.amazonaws.com",
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsObservabilityCreateServiceLinkedAccess",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/observability.aoss.amazonaws.com/AWSServiceRoleForAmazonOpenSearchServerless",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "observability.aoss.amazonaws.com",
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsCollectionRequestAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:CreateCollection"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:RequestTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "CloudWatchOpenSearchIntegration"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsApplicationRequestAccess",
 "Effect": "Allow",
 "Action": [
 "es:CreateApplication"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:RequestTag/OpenSearchIntegration": [
 "Dashboards"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "OpenSearchIntegration"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsCollectionResourceAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:DeleteCollection"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:ResourceTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ]
 }
 }
 },
 {
 "Sid": "CloudWatchLogsApplicationResourceAccess",
 "Effect": "Allow",
 "Action": [
 "es:UpdateApplication",
 "es:GetApplication"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:ResourceTag/OpenSearchIntegration": [
 "Dashboards"
 ]
 }
 }
 },
 {
 "Sid": "CloudWatchLogsCollectionPolicyAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:CreateSecurityPolicy",
 "aoss:CreateAccessPolicy",
 "aoss:DeleteAccessPolicy",
 "aoss:DeleteSecurityPolicy",
 "aoss:GetAccessPolicy",
 "aoss:GetSecurityPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aoss:collection": "cloudwatch-logs-*",
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsAPIAccessAll",
 "Effect": "Allow",
 "Action": [
 "aoss:APIAccessAll"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aoss:collection": "cloudwatch-logs-*"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsIndexPolicyAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:CreateAccessPolicy",
 "aoss:DeleteAccessPolicy",
 "aoss:GetAccessPolicy",
 "aoss:CreateLifecyclePolicy",
 "aoss:DeleteLifecyclePolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aoss:index": "cloudwatch-logs-*",
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsDQSRequestQueryAccess",
 "Effect": "Allow",
 "Action": [
 "es:AddDirectQueryDataSource"
 ],
 "Resource": "arn:aws:opensearch:*:*:datasource/cloudwatch_logs_*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:RequestTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "CloudWatchOpenSearchIntegration"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsStartDirectQueryAccess",
 "Effect": "Allow",
 "Action": [
 "opensearch:StartDirectQuery",
 "opensearch:GetDirectQuery"
 ],
 "Resource": "arn:aws:opensearch:*:*:datasource/cloudwatch_logs_*"
 },
 {
 "Sid": "CloudWatchLogsDQSResourceQueryAccess",
 "Effect": "Allow",
 "Action": [
 "es:GetDirectQueryDataSource",
 "es:DeleteDirectQueryDataSource"
 ],
 "Resource": "arn:aws:opensearch:*:*:datasource/cloudwatch_logs_*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:ResourceTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ]
 }
 }
 },
 {
 "Sid": "CloudWatchLogsPassRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "directquery.opensearchservice.amazonaws.com",
 "aws:CalledViaFirst": "logs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsAossTagsAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:TagResource"
 ],
 "Resource": "arn:aws:aoss:*:*:collection/*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "logs.amazonaws.com",
 "aws:ResourceTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ]
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "CloudWatchOpenSearchIntegration"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsEsApplicationTagsAccess",
 "Effect": "Allow",
 "Action": [
 "es:AddTags"
 ],
 "Resource": "arn:aws:opensearch:*:*:application/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/OpenSearchIntegration": [
 "Dashboards"
 ],
 "aws:CalledViaFirst": "logs.amazonaws.com"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "OpenSearchIntegration"
 }
 }
 },
 {
 "Sid": "CloudWatchLogsEsDataSourceTagsAccess",
 "Effect": "Allow",
 "Action": [
 "es:AddTags"
 ],
 "Resource": "arn:aws:opensearch:*:*:datasource/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/CloudWatchOpenSearchIntegration": [
 "Dashboards"
 ],
 "aws:CalledViaFirst": "logs.amazonaws.com"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "CloudWatchOpenSearchIntegration"
 }
 }
 }
 ]
}`

```

## Create the integration

Use these steps to create the integration.

###### To integrate CloudWatch Logs with Amazon OpenSearch Service

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs Insights** and
   then choose the **Analyze with OpenSearch** tab.
3. Choose **Create integration**.
4. For **Integration name**, enter a name for the
   integration.
5. (Optional) To encrypt the data written to OpenSearch Service Serverless, enter the ARN
   of the AWS KMS key that you want to use in **KMS key ARN**.
   For more information, see [Encryption at rest](../../../opensearch-service/latest/developerguide/serverless-encryption.md "../../../opensearch-service/latest/developerguide/serverless-encryption.md") in the Amazon OpenSearch Service Developer Guide.
6. For **Data retention**, enter the amount of time that you
   want the OpenSearch Service data indexes to be retained. This also defines the maximum
   time period for which you can view data in the dashboards. Choosing a longer
   data retention period will incur additional searching and indexing costs.
   For more information, see [OpenSearch Service Serverless
   Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

The maximum retention period is 30 days.

The data retention length will also be used to create the OpenSearch Service collection
lifecycle policy. 7. For **IAM role for writing to OpenSearch collection**,
create a new IAM role or select an existing IAM role to be used to write
to the OpenSearch Service collection.

Creating a new role is the simplest method, and the role will be created
with the necessary permissions.

###### Note

If you create a role, it will have permissions to read from all log
groups in the account.

If you want to select an existing role, it should have the permissions
listed in [Permissions that the integration needs](OpenSearch-Dashboards-CreateRole.md "OpenSearch-Dashboards-CreateRole.md"). Alternatively, you
can choose **Use an existing role** and then in the
**Verify access permissions of the selected role**
section you can choose **Create role**. This way you can
use the permissions listed in [Permissions that the integration needs](OpenSearch-Dashboards-CreateRole.md "OpenSearch-Dashboards-CreateRole.md") as a template and
modify it. For example, if you want to specify a finer-grain control of log
groups. 8. For **IAM roles and users who can view dashboards**, you
select how you want to grant access to IAM roles and IAM users for
vended logs dashboard access:

    * To limit the dashboard access to just some users, choose
     **Select IAM roles and users who can view
     dashboards** and then in the text box search for and
     select the IAM roles and IAM users that you want to grant access
     to.
    * To grant dashboard access to all users, choose **Allow all
     roles and users in this account to view
     dashboards**.


    ###### Important

    Selecting roles or users, or choosing all users, only adds
     them to the [data access policy](../../../opensearch-service/latest/developerguide/serverless-data-access.md "../../../opensearch-service/latest/developerguide/serverless-data-access.md") needed for accessing OpenSearch Service
     collection that stores the dashboard data. **For them to
     be able to view the vended logs dashboards, you must also
     grant those roles and users the [CloudWatchOpenSearchDashboardAccess](iam-identity-based-access-control-cwl.md#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess "iam-identity-based-access-control-cwl.md#managed-policies-cwl-CloudWatchOpenSearchDashboardAccess") managed IAM policy.**

9. Choose **Create integration**

Creating the integration will take a few minutes.
