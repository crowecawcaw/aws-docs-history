# Encrypt Athena query results

stored in Amazon S3

You set up query result encryption using the Athena console or when using JDBC or
ODBC. Workgroups allow you to enforce the encryption of query results.

###### Note

When you encrypt query results, Athena encrypts all objects written by the
query. This includes the results of statements like `INSERT INTO`,
`UPDATE`, and queries of data in Iceberg or other formats.

In the console, you can configure the setting for encryption of query results in
two ways:

- **Client-side settings** – When you use
  **Settings** in the console or the API operations to
  indicate that you want to encrypt query results, this is known as using
  client-side settings. Client-side settings include query results location
  and encryption. If you specify them, they are used, unless they are
  overridden by the workgroup settings.
- **Workgroup settings** – When you [create or edit a workgroup](creating-workgroups.md "creating-workgroups.md") and
  select the **Override client-side settings** field, then
  all queries that run in this workgroup use the workgroup encryption and
  query results location settings. For more information, see [Override client-side settings](workgroups-settings-override.md "workgroups-settings-override.md").

###### To encrypt

query results stored in Amazon S3 using the console

###### Important

If your workgroup has the **Override client-side
settings** field selected, then all queries in the workgroup
use the workgroup settings. The encryption configuration and the query
results location specified on the **Settings** tab in the
Athena console, by API operations and by JDBC and ODBC drivers aren't used.
For more information, see [Override client-side settings](workgroups-settings-override.md "workgroups-settings-override.md").

1. In the Athena console, choose **Settings**.

![The Settings tab of the Athena query editor.](images/settings.png) 2. Choose **Manage**. 3. For **Location of query result**, enter or choose an Amazon S3
path. This is the Amazon S3 location where query results are stored. 4. Choose **Encrypt query results**.

![The Encrypt query results option on the Manage settings page of the Athena console.](images/encrypt-query-results.png) 5. For **Encryption type**, choose
**CSE-KMS**, **SSE-KMS**, or
**SSE-S3**. Of these three,
**CSE-KMS** offers the highest level of encryption and
**SSE-S3** the lowest. 6. If you chose **SSE-KMS** or **CSE-KMS**,
specify an AWS KMS key.

    * For **Choose an AWS KMS key**, if your account has
     access to an existing AWS KMS customer managed key, choose its alias or enter an
     AWS KMS key ARN.
    * If your account doesn't have access to an existing customer managed key,
     choose **Create an AWS KMS key**, and then open the
     [AWS KMS console](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"). For more
     information, see [Creating
     keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.


    ###### Note

    Athena supports only symmetric keys for reading and writing
     data.

7. Return to the Athena console and choose the key that you created by alias
   or ARN.
8. Choose **Save**.

## Encrypt Athena

query results when you use JDBC or ODBC

If you connect using a JDBC or ODBC driver, you configure driver options to
specify the type of encryption to use and the Amazon S3 staging directory location.
To configure a JDBC or ODBC driver to encrypt your query results using any of
the encryption protocols that Athena supports, see [Connect to Amazon Athena with ODBC and JDBC
drivers](athena-bi-tools-jdbc-odbc.md "athena-bi-tools-jdbc-odbc.md").
