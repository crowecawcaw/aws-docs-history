

# Integrating AWS Marketplace with procurement systems
<a name="procurement-system-integration"></a>

You can configure procurement software to integrate with AWS Marketplace following the commerce extensible markup language (cXML) protocol. This integration creates an access point into a third party's catalog, known as a *punchout*. 

The integration differs slightly, based on the procurement system:
+ **Coupa** – Using the Coupa Open Buy feature, you can search AWS Marketplace from within Coupa. Coupa displays search results, and when the user chooses a product, they're redirected to AWS Marketplace to see the details. Alternatively, users of Coupa's procurement software can access the AWS Marketplace catalog in the **Shop Online** section of their home page. The user can also choose to start directly in AWS Marketplace to browse for products.
+ **SAP Ariba** – Ariba redirects users to AWS Marketplace to search for software and get details about a product. After an administrator configures the punchout integration, users of Ariba's procurement software can find AWS Marketplace software by choosing the **Catalog** tab, and then selecting the AWS Marketplace catalog. This redirects them to AWS Marketplace to find the products they're interested in. 

  Ariba users must initiate their purchase from within Ariba, not AWS Marketplace.

When the user wants to purchase a subscription that they're browsing in AWS Marketplace, they create a subscription request within AWS Marketplace. On the product's subscription page, instead of completing the purchase, the user requests approval. The request is sent back to a shopping cart in the procurement system to complete the approval process. The following diagram shows the process for a procurement system subscription request.

 ![Flow chart for procurement system subscription request](https://docs.aws.amazon.com/marketplace/latest/buyerguide/images/procurement-flow-01.png) 

 When the procurement system receives the request from AWS Marketplace, the procurement system starts a workflow to complete the approval process. After the request is approved, the procurement system's purchase order system automatically completes the transaction on AWS Marketplace and notifies the user that their subscription is ready to deploy. The requester doesn't need to return to AWS Marketplace to complete the purchase. However, they may want to return to AWS Marketplace for instructions on how to use the product they have purchased. AWS Marketplace sends an email message to the AWS account used to access AWS Marketplace. The email message informs the recipient that the subscription succeeded and the software is available through AWS Marketplace. The following diagram shows the approval process for a procurement system subscription request.

 ![Flowchart for procurement system subscription approval](https://docs.aws.amazon.com/marketplace/latest/buyerguide/images/procurement-flow-02.png) 

Additional notes about integrating with procurement systems include the following:
+ SaaS products with usage-based pricing let you set a budget estimate for your expected usage. You can submit this estimate through your procurement system for approval. If you choose to get pre-approval, your actual charges will be based on your real usage and billed monthly against the approved purchase order. You will be charged based on your actual usage, regardless of your initial estimate. If your actual usage exceeds your estimated amount, you may need to submit an additional purchase requisition to cover the difference.
+ Free trials don't generate an invoice in the procurement system, because they don't have a charge associated with them.
+ Server annual agreements (including AMI, container, and Helm chart options) involve both ongoing pay-as-you-go charges and a one-time upfront charge, requiring a two-step approval process. First, submit an approval request for the pay-as-you-go agreement, which defaults to $10,000 (this amount is not invoiced against). After AWS Marketplace receives the PO from this first approval, return to the procurement page to route for a second approval, which will show the total contract value. Once this second approval is complete, you'll have a final contract agreement.
+ Customers with PSI (Procurement System Integrations) can turn on pre-approvals for free products and BYOL products. There are two settings, one each for Free and BYOL. When the setting is enabled, orders are pre-approved in AWS Marketplace, and customers do not need to submit orders to their procurement system for approval. When the setting is disabled, customers will submit approvals via the **Request Approval** button to their procurement system. When the pre-approval setting for Free and BYOL products is disabled, $0.00 orders are produced in the customer's procurement system. For more information regarding Procurement System Integrations, see [https://aws.amazon.com/marketplace/features/procurementsystem](https://aws.amazon.com/marketplace/features/procurementsystem)

## UNSPSC codes used by AWS Marketplace
<a name="procurement-integration-setup-unspsc-codes"></a>

AWS Marketplace uses United Nations Standard Products and Services codes (UNSPSC) to classify line items that are sent back to the procurement cart. The code assigned to each line item depends on the line item type.


| Line item type | UNSPSC code | Description | When used | 
| --- | --- | --- | --- | 
| Service (amount-based) | 81162000 | IT Service Delivery | An offer with a single, non-usage charge (for example, a contract upfront charge). Quantity is set to 1 and the unit price equals the full charge amount. Only one invoice can post against the purchase order line. | 
| Material (quantity-based) | 43232701 | Software | Any usage-based charge (for example, pay-as-you-go (PAYG)), or an offer with more than one charge (for example, multiple flexible payment schedule (FPS) installments). Quantity is calculated from the charge amount (the amount divided by 0.01) and the unit price is $0.01. Multiple invoices can post against the purchase order line. | 

### How line item type is determined
<a name="procurement-integration-unspsc-line-item-type"></a>

AWS Marketplace automatically classifies each line item based on the pricing terms of the offer.

Service  
The line item represents an offer with a single, non-usage charge (for example, a contract upfront charge or a $0 agreement). These are amount-based line items with a quantity of 1, and only one invoice can post against the purchase order line.

Material  
The line item represents an offer that has a usage or consumption-based charge, or an offer with more than one charge (for example, multiple flexible payment schedule installments). These are quantity-based line items, and multiple invoices can post against the purchase order line.

For offers that combine both contract and usage charges (for example, a SaaS contract with additional usage pricing), the classification depends on how you choose to structure the purchase order line items:
+ **Single line item** – If any charge is usage-based, or the offer has more than one charge (for example, multiple scheduled flexible payment schedule installments), the consolidated line item is classified as Material. Only an offer with a single, non-usage charge is classified as Service.
+ **Split line items** – Each charge is classified independently. Contract charges are Service line items and usage charges are Material line items.

### Procurement system configuration
<a name="procurement-integration-unspsc-configuration"></a>

Procurement systems such as Coupa can use the UNSPSC code to automatically map line items to the correct purchasing category (for example, mapping 81162000 to a Services category).

AWS Marketplace also includes a `LineType` extrinsic in the cXML purchase order output message (POOM) that procurement systems can use for additional classification logic.