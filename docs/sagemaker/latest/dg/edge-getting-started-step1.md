# Setting Up

Before you begin using SageMaker Edge Manager to manage models on your device fleets, you
must first create IAM Roles for both SageMaker AI and AWS IoT. You will also want to create at
least one Amazon S3 bucket where you will store your pre-trained model, the output of your
SageMaker Neo compilation job, as well as input data from your edge devices.

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Create roles and storage

SageMaker Edge Manager needs access to your Amazon S3 bucket URI. To facilitate this,
create an IAM role that can run SageMaker AI and has permission to access Amazon S3. Using
this role, SageMaker AI can run under your account and access to your Amazon S3
bucket.

You can create an IAM role by using the IAM console, AWS SDK for Python
(Boto3), or AWS CLI. The following is an example of how to create an IAM role,
attach the necessary policies with the IAM console, and create an Amazon S3 bucket.

1.  **Create an IAM role for Amazon SageMaker AI.**
    1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. In the navigation pane of the IAM console, choose
       **Roles**, and then choose **Create
       role**.
    3. For **Select type of trusted entity**, choose
       **AWS service**.
    4. Choose the service that you want to allow to assume this role. In this
       case, choose **SageMaker AI**. Then choose **Next:
       Permissions**.
       - This automatically creates an IAM policy that grants access
         to related services such as Amazon S3, Amazon ECR, and CloudWatch Logs.

    5. Choose **Next: Tags**.
    6. (Optional) Add metadata to the role by attaching tags as key–value
       pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md").
    7. Choose **Next: Review**.
    8. Type in a **Role name**.
    9. If possible, type a role name or role name suffix. Role names must be
       unique within your AWS account. They are not distinguished by case. For
       example, you cannot create roles named both `PRODROLE` and
       `prodrole`. Because other AWS resources might reference
       the role, you cannot edit the name of the role after it has been
       created.
    10. (Optional) For **Role description**, type a
        description for the new role.
    11. Review the role and then choose **Create
        role**.

    Note the SageMaker AI Role ARN, which you use to create a compilation job with
    SageMaker Neo and a packaging job with Edge Manager. To find out the role ARN
    using the console, do the following:

        1. Go to the IAMconsole: [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")
        2. Select **Roles**.
        3. Search for the role you just created by typing in the name of
         the role in the search field.
        4. Select the role.
        5. The role ARN is at the top of the **Summary**
         page.

2.  **Create an IAM role for AWS IoT.**

The AWS IoT IAM role you create is used to authorize your thing objects. You
also use the IAM role ARN to create and register device fleets with a SageMaker AI
client object.

Configure an IAM role in your AWS account for the credentials provider to
assume on behalf of the devices in your device fleet. Then, attach a policy to
authorize your devices to interact with AWS IoT services.

Create a role for AWS IoT either programmatically or with the IAM console,
similar to what you did when you created a role for SageMaker AI.

    1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. In the navigation pane of the IAM console, choose
     **Roles**, and then choose **Create
     role**.
    3. For **Select type of trusted entity**, choose
     **AWS service**.
    4. Choose the service that you want to allow to assume this role. In this
     case, choose **IoT**. Select **IoT**
     as the **Use Case**.
    5. Choose **Next: Permissions**.
    6. Choose **Next: Tags**.
    7. (Optional) Add metadata to the role by attaching tags as key–value
     pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md").
    8. Choose **Next: Review**.
    9. Type in a **Role name**. The role name must start
     with `SageMaker AI`.
    10. (Optional) For **Role description**, type a
     description for the new role.
    11. Review the role and then choose **Create
     role**.
    12. Once the role is created, choose **Roles** in the
     IAM console. Search for the role you created by typing in role name in
     the **Search** field.
    13. Choose your role.
    14. Next, choose **Attach Policies**.
    15. Search for `AmazonSageMakerEdgeDeviceFleetPolicy` in the
     **Search** field. Select
     `AmazonSageMakerEdgeDeviceFleetPolicy`.
    16. Choose **Attach policy**.
    17. Add the following policy statement to the trust relationship:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {"Service": "credentials.iot.amazonaws.com"},
     "Action": "sts:AssumeRole"
     },
     {
     "Effect": "Allow",
     "Principal": {"Service": "sagemaker.amazonaws.com"},
     "Action": "sts:AssumeRole"
     }
     ]
    }`

    ```





    A trust policy is a [JSON
     policy document](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") in which you define the principals that
     you trust to assume the role. For more information about trust
     policies, see [Roles terms and concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md").
    18. Note the AWS IoT role ARN. You use the AWS IoT Role ARN to create and
     register the device fleet. To find the IAM role ARN with the
     console:


    	1. Go to the IAM console: [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")
    	2. Choose **Roles**.
    	3. Search for the role you created by typing in the name of the
    	 role in the **Search** field.
    	4. Select the role.
    	5. The role ARN is on the Summary page.

3. **Create an Amazon S3 bucket.**

SageMaker Neo and Edge Manager access your pre-compiled model and compiled model
from an Amazon S3 bucket. Edge Manager also stores sample data from your device fleet
in Amazon S3.

    1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
    2. Choose **Create bucket**.
    3. In **Bucket name**, enter a name for your
     bucket.
    4. In **Region**, choose the AWS Region where you want
     the bucket to reside.
    5. In **Bucket settings for Block Public Access**,
     choose the settings that you want to apply to the bucket.
    6. Choose **Create bucket**.For more information about creating Amazon S3 buckets, see [Getting started with Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md").
