Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Removing authorization from a

datashare in Amazon Redshift

With Amazon Redshift, you can control access to datashares by revoking authorization for
specified consumers. This sections provides instructions for revoking consumer
access to your datashares in Amazon Redshift.

###### Note

To remove authorization for the datashare, there must be at least one data
consumer added to the datashare.

Console
Choose one or more consumer clusters that you want to remove
authorization from. Then, choose **Remove
authorization**.

After authorization is removed, data consumers lose access to the
datashare immediately.

API
The producer security administrator determines the following:

- Whether or not another account can have access to the
  datashare.
- If an account has access to the datashare, whether or not that
  account has write permissions.

The following IAM permissions are required to deauthorize a
datashare:

**redshift:DeauthorizeDataShare**

You can deauthorize usage and writes using either a CLI call or with
the API:

```
deauthorize-data-share
--data-share-arn <value>
--consumer-identifier <value>
```

For more information about the command, see [deauthorize-data-share](../../../cli/latest/reference/redshift/deauthorize-data-share.md "../../../cli/latest/reference/redshift/deauthorize-data-share.md").
