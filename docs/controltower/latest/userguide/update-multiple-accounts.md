# Update multiple accounts in the same OU

Repeat these steps for each OU in your AWS Control Tower organization, if you need to update
all of your accounts and OUs.

###### To update multiple accounts in one OU, with one action

1. Sign in to the AWS Control Tower console at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/controltower "https://console.aws.amazon.com/controltower").
2. In the left-pane navigation menu, choose **Organization** .
3. On the **Organization** page, choose any OU to view the
   **OU details** page.
4. If AWSControlTowerBaseline is enabled on the OU, select **Re-Register OU**
   under **Actions**. If AWSControlTowerBaseline is not enabled on the OU,
   select **Reset AWS Config baseline** under **Actions**
   to reset enabled baseline and select enabled controls and **Reset control**
   under "Enabled controls" section to reset enabled controls.
   Alternatively, you can select any account that shows a status of **Update
   available** and then choose **Update account**, for as
   many accounts as needed.
