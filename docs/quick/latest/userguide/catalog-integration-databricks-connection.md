

# Setting up the Databricks connection
<a name="catalog-integration-databricks-connection"></a>

The Databricks connector supports catalog integration without requiring a new connector. The following connection options are available:
+ The agentic experience (**Explore Data**) is available for existing Databricks data sources that use a Personal Access Token (PAT).
+ A single Databricks connection provides access to both metadata and data. This differs from AWS Glue Data Catalog, which requires two separate connections.
+ Supported authentication options: Personal Access Token (PAT) or OAuth 3LO.

To create a Databricks data source, navigate to **Create Data Source** and select **Databricks**. Choose your preferred authentication method and enter the connection details.

**Note**  
Databricks Metrics Views are not yet supported.