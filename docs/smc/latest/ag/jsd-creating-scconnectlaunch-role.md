# Creating

SCConnectLaunch Role

The following section describes how to create the
**SCConnectLaunch** role. This role places baseline
AWS service permissions into the Service Catalog launch constraints. For more
information, see CORRECT LINK.

###### To create SCConnectLaunch role

1. Create the **AWSCloudFormationFullAccess**
   policy. Choose **create policy** and then paste the
   following in the JSON editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
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
 "Resource": "*"
 }
 ]
}`

```

2. Create a policy called
   **ServiceCatalogSSMActionsBaseline**. Follow the
   instructions in [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"), and paste the following into the
   JSON editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1536341175150",
 "Action": [
 "servicecatalog:ListServiceActionsForProvisioningArtifact",
 "servicecatalog:ExecuteprovisionedProductServiceAction",
 "ssm:DescribeDocument",
 "ssm:GetAutomationExecution",
 "ssm:StartAutomationExecution",
 "ssm:StopAutomationExecution",
 "cloudformation:ListStackResources",
 "ec2:DescribeInstanceStatus",
 "ec2:StartInstances",
 "ec2:StopInstances"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

3. Create the **SCConnectLaunch** role. Assign the
   trust relationship to Service Catalog.

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
   **SCConnectLaunch** role. Attach the following
   baseline IAM policies:
   - **AmazonEC2FullAccess** (AWS managed
     policy)
   - **AmazonS3FullAccess** (AWS managed
     policy)
   - **AWSCloudFormationFullAccess** (custom
     managed policy)
   - **ServiceCatalogSSMActionsBaseline**
     (custom managed policy)

###### Note

You can use the available AWS CloudFormation templates for the JSM
connector to configure your AWS account to enable AWS Service Catalog
integration. This stack includes the _Sync user_
and _End user_ roles, which attach the required
permissions for all available integrations. For more information, see
[Baseline Permissions](jsd-baseline-permissions.md "jsd-baseline-permissions.md").
