

# Create an object type mapping in the Connect Customer console
<a name="create-mapping-console"></a>

The console provides a no-code experience for mapping data from your own and third-party applications with Amazon S3, Salesforce, ServiceNow, Zendesk, and Marketo.

## Step 1: Set up data mapping
<a name="step1-how-to-set-up-data-mapping"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](https://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the navigation pane, choose **Customer profiles**, **Data mappings**.

1. Choose **Create data mapping**.

1. On the **Set up data mapping** page, in the **Description** section, add a name that helps you identify the source or purpose of this mapping. This becomes the object type's metadata.

1. In the **Data source** section:

   1. Choose where the data is coming from, such as Salesforce or Zendesk. Connect Customer automatically selects the available destinations based on the predefined template.

   1. Choose the source object used to build your unified profile.

   1. In the **Mapping destination** section, choose the data you want to use to build your unified profile. This information can be shown to your flows and agents to personalize contact interactions.

   1. In the **Additional options** section, choose whether to opt out of creating new profiles and how long to retain data.
**Note**  
By default, the domain retention period is 366 days. If a profile receives no writes for that period, it expires. Reads don't reset the timer—only write operations (such as ingesting a new profile object or calling [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html)) do.  
To change the retention period, use the [UpdateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html) API. To retain expired profiles for long-term storage, enable the Data store feature on the domain.

1. If you chose a source other than S3, in the **Establish a connection** section, choose an existing Amazon AppFlow or Amazon EventBridge connection, or create a new one.

1. Choose **Next**.

## Step 2: Map attributes
<a name="step2-how-to-map-attributes"></a>

On the **Map *type* attributes** page, the field mappings table is prefilled from the predefined template based on your mapping destination (for example, customer, product, case, or order attributes). You can change a mapping by choosing an attribute (such as `AccountNumber`) and selecting a different destination, or by entering a custom attribute.

The following image shows an example of the page filled with customer attributes from the template.

![The Connect Customer navigation menu, the Map customer attributes page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-data-mapping-2.png)


You can remove what you don't want populated in the profile, change the source, and add custom attributes. This mapping uses your data source to populate profile contact information, such as a phone number, using attributes from the standard profile template.

**Tip**  
Custom attributes always have the prefix `Attributes.` added to the destination so Customer Profiles recognizes them as custom.  

![Customer attribute mapping interface showing source fields mapped to destination fields.](https://docs.aws.amazon.com/connect/latest/adminguide/images/custom-attribute-cp.png)

Agents view custom attributes in the Connect Customer agent workspace under the **Additional Information** tab. Custom attribute names support the following format: `/^Attributes\.[a-zA-Z0-9]+(?:[ _\-]+[a-zA-Z0-9]+)*$/`
All ingested custom attributes are displayed to agents. If you don't want certain information shown, don't ingest it as a custom attribute.

## Step 3: Specify identifiers
<a name="step3-how-to-specify-identifiers"></a>

On the **Specify identifiers** page, complete the following sections. Depending on the data you're mapping, not all of these appear.

**Note**  
The names `_profileId`, `_orderId`, `_caseId`, and `_assetId` are reserved for internal use. If you use these names as identifiers, they must be declared as `LOOKUP_ONLY`, which means Customer Profiles doesn't save them for matching or searching. To make these keys usable for searching and matching, rename them. For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).
+ **Unique identifier**: Required. Also known as the unique key. Customer Profiles uses it to distinguish this object from other source objects and to index it for search and updates. There can be only one.
+ **Customer identifier**: At least one is required. Also known as the profile key. Customer Profiles uses it to associate the object with an existing profile or to create a new one. You can have multiple.
+ **Product identifier**: Required when mapping product data. Also known as the asset key.
+ **Case identifier**: Required when mapping case data. Also known as the case key.
+ **Order identifier**: Required when mapping order data. Also known as the order key.
+ **Additional search attributes (optional)**: Other attributes you want to index for search. By default, all identifiers are indexed.
+ **Data object timestamp**: Used to resolve profile conflicts when Identity Resolution is enabled for consolidating similar profiles.

**Tip**  
If your search attributes mostly contain the same value, ingestion can be slower. Create search attributes that are unique in your source objects.

## Step 4: Review and create
<a name="step4-how-to-review"></a>

Review your mapping, then create it. After the mapping is created, choose **Add data source integration** to start ingesting data against this object type.

![Connect Customer Customer Profiles interface showing sample data mapping details and integration status.](https://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-data-mapping-3.png)


For what to do when you need to change a mapping later, see [Update and validate an object type mapping in Customer Profiles](update-and-validate-mapping.md).