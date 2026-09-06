

# Buy With AWS
<a name="storefronts-buy-with-aws"></a>

Configure the Buy With AWS procurement widget, its form fields, and currency settings.

## Configuring Buy With AWS
<a name="configuring-bwa"></a>

Buy With AWS (BWA) is the procurement widget that enables buyers to initiate purchases directly from your storefront through AWS Marketplace. When configured, buyers can subscribe to products, accept offers, and complete procurement without leaving the storefront experience.

### Prerequisites
<a name="configuring-bwa-prerequisites"></a>
+ A deployed storefront with at least one product
+ A connected AWS Marketplace seller account (for private offer creation)

### To configure Buy With AWS
<a name="configuring-bwa-configure"></a>

1. Open the storefront and choose the **Checkout & Deployment** tab.

1. In the **Buy With AWS** section, enable the BWA toggle.

1. Configure the following settings:

1. Choose **Save**.

#### Field configuration
<a name="configuring-bwa-fields"></a>

The default fields on the procurement request form are:
+ **AWS Account ID**
+ **Company Name**
+ **Contact Full Name**
+ **Contact Email**

You can add custom fields specific to your workflow.

#### Currency settings
<a name="configuring-bwa-currency"></a>

Configure which currencies are available for offers created through BWA:

1. In the **Currency** section, select the supported currencies.

1. Set the default currency for new offers.

#### Role-based access
<a name="configuring-bwa-roles"></a>

Storefront-level roles control who can manage Buy With AWS requests. Storefront Admin manages Buy With AWS requests, edits storefront content, and views reports. Content Editor edits storefront content. Reporting Management views storefront reports. Assign these roles in the Edit User dialog under the Storefronts scope.

### BWA workflow
<a name="configuring-bwa-workflow"></a>

When a buyer initiates a purchase through BWA:

1. Buyer chooses **Buy With AWS** on a product in the storefront.

1. Buyer fills in the configured fields (AWS Account ID, Company Name, Contact Full Name, Contact Email).

1. The request is submitted to your team.

1. Your team creates a private offer in AWS Marketplace for the buyer.

1. Buyer receives the offer and completes acceptance through AWS Marketplace.

### Related topics
<a name="configuring-bwa-related"></a>
+ [Currency settings](#currency-settings)
+ [Field configuration](#field-configuration)
+ Orders

## Field configuration
<a name="field-configuration"></a>

You can configure which fields appear in the Buy With AWS (BWA) procurement form that buyers fill out when requesting a purchase from your storefront.

### Default fields
<a name="field-configuration-default"></a>

The following default fields appear on the Buy With AWS request form:


| Name | Type | Required | 
| --- | --- | --- | 
| AWS Account ID | Text | Yes (locked) | 
| Company Name | Text | No | 
| Contact Full Name | Text | No | 
| Contact Email | Email | No | 

### To configure fields
<a name="field-configuration-configure"></a>

1. Open the storefront and choose the **Checkout & Deployment** tab.

1. In the **Buy with AWS configuration** section, on the **Storefront** tab, scroll to **Fields to be shown on the form**.

1. For each field, configure the **Name**, **Type**, and **Required** columns.

1. To add a custom field, choose **\+ Add Field**.

1. Choose **Save**.

### Additional controls
<a name="field-configuration-additional"></a>

On the **Storefront** and **Standalone** sub-tabs, configure the **Buyer subscription options** (Free Trial, Private Offer, Public Offer), the required **Seller ID**, and the **Enable Buy with AWS on location** dropdown (Homepage and Product page).

### Field display order
<a name="field-configuration-order"></a>

Fields appear in the BWA form in the order listed in the configuration. To reorder fields, drag them to the desired position.

### Buyer experience
<a name="field-configuration-experience"></a>

When a buyer chooses **Buy With AWS** on a product:

1. A form appears with the configured fields.

1. Required fields are marked with an asterisk (\*).

1. The buyer fills in the form and submits.

1. The request appears in your BWA requests queue for processing.

### Notes
<a name="field-configuration-notes"></a>
+ Changes to field configuration apply to new BWA requests only.
+ Custom fields are stored with the request and visible in the request detail view.

### Related topics
<a name="field-configuration-related"></a>
+ [Configuring Buy With AWS](#configuring-bwa)
+ Custom roles

## Currency settings
<a name="currency-settings"></a>

You can configure which currencies are available for offers created through the Buy With AWS (BWA) procurement widget on your storefront.

### To configure currencies
<a name="currency-settings-configure"></a>

1. Open the storefront and choose the **Checkout & Deployment** tab.

1. In the **Buy with AWS configuration** section, turn on **Enable Currency**, then set **Default Currency** and **Allowed Currencies**.

1. Choose **Save**.

### Supported currencies
<a name="currency-settings-supported"></a>

AWS Marketplace Storefront supports all currencies available through AWS Marketplace private offers. The currency selected applies to the private offer created from the BWA request.

### Notes
<a name="currency-settings-notes"></a>
+ Currency selection affects the offer creation workflow only. Actual billing and invoicing currencies are determined by AWS Marketplace.
+ If you support multiple currencies, buyers see a currency selector in the BWA form.
+ Changes to currency settings apply to new BWA requests only. Existing requests retain their original currency.

### Related topics
<a name="currency-settings-related"></a>
+ [Configuring Buy With AWS](#configuring-bwa)
+ [Field configuration](#field-configuration)