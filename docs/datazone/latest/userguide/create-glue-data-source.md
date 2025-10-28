# Create and run an Amazon DataZone data source for

the AWS Glue Data Catalog

In Amazon DataZone, you can create an AWS Glue Data Catalog data source in order to import technical
metadata of database tables from AWS Glue. To add a data source for the AWS Glue Data Catalog, the
source database must already exist in AWS Glue.

When you create and run an AWS Glue data source, you add assets from the source AWS Glue
database to your Amazon DataZone project's inventory. You can run your AWS Glue data sources on
a set schedule or on demand to create or update your assets' technical metadata. During
the data source runs, you can optionally choose to publish your assets to the Amazon DataZone
catalog and thus make them discoverable by all domain users. You can also publish your
project inventory assets after editing their business metadata. Domain users can search
for and discover your published assets, and request subscriptions to these assets.

###### To add an AWS Glue data source

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project to which you want to add the data source.
3. Navigate to the **Data** tab for the project.
4. Choose **Data sources** from the left navigation pane, then
   choose **Create data source**.
5. Configure the following fields:
   - **Name** – The data source name.
   - **Description** – The data source
     description.

6. Under **Data source type**, choose
   **AWS Glue**.
7. Under **Select an environment**, specify an environment in
   which to publish the AWS Glue tables.
8. Under **Data selection**, provide an AWS Glue database and enter
   your table selection criteria. For example, if you choose
   **Include** and enter `*corporate`, the database
   will include all source tables that end with the word
   `corporate`.

You can either choose an AWS Glue database form the dropdown or type a database
name. The dropdown includes two databases: the publishing database and the
subscription database of the environment. If you want to bring assets form a
database that is not created by the environment, then you must type the name of
the database instead of selecting it from the dropdown.

You can add multiple include and exclude rules for tables within a single
database. You can also add multiple databases using the **Add another
database** button. 9. Under **Data quality**, you can choose to **Enable
data quality for this data source**. If you do this, Amazon DataZone
imports your existing AWS Glue data quality output into your Amazon DataZone
catalog. By default, Amazon DataZone imports the latest existing 100 quality reports
with no expiration date from AWS Glue.

Data quality metrics in Amazon DataZone help you understand the completeness and
accuracy of your data sources. Amazon DataZone pulls these data quality metrics from
AWS Glue in order to provide context during a point in time, for example,
during a business data catalog search. Data users can see how data quality
metrics change over time for their subscribed assets. Data producers can ingest
AWS Glue data quality scores on a schedule. The Amazon DataZone business data
catalog can also display data quality metrics from third-party systems through
data quality APIs. For more information, see [Data quality in Amazon DataZone](datazone-data-quality.md "datazone-data-quality.md") 10. Choose **Next**. 11. For **Publishing settings**, choose whether assets are
immediately discoverable in the business data catalog. If you only add them to
the inventory, you can choose subscription terms later and publish them to the
business data catalog. 12. For **Automated business name generation**, choose whether to
automatically generate metadata for assets as they're imported from the
source. 13. (Optional) For **Metadata forms**, add forms to define the
metadata that is collected and saved when the assets are imported into
Amazon DataZone. For more information, see [Create a metadata form in Amazon DataZone](create-metadata-form.md "create-metadata-form.md"). 14. For **Run preference**, choose when to run the data
source.

    * **Run on a schedule** – Specify the dates and
     time to run the data source.
    * **Run on demand** – You can manually initiate
     data source runs.

15. Choose **Next**.
16. Review your data source configuration and choose
    **Create**.

###### Note

When an AWS Glue data source is created, Amazon DataZone creates the Lake Formation
'read only' permissions for the IAM role of the environment that is used to create
the data source to access all the tables in the AWS Glue databases used in the
data source. You can monitor the status of these grants under data sources on your
environment's details page. Amazon DataZone adds the following AWS tags to the AWS
Glue database when granting access to the publishing environment’s IAM role:
`DataZoneDiscoverable_${domainId}: true`

For the environments created prior to the current release of Amazon DataZone, project
members will not be able to see granted tables in Amazon Athena.
