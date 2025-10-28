# Create and run an Amazon DataZone data source

for Amazon Redshift

In Amazon DataZone, you can create an Amazon Redshift data source in order to import technical
metadata of database tables and views from the Amazon Redshift data warehouse. To add a
Amazon DataZone data source for Amazon Redshift, the source data warehouse must already exist in the
Amazon Redshift.

When you create and run an Amazon Redshift data source, you add assets from the source
Amazon Redshift data warehouse to your Amazon DataZone project's inventory. You can run your
Amazon Redshift data sources on a set schedule or on demand to create or update your assets'
technical metadata. During the data source runs, you can optionally choose to publish
your project inventory assets to the Amazon DataZone catalog and thus make them discoverable
by all domain users. You can also publish your inventory assets after editing their
business metadata. Domain users can search for and discover your published assets and
request subscriptions to these assets.

###### To add an Amazon Redshift data source

1.  Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
    (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
    navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
    AWS account where the domain was created, then choose **Open data
    portal**.
2.  Choose **Select project** from the top navigation pane and
    select the project to which you want to add the data source.
3.  Navigate to the **Data** tab for the project.
4.  Choose **Data sources** from the left navigation pane, then
    choose **Create data source.**
5.  Configure the following fields:
    - **Name** – The data source name.
    - **Description** – The data source
      description.

6.  Under **Data source type**, choose
    **Amazon Redshift**.
7.  Under **Select an environment**, specify an environment in
    which to publish the Amazon Redshift tables.
8.  Depending on the environment you select, Amazon DataZone will automatically apply
    the Amazon Redshift credentials and other parameters directly from the
    environment or give you the option to choose your own.
    - If you have selected an environment that only allows publishing from
      environment’s default Amazon Redshift schema, then Amazon DataZone will
      automatically apply the Amazon Redshift credentials and other parameters
      including the Amazon Redshift cluster or workgroup name, AWS secret,
      database name, and schema name. You cannot edit these auto-populated
      parameters.
    - If you select an environment that does not allow to publish any data,
      you will not be able to proceed with data source creation.
    - If you select an environment that allows publishing data from any
      schema, you will see the option to either use the credentials and other
      Amazon Redshift parameters from the environment or to enter your own
      credentials/parameters.

9.  If you choose to use your own credentials to create the data source, provide
    the following details:
    - Under **Provide Amazon Redshift credentials**, choose
      whether to use a provisioned Amazon Redshift cluster or an Amazon
      Redshift Serverless workspace as your data source.
    - Depending on your selection in the step above, choose your Amazon
      Redshift cluster or workspace from the dropdown menu, then choose the
      secret in AWS Secrets Manager to use for authentication. You can
      choose an existing secret or create a new one.
    - In order for the existing secret to appear in the drop down, make sure
      that your secret in AWS Secrets Manager includes the following tags
      (key/value):

          + AmazonDataZoneProject: <projectID>
          + AmazonDataZoneDomain: <domainID>

      If you choose to create a new secret, then the secret is automatically
      tagged with the tags referenced above and no extra steps are needed. For
      more information, see [Storing
      database credentials in AWS Secrets Manager](../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets "../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets").

    Amazon Redshift users in the AWS secret provided for creating the
    data source must have `SELECT` permissions on the tables that
    are to be published. If you want Amazon DataZone to also manage the
    subscriptions (access) on your behalf, the database users in the AWS
    secret must also have the following permissions:

        + `CREATE DATASHARE`
        + `ALTER DATASHARE`
        + `DROP DATASHARE`

10. Under **Data selection**, provide an Amazon Redshift database,
    schema, and enter your table or view selection criteria. For example, if you
    choose **Include** and enter `*corporate`, the asset
    will include all source tables that end with the word
    `corporate`.

You can add multiple include rules for tables within a single database. You
can also add multiple databases using the **Add another
database** button. 11. Choose **Next**. 12. For **Publishing settings**, choose whether assets are
immediately discoverable in the data catalog. If you only add them to the
inventory, you can choose subscription terms later and publish them to the
business data catalog. 13. For **Automated business name generation**, choose whether to
automatically generate metadata for assets as they're published and updated from
the source. 14. (Optional) For **Metadata forms**, add forms to define the
metadata that is collected and saved when the assets are imported into
Amazon DataZone. For more information, see [Create a metadata form in Amazon DataZone](create-metadata-form.md "create-metadata-form.md"). 15. For **Run preference**, choose when to run the data
source.

    * **Run on a schedule** – Specify the dates and
     time to run the data source.
    * **Run on demand** – You can manually initiate
     data source runs.

16. Choose **Next**.
17. Review your data source configuration and choose
    **Create**.

###### Note

When an Amazon Redshift data source is created, Amazon DataZone grants read only'
access to the environment used to create the data source to access all the tables in
the Amazon Redshift schemas used in the data source. You can monitor the status of
these grants under data sources on your environment's details page.

When using a different Amazon Redshift cluster or a Serverless workgroup than the
one used to create the environment, you must ensure that the following AWS tag is
added to the cluster or workgroup. This is necessary for the environment users to be
able to view the granted database in the Amazon Redshift Query Editor V2:
`DataZoneDiscoverable_${domainId}: true`

For the environments created prior to the current release of Amazon DataZone, project
members will not be able to see granted tables in Amazon Redshift.
