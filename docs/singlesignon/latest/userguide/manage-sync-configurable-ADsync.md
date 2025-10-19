# First-time Active Directory to IAM Identity Center sync
 setup

If you are synchronizing your users and groups from Active Directory into IAM Identity Center for the
 first time, follow these steps. Alternatively, you can follow steps outlined in [Change your identity source](manage-your-identity-source-change.md "manage-your-identity-source-change.md") to change your identity source from
 IAM Identity Center to Active Directory.


## Guided setup


1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").


###### Note

Make sure that the IAM Identity Center console is using one of the AWS Regions where your
 AWS Managed Microsoft AD directory is located before you move to the next step.
2. Choose **Settings**.
3. At the top of the page, in the notification message, choose **Start guided
 setup**.
4. In **Step 1 – *optional*: Configure attribute
 mappings**, review the default user and group attribute mappings. If no
 changes are required, choose **Next**. If changes are required, make
 the changes, and then choose **Save changes**.
5. In **Step 2 – *optional*: Configure sync
 scope**, choose the **Users** tab. Then, enter the exact
 username of the user that you want to add to your sync scope and choose
 **Add**. Next, choose the **Groups** tab. Enter
 the exact group name of the group that you want to add to your sync scope and choose
 **Add**. Then, choose **Next**. If you want to add
 users and groups to your sync scope later, make no changes and choose
 **Next**.
6. In **Step 3: Review and save configuration**, confirm your
 **Attribute mappings** in **Step 1: Attribute
 mappings** and your **Users and groups** in **Step
 2: Sync scope**. Choose **Save configuration**. This takes
 you to the **Manage Sync** page.
