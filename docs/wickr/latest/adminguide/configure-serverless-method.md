This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Configure serverless method

## STEP 1: Access serverless method

Complete the following procedure to access the serverless method.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **Network policies**, and
   then select **Data retention**.
4. On step 1 for **Install/Config data retention module**, review the comparison
   of Docker-bot vs. Serverless type.
5. Choose **Serverless** from module type.

## STEP 2: Import Service Catalog Portfolio

Complete the following procedure to import a service catalog portfolio. The
Wickr console will provide you with a Service Catalog Portfolio ID.

1. Copy the provided Portfolio ID.
2. Open the AWS Service Catalog, and select the
   **Portfolios** page.
3. Choose **Actions**, and then select
   **Import**.
4. Paste the Portfolio ID.
5. Open the imported Wickr Bot Products portfolio and grant access to your
   current AWS role.
6. Select the **Products** tab, and then choose
   **Wickr Network Data Retention**.
7. Choose **Launch product** in the top right.
8. Enter a provisioned product name and set the Network ID parameter to
   <Your Network ID>.

For more information on setting up custom KMS key for your product, see
[Custom KMS key setup for data retention service](custom-kms-key.md "custom-kms-key.md"). 9. Wait for the provisioned product to reach **Available**
status. Then, return to this page to activate serverless.

## STEP 3: Complete setup in Wickr console

1. Return to the AWS Wickr Console **Data Retention**
   page.
2. Once the product is installed, select the **Active**
   checkbox and choose **Save and continue**.

###### Note

If you are migrating from docker data retention, see [Password recovery instruction](password-recovery-instruction.md "password-recovery-instruction.md") before activating serverless. 3. Once the bot is activated, on step 2 for **Enable/Disable data
retention**, toggle the data retention status to
**enable** and choose **submit**.

## STEP 4: Verify configuration

After configuration is complete, return to the AWS Wickr Console Data Retention page and verify the following:

- The module status overview shows Serverless as **Active**.
- Data retention status is set to **Enabled**.

If both conditions are met, data retention is active and messages in your network will be retained.

All clients in your network will receive a banner notification informing them that
data retention is enabled.
