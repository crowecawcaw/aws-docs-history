Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authorizing a datashare in Amazon Redshift

With Amazon Redshift, you can control access to datashares by authorizing specified
consumers. Datashares allow you to share live data across Amazon Redshift clusters in the
same or different AWS accounts, providing a seamless way to distribute and
consume analytical data. This section provides step-by-step instructions for
authorizing and revoking consumer access to your datashares in Amazon Redshift.

###### Note

If you are adding a namespace as a data consumer, you don't have to perform
authorization. To authorize a datashare, there must be at least one data
consumer added to the datashare.

Console
As a producer administrator on the console, you can choose which data
consumers to authorize to access datashares or to remove authorization
from. Authorized data consumers receive notifications to take actions on
datashares. If you are adding a namespace as a data consumer, you
don't have to perform authorization.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Datashares**.
   From here you can see a list called **Datashares
   consumers**. Choose one or more consumer clusters that
   you want to authorize. Then choose
   **Authorize**.
3. The **Authorize account** dialog appears. You
   can choose among a couple authorization types.
   - **Read-only on [cluster name or workgroup
     name]** – This means that no write
     permissions are available on the consumer, even if the
     datashare creator granted write permissions.
   - **Read and write on [cluster name or workgroup
     name]** – This means that all permissions
     granted by the creator, including write permissions, are
     available on the consumer.

4. Choose **Save**.

You can also authorize AWS Data Exchange as a consumer.

1. If you chose **Publish to AWS Glue Data Catalog** when
   creating the datashare, you can only grant authorization of the
   datashare to a Lake Formation account.

For AWS Data Exchange datashare, you can only authorize one datashare at a
time.

When you authorize an AWS Data Exchange datashare, you are sharing the
datashare with the AWS Data Exchange service and allowing AWS Data Exchange to manage
access to the datashare on your behalf. AWS Data Exchange allows access to
consumers by adding consumer accounts as data consumers to the
AWS Data Exchange datashare when they subscribe to the products. AWS Data Exchange
doesn't have read access to the datashare. 2. Choose **Save**.

After data consumers are authorized, they can access datashare objects
and create a consumer database to query the data.

API
The producer security administrator determines the following:

- Whether or not another account can have access to the
  datashare.
- If an account has access to the datashare, whether or not that
  account has write permissions.

The following IAM permissions are required to authorize a datashare:

**redshift:AuthorizeDataShare**

You can authorize usage and writes using either a CLI call or with the
API:

```
authorize-data-share
--data-share-arn <value>
--consumer-identifier <value>
[--allow-writes | --no-allow-writes]
```

For more information about the command, see [authorize-data-share](../../../cli/latest/reference/redshift/authorize-data-share.md "../../../cli/latest/reference/redshift/authorize-data-share.md").

The consumer identifier can be either:

- A twelve digit AWS account ID.
- The namespace identifier ARN.

###### Note

Write permissions aren’t granted at the authorizing step.
Authorizing a datashare for writes just allows the account to have
write permissions that were granted by the datashare administrator. If
an administrator does not allow writes, the only permissions available
to the specific consumer are SELECT, USAGE, and EXECUTE.

You can change the authorization of a datashare consumer by calling
`authorize-data-share` again, but with a different value.
The old authorization is overwritten by the new authorization. So if you
originally authorize and allow writes, but re-authorize and specify
`no-allow-writes` or simply do not specify a value, the
consumer will have their write permissions revoked.
