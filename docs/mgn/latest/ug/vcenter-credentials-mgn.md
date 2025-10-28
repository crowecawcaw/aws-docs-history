NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Generating vCenter Client IAM credentials

In order to use the Application Migration Service vCenter Client, you must first generate the correct IAM
credentials.

You need to create at least one AWS Identity and Access Management (IAM) user, and assign the proper
permission policies to this user. Obtain an Access key ID and Secret access key, which
you need to enter into the Agent installation prompt in order to begin the installation. We
recommend that you use **IAM access last used information** to
rotate and remove access keys safely. For more information, see [Rotating access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey").

1. Open the **AWS Management Console** and look for **IAM** under **Find Services**.
2. From the **IAM** main page, choose **Users** from the left-hand navigation menu.
3. You can either select an existing user or add a new user. To add a new user, click
   **Add user**.
4. Give the user a **User name** and select the **Programmatic access** access type. Click **Next:
   Permissions**.
5. Choose the **Attach existing policies directly** option.
   Search for **AWSApplicationMigrationVCenterClientPolicy** and
   **AWSApplicationMigrationAgentPolicy**. Select the policies and
   click **Next: Tags.**
6. Add tags if you wish to use them and then click **Next:
   Review.**
7. Review the information. Ensure that the **Programmatic
   access** type is selected and that the correct policy is attached to the user.
   Choose **Create user**.
8. A confirmation message appears and you can see the **Access key
   ID** and **Secret access key** that you need in
   order to install the AWS Replication Agent on your source servers.

To save this information as .csv file, click **Download
.csv**.

You can also access this information and re-generate your security credentials by
navigating to **IM > Users > Your user**.

Open the **Security credentials** tab and scroll down to
**Access keys**. Here you can manage your access keys (create,
delete, and more).
