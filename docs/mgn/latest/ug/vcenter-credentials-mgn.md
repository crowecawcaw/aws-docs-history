

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Generating vCenter Client IAM credentials
<a name="vcenter-credentials-mgn"></a>

In order to use the MGN vCenter Client, you must first generate the correct IAM credentials.

You need to create at least one AWS Identity and Access Management (IAM) user, and assign the proper permission policies to this user. Obtain an Access key ID and Secret access key, which you need to enter into the Agent installation prompt in order to begin the installation. We recommend that you use **IAM access last used information** to rotate and remove access keys safely. For more information, see [Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey).

1. Open the **AWS Management Console** and look for **IAM** under **Find Services**.

1. From the **IAM** main page, choose **Users** from the left-hand navigation menu.

1. You can either select an existing user or add a new user. To add a new user, choose **Add user**.

1. Give the user a **User name** and select the **Programmatic access** access type. Choose **Next: Permissions**. 

1. Choose the **Attach existing policies directly** option. Search for **AWSApplicationMigrationVCenterClientPolicy** and **AWSApplicationMigrationAgentPolicy**. Select the policies and choose **Next: Tags.**

1. Add tags if you wish to use them and then choose **Next: Review.** 

1. Review the information. Ensure that the **Programmatic access** type is selected and that the correct policy is attached to the user. Choose **Create user**.

1. A confirmation message appears and you can see the **Access key ID** and **Secret access key** that you need in order to install the AWS Replication Agent on your source servers. 

   To save this information as .csv file, choose **Download .csv**. 

   You can also access this information and re-generate your security credentials by navigating to **IAM > Users > Your user**.

   Open the **Security credentials** tab and scroll down to **Access keys**. Here you can manage your access keys (create, delete, and more). 