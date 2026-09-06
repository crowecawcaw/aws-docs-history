

# Setting up an AWS account to use the Amazon Inspector CI/CD integration
<a name="configure-cicd-account"></a>

 To use the Amazon Inspector CI/CD integration, you must sign up for an AWS account. The AWS account must have an IAM role that grants your CI/CD pipleline access to the Amazon Inspector Scan API. Complete the tasks in the following topics to sign up for an AWS account, create an administrator user, and configure an IAM role for CI/CD integration. 

**Note**  
 If you already signed up for an AWS account, you can skip to [Configure an IAM role for CI/CD integration](#cicd-iam-role). 

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Configure an IAM role for CI/CD integration](#cicd-iam-role)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Configure an IAM role for CI/CD integration
<a name="cicd-iam-role"></a>

To integrate Amazon Inspector scanning into your CI/CD pipeline you need to create an IAM policy that allows access to the Amazon Inspector Scan API that scans the software bill of materials (SBOMs). Then, you can attach that policy to an IAM role that your account can assume to run the Amazon Inspector Scan API.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, **Policies** and then choose **Create Policy**.

1. In **Policy Editor** select **JSON** and paste the following statement:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "VisualEditor0",
               "Effect": "Allow",
               "Action": "inspector-scan:ScanSbom",
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. Give the policy a name, for example `InspectorCICDscan-policy`, and add an optional description, then choose **Create Policy**. This policy will be attached to the role you’ll create in the next steps.

1. In the navigation pane of the IAM console, select **Roles** and then select **Create New Role**.

1. For **Trusted entity type** choose **Custom trust policy** and paste the following policy:

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
                   "AWS": "arn:aws:iam::{{111122223333}}:root"
               },
               "Action": "sts:AssumeRole",
               "Condition": {}
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. In **Add permissions** search for and select the policy you created earlier, then choose **Next**.

1. Give the role a name, for example `InspectorCICDscan-role`, and add an optional description, then choose `Create Role`.