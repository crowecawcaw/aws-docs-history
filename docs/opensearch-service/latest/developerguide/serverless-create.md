# Creating collections

You can use the console or the AWS CLI to create a serverless collection. These steps
cover how to create a _search_ or _time series_
collection. To create a _vector search_ collection, see [Working with vector search collections](serverless-vector-search.md "serverless-vector-search.md").

Before you create a collection, ensure that you have the required permissions. For more information, see [Configuring permissions for collections](serverless-collection-permissions.md "serverless-collection-permissions.md").

Amazon OpenSearch Serverless supports two collection generations:

- **NextGen** – The latest generation of
  OpenSearch Serverless with instant auto scaling and scale-to-zero for cost optimization.
  Uses collection groups for shared capacity management across multiple
  collections. Offers a simplified single-page creation flow with Express Create
  and Standard Create options.
- **Classic** – Uses a multi-step wizard
  with per-collection security, network, and encryption configuration. Each
  collection is configured independently.
  When you choose **Create collection** from the Collections page,
  the console opens the **NextGen** creation form by
  default. You can switch between generations at any time using the **Switch to
  Classic** or **Switch to NextGen** link in the
  **Serverless generation** field on the creation form.

- [Create a NextGen collection (Express Create)](#serverless-create-nextgen-easy "#serverless-create-nextgen-easy")
- [Create a NextGen collection (Standard Create)](#serverless-create-nextgen-standard "#serverless-create-nextgen-standard")
- [Create a Classic collection](#serverless-create-classic "#serverless-create-classic")
- [Configure collection settings (Classic)](#serverless-create-console-step-2 "#serverless-create-console-step-2")
- [Configure additional search fields (Classic)](#serverless-create-console-step-3 "#serverless-create-console-step-3")

## Configure NextGen collection settings

The following steps are common to both Express Create and Standard Create
methods.

###### To configure NextGen collection settings

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/").
2. Expand **Serverless** in the left navigation pane and
   choose **Collections**.
3. Choose **Create collection**. The NextGen collection
   creation form appears by default.

###### Tip

To create a Classic collection instead, choose **Switch to
Classic** in the **Serverless
generation** field. 4. Provide a name and description for the collection. The name must meet the
following criteria:

    * Is unique to your account and AWS Region
    * Contains only lowercase letters a-z, the numbers 0–9, and
     the hyphen (-)
    * Contains between 3 and 32 characters

5.  Choose a collection type:

        * **Search** – Full-text search that powers
         applications in your internal networks and internet-facing
         applications. All search data is stored in hot storage to ensure
         fast query response times.
        * **Vector search** – Semantic search on
         vector embeddings that simplifies vector data management. Powers
         machine learning (ML) augmented search experiences and generative AI
         applications.

    For more information, see [Choosing a collection type](serverless-overview.md#serverless-usecase "serverless-overview.md#serverless-usecase").

6.  Choose a collection creation method: **Express Create** or
    **Standard Create**.

## Create a NextGen collection (Express Create)

Express Create lets you quickly set up a NextGen collection with sensible defaults.
OpenSearch Serverless automatically creates the required collection group, encryption, network, and
data access policies for you based on the collection name and collection type you
provide.

###### Note

You can also access Express Create from:

- The **Express create** button in the blue info banner
  on the Amazon OpenSearch Service landing page
- The **Express create** button on the Get Started
  Quick Create card
  Both open an Express Create modal directly without navigating to the full
  create page.

When you use Express Create from the modal, you can create a collection in
seconds without navigating to the full create collection form. Enter a collection
name, choose a collection type (**Search** or **Vector
search**), and choose **Create collection**. OpenSearch Serverless
automatically configures the remaining settings with sensible defaults.

You can expand the **Configuration details** section to review
or modify settings such as collection group, OpenSearch UI settings, encryption,
network access, and data access before creating the collection. Some settings can
also be changed after creation.

###### To create a NextGen collection using Express Create

1. After configuring the collection name, description, and type (see [Configure NextGen collection settings](#serverless-create-nextgen-settings "#serverless-create-nextgen-settings")), choose
   **Express Create** as the collection creation
   method.
2. Review the default settings table that OpenSearch Serverless configures on your
   behalf:
   - **Collection group** – For a
     first-time user, a default collection group name is auto-generated
     based on the collection name. You can edit the name by
     choosing the edit icon. For a returning user, existing NextGen
     collection groups of the selected type are displayed. One is selected by default. You can select any other existing
     collection group from the dropdown.
   - **OpenSearch UI settings** –
     Uses an existing OpenSearch application by default. The application
     name and workspace name are editable after creation.
   - **Encryption** – The
     collection is encrypted with an AWS owned key.
   - **Network access** – The
     collection is accessible from public networks.
   - **Data access** – A data
     access policy is automatically created that grants the current IAM
     principal full access to the collection and its indexes.

3. Choose **Create collection**.

The collection status shows `Creating`. Wait for the collection status
to change to `Active` before you begin indexing data. This typically
takes several minutes.

## Create a NextGen collection (Standard Create)

Standard Create gives you full control over collection group, encryption, network,
and data access configuration.

###### To create a NextGen collection using Standard Create

1. Follow steps 1–5 from [Configure NextGen collection settings](#serverless-create-nextgen-settings "#serverless-create-nextgen-settings").
2. Under **Collection creation method**, select
   **Standard create**.

The form expands to show the full configuration sections described
in the following sections.

### Configure collection group

Choose how to assign a collection group. You can select an existing
compatible group or create a new one, even if compatible groups already
exist.

- **Select existing** – Choose a compatible
  collection group from the dropdown. The group must support your selected
  collection type. The console displays the group's current capacity limits
  (min/max OCU for indexing and search).
- **Create new** – Create a new collection
  group with custom capacity limits:
  - **Collection group name** –
    Auto-generated as `nextgen-{collection-name}`. You
    can edit this name. The name is normalized to lowercase, hyphens
    replace underscores, and it is truncated to 32
    characters.
  - **Min Indexing Capacity** (in OCUs) –
    Optional. Leave blank for no minimum.
  - **Max Indexing Capacity** (in OCUs) –
    Default is 96.
  - **Min Search Capacity** (in OCUs) –
    Optional. Leave blank for no minimum.
  - **Max Search Capacity** (in OCUs) –
    Default is 96.

### Configure encryption

Choose an encryption option:

- **Use AWS owned key** (default) – Amazon OpenSearch Service
  manages the encryption key at no additional cost.
- **Use customer managed key** – Select a AWS KMS
  key from your account.

(Optional) Select the **Customize encryption settings**
checkbox to choose or create a different AWS KMS key.

For more information about encryption policies, see [Encryption in Amazon OpenSearch Serverless](serverless-encryption.md "serverless-encryption.md").

### Configure network access

Configure network access for your collection:

- Enable or disable **public access** to the OpenSearch
  endpoint.
- (Optional) Add VPC endpoint rules to restrict access.

### Configure data access policy

Choose how to configure data access:

- **Create new policy** – Define a new data
  access policy:
  - Enter a **policy name** and optional
    **description**.
  - Use the **visual editor** to add statements
    with principals and resource permissions, or switch to the
    **JSON editor** for direct policy
    editing.
  - Add principals: IAM users and roles, SAML users and groups,
    or users and groups.
  - Specify resource permissions for collections and
    indexes.

- **Add to existing policy** – Select an
  existing data access policy from the dropdown.

### Configure additional settings

- (Optional) Add **tags** to your collection as
  key-value pairs.

### Configure OpenSearch UI settings

Configure the OpenSearch application and workspace for your collection:

- For **OpenSearch application selection**, choose one
  of the following:
  - **Select existing OpenSearch application**
    – Choose an existing application from the
    **OpenSearch application name**
    dropdown. Then for **Workspace selection**,
    choose **Select existing workspace** or
    **Create new workspace** and enter a
    name.
  - **Create new OpenSearch application**
    – Enter a name for the new application. You must also
    create a new workspace – enter a name for the
    workspace.

To create the collection, review your configuration and choose
**Submit**.

After you submit, the collection enters a **Creating** status. The console also creates the
collection group (if new), encryption policy, network policy, and data access
policy as needed. When the collection status changes to **Active**, it is ready to use. This typically takes several minutes.

## Create a Classic collection

Classic collections use a multi-step wizard with per-collection security, network,
and encryption configuration. Each collection is configured independently.

### Configure collection settings (Classic)

###### To configure basic collection settings (Classic)

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/"). In the left
   navigation pane, expand **Serverless** and choose
   **Collections**.
2. Choose **Create collection**.

The console opens the **Create NextGen collection**
form by default. 3. In the **Serverless generation** field, choose
**Switch to Classic**.

The console navigates to the Classic collection creation wizard. The
**Serverless generation** field now displays
**Classic** with a description:
_This is the Classic collections create
flow._

###### Tip

To switch back to NextGen, choose **Switch to
NextGen** in the **Serverless
generation** field. 4. Provide a **name** and
**description** for the collection. The name must
meet the following criteria:

    * Is unique to your account and AWS Region
    * Contains only lowercase letters a–z, the numbers
     0–9, and the hyphen (-)
    * Contains between 3 and 32 characters

5. Choose a **collection type**:
   - **Time series** – Log analytics
     segment that focuses on analyzing large volumes of
     semi-structured, machine-generated data. At least 24 hours of
     data is stored on hot indexes, and the rest remains in warm
     storage.
   - **Search** – Full-text search that
     powers applications in your internal networks and
     internet-facing applications. All search data is stored in hot
     storage to ensure fast query response times. Choose this option
     if you are enabling automatic semantic search.
   - **Vector search** – Semantic search on
     vector embeddings that simplifies the management of vector data.
     Powers machine learning (ML) augmented search experiences and
     generative AI applications such as chatbots, personal
     assistants, and fraud detection.

6. (Optional) Configure **deployment options**:
   - **Standby replicas** – Choose whether
     to enable standby replicas for high availability.
   - **GPU acceleration** – For vector
     search collections, choose whether to enable GPU
     acceleration.

7. Choose **Next**.

###### To configure security and access policies (Classic)

1.  **Encryption policy** – Choose how
    to encrypt data in your collection:

        * **Use AWS owned key** (default) –
         Amazon OpenSearch Service manages the encryption key at no additional
         cost.
        * **Use customer managed key** – Select
         a AWS KMS key from your account for encryption.

    (Optional) Select **Use existing policy** if a
    matching encryption policy already exists for your collection
    name.

2.  **Network access** – Configure how
    users and applications access your collection:
    - Enable or disable **access to OpenSearch
      endpoint**.
    - Enable or disable **access to OpenSearch Dashboards** .
    - Choose **Public** access or restrict access
      through **VPC endpoints**.

3.  **Data access policy** – Define
    which principals can access your collection's data:
    - **Create new policy** – Define a new
      data access policy using the visual editor or JSON editor. Add
      principals (IAM users, IAM roles, or SAML users and groups)
      and specify resource permissions.
    - **Add to existing policy** – Select an
      existing data access policy from the dropdown.

4.  Choose **Next**.

### Configure OpenSearch UI (Classic)

Configure the OpenSearch application and workspace for your collection:

- For **OpenSearch application selection**, choose one
  of the following:
  - **Select existing OpenSearch application**
    – Choose an existing application from the
    **OpenSearch application name**
    dropdown. Then for **Workspace selection**,
    choose **Select existing workspace** or
    **Create new workspace** and enter a
    name.
  - **Create new OpenSearch application**
    – Enter a name for the new application. You must also
    create a new workspace – enter a name for the
    workspace.

Choose **Next**.

### Configure additional search fields (Classic)

The options you see on this page depend on the type of collection you are
creating.

- **Search collections** – Configure
  automatic semantic enrichment and lexical search fields.
- **Time series collections** –
  Configure time series search fields.
- **Vector search collections** –
  Configure vector fields, including field name, dimensions, and distance
  metric.

(Optional) Configure the search fields relevant to your collection type.
Choose **Next**. Review all settings on the summary page and
choose **Submit** to create the collection.

After you submit, the collection enters a **Creating** status. When the status changes to
**Active**, the collection is ready to
use.

###### Topics

- [Configure automatic semantic enrichment](#serverless-create-console-step-3-semantic-enrichment-fields "#serverless-create-console-step-3-semantic-enrichment-fields")
- [Configure time series search fields](#serverless-create-console-step-3-time-series-fields "#serverless-create-console-step-3-time-series-fields")
- [Configure lexical search fields](#serverless-create-console-step-3-lexical-fields "#serverless-create-console-step-3-lexical-fields")
- [Configure vector search fields](#serverless-create-console-step-3-vector-search-fields "#serverless-create-console-step-3-vector-search-fields")

#### Configure automatic semantic enrichment

When you create or edit a collection, you can configure automatic semantic
enrichment, which simplifies semantic search implementation and capabilities
in Amazon OpenSearch Service. Semantic search returns query results that incorporate not just
keyword matching, but the intent and contextual meaning of the user's
search. For more information, see [Automatic semantic enrichment for Serverless](serverless-semantic-enrichment.md "serverless-semantic-enrichment.md").

###### To configure automatic semantic enrichment

1. In the **Index details** section, for
   **Index name**, specify a name.
2. In the **Automatic semantic enrichment fields**
   section, choose **Add semantic search
   field**.
3. In the **Input field name for semantic
   enrichment** field, enter the name of a field that you
   want to enrich.
4. **Data type** is **Text**. You
   can't change this.
5. For **Language**, choose either
   **English** or
   **Multilingual**.
6. Choose **Add field**.
7. After you finish configuring optional fields for your collection,
   choose **Next**.
8. Review your changes and choose
   **Submit** to create the collection.

#### Configure time series search fields

The options in the **Time series search fields** section
pertain to time series data and data streams. For more information about
these subjects, see [Managing time-series data in Amazon OpenSearch Service with data streams](data-streams.md "data-streams.md").

###### To configure time series search fields

1. In the **Time series search fields** section,
   choose **Add time series field**.
2. For **Field name**, enter a name.
3. For **Data type**, choose a type from the
   list.
4. Choose **Add field**.
5. After you finish configuring optional fields for your collection,
   choose **Next**.
6. Review your changes and choose
   **Submit** to create the collection.

#### Configure lexical search fields

Lexical search seeks an exact match between a search query and indexed
terms or keywords.

###### To configure lexical search fields

1. In the **Lexical search fields** section, choose
   **Add search field**.
2. For **Field name**, enter a name.
3. For **Data type**, choose a type from the
   list.
4. Choose **Add field**.
5. After you finish configuring optional fields for your collection,
   choose **Next**.
6. Review your changes and choose
   **Submit** to create the collection.

#### Configure vector search fields

###### Note

The `Engine` property is only configurable with Classic collections
and is unsupported for NextGen collections.

###### To configure vector search fields

1. In the **Vector fields** section, choose **Add vector field**.
2. For **Field name**, enter a name.
3. For **Engine**, choose a type from the list.
4. Enter the number of dimensions.
5. For **Distance Metric**, choose a type from the list.
6. After you finish configuring optional fields for your collection, choose **Next**.
7. Review your changes and choose **Submit** to create the collection.
