# Creating SCConnectLaunch

role

This section describes how to create the
`SCConnectLaunch` role. This role places baseline AWS
service permissions in the AWS Service Catalog launch constraints. For more
information, refer to [AWS Service Catalog
launch constraints](../../../servicecatalog/latest/adminguide/constraints-launch.md "../../../servicecatalog/latest/adminguide/constraints-launch.md").

The `SCConnectLaunch` role is an IAM role that places
baseline AWS service permissions into the AWS Service Catalog launch
constraints. Configuring this role enables segregation of duty through
provisioning product resources for Jira internal customers, Jira
agents, and end users.

The `SCConnectLaunch` role baseline contains
permissions to Amazon EC2 and Amazon S3 services. If your products contain
additional AWS services, you must either include those services in
the `SCConnectLaunch` role or create a new launch role.

###### \*\*To create SCConnectLaunch

role\*\*

1. Create this policy: `AWSCloudFormationFullAccess`
   policy and then follow the instructions in [Creating
   IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"). Choose **create
   policy** and add this code in the JSON editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "cloudformation:DescribeStackResource",
 "cloudformation:DescribeStackResources",
 "cloudformation:GetTemplate",
 "cloudformation:List*",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStacks",
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStacks",
 "cloudformation:GetTemplateSummary",
 "cloudformation:SetStackPolicy",
 "cloudformation:ValidateTemplate",
 "cloudformation:UpdateStack",
 "cloudformation:CreateChangeSet",
 "cloudformation:DescribeChangeSet",
 "cloudformation:ExecuteChangeSet",
 "cloudformation:DeleteChangeSet",
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

###### Note

`AWSCloudFormationFullAccess` includes additional
permissions for ChangeSets. 2. Create this policy:
`ServicecodeCatalogSSMActionsBaseline` policy and
then follow the instructions in [Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"). Choose **create
policy** and add this code in the JSON editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1536341175150",
 "Action": [
 "servicecatalog:AssociateResource",
 "servicecatalog:DisassociateResource",
 "servicecatalog:ListServiceActionsForProvisioningArtifact",
 "servicecatalog:ExecuteprovisionedProductServiceAction",
 "ssm:DescribeDocument",
 "ssm:GetAutomationExecution",
 "ssm:StartAutomationExecution",
 "ssm:StopAutomationExecution",
 "ssm:StartChangeRequestExecution",
 "cloudformation:ListStackResources",
 "ec2:DescribeInstanceStatus",
 "ec2:StartInstances",
 "ec2:StopInstances"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm.amazonaws.com"
 }
 }
 }
 ]
}`

```

3. Create the `SCConnectLaunch` role. Then assign the
   trust relationship to AWS Service Catalog using this code in the JSON
   editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "servicecatalog.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. Attach the relevant policies to the
   `SCConnectLaunch` role.

Service Management Connector recommends that you customize and
scope your launch policies to the specific AWS services, which
are in the associated CloudFormation template for the given Service Catalog product.

For example, to provision Amazon EC2 and Amazon S3 products, the
recommended policies are as follows:

    * `AmazonEC2FullAccess` (AWS managed
     policy)
    * `AmazonS3FullAccess` (AWS managed policy)
    * `AWSCloudFormationFullAccess` (custom managed
     policy)
    * `ServiceCatalogSSMActionsBaseline` (custom
     managed policy)
