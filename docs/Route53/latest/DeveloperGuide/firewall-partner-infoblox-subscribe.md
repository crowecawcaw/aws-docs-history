

# Subscribe to Infoblox DNS threat protection

You can subscribe to Infoblox directly from the DNS Firewall console during the rule creation flow, or from AWS Marketplace. When you subscribe, you authorize AWS to share DNS query metadata with Infoblox.

**Subscribe through the DNS Firewall console (recommended)**  
Use the following procedure to subscribe through the console.

1. Sign in to the AWS Management Console and open the Amazon Virtual Private Cloud console.

1. In the navigation pane, under **DNS Firewall**, choose **Rule groups**.

1. Select the rule group where you want to add partner managed DNS protections.

1. Choose **Add rule**.

1. Under **Rule details**, enter a **Name** for the rule (for example, `Infoblox Threat Protection Rule`). Valid characters: A-Z, a-z, 0-9, hyphen (-), and underscore (\_). Maximum 64 characters. Select the **Advanced** pricing option.

1. Under **Rule configurations** > **Rule type**, select **Partner managed DNS threat protection**.

1. Under **Vendor**, select **Infoblox**.

If you are not yet subscribed, a banner appears indicating that a subscription is required through AWS Marketplace for Infoblox.

1. Choose **View subscription options**. A subscription dialog appears showing available offers, pricing details, and legal terms.

1. Review the terms and pricing, then choose **Subscribe**.

1. Wait for the subscription to process. A status banner indicates that your AWS Marketplace subscription is being processed. The form updates automatically when your subscription is active.

1. After your subscription is active, the DNS security categories dropdown becomes available, so you can select threat list feeds for rule creation.

**Subscribe through AWS Marketplace**  
Use the following procedure to subscribe through Marketplace.

1. Open the AWS Marketplace console.

1. Search for **Infoblox**, and choose the Infoblox DNS threat protection product for DNS Firewall.

1. Review the product listing, pricing, and terms.

1. Choose **Subscribe**.

1. After subscribing, return to the DNS Firewall console to create rules using the partner managed rule type.

**Note**  
When you subscribe through the Marketplace console, you are redirected to the seller's home page. If you subscribe through the DNS Firewall console, you are not redirected. We recommend that you visit the seller's home page separately to complete any required registration details.