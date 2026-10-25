

# Setting up connections
<a name="setting-up-connections"></a>

Complete the tasks in this section to get set up for creating and using the connections feature in the Developer Tools console.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Create and apply a policy with permissions to create connections](#setting-up-connections-iamuser)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Create and apply a policy with permissions to create connections
<a name="setting-up-connections-iamuser"></a>



**To use the JSON policy editor to create a policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

   If this is your first time choosing **Policies**, the **Welcome to Managed Policies** page appears. Choose **Get Started**.

1. At the top of the page, choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Enter the following JSON policy document:

   ```
    {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "codeconnections:CreateConnection",
                   "codeconnections:DeleteConnection",
                   "codeconnections:GetConnection",
                   "codeconnections:ListConnections",
                   "codeconnections:GetInstallationUrl",
                   "codeconnections:GetIndividualAccessToken",
                   "codeconnections:ListInstallationTargets",
                   "codeconnections:StartOAuthHandshake",
                   "codeconnections:UpdateConnectionInstallation",
                   "codeconnections:UseConnection"
               ],
               "Resource": [
                   "*"
               ]
           }
       ]
   }
   ```

1. Choose **Next**.
**Note**  
You can switch between the **Visual** and **JSON** editor options anytime. However, if you make changes or choose **Next** in the **Visual** editor, IAM might restructure your policy to optimize it for the visual editor. For more information, see [Policy restructuring](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure) in the *IAM User Guide*.

1. On the **Review and create** page, enter a **Policy name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. Choose **Create policy** to save your new policy.