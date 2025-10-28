# Connecting to data in Ray jobs

AWS Glue Ray jobs can use a broad array of Python packages that are designed for you to quickly integrate data.
We provide a minimal set of dependencies in order to not clutter your environment. For more information about
what is included by default, see [Modules provided with Ray jobs](edit-script-ray-env-dependencies.md#edit-script-ray-modules-provided "edit-script-ray-env-dependencies.md#edit-script-ray-modules-provided").

###### Note

AWS Glue extract, transform, and load (ETL) provides the DynamicFrame abstraction to streamline ETL workflows
where you resolve schema differences between rows in your dataset. AWS Glue ETL provides additional
features—job bookmarks and grouping input files. We don't currently provide corresponding features in
Ray jobs.

AWS Glue for Spark provides direct support for connecting to certain data formats, sources and sinks. In Ray,
AWS SDK for pandas and current third-party libraries substantively cover that need. You will need to
consult those libraries to understand what capabilities are available.

AWS Glue for Ray integration with Amazon VPC is not currently available. Resources in Amazon VPC will not be accessible
without a public route. For more information about using AWS Glue with Amazon VPC, see [Configuring interface VPC endpoints (AWS PrivateLink) for AWS Glue
(AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

## Common libraries for working with data in Ray

**Ray Data** – Ray Data provides methods to handle common data
formats, sources and sinks. For more information about supported formats and sources in Ray Data, see [Input/Output](https://docs.ray.io/en/latest/data/api/input_output.html "https://docs.ray.io/en/latest/data/api/input_output.html") in the Ray Data
documentation. Ray Data is an opinionated library, rather than a general-purpose library, for handling
datasets.

Ray provides certain guidance around use cases where Ray Data might be the best solution for your job. For
more information, see
[Ray use cases](https://docs.ray.io/en/latest/ray-overview/use-cases.html "https://docs.ray.io/en/latest/ray-overview/use-cases.html") in the Ray documentation.

**AWS SDK for pandas (awswrangler)** – AWS SDK for pandas is an
AWS product that delivers clean, tested solutions for reading from and writing to AWS services when your
transformations manage data with pandas DataFrames. For more information about supported formats and sources
in the AWS SDK for pandas, see the [API Reference](https://aws-sdk-pandas.readthedocs.io/en/stable/api.html "https://aws-sdk-pandas.readthedocs.io/en/stable/api.html") in the AWS SDK for pandas documentation.

For examples of how to read and write data with the AWS SDK for pandas, see [Quick Start](https://aws-sdk-pandas.readthedocs.io/en/stable/ "https://aws-sdk-pandas.readthedocs.io/en/stable/") in the AWS SDK for pandas
documentation. The AWS SDK for pandas doesn't provide transforms for your data. It only provides support
for reading and writing from sources.

**Modin** – Modin is a Python library that implements common pandas
operations in a distributable way. For more information about Modin, see the [Modin documentation](https://modin.readthedocs.io/en/stable/ "https://modin.readthedocs.io/en/stable/"). Modin itself doesn't provide
support for reading and writing from sources. It provides distributed implementations of common transforms.
Modin is supported by the AWS SDK for pandas.

When you run Modin and the AWS SDK for pandas together in a Ray environment, you can perform common ETL
tasks with performant results. For more information about using Modin with the AWS SDK for pandas, see
[At scale](https://aws-sdk-pandas.readthedocs.io/en/stable/scale.html "https://aws-sdk-pandas.readthedocs.io/en/stable/scale.html") in the AWS SDK
for pandas documentation.

**Other frameworks** – For more information about frameworks that Ray
supports, see
[The Ray Ecosystem](https://docs.ray.io/en/latest/ray-overview/ray-libraries.html "https://docs.ray.io/en/latest/ray-overview/ray-libraries.html") in the Ray documentation. We don't provide support for other frameworks in AWS Glue for
Ray.

## Connecting to data through the Data Catalog

Managing your data through the Data Catalog in conjunction with Ray jobs is supported with the AWS SDK for
pandas. For more information, see [Glue
Catalog](https://aws-sdk-pandas.readthedocs.io/en/3.0.0rc2/tutorials/005%20-%20Glue%20Catalog.html "https://aws-sdk-pandas.readthedocs.io/en/3.0.0rc2/tutorials/005%20-%20Glue%20Catalog.html") on the AWS SDK for pandas website.
