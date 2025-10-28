Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Associating a datashare from a different

AWS account in Amazon Redshift

With Amazon Redshift, you can associate datashares shared by other AWS accounts,
enabling seamless and secure data sharing across organizational boundaries.
Datashares are shareable database objects that encapsulate data from one or more
Amazon Redshift databases. The following sections demonstrate the process of associating
datashares.

Console
As a consumer administrator, you can associate one or more datashares
that are shared from other accounts to your entire AWS account or
specific namespaces in your account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Datashares**.
   The datashare list page appears. Choose **From other
   accounts**.
3. In the **Datashares from other accounts**
   section, choose the datashare that you want to associate and choose
   **Associate**. When the
   **Associate** datashare page appears, choose
   one of the following association types:
   - Choose **Entire AWS account** to
     associate all existing and future namespaces across different
     AWS Regions in your AWS account with the
     datashare.
   - If the datashare is published to the AWS Glue Data Catalog, you can
     only associate the datashare with the entire AWS
     account.

4. From here you can choose **Allowed
   permissions**. The choices are:
   - **Read-only** – If you
     choose read only, write permissions like UPDATE or INSERT
     aren't available on the consumer, even if these permissions
     were granted and authorized on the producer.
   - **Read and write** –
     Consumer datashare users will have all of the permissions,
     both read and write, that were granted and authorized by the
     producer.

5. Alternatively, choose **Specific AWS Regions and
   namespaces** to associate one or more AWS Regions and
   specific namespaces with the datashare. Choose **Add
   Region** to add specific AWS Regions and namespaces
   to the datashare. The **Add AWS Region** page
   appears.
6. Choose an **AWS Region**.
7. Do one of the following:
   - Choose **Add all namespaces** to add all
     existing and future namespaces in this Region to the
     datashare.
   - Choose **Add specific namespaces** to add
     one or more specific namespaces in this Region to the
     datashare.
   - Choose one or more namespaces and choose **Add
     AWS Region**.

8. Choose **Associate**.

It's possible for the producer to go back and change settings for an
authorization, which can affect association settings on consumers.

If you're associating the datashare with a Lake Formation account, go to the
Lake Formation console to create a database, then define permissions over the
database. For more information, see [Setting up
permissions for Amazon Redshift datashares](../../../lake-formation/latest/dg/setup-ds-perms.md "../../../lake-formation/latest/dg/setup-ds-perms.md") in the AWS Lake Formation Developer Guide. Once
you create a AWS Glue database or a federated database, you can use query editor v2
or any preferred SQL client with your consumer cluster to query the data.

After the datashare is associated, the datashares become
available.

###### Note

You can also change datashare association at any time. When
changing association from specific AWS Regions and namespaces to the
entire AWS account, Amazon Redshift overwrites the specific Region and
namespaces information with AWS account information. All the AWS
Regions and namespaces in the AWS account then have access to the
datashare.

API

###### Note

The steps in this section are performed after the producer
administrator grants specific actions on the shared database objects
and, if the datashare is being shared with another account, the
producer security administrator authorizes access.

The consumer security administrator determines the following:

- Whether or not all namespaces in an account, namespaces in
  specific regions in the account, or specific namespaces have access
  to the datashare.
- If namespaces have access to the datashare, whether or not those
  namespace have write permissions.

The consumer security administrator can associate the datashare with
the following command:

```
associate-data-share-consumer
--data-share-arn <value>
--consumer-identifier <value>
[--allow-writes | --no-allow-writes]
```

For more information about the command, see [associate-data-share-consumer](../../../cli/latest/reference/redshift/associate-data-share-consumer.md "../../../cli/latest/reference/redshift/associate-data-share-consumer.md").

The consumer security administrator must explicitly set
`allow-writes` to true when associating a datashare with a
namespace, to allow use of INSERT and UPDATE commands. If they don't, the
users can perform only read operations, such as SELECT, USAGE, or EXECUTE
privileges.

You can change the association of a namespace for a datashare by
calling `associate-data-share-consumer` again, with a
different value. The old association is overwritten by the new
association, so if you originally associate and set
`allow-writes`, but associate and specify
`no-allow-writes`, or simply do not specify a value, the
consumer will have their write permissions revoked.
