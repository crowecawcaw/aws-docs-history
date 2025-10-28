# Automate lineage capture from data connections

###### Topics

- [Configure automated lineage capture for AWS Glue (Lakehouse)
  connections](#datazone-data-lineage-automate-capture-from-data-connections-glue "#datazone-data-lineage-automate-capture-from-data-connections-glue")
- [Configure automated lineage capture for Amazon Redshift connections](#datazone-data-lineage-automate-capture-from-data-connections-redshift "#datazone-data-lineage-automate-capture-from-data-connections-redshift")

## Configure automated lineage capture for AWS Glue (Lakehouse)

connections

As databases and tables are added to the Amazon SageMaker Unified Studio’s catalog, the lineage
extraction can be automated from source for those assets using data source runs
in Create Connection workflow. For every connection created, lineage is not
automatically enabled.

###### To enable lineage capture for an AWS Glue connection

1. Navigate to Amazon SageMaker Unified Studio using the URL from your
   admin and log in using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation
   pane and select the project to which you want to add the data
   source.
3. Choose **Data sources** from the left navigation pane
   under Project catalog.
4. Choose the data source that you want to modify.
5. Expand the **Actions** menu, then choose
   **Edit data source** or click on the Data Source
   run name to view the details and go to **Data Source
   Definition** tab and choose **Edit** in
   **Connection** details.
6. Go to the connections and select **Import data
   lineage** checkbox to configure lineage capture from the
   source.
7. Make other changes to the data source fields as desired, then choose
   **Save**.

**Limitations**

Lineage is captured only for crawlers which imported less than 250
tables in a crawler run.

###### Note

When enabled, the lineage runs asynchronously to capture metadata from the
source and generate lineage events to be stored in SageMaker Catalog to be
visualized from a particular asset. The status of lineage runs for the data
source can be viewed along with data source run details.

## Configure automated lineage capture for Amazon Redshift connections

Capturing lineage from Amazon Redshift can be automated when the connection is
added to an Amazon Redshift source in Amazon SageMaker Unified Studio’s Data explorer. Lineage capture
can be automated for a connection at the data source configuration. For every
connection created, lineage is not automatically enabled.

###### To enable lineage capture for an Amazon Redshift connection

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using
   your SSO or AWS credentials.
2. Choose **Select project** from the top navigation
   pane and select the project to which you want to add the data
   source.
3. Choose **Data sources** from the left navigation pane
   under **Project catalog**.
4. Choose the data source that you want to modify.
5. Expand the **Actions** menu, then choose
   **Edit data source** or click on the data source
   run name to view the details and go to Data Source Definition tab and
   select **Edit** in **Connection
   details**.
6. Go to the connections and select **Import data
   lineage** checkbox to configure lineage capture from the
   source.
7. Make other changes to the data source fields as desired, then choose
   **Save**.

###### Note

When enabled, the lineage runs captures queries executed for a given
database and generates lineage events to be stored in Amazon DataZone to be
visualized from a particular asset. The lineage run for Amazon Redshift is
set up for a daily run to pull from the Amazon Redshift system tables to
derive lineage. For the first run, after enabling the feature, the first
pull is scheduled for ~5 minutes after and set for a daily run. You can
configure specific time programmatically.
