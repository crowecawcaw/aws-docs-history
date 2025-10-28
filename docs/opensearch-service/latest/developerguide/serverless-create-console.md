# Create a collection (console)

Use the procedures in this section to create a collection by using the AWS Management Console.
These steps cover how to create a _search_ or _time
series_ collection. To create a _vector search_
collection, see [Working with vector search collections](serverless-vector-search.md "serverless-vector-search.md").

###### Topics

- [Configure collection
  settings](#serverless-create-console-step-2 "#serverless-create-console-step-2")
- [Configure additional search
  fields](#serverless-create-console-step-3 "#serverless-create-console-step-3")

## Configure collection

settings

Use the following procedure configure information about your collection.

###### To configure collection settings using the console

1.  Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/").
2.  Expand **Serverless** in the left navigation pane and
    choose **Collections**.
3.  Choose **Create collection**.
4.  Provide a name and description for the collection. The name must meet
    the following criteria:
    - Is unique to your account and AWS Region
    - Contains only lowercase letters a-z, the numbers 0–9,
      and the hyphen (-)
    - Contains between 3 and 32 characters

5.  Choose a collection type:

        * **Time series** – Log analytics
         segment that focuses on analyzing large volumes of
         semi-structured, machine-generated data. At least 24 hours of
         data is stored on hot indexes, and the rest remains in warm
         storage.
        * **Search** – Full-text search that
         powers applications in your internal networks and
         internet-facing applications. All search data is stored in hot
         storage to ensure fast query response times.


        ###### Note

        Choose this option if you are enabling automatic semantic
         search, as described in Configure collection
         settings.
        * **Vector search** – Semantic search on
         vector embeddings that simplifies vector data management. Powers
         machine learning (ML) augmented search experiences and
         generative AI applications such as chatbots, personal
         assistants, and fraud detection.

    For more information, see [Choosing a collection type](serverless-overview.md#serverless-usecase "serverless-overview.md#serverless-usecase").

6.  For **Deployment type**, choose the redundancy
    setting for your collection. By default, each collection has redundancy,
    which means that the indexing and search OpenSearch Compute Units (OCUs)
    each have their own standby replicas in a different Availability Zone.
    For development and testing purposes, you can choose to disable
    redundancy, which reduces the number of OCUs in your collection to two.
    For more information, see [How it works](serverless-overview.md#serverless-process "serverless-overview.md#serverless-process").
7.  For **Security**, choose **Standard
    create**.
8.  For **Encryption**, choose an AWS KMS key to encrypt
    your data with. OpenSearch Serverless notifies you if the collection name that you
    entered matches a pattern defined in an encryption policy. You can
    choose to keep this match or override it with unique encryption
    settings. For more information, see [Encryption in Amazon OpenSearch Serverless](serverless-encryption.md "serverless-encryption.md").
9.  For **Network access settings**, configure network
    access for the collection.

        * For **Access type**, select public or
         private.


        If you choose private, specify which VPC endpoints and
         AWS services can access the collection.




        	+ **VPC endpoints for access** –
        	 Specify one or more VPC endpoints to allow access
        	 through. To create a VPC endpoint, see [Access Amazon OpenSearch Serverless using an interface endpoint
        	 (AWS PrivateLink)](serverless-vpc.md "serverless-vpc.md").
        	+ **AWS service private access**
        	 – Select one or more supported services to allow
        	 access to.
        * For **Resource type**, select whether users
         can access the collection through its
         *OpenSearch* endpoint (to make API calls
         through cURL, Postman, and so on), through the
         *OpenSearch Dashboards* endpoint (to work with
         visualizations and make API calls through the console), or
         both.


        ###### Note

        AWS service private access applies only to the OpenSearch
         endpoint, not to the OpenSearch Dashboards endpoint.

    OpenSearch Serverless notifies you if the collection name that you entered matches a
    pattern defined in a network policy. You can choose to keep this match
    or override it with custom network settings. For more information, see
    [Network access for Amazon OpenSearch Serverless](serverless-network.md "serverless-network.md").

10. (Optional) Add one or more tags to the collection. For more
    information, see [Tagging Amazon OpenSearch Serverless collections](tag-collection.md "tag-collection.md").
11. Choose **Next**.

## Configure additional search

fields

The options you see on page two of the create collection workflow depend on
the type of collection you are creating. This section describes how to configure
additional search fields for each collection type. This section also describes
how to configure automatic semantic enrichment. Skip any section that doesn't
apply to your collection type.

###### Topics

- [Configure automatic semantic enrichment](#serverless-create-console-step-3-semantic-enrichment-fields "#serverless-create-console-step-3-semantic-enrichment-fields")
- [Configure time series search fields](#serverless-create-console-step-3-time-series-fields "#serverless-create-console-step-3-time-series-fields")
- [Configure
  lexical search fields](#serverless-create-console-step-3-lexical-fields "#serverless-create-console-step-3-lexical-fields")
- [Configure vector search fields](#serverless-create-console-step-3-vector-search-fields "#serverless-create-console-step-3-vector-search-fields")

### Configure automatic semantic enrichment

When you create or edit a collection, you can configure automatic semantic
enrichment, which simplifies semantic search implementation and capabilities
in Amazon OpenSearch Service. Semantic search returns query results that incorporate not just
keyword matching, but the intent and contextual meaning of the user's
search. For more information, see [About automatic semantic
enrichment](serverless-semantic-enrichment.md "serverless-semantic-enrichment.md").

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
   choose **Next**. Review your changes and choose
   **Submit** to create the collection.

### Configure time series search fields

The options in the **Time series search fields** section
pertain to time series data and data streams. For more information about
these subjects, see [Managing time-series data in Amazon OpenSearch Service with data
streams](data-streams.md "data-streams.md").

###### To configure time series search fields

1. In the **Time series search fields** section,
   choose **Add time series field**.
2. For **Field name**, enter a name.
3. For **Data type**, choose a type from the
   list.
4. Choose **Add field**
5. After you finish configuring optional fields for your collection,
   choose **Next**. Review your changes and choose
   **Submit** to create the collection.

### Configure

lexical search fields

Lexical search seeks an exact match between a search query and indexed
terms or keywords.

###### To configure lexical search fields

1. In the **Lexical search fields** section, choose
   **Add search field**.
2. For **Field name**, enter a name.
3. For **Data type**, choose a type from the
   list.
4. Choose **Add field**
5. After you finish configuring optional fields for your collection,
   choose **Next**. Review your changes and choose
   **Submit** to create the collection.

### Configure vector search fields

###### To configure vector search fields

1. In the **Vector fields** section, choose **Add vector field**.
2. For **Field name**, enter a name.
3. For **Engine**, choose a type from the list.
4. Enter the number of dimensions.
5. For **Distance Metric**, choose a type from the list.
6. After you finish configuring optional fields for your collection, choose **Next**.
7. Review your changes and choose **Submit** to create the collection.
