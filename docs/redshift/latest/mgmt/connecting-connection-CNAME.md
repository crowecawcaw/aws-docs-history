Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Custom domain names for client

connections

You can create a custom domain name, also known as a custom URL, for both your Amazon Redshift
cluster and Amazon Redshift Serverless workgroup. It's an easy-to-read DNS record that routes SQL
client connections to your endpoint. You can configure it for an existing cluster or
workgroup at any time. It provides several benefits:

- The custom domain name is a more simple string than the default URL, which
  typically includes the cluster name or the workgroup name and the region. It's
  easier to recall and use.
- You can quickly route traffic to a new cluster or workgroup in a fail-over case,
  for example. This makes it so clients don't have to make a configuration change when
  they reconnect. Connections can be re-routed centrally, with minimal disruption.
- You can avoid sharing private information like a server name in a connection URL.
  You can hide it in a custom URL.
  When you set up a custom domain name using a CNAME, there isn't any additional charge from
  Amazon Redshift. You may be billed from your DNS provider for a domain name, if you create a new one,
  but this cost is typically small.
