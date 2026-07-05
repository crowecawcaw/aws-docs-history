Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Multi-AZ deployment

Amazon Redshift supports multiple Availability Zones (Multi-AZ) deployments for provisioned RG or RA3
clusters. By using Multi-AZ deployments, your Amazon Redshift data warehouse can continue operating in
failure scenarios when an unexpected event happens in an Availability Zone. A Multi-AZ
deployment deploys compute resources in two Availability Zones (AZs) and these compute
resources can be accessed through a single endpoint. In the event of an entire Availability
Zone failure, the remaining compute resources in the second Availability Zone are available
to continue processing workloads. Amazon Redshift charges the same hourly compute rates for RG or RA3
when running a Multi-AZ data warehouse. Storage costs remain the same as it is shared across
all Availability Zones within and AWS Region.

Currently, Amazon Redshift supports zero Recovery Point Objective (RPO) that allows data to be
current and up-to-date in the event of a failure. With Multi-AZ deployment, Amazon Redshift further
enhances its existing recovery capabilities and reduces its Recovery Time Objective (RTO).
This is possible because a Multi-AZ deployment can recover faster from a failure or disaster
thereby elevating the Amazon Redshift Service Level Agreement (SLA) to 99.99% as compared to
99.9% with a Single-AZ data warehouse.
