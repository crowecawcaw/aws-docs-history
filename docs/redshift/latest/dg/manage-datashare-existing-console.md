Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing existing

datashares

With Amazon Redshift, you can manage existing datashares to control access to your data in an
Amazon Redshift cluster. The following sections provide step-by-step guidance on managing
datashares in your Amazon Redshift environment.

## Viewing datashares

View datashares from the **DATASHARES** or
**CLUSTERS** tab.

- Use the **DATASHARES** tab to list datashares in your
  account or from other accounts.
  - To view datashares created in your account, choose **In my
    account**, then choose the datashare you want to
    view.
  - To view datashares that are shared from other accounts, choose
    **From other accounts**, then choose the datashare
    you want to view.

- Use the **CLUSTERS** tab to list datashares in your
  cluster or from other clusters.

Connect to a database. For more information, see [Connecting to a database](connect-database-console.md "connect-database-console.md").

Then choose a datashare either from the **Datashares from other
clusters** or **Datashares created in my
cluster** section to view its details.

## Removing datashare objects from

datashares

You can remove one or more objects from a datashare by using the following
procedure.

###### To remove one or more objects from a datashare

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   your cluster. The cluster details page appears.
3. Choose **Datashares**.
4. In the **Datashares created in my account** section,
   choose **Connect to database**. For more information, see
   [Connecting to a database](connect-database-console.md "connect-database-console.md").
5. Choose the datashare you want to edit, then choose
   **Edit**. The datashare details page appears.
6. To remove one or more datashare objects to the datashare, do one of the
   following:
   - To remove schemas from the datashare, choose one or more schemas.
     Then choose **Remove**. Amazon Redshift removes the
     specified schemas and all the objects of the specified schemas from
     the datashare.
   - To remove tables and views from the datashare, choose one or more
     tables and views. Then choose **Remove**.
     Alternatively, choose **Remove by schema** to remove
     all tables and views in the specified schemas.
   - To remove user-defined functions from the datashare, choose one or
     more user-defined functions. Then choose **Remove**.
     Alternatively, choose **Remove by schema** to remove
     all user-defined functions in the specified schemas.

## Removing data consumers from

datashares

You can remove one or more data consumers from a datashare. Data consumers can
be namespaces that uniquely identified Amazon Redshift clusters or AWS accounts.

Choose one or more data consumers either from the namespace IDs or AWS
account, then choose **Remove**.

Amazon Redshift removes the specified data consumers from the datashare. They lose
access to the datashare immediately.

## Editing datashares created in your

account

Edit datashares created in your account using the console. Connect to a
database first to see the list of datashares created in your account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   your cluster. The cluster details page appears.
3. Choose **Datashares**.
4. In the **Datashares created in my account** section,
   choose **Connect to database**. For more information, see
   [Connecting to a database](connect-database-console.md "connect-database-console.md").
5. Choose the datashare you want to edit, then choose
   **Edit**. The datashare details page appears.
6. Make any changes in the **Datashare objects** or
   **Data consumers** section.

###### Note

If you chose to publish your datashare to the AWS Glue Data Catalog, you
can't edit the configuration to publish the datashare to other Amazon Redshift
accounts. 7. Choose **Save changes**.

Amazon Redshift updates your datashare with the changes.

## Deleting a datashare created in your

account

Delete datashares created in your account using the console. Connect to a
database first to see the list of datashares created in your account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   your cluster. The cluster details page appears.
3. Choose **Datashares**. The datashare list
   appears.
4. In the **Datashares created in my account** section,
   choose **Connect to database**. For more information, see
   [Connecting to a database](connect-database-console.md "connect-database-console.md").
5. Choose one or more datashares you want to delete, then choose
   **Delete**. The Delete datashares page appears.

Deleting a datashare shared with Lake Formation doesn't automatically remove
the associated permissions in Lake Formation. To remove them, go to the Lake Formation
console. 6. Type **Delete** to confirm deleting the specified
datashares. 7. Choose **Delete**.

After datashares are deleted, datashare consumers lose access to the
datashares.
