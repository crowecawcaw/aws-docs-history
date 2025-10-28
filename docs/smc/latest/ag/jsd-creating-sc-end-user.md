# Creating AWS Service

Management Connector End User

The following section describes how to create the AWS Service
Management Connector end user and associate the appropriate IAM
permissions. To perform this task, you need IAM permissions to create
new users.

###### To create AWS Service Management Connector end user

1. Follow the instructions in [Creating an IAM user in your AWS Account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") to create a
   user (such as SCEndUser). The user needs programmatic and AWS Management Console
   access to follow the Connector for Jira Service Management
   installation instructions.
2. For products with AWS CloudFormation StackSets, you need to create a stack
   set inline policy. With AWS CloudFormation StackSets, you can create products to
   deploy across multiple accounts and Regions.

Using an administrator account, you define and manage a Service Catalog
product and use it as the basis for provisioning stacks into
selected target accounts across specified Regions. You need to have
the necessary permissions defined in your AWS accounts.

To set up the necessary permissions, follow the instructions in
[Granting
Permissions for Stack Set Operations](../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs.md") to create an
**AWSCloudFormationStackSetAdministrationRole**
and an
**AWSCloudFormationStackSetExecutionRole**. 3. Create the stack set inline policy to enable the provisioning of
a product across multiple Regions in one account, replacing the
`arn` number string with your account number.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789123:role/AWSCloudFormationStackSetExecutionRole"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole"
 }
 ]
}`

```

4. Add the following permissions (policies) to the user
   **SCEndUser**:
   - **AWServiceCatalogEndUserFullAccess** - (AWS managed policy)
   - **StackSet** - (inline
     policy)
   - **AmazonS3ReadOnlyAccess** -
     (AWS managed policy)
   - **AmazonEC2ReadOnlyAccess** -
     (AWS managed policy)
   - **AWSConfigUserAccess** -
     (AWS managed policy)
   - **SSMOpsItemActionPolicy** -
     (inline policy)
   - **ConfigBidirectionalSecurityHubSQSBaseline** -
     (inline policy)

###### Note

For Service Catalog products with AWS CloudFormation StackSets, you need to include
the read only permissions for the services you want to provision.
For example, to provision an Amazon S3 bucket, include the
**AmazonS3ReadOnlyAccess** policy to the
**SCEndUser** role. 5. Also add a policy that allows the following on all resources
(\*): **ssm:DescribeAutomationExecutions**,
**ssm:DescribeDocument**, and
ssm:**StartAutomationExecution**. 6. Review and choose **Create User**. 7. Note the access and secret access information. Download the .csv
file that contains the user credential information.
