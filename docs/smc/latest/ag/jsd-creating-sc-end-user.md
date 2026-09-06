

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating AWS Service Management Connector End User
<a name="jsd-creating-sc-end-user"></a>

The following section describes how to create the AWS Service Management Connector end user and associate the appropriate IAM permissions. To perform this task, you need IAM permissions to create new users.

**To create AWS Service Management Connector end user**

1. Follow the instructions in [Creating an IAM user in your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to create a user (such as SCEndUser). The user needs programmatic and AWS Management Console access to follow the Connector for Jira Service Management installation instructions.

1. For products with CloudFormation StackSets, you need to create a stack set inline policy. With CloudFormation StackSets, you can create products to deploy across multiple accounts and Regions.

   Using an administrator account, you define and manage a Service Catalog product and use it as the basis for provisioning stacks into selected target accounts across specified Regions. You need to have the necessary permissions defined in your AWS accounts.

   To set up the necessary permissions, follow the instructions in [Granting Permissions for Stack Set Operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) to create an **AWSCloudFormationStackSetAdministrationRole** and an **AWSCloudFormationStackSetExecutionRole**.

1. Create the stack set inline policy to enable the provisioning of a product across multiple Regions in one account, replacing the `arn` number string with your account number.

------
#### [ JSON ]

****  

   ```
   {
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
           "Resource":       "arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole"
           }
        ]
   }
   ```

------

1. Add the following permissions (policies) to the user **SCEndUser**:
   + **AWServiceCatalogEndUserFullAccess **- (AWS managed policy)
   + **StackSet** - (inline policy)
   + **AmazonS3ReadOnlyAccess** - (AWS managed policy)
   + **AmazonEC2ReadOnlyAccess** - (AWS managed policy)
   + **AWSConfigUserAccess** - (AWS managed policy)
   + **SSMOpsItemActionPolicy** - (inline policy)
   + **ConfigBidirectionalSecurityHubSQSBaseline** - (inline policy)
**Note**  
For Service Catalog products with CloudFormation StackSets, you need to include the read only permissions for the services you want to provision. For example, to provision an Amazon S3 bucket, include the **AmazonS3ReadOnlyAccess** policy to the **SCEndUser** role.

1. Also add a policy that allows the following on all resources (\*): **ssm:DescribeAutomationExecutions**, **ssm:DescribeDocument**, and ssm:**StartAutomationExecution**.

1. Review and choose **Create User**.

1. Note the access and secret access information. Download the .csv file that contains the user credential information.