

# Create an IAM role for repository creation templates
<a name="repository-creation-templates-create-iam"></a>

You can use the AWS Management Console to create a role that can be used by Amazon ECR when you specify the repository creation role in a repository creation template that is using repository tags or KMS in a template.

------
#### [ AWS Management Console ]

**To create a role.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Roles** and then choose **Create role**.

1. Choose **Custom trust policy** role type.

1. In the **Custom trust policy** section, paste the custom trust policy listed below: 

------
#### [ JSON ]

****  

   ```
   {
   "Version":"2012-10-17",		 	 	 
   "Statement": [
       {
           "Effect": "Allow",
           "Principal": {
               "Service": "ecr.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
       }
       ]
   }
   ```

------

1. Choose **Next**.

1. From the **Add permissions** page, select the check box next to the custom policy you created earlier from the list of Permissions policies and choose **Next**.

1. For **Role name**, enter a name for your role. Role names must be unique within your AWS account. When a role name is used in a policy or as part of an ARN, the role name is case sensitive. When a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive. Because various entities might reference the role, you can't edit the name of the role after it is created.

1. (Optional) For **Description**, enter a description for the new role.

1. Review the role and then choose **Create role**.

------