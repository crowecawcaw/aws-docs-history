

# Getting started with CodePipeline
<a name="getting-started-codepipeline"></a>

If you are new to CodePipeline, you can follow the tutorials in this guide after following the steps in this chapter to get set up.

The CodePipeline console includes helpful information in a collapsible panel that you can open from the information icon or any **Info** link on the page. (![Image showing the lower-case letter i that is used as the console info icon](http://docs.aws.amazon.com/codepipeline/latest/userguide/images/console-info-icon.png)). You can close this panel at any time.

The CodePipeline console also provides a way to quickly search for your resources, such as repositories, build projects, deployment applications, and pipelines. Choose **Go to resource** or press the `/` key, and then type the name of the resource. Any matches appear in the list. Searches are case insensitive. You only see resources that you have permissions to view. For more information, see [Viewing resources in the console](security-iam-resources-console.md). 

Before you can use AWS CodePipeline for the first time, you must create your AWS account and create your first administrative user.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Apply a managed policy for administrative access to CodePipeline](#assign-permissions)
+ [Install the AWS CLI](#install-cli)
+ [Open the console for CodePipeline](#open-codepipeline-console)
+ [Next steps](#next-steps)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Apply a managed policy for administrative access to CodePipeline
<a name="assign-permissions"></a>

You must grant permissions to interact with CodePipeline. The quickest way to do this is to apply the `AWSCodePipeline_FullAccess` managed policy to the administrative user. 

**Note**  
The `AWSCodePipeline_FullAccess` policy includes permissions that allow the console user to pass an IAM role to CodePipeline or other AWS services. This allows the service to assume the role and perform actions on your behalf. When you attach the policy to a user, role, or group, the `iam:PassRole` permissions are applied. Make sure the policy is only applied to trusted users. When users with these permissions use the console to create or edit a pipeline, the following choices are available:  
Create a CodePipeline service role or choose an existing one and pass the role to CodePipeline
Might choose to create a CloudWatch Events rule for change detection and pass the CloudWatch Events service role to CloudWatch Events 
For more information, see [Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).

**Note**  
The `AWSCodePipeline_FullAccess` policy provides access to all CodePipeline actions and resources that the IAM user has access to, as well as all possible actions when creating stages in a pipeline, such as creating stages that include CodeDeploy, Elastic Beanstalk, or Amazon S3. As a best practice, you should grant individuals only the permissions they need to perform their duties. For more information about how to restrict IAM users to a limited set of CodePipeline actions and resources, see [Remove permissions from the CodePipeline service role](how-to-custom-role.md#remove-permissions-from-policy).

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Install the AWS CLI
<a name="install-cli"></a>

To call CodePipeline commands from the AWS CLI on a local development machine, you must install the AWS CLI. This step is optional if you intend to get started using only the steps in this guide for the CodePipeline console.

**To install and configure the AWS CLI**

1. On your local machine, download and install the AWS CLI. This will enable you to interact with CodePipeline from the command line. For more information, see [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html).
**Note**  
CodePipeline works only with AWS CLI versions 1.7.38 and later. To determine which version of the AWS CLI that you may have installed, run the command **aws --version**. To upgrade an older version of the AWS CLI to the latest version, follow the instructions in [Uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-uninstall.html), and then follow the instructions in [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

1. Configure the AWS CLI with the **configure** command, as follows:

   ```
   aws configure
   ```

   When prompted, specify the AWS access key and AWS secret access key of the IAM user that you will use with CodePipeline. When prompted for the default region name, specify the Region where you will create the pipeline, such as `us-east-2`. When prompted for the default output format, specify `json`. For example:

   ```
   AWS Access Key ID [None]: {{Type your target AWS access key ID here, and then press Enter}}
   AWS Secret Access Key [None]: {{Type your target AWS secret access key here, and then press Enter}}
   Default region name [None]: {{Type}} us-east-2 {{here, and then press Enter}}
   Default output format [None]: {{Type}} json {{here, and then press Enter}}
   ```
**Note**  
For more information about IAM, access keys, and secret keys, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html) and [How Do I Get Credentials?](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html#IAM_SecurityCredentials).   
For more information about the Regions and endpoints available for CodePipeline, see [AWS CodePipeline endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/codepipeline.html).

## Open the console for CodePipeline
<a name="open-codepipeline-console"></a>
+ Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home).

## Next steps
<a name="next-steps"></a>

You have completed the prerequisites. You can begin using CodePipeline. To start working with CodePipeline, see the [CodePipeline tutorials](tutorials.md).