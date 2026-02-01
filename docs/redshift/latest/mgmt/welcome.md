Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# What is Amazon Redshift?

Welcome to the _Amazon Redshift Management Guide_. Amazon Redshift is a fully managed,
petabyte-scale data warehouse service in the cloud. Amazon Redshift Serverless lets you access and
analyze data without all of the configurations of a provisioned data warehouse. Resources
are automatically provisioned and data warehouse capacity is intelligently scaled to deliver
fast performance for even the most demanding and unpredictable workloads. You don't incur
charges when the data warehouse is idle, so you only pay for what you use. You can load data
and start querying right away in the Amazon Redshift query editor v2 or in your favorite business
intelligence (BI) tool. Enjoy the best price performance and familiar SQL features in an
easy-to-use, zero administration environment.

Regardless of the size of the dataset, Amazon Redshift offers fast query performance using the
same SQL-based tools and business intelligence applications that you use today.

## Are you a first-time Amazon Redshift

user?

If you are a first-time user of Amazon Redshift, we recommend that you begin by reading the
following sections:

- [Service Highlights
  and Pricing](https://aws.amazon.com/redshift/redshift-serverless "https://aws.amazon.com/redshift/redshift-serverless") – This product detail page provides the Amazon Redshift
  value proposition, service highlights, and pricing.
- [Get started with Amazon Redshift Serverless data warehouses](../gsg/new-user-serverless.md "../gsg/new-user-serverless.md") – This
  topic walks you through the process of setting up a serverless data warehouse,
  creating resources, and querying sample data.
- [Amazon Redshift Database Developer Guide](../dg.md "../dg.md") – If you are a database developer, this guide explains how
  to design, build, query, and maintain the databases that make up your data
  warehouse.

If you prefer to manage your Amazon Redshift resources manually, you can create provisioned
clusters for your data querying needs. For more information, see [Amazon Redshift
clusters](working-with-clusters.md "working-with-clusters.md").

As an application developer, you can use the Amazon Redshift API or the AWS Software
Development Kit (SDK) libraries to manage clusters programmatically. If you use the
Amazon Redshift API, you must authenticate every HTTP or HTTPS request to the API by signing
it. For more information about signing requests, go to [Signing an HTTP request](amazon-redshift-signing-requests.md "amazon-redshift-signing-requests.md").

For information about the API, CLI, and SDKs, go to the following links:

- [Amazon Redshift Serverless API
  Reference](../../../redshift-serverless/latest/APIReference/Welcome.md "../../../redshift-serverless/latest/APIReference/Welcome.md")
- [Amazon Redshift API Reference](../APIReference.md "../APIReference.md")
- [Amazon Redshift Data API API
  Reference](../../../redshift-data/latest/APIReference/Welcome.md "../../../redshift-data/latest/APIReference/Welcome.md")
- [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")
- SDK References in [Tools for Amazon Web
  Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
