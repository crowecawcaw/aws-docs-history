

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Managing AWS Data Exchange datashares
<a name="manage-adx-datashare-console"></a>

With Amazon Redshift, you can securely share and receive live data from AWS Data Exchange without having to create and manage data extracts or pipelines. By managing AWS Data Exchange datashares, you can subscribe to third-party data products and integrate live data streams directly into your Amazon Redshift data warehouse. The following sections demonstrate managing AWS Data Exchange datashares within your Amazon Redshift clusters.

## Creating data sets on AWS Data Exchange
<a name="create-dataset-console"></a>

Create data sets on AWS Data Exchange.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose your cluster. The cluster details page appears.

1. Choose **Datashares**.

1. In the **Datashares created in my account** section, choose an AWS Data Exchange datashare.

1. Choose **Create data set on AWS Data Exchange**. For more information, see [Publishing a new product](https://docs.aws.amazon.com/data-exchange/latest/userguide/publishing-products.html).

## Editing AWS Data Exchange datashares
<a name="edit-adx-datashare-console"></a>

Edit AWS Data Exchange datashares using the console. Connect to a database first to see the list of datashares created in your account.

For AWS Data Exchange datashares, you can't make changes to data consumers.

To edit the publicly accessible setting for AWS Data Exchange datashares, use the Query editor v2. Amazon Redshift generates a random one-time value to set the session variable to allow turning this setting off. For more information, see [ALTER DATASHARE usage notes](r_ALTER_DATASHARE.md#r_ALTER_DATASHARE_usage).

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose your cluster. The cluster details page appears.

1. From the navigator menu, choose **Editor**, then **Query editor v2**.

1. If this is the first time you use the Query editor v2, configure your AWS account. By default, an AWS owned key is used to encrypt resources. For more information about configuring your AWS account, see [Configuring your AWS account](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-getting-started.html) in the *Amazon Redshift Management Guide*.

1. To connect to the cluster that your AWS Data Exchange datashare is in, choose **Database** and the cluster name in the tree-view panel. If prompted, enter the connection parameters.

1. Copy the following SQL statement. The following example changes the publicly accessible setting of the salesshare datashare.

   ```
   ALTER DATASHARE salesshare SET PUBLICACCESSIBLE FALSE;
   ```

1. To run the copied SQL statement, choose **Queries** and paste the copied SQL statement in the query area. Then choose **Run**.

   An error appears following:

   ```
   ALTER DATASHARE salesshare SET PUBLICACCESSIBLE FALSE;
   ERROR:  Alter of ADX-managed datashare salesshare requires session variable datashare_break_glass_session_var to be set to value 'c670ba4db22f4b'
   ```

   The value 'c670ba4db22f4b' is a random one-time value that Amazon Redshift generates when an unrecommended operation occurs.

1. Copy and paste the following sample statement into the query area. Then run the command. The `SET datashare_break_glass_session_var` command applies a permission to allow an unrecommended operation for an AWS Data Exchange datashare.

   ```
   SET datashare_break_glass_session_var to 'c670ba4db22f4b';
   ```

1. Run the ALTER DATASHARE statement again.

   ```
   ALTER DATASHARE salesshare;
   ```

Amazon Redshift updates your datashare with the changes.

## Deleting AWS Data Exchange datashares created in your account
<a name="delete-adx-datashare-console"></a>

Delete AWS Data Exchange datashares created in your account using the console. Connect to a database first to see the list of datashares created in your account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose your cluster. The cluster details page appears.

1. From the navigator menu, choose **Editor**, then **Query editor v2**.

1. If this is the first time you use the Query editor v2, configure your AWS account. By default, an AWS owned key is used to encrypt resources. For more information about configuring your AWS account, see [Configuring your AWS account](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-getting-started.html) in the *Amazon Redshift Management Guide*.

1. To connect to the cluster that your AWS Data Exchange datashare is in, choose **Database** and the cluster name in the tree-view panel. If prompted, enter the connection parameters.

1. Copy the following SQL statement. The following example drops the salesshare datashare.

   ```
   DROP DATASHARE salesshare
   ```

1. To run the copied SQL statement, choose **Queries** and paste the copied SQL statement in the query area. Then choose **Run**.

   An error appears following:

   ```
   ERROR:  Drop of ADX-managed datashare salesshare requires session variable datashare_break_glass_session_var to be set to value '620c871f890c49'
   ```

   The value '620c871f890c49' is a random one-time value that Amazon Redshift generates when an unrecommended operation occurs.

1. Copy and paste the following sample statement into the query area. Then run the command. The `SET datashare_break_glass_session_var` command applies a permission to allow an unrecommended operation for an AWS Data Exchange datashare.

   ```
   SET datashare_break_glass_session_var to '620c871f890c49';
   ```

1. Run the DROP DATASHARE statement again.

   ```
   DROP DATASHARE salesshare;
   ```

After the datashare is deleted, datashare consumers lose access to the datashare. 

Deleting a shared AWS Data Exchange datashare can breach data product terms in AWS Data Exchange.