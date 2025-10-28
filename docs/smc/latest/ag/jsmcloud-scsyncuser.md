# Creating AWS Service Management Connector Sync

user

This section describes how to create the AWS Sync user and
associate the appropriate IAM permission. To perform this task, you
must have IAM permissions to create new users. The following steps
to create a Sync user and End user are not required if you use the
CloudFormation template to deploy the permissions. Refer to the AWS
configurations for Connector for Jira Service Management [AWS Commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNowv-AWS_Configurations_Commercialv4.7.5.json "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNowv-AWS_Configurations_Commercialv4.7.5.json") and [AWS GovCloud Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNowv-AWS_Configurations_GovCloudv4.7.5.json "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNowv-AWS_Configurations_GovCloudv4.7.5.json").

###### To create AWS Service Management Connector sync user

1. Follow the instructions in [Creating an
   IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") to create a sync user
   (SMSyncUser). This user needs programmatic and AWS Management
   Console access to follow the Connector for Jira installation
   instructions.
2. Set permissions for your sync user (SMSyncUser). Choose
   **Attach existing policies directly** and
   select:

**`AWSServiceCatalogAdminReadOnlyAccess`**
(AWS managed policy) 3. Create this policy: `AWSSecurityHubPolicy`. Then
follow the instructions in [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and add this code in the JSON
editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Action": [
 "sqs:ReceiveMessage",
 "sqs:DeleteMessage"
 ],
 "Resource": "arn:aws:sqs:`us-east-1`:`111122223333`:`QueueName`",
 "Effect": "Allow"
 },
 {"Action": [
 "securityhub:BatchUpdateFindings"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

4. Create this policy: `ConfigHealthSQSBaseline`. Then
   follow the instructions in [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and add this code in the JSON
   editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Action": [
 "sqs:ReceiveMessage",
 "sqs:DeleteMessage"
 ],
 "Resource": "arn:aws:sqs:`us-east-1`:`111122223333`:`QueueName`",
 "Effect": "Allow"
 }
 ]
}`

```

5. Create this policy: `OpsCenterExecutionPolicy`.
   Then follow the instructions in [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and add this code in the JSON
   editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Effect": "Allow",
 "Action": [
 "ssm:CreateOpsItem",
 "ssm:GetOpsItem",
 "ssm:UpdateOpsItem",
 "ssm:DescribeOpsItems"
 ],
 "Resource": "*"
 }
 ]
}`

```

6. Create this policy: `AWSIncidentBaselinePolicy`.
   Then follow the instructions in [Creating
   IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and add this code in the JSON
   editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Action": [
 "ssm-incidents:ListIncidentRecords",
 "ssm-incidents:GetIncidentRecord",
 "ssm-incidents:UpdateRelatedItems",
 "ssm-incidents:ListTimelineEvents",
 "ssm-incidents:GetTimelineEvent",
 "ssm-incidents:UpdateIncidentRecord",
 "ssm-incidents:ListRelatedItems",
 "ssm:ListOpsItemRelatedItems",
 "ssm-incidents:ListRelatedItems",
 "ssm-incidents:ListResponsePlans",
 "ssm-incidents:StartIncident"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

7. Choose **Attach existing policies directly**
   and then select the following policies:
   - **AmazonSSMReadOnlyAccess** (AWS
     managed policy)
   - **AWSSupportAccess** (AWS managed
     policy)

8. Add a policy that allows `budgets:ViewBudget` on
   all resources (\*).
9. Review and then choose **Create User**. Note
   the access and secret access information, and then download the
   .csv file containing the user credential information.

###### Note

To align with best practices, AWS recommends periodically
rotating IAM user access keys. For more information, refer to
[Manage access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#securing_access-keys "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#securing_access-keys").
