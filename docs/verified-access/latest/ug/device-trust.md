# Device-based trust providers for Verified Access

You can use device trust providers with AWS Verified Access. You can use one or multiple
device trust providers with your Verified Access instance.

###### Contents

- [Supported device trust providers](#supported-trust-providers "#supported-trust-providers")
- [Create a device-based trust provider](#create-device-trust "#create-device-trust")
- [Modify a device-based trust provider](#modify-device-trust "#modify-device-trust")
- [Delete a device-based trust provider](#delete-device-trust "#delete-device-trust")

## Supported device trust providers

The following device trust providers can be integrated with Verified Access:

- CrowdStrike – [Securing private applications with CrowdStrike and AWS Verified Access](https://github.com/CrowdStrike/Cloud-AWS/tree/main/verified-access "https://github.com/CrowdStrike/Cloud-AWS/tree/main/verified-access")
- Jamf – [Integrating Verified Access with Jamf Device Identity](https://learn.jamf.com/en-US/bundle/technical-paper-aws-verified-access/page/Overview.html "https://learn.jamf.com/en-US/bundle/technical-paper-aws-verified-access/page/Overview.html")
- JumpCloud – [Integrating JumpCloud and AWS Verified Access](https://jumpcloud.com/support/integrate-with-aws-verified-access "https://jumpcloud.com/support/integrate-with-aws-verified-access")

## Create a device-based trust provider

Follow these steps to create and configure a device trust provider to use with
Verified Access.

###### To create a Verified Access device trust provider (AWS console)

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access trust providers**, and
   then **Create Verified Access trust provider**.
3. (Optional) For **Name tag** and **Description**,
   enter a name and description for the trust provider.
4. Enter an identifier to use later when working with policy rules for **Policy
   reference name**.
5. For **Trust provider type**, select **Device
   identity**.
6. For **Device identity type**, choose **Jamf**,
   **CrowdStrike**, or **JumpCloud**.
7. For **Tenant ID**, enter the identifier of the tenant
   application.
8. (Optional) For **Public signing key URL**, enter the unique key URL
   shared by your device trust provider. (This parameter is not required for Jamf,
   CrowdStrike or Jumpcloud.)
9. Choose **Create Verified Access trust provider**.

###### Note

You will need to add a redirect URI to your OIDC provider's allowlist. You will want
to use the `DeviceValidationDomain` of the Verified Access endpoint for this purpose.
This can be found in the AWS Management Console, under the **Details** tab for your
Verified Access endpoint or by using the AWS CLI to describe the endpoint. Add the following to
your OIDC provider's allowlist:
https://`DeviceValidationDomain`/oauth2/idpresponse

###### To create a Verified Access device trust provider (AWS CLI)

- [create-verified-access-trust-provider](../../../cli/latest/reference/ec2/create-verified-access-trust-provider.md "../../../cli/latest/reference/ec2/create-verified-access-trust-provider.md") (AWS CLI)

## Modify a device-based trust provider

After you create a trust provider, you can update its configuration.

###### To modify a Verified Access device trust provider (AWS console)

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access trust
   providers**.
3. Select the trust provider.
4. Choose **Actions**, then select **Modify Verified Access trust
   provider**.
5. Modify the description as needed.
6. (Optional) For **Public signing key URL**, modify the unique key
   URL shared by your device trust provider. (This parameter is not required if your device
   trust provider is Jamf, CrowdStrike or Jumpcloud.)
7. Choose **Modify Verified Access trust provider**.

###### To modify a Verified Access device trust provider (AWS CLI)

- [modify-verified-access-trust-provider](../../../cli/latest/reference/ec2/modify-verified-access-trust-provider.md "../../../cli/latest/reference/ec2/modify-verified-access-trust-provider.md") (AWS CLI)

## Delete a device-based trust provider

When you are finished with a trust provider, you can delete it.

###### To delete a Verified Access device trust provider (AWS console)

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access trust
   providers**.
3. Select the trust provider you want to delete under **Verified Access trust
   providers**.
4. Choose **Actions**, then select **Delete Verified Access trust
   provider**.
5. When prompted for confirmation, enter `delete`, and then choose
   **Delete**.

###### To delete a Verified Access device trust provider (AWS CLI)

- [delete-verified-access-trust-provider](../../../cli/latest/reference/ec2/delete-verified-access-trust-provider.md "../../../cli/latest/reference/ec2/delete-verified-access-trust-provider.md") (AWS CLI)
