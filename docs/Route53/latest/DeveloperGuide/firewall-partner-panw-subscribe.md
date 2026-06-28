# Subscribe to Palo Alto Networks Advanced DNS Security

You can subscribe to Palo Alto Networks Advanced DNS Security directly from the
DNS Firewall console during the rule creation flow, or from AWS Marketplace. When you
subscribe, you authorize AWS to share DNS query metadata with Palo Alto
Networks.

###### Subscribe through the DNS Firewall console (recommended)

Use the following procedure to subscribe through the console.

1. Sign in to the AWS Management Console and open the Amazon Virtual Private Cloud
   console.
2. In the navigation pane, under **DNS Firewall**, choose
   **Rule groups**.
3. Select the rule group where you want to add partner managed DNS
   protections.
4. Choose **Add rule**.
5. Under **Rule details**, enter a
   **Name** for the rule (for example, `PAN Threat Protection
 Rule`). Valid characters: A-Z, a-z, 0-9, hyphen (-), and underscore (\_).
   Maximum 64 characters. Select the **Advanced** pricing
   option.
6. Under **Rule configurations** >
   **Rule type**, select **Partner managed DNS threat
   protection**.
7. Under **Vendor**, select **Palo Alto
   Networks**.
   If you are not yet subscribed, a banner appears indicating that a subscription is
   required through AWS Marketplace for Palo Alto Networks.

8. Choose **View subscription options**. A subscription
   dialog appears showing available offers, pricing details, and legal
   terms.
9. Review the terms and pricing, then choose
   **Subscribe**.
10. Wait for the subscription to process. A status banner indicates that your
    AWS Marketplace subscription is being processed. The form updates
    automatically when your subscription is active.
11. After successful subscription, the DNS security categories dropdown becomes
    available, allowing you to select threat list feeds for rule
    creation.

###### Subscribe through AWS Marketplace

Use the following procedure to subscribe through Marketplace.

1. Open the AWS Marketplace console.
2. Search for the "Palo Alto Networks Advanced DNS Security for Amazon
   Route 53" product.
3. Review the product listing, pricing, and terms.
4. Choose **Subscribe**.
5. After subscribing, return to the DNS Firewall console to create rules using the
   partner managed rule type.

###### Note

When subscribing through the Marketplace console, you are redirected to the
seller's home page. If you subscribe through the DNS Firewall console, you are not
redirected. We recommend visiting the seller's home page separately to complete
any required registration details.
