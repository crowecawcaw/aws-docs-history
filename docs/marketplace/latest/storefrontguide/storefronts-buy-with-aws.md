# Buy With AWS

Configure the Buy With AWS procurement widget, its form fields, and currency settings.

## Configuring Buy With AWS

Buy With AWS (BWA) is the procurement widget that enables buyers to initiate purchases
directly from your storefront through AWS Marketplace. When configured, buyers can
subscribe to products, accept offers, and complete procurement without leaving the
storefront experience.

### Prerequisites

- A deployed storefront with at least one product
- A connected AWS Marketplace seller account (for private offer
  creation)

### To configure Buy With AWS

1. Open the storefront and choose the **Checkout &
   Deployment** tab.
2. In the **Buy With AWS** section, enable the
   BWA toggle.
3. Configure the following settings:
4. Choose **Save**.

#### Field configuration

The default fields on the procurement request form are:

- **AWS Account ID**
- **Company Name**
- **Contact Full Name**
- **Contact Email**

You can add custom fields specific to your workflow.

#### Currency settings

Configure which currencies are available for offers created through
BWA:

1. In the **Currency** section, select the
   supported currencies.
2. Set the default currency for new offers.

#### Role-based access

Storefront-level roles control who can manage Buy With AWS requests.
Storefront Admin manages Buy With AWS requests, edits storefront content, and
views reports. Content Editor edits storefront content. Reporting Management
views storefront reports. Assign these roles in the Edit User dialog under the
Storefronts scope.

### BWA workflow

When a buyer initiates a purchase through BWA:

1. Buyer chooses **Buy With AWS** on a product in
   the storefront.
2. Buyer fills in the configured fields (AWS Account ID, Company Name,
   Contact Full Name, Contact Email).
3. The request is submitted to your team.
4. Your team creates a private offer in AWS Marketplace for the buyer.
5. Buyer receives the offer and completes acceptance through AWS
   Marketplace.

### Related topics

- [Currency settings](#currency-settings "#currency-settings")
- [Field configuration](#field-configuration "#field-configuration")
- Orders

## Field configuration

You can configure which fields appear in the Buy With AWS (BWA) procurement form that
buyers fill out when requesting a purchase from your storefront.

### Default fields

The following default fields appear on the Buy With AWS request form:

| Name              | Type  | Required     |
| ----------------- | ----- | ------------ |
| AWS Account ID    | Text  | Yes (locked) |
| Company Name      | Text  | No           |
| Contact Full Name | Text  | No           |
| Contact Email     | Email | No           |

### To configure fields

1. Open the storefront and choose the **Checkout &
   Deployment** tab.
2. In the **Buy with AWS configuration**
   section, on the **Storefront** tab, scroll to
   **Fields to be shown on the form**.
3. For each field, configure the **Name**,
   **Type**, and **Required** columns.
4. To add a custom field, choose **+ Add
   Field**.
5. Choose **Save**.

### Additional controls

On the **Storefront** and **Standalone** sub-tabs, configure the **Buyer
subscription options** (Free Trial, Private Offer, Public Offer), the
required **Seller ID**, and the **Enable Buy with AWS on location** dropdown (Homepage and Product
page).

### Field display order

Fields appear in the BWA form in the order listed in the configuration. To reorder
fields, drag them to the desired position.

### Buyer experience

When a buyer chooses **Buy With AWS** on a
product:

1. A form appears with the configured fields.
2. Required fields are marked with an asterisk (\*).
3. The buyer fills in the form and submits.
4. The request appears in your BWA requests queue for processing.

### Notes

- Changes to field configuration apply to new BWA requests only.
- Custom fields are stored with the request and visible in the request
  detail view.

### Related topics

- [Configuring Buy With AWS](#configuring-bwa "#configuring-bwa")
- Custom roles

## Currency settings

You can configure which currencies are available for offers created through the Buy
With AWS (BWA) procurement widget on your storefront.

### To configure currencies

1. Open the storefront and choose the **Checkout &
   Deployment** tab.
2. In the **Buy with AWS configuration**
   section, turn on **Enable Currency**, then set
   **Default Currency** and **Allowed Currencies**.
3. Choose **Save**.

### Supported currencies

AWS Marketplace Storefront supports all currencies available through AWS
Marketplace private offers. The currency selected applies to the private offer
created from the BWA request.

### Notes

- Currency selection affects the offer creation workflow only. Actual
  billing and invoicing currencies are determined by AWS Marketplace.
- If you support multiple currencies, buyers see a currency selector in the
  BWA form.
- Changes to currency settings apply to new BWA requests only. Existing
  requests retain their original currency.

### Related topics

- [Configuring Buy With AWS](#configuring-bwa "#configuring-bwa")
- [Field configuration](#field-configuration "#field-configuration")
