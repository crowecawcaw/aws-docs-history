• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Changing identity providers

By default, just-in-time node access uses IAM for an identity provider. After
enabling just-in-time node access, customers using the unified console with an
organization can modify this setting to use IAM Identity Center. Just-in-time node
access doesn't support IAM Identity Center as an identity provider when set up for
a single account and Region.

The following procedure describes how to modify the identity provider for
just-in-time node access.

###### To modify identity providers

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **User identity** section, select
   **Edit**.
5. Choose **AWS IAM Identity Center**.
6. Select **Save**.
