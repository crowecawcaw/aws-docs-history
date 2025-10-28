# Best practice 11.1 – Decouple storage from compute

It’s common for data assets to grow exponentially year over
year. However, your compute needs might not grow at the same
rate. Decoupling storage from compute allows you to manage
the cost of storage and compute separately, and implement
different cost optimization features to minimize cost.

## Suggestion 11.1.1 – Use services that decouple compute from storage

Services that allow independent scaling of storage and compute allow for greater flexibility when handling workloads. This means when your workload is compute intensive you do not need to deploy a large storage array to meet the compute power for running your workload.

## Suggestion 11.1.2 – Use Amazon Redshift RA3 instances types

Amazon Redshift RA3 instance types support the ability to
decouple the compute and storage. This allows your Amazon Redshift storage to scale independently from your compute
resources, which improves cost efficiencies for your data
warehousing workloads.

## Suggestion 11.1.3 – Use a decoupled ﬁle system for Big Data workloads

The EMR file system (EMRFS) is an implementation of HDFS
that all Amazon EMR clusters use for reading and writing
regular files from Amazon EMR directly to Amazon S3. By
using EMRFS, your organization is only charged for the
storage used, rather than paying for overprovisioned and
underutilized HDFS EBS storage.
