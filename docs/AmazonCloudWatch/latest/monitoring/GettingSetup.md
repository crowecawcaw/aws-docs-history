# Getting set up

To use Amazon CloudWatch you need an AWS account. Your AWS account allows you to use services (for example,
 Amazon EC2) to generate metrics that you can view in the CloudWatch console, a point-and-click
 web-based interface. In addition, you can install and configure the AWS command line
 interface (CLI).


## Sign up for an AWS account


If you do not have an AWS account, complete the following steps to create one.


###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.


Part of the sign-up procedure involves receiving a phone call or text message and entering 
 a verification code on the phone keypad.


When you sign up for an AWS account, an *AWS account root user* is created. The root user has access to all AWS services
 and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
 Account**.


## Create a user with administrative access


After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you 
don't use the root user for everyday tasks.


###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.


For help signing in by using root user, see [Signing in as the root user](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial "https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial") in the *AWS Sign-In User Guide*.
2. Turn on multi-factor authentication (MFA) for your root user.


For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html") in the *IAM User Guide*.

###### Create a user with administrative access

1. Enable IAM Identity Center.


For instructions, see [Enabling
 AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
 *AWS IAM Identity Center User Guide*.
2. In IAM Identity Center, grant administrative access to a user.


For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
 *AWS IAM Identity Center User Guide*.

###### Sign in as the user with administrative access

* To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.


For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html "https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html") in the *AWS Sign-In User Guide*.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.


For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the *AWS IAM Identity Center User Guide*.
2. Assign users to a group, and then assign single sign-on access to the group.


For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the *AWS IAM Identity Center User Guide*.

## Sign in to the Amazon CloudWatch console


###### To sign in to the Amazon CloudWatch console

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, use the navigation bar to change the Region to the Region where you have your AWS resources.
3. Even if this is the first time you are using the CloudWatch console, **Your Metrics** 
 could already report metrics, because you have used an AWS product that automatically pushes metrics 
 to Amazon CloudWatch for free. Other services require that you enable metrics.


If you do not have any alarms, the **Your Alarms** section will
 have a **Create Alarm** button.

## Set up the AWS CLI


You can use the AWS CLI or the Amazon CloudWatch CLI to perform CloudWatch commands. 
 Note that the AWS CLI replaces the CloudWatch CLI; we include new CloudWatch features only in the AWS CLI.


For information about how to install and configure the AWS CLI, see 
 [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html") 
 in the *AWS Command Line Interface User Guide*.


For information about how to install and configure the Amazon CloudWatch CLI, see 
 [Set Up the Command Line Interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/SetupCLI.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/SetupCLI.html") 
 in the *Amazon CloudWatch CLI Reference*.
