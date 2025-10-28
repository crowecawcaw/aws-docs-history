Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an authentication

profile to connect to Amazon Redshift

If you have many connections to Amazon Redshift, it can be difficult to manage settings for
all of them. Often, each JDBC or ODBC connection uses specific configuration options. By
using an authentication profile, you can store connection options together. This way,
your users can choose a profile to connect with and avoid managing settings for
individual options. Profiles can apply to various scenarios and user types.

After you create an authentication profile, users can add the ready-to-use profile to
a connection string. By doing this, they can connect to Amazon Redshift with the right settings for
each role and use case.

For Amazon Redshift API information, see [CreateAuthenticationProfile](../APIReference/redshift-api.md#API_CreateAuthenticationProfile "../APIReference/redshift-api.md#API_CreateAuthenticationProfile").
