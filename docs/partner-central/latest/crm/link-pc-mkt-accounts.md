# Linking your AWS Partner Central and AWS Marketplace accounts

The following steps explain how to link your AWS Partner Central and AWS Marketplace seller accounts. You must be have Salesforce alliance lead permissions to complete these steps.
You must link the accounts before you can create any type of CRM integration.

###### To link the accounts

1. Do the following:
   - Sign in to your AWS Partner Central account as an alliance lead or cloud administrator.
   - Sign in to your AWS Marketplace seller account.

2. On the Partner Central home page, in the In the upper-right corner, choose **Link accounts**.

The **Account linking prerequisites** dialog box appears. 3. Choose **Continue to account linking**, then choose **Initiate account linking**.

That takes you to the AWS Console and your AWS Marketplace seller account. 4. Do the following:

    1. Ensure the correct value appears under **AWS account ID**.
    2. In the **Legal business name** box, enter the legal name of your business.
    3. Choose **Next**.That returns you to Partner Central and the **Standard IAM roles** page.

5. Select the following checkboxes:
   - Under **Cloud admin IAM role**, choose **Assign PartnerCentralRoleForCloudAdmin-###
     role to the AWS Partner Central alliance lead and all active cloud admin users**.
   - Under **Alliance team IAM role**, choose **Assign PartnerCentralRoleForAlliance-###
     role to all active AWS Partner Central alliance team users**.
   - Under **ACE IAM role**, choose **Assign PartnerCentralRoleForAce-###
     role to the AWS Partner Central ACE managers and users.**.

6. Choose **Next**, then choose **Link accounts**.
   Success messages appear when the linking process finishes.
