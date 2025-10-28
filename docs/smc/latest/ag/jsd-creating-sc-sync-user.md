# Creating AWS Service

Management Connector Sync User

The following section describes how to create the AWS Connector
sync user and associate the appropriate IAM permissions. To perform
this task, you need IAM permissions to create new users.

###### To create AWS Service Management Connector sync user

1. Follow the instructions in **[Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")** to create the
   policy, **SSMOpsItemActionPolicy**.
   This policy enables Jira administrators to create and manage
   AWS Systems Manager OpsItems.

Copy this policy and paste it into **Policy
Document**:

JSON

```
`{

 "Version":"2012-10-17",

 "Statement": [

 {

 "Effect": "Allow",

 "Action": [

 "ssm:CreateOpsItem",

 "ssm:GetOpsItem",

 "ssm:UpdateOpsItem",

 "ssm:DescribeOpsItems",

 "ssm:CreateOpsItem"

 ],

 "Resource": "*"

 }

 ]

}`

```

2. Follow the instructions in [Creating
   IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and create the policy, **ConfigBidirectionalSecurityHubSQSBaseline**.

Copy this policy and paste it in the JSON editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"VisualEditor0",
 "Effect":"Allow",
 "Action":[
 "cloudformation:RegisterType",
 "cloudformation:DescribeTypeRegistration",
 "cloudformation:DeregisterType",
 "sqs:ReceiveMessage",
 "sqs:DeleteMessage",
 "securityhub:BatchUpdateFindings"
 ],
 "Resource":"*"
 }
 ]
 }`

```

3. Follow the instructions in **[Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")** to create the
   policy, **AWSIncidentBaselinePolicy**.

Copy this policy and paste it in the JSON editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "ssm-incidents:ListIncidentRecords",
 "ssm-incidents:GetIncidentRecord",
 "ssm-incidents:UpdateRelatedItems",
 "ssm-incidents:ListTimelineEvents",
 "ssm-incidents:GetTimelineEvent",
 "ssm-incidents:UpdateIncidentRecord",
 "ssm-incidents:ListRelatedItems",
 "ssm:ListOpsItemRelatedItems"
 ],
 "Resource":"*"
 }
 ]
 }`

```

4. Follow the instructions in **[Creating an IAM User in your AWS Account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md")**
   to create a sync user (SCSyncUser). The user needs programmatic
   access and AWS Management Console access to follow the Connector
   for Jira Service Management installation instructions.

Set permissions for your sync user (SCSyncUser). Choose
**Attach the following policies
directly** and select **AWSServiceCatalogAdminReadOnlyAccess**, **AmazonSSMReadOnlyAccess**, **SSMOpsItemActionPolicy**, **AWSSupportAccess**,**AWSIncidentBaselinePolicy**, and**ConfigBidirectionalSecurityHubSQSBaseline.** 5. Add a policy that allows **budgets:ViewBudget**
on all resources (\*). 6. Review and choose **Create User**. 7. Note the access and secret access information. Download the .csv
file that contains the user credential information.
