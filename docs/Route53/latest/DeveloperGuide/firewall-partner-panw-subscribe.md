

# Subscribe to Palo Alto Networks Advanced DNS Security
<a name="firewall-partner-panw-subscribe"></a>

You can subscribe to Palo Alto Networks Advanced DNS Security directly from the DNS Firewall console during the rule creation flow, or from AWS Marketplace. When you subscribe, you authorize AWS to share DNS query metadata with Palo Alto Networks.

**Subscribe through the DNS Firewall console (recommended)**  
Use the following procedure to subscribe through the console.

1. Sign in to the AWS Management Console and open the Amazon Virtual Private Cloud console.

1. In the navigation pane, under **DNS Firewall**, choose **Rule groups**.

1. Select the rule group where you want to add partner managed DNS protections.

1. Choose **Add rule**.

1. Under **Rule details**, enter a **Name** for the rule (for example, `PAN Threat Protection Rule`). Valid characters: A-Z, a-z, 0-9, hyphen (-), and underscore (\_). Maximum 64 characters. Select the **Advanced** pricing option.

1. Under **Rule configurations** > **Rule type**, select **Partner managed DNS threat protection**.

1. Under **Vendor**, select **Palo Alto Networks**.

If you are not yet subscribed, a banner appears indicating that a subscription is required through AWS Marketplace for Palo Alto Networks.

1. Choose **View subscription options**. A subscription dialog appears showing available offers, pricing details, and legal terms.

1. Review the terms and pricing, then choose **Subscribe**.

1. Wait for the subscription to process. A status banner indicates that your AWS Marketplace subscription is being processed. The form updates automatically when your subscription is active.

1. After successful subscription, the DNS security categories dropdown becomes available, allowing you to select threat list feeds for rule creation.

**Subscribe through AWS Marketplace**  
Use the following procedure to subscribe through Marketplace.

1. Open the AWS Marketplace console.

1. Search for the "Palo Alto Networks Advanced DNS Security for Amazon Route 53" product.

1. Review the product listing, pricing, and terms.

1. Choose **Subscribe**.

1. After subscribing, return to the DNS Firewall console to create rules using the partner managed rule type.

**Note**  
When subscribing through the Marketplace console, you are redirected to the seller's home page. If you subscribe through the DNS Firewall console, you are not redirected. We recommend visiting the seller's home page separately to complete any required registration details.