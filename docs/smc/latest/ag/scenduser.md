

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating the AWS Service Management Connector end user
<a name="scenduser"></a>

 This section describes how to create the AWS Service Management Connector end user and associates the appropriate IAM permission. To perform this task, you need IAM permissions to create new users. 

****To create AWS Service Management Connector end user****

1.  Follow the instructions in [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to create a user (SMEndUser). The user needs programmatic and AWS Management Console access to follow the Connector for ServiceNow installation instructions.

    For products using CloudFormation StackSets, you need to create a StackSet inline policy. With CloudFormation StackSets, you are able to create products across multiple accounts and Regions. 

   Using an administrator account, you define and manage a Service Catalog product. You also use it to provision stacks into selected target accounts across specified Regions. You need to have the necessary permissions defined in your AWS accounts. 

   To set up the necessary permissions, see [Granting Permissions for Stack Set Operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html). Follow the instructions to create an `AWSCloudFormationStackSetAdministrationRole` and an `AWSCloudFormationStackSetExecutionRole`. 

1. Add the following permissions (policies) to the user:
   + `AWSServiceCatalogEndUserFullAccess` (AWS managed policy)
   + `StackSet` (inline policy) - For Service Catalog products with stack sets, you need to modify the SMEndUser to include the Read Only permissions for the services you want to provision. For example, to provision an Amazon S3 bucket, include the `AmazonS3ReadOnlyAccess` policy to the `SMEndUser`.
   + `OpsCenterExecutionPolicy`
   + `AmazonEC2ReadOnlyAccess` (AWS managed policy)
   + `AmazonS3ReadOnlyAccess` (AWS managed policy)