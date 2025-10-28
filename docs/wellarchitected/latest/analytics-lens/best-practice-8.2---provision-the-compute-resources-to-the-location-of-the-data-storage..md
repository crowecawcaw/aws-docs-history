# Best practice 8.2 – Provision the compute resources to the location of the data storage

Data analytics workloads require moving data through a
pipeline, either for ingesting data, processing intermediate
results, or producing curated datasets. It is often
more efficient to select the location of data processing
services near where the data is stored. This approach is
preferred instead of copying or streaming large amounts
of data to the processing location. For example, if an
Amazon Redshift cluster frequently ingests data from a data
lake, ensure that the Amazon Redshift cluster is in the same
Region as your data lake S3 buckets.

This extends to considering where your compute and storage are located at the Availability Zone level. Co-locating in the same Availability Zone allows fast, lower latency access. It is still important, however, to replicate data across zones when required.

## Suggestion 8.2.1 – Migrate or copy primary data stores from on-premises environments to AWS so that cloud compute and storage are closely located

Minimize duplication of data when transferring datasets from on-premises storage to the cloud. Instead, create copies of your data near the analytics platform to avoid data transfer latency and improve overall performance of the analytics solution. For optimal performance, keep your data and analytics systems in the same AWS Region. If they are in separate Regions, relocate one of them.

## Suggestion 8.2.2 – Consider where your analytics resources are placed

For optimal performance, your organization should align the location of the data with the location of the resources that process it. Where possible, your organization should
consider using a permanent Region for all data analytics
processing as this will help with data transferring
overhead.

## Suggestion 8.2.3 – Consider the use of provisioned compared to serverless offerings to match your workload pattern

When considering services for ingesting, transforming, and analyzing your data, there is often the choice between provisioned or serverless solutions. There are many trade-offs and potential advantages of each, but from a performance perspective, it can be beneficial to use serverless offerings when your workloads are consistently and unpredictably spikey. Whereas provisioned deployments may offer advantages when you have more stable, predictable workloads.
