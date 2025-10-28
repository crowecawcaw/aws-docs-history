# Creating the SCConnectLaunch role

The `SCConnectLaunch` role is an IAM role that places baseline
AWS service permissions into the AWS Service Catalog launch constraints. Configuring this
role enables segregation of duty through provisioning product resources for
ServiceNow end users.

The `SCConnectLaunch` role baseline contains permissions to Amazon EC2 and Amazon S3 services. If your products contain more AWS services, you
must either include those services in the `SCConnectLaunch` role or
create new launch roles.

This section describes how to create the `SCConnectLaunch` role.
This role places baseline AWS service permissions in the Service Catalog launch
constraints. For more information, see [Service Catalog Launch
Constraints](../../../servicecatalog/latest/adminguide/constraints-launch.md "../../../servicecatalog/latest/adminguide/constraints-launch.md").

###### **To create SCConnectLaunch role**

1. Create this policy: `AWSCloudFormationFullAccess` policy.
   Choose **create policy** and add this code in the JSON
   editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
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
 "Resource":"*"
 }
 ]
}`

```

###### Note

`AWSCloudFormationFullAccess` includes additional
permissions for ChangeSets. 2. Create this policy: `ServicecodeCatalogSSMActionsBaseline`.
Follow the instructions in [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and add this code in the JSON editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"Stmt1536341175150",
 "Action":[
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
 "Effect":"Allow",
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":"iam:PassRole",
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "iam:PassedToService":"ssm.amazonaws.com"
 }
 }
 }
 ]
}`

```

3. Create the `SCConnectLaunch` role. Then assign the trust
   relationship to Service Catalog.

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

4. Attach the relevant policies to the `SCConnectLaunch` role.

We recommend you customize and scope your launch policies to the
specific AWS Services, which are in the associated CloudFormation
template for the given Service Catalog product.

For example, to provision EC2 and S3 products, your role policies are
as follows:

    * `AmazonEC2FullAccess` AWS managed policy)
    * `AmazonS3FullAccess` AWS managed policy)
    * `AWSCloudFormationFullAccess` (custom managed
     policy)
    * `ServiceCatalogSSMActionsBaseline` (custom managed
     policy)
