

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Adding a query monitoring policy
<a name="serverless-monitor-access"></a>

A superuser can provide access to users who aren't superusers so that they can perform query monitoring for all users. First, you add a policy for a user or a role to provide query monitoring access. Then, you grant query monitoring permission to the user or role. 

**To add the query monitoring policy**

1. Choose [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Under **Access management**, choose **Policies**.

1. Choose **Create Policy**.

1. Choose **JSON** and paste the following policy definition.

------
#### [ JSON ]

****  

   ```
   {
   "Version":"2012-10-17",		 	 	 
   "Statement": [
   {
   "Effect": "Allow",
   "Action": [
       "redshift-data:ExecuteStatement",
       "redshift-data:DescribeStatement",
       "redshift-data:GetStatementResult",
       "redshift-data:ListDatabases"
   ],
   "Resource": "*"
   },
   {
   "Effect": "Allow",
   "Action": "redshift-serverless:GetCredentials",
   "Resource": "*"
   }
   ]
   }
   ```

------

1. Choose **Review policy**.

1. For **Name**, enter a name for the policy, such as `query-monitoring`.

1. Choose **Create policy**.

After you create the policy, you can grant the appropriate permissions.

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.