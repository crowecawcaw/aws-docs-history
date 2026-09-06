

# HubSpot connector
<a name="connector-hubspot"></a>

Use the HubSpot connector to synchronize deal, company, and contact data with HubSpot.

## HubSpot connector
<a name="hubspot"></a>

The HubSpot connector synchronizes deal, company, and contact data between AWS Marketplace Storefront and your HubSpot CRM.

### Prerequisites
<a name="hubspot-prerequisites"></a>
+ A HubSpot account with API access (Professional or Enterprise tier)
+ Super Admin or appropriate permissions in HubSpot
+ Owner or Admin role at the organization level

### To connect HubSpot
<a name="hubspot-to-connect-hubspot"></a>

The HubSpot connector wizard has four steps: Connect; Connect to HubSpot; Create or edit field-mapping template; Configure.

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Connectors** tab.

1. Find **HubSpot** and choose **Connect**.

1. Enter the **Email**, choose a **Seller Account**, then choose **Save**.

### Configuration
<a name="hubspot-configuration"></a>

#### Field mapping
<a name="hubspot-field-mapping"></a>

For each row, choose one of three options: use an existing HubSpot property, create a new HubSpot property by entering a Display Name, or set a default value.

Select the **Create on HubSpot** checkbox to create a property in HubSpot that does not already exist.

The following table shows sample mappings for Customer > Account:


| HubSpot Property Name | HubSpot Display Name | Ace Default Value | 
| --- | --- | --- | 
| Company Name | Company Name |  | 
| Website Url | Website Url |  | 
| Industry | Industry |  | 

1. In the HubSpot connector settings, choose **Field Mapping**.

1. Map each field by choosing a property, entering a Display Name, or setting a default value.

1. Choose **Save**.

#### Sync settings
<a name="hubspot-sync-settings"></a>


| Setting | Description | 
| --- | --- | 
| Sync direction | Bidirectional or one-way | 
| Sync trigger | Real-time or scheduled (hourly, daily) | 
| Pipeline mapping | Map Storefront stages to HubSpot deal stages | 

### What syncs
<a name="hubspot-what-syncs"></a>


| Direction | Data | 
| --- | --- | 
| Storefront → HubSpot | New deals from offers/BWA requests, status updates | 
| HubSpot → Storefront | Deal stage changes, revenue updates, contact info | 

### To disconnect
<a name="hubspot-to-disconnect"></a>

1. In the HubSpot connector settings, choose **Disconnect**.

1. Confirm. Previously synced data remains in both systems.

### Related topics
<a name="hubspot-related-topics"></a>
+ Connector overview
+ Private offer automation