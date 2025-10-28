Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up Multi-AZ deployment

To set up a Multi-AZ deployment, select the **Multi-AZ** option and
specify the number of compute nodes to provision in each Availability Zone. Amazon Redshift
automatically deploys equal compute resources across two Availability Zones and all
compute resources are always available for both read and write processing during normal
operation. This allows a Multi-AZ deployment to act as a single data warehouse with a
single endpoint, removing the need for application changes when a disaster occurs.
Although a Multi-AZ deployment processes an individual query using the compute resources
residing in only one Availability Zone, it can automatically distribute processing of
multiple simultaneous queries to both Availability Zones to boost overall throughput for
high concurrency workloads.

You can also convert an existing Single-AZ data warehouse into a Multi-AZ data
warehouse or vice versa. Everything remains the same except that additional compute
resources are provisioned in the second Availability Zone. When migrating to Multi-AZ
from an existing Single-AZ cluster, you might be required to double the number of
cluster nodes needed, to facilitate that single query performance is maintained. Most
workloads observe an increase in overall query processing throughput with a Multi-AZ
data warehouse as there is twice the amount of compute resources available.

In the event of a failure in an Availability Zone, Amazon Redshift continues operating by
using the resources in the remaining Availability Zone automatically. However, user
connections might be lost and must be re-established. In addition, queries that were
running in the failed Availability Zone can fail and must be retried. However, you can
reconnect to your cluster and reschedule queries immediately, and Amazon Redshift will process
the queries in the remaining Availability Zone. Queries issued at or after a failure
occurs might experience runtime delays while the Multi-AZ data warehouse is
recovering.

###### Note

To achieve better performance and higher availability, we recommend that you use
SNAPSHOT ISOLATION with your Multi-AZ clusters. For more information, see [CREATE
DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md").

## Limitations

A Multi-AZ data warehouse has the same functional capabilities as a Single-AZ data
warehouse, except for the following limitations that apply to a Multi-AZ data
warehouse:

- You can't create an unencrypted Multi-AZ data warehouse. Make sure to
  add an encryption when creating a new Multi-AZ data warehouse, converting a
  Single-AZ data warehouse into a Multi-AZ data warehouse, or converting a
  Single-AZ data warehouse into a Multi-AZ data warehouse.
- You can't create a single node Multi-AZ deployment for any of the RA3
  instance types. Choose 2 or more nodes per Availability Zone while creating
  a Multi-AZ deployment.
- Amazon Redshift doesn't support a subnet configuration that can support
  fewer than three Availability Zones. In other words, the configured subnet
  group requires three or more subnets.
- You can't relocate a Multi-AZ deployment to another Availability
  Zone. Relocation will be automatically determined and conducted by Amazon Redshift
  when using Multi-AZ deployment.
- You can't pause or resume a Multi-AZ deployment.
- You can't run your Multi-AZ deployment outside of the supported port
  ranges 5431 to 5455 and 8191 to 8215.
- You can't use STL, SVCS, SVL, SVV, STV views with Multi-AZ
  deployments as they only support system monitoring views (SYS\_\* views).
  Change your monitoring queries to use system monitoring views (SYS\_\*
  views).
- You can't attach an Elastic IP address to an existing cluster with
  Multi-AZ enabled.
- You can't convert a cluster with an attached Elastic IP address from
  Single-AZ to Multi-AZ.
- Amazon Redshift Multi-AZ deployment is available in the following AWS Regions:
  - US East (Ohio) (us-east-2)
  - US East (N. Virginia) (us-east-1)
  - US West (Oregon) (us-west-2)
  - Africa (Cape Town) (af-south-1)
  - Asia Pacific (Hong Kong) (ap-east-1)
  - Asia Pacific (Taipei) (ap-east-2)
  - Asia Pacific (Hyderabad) (ap-south-2)
  - Asia Pacific (Jakarta) (ap-southeast-3)
  - Asia Pacific (Malaysia) (ap-southeast-5)
  - Asia Pacific (Melbourne) (ap-southeast-4)
  - Asia Pacific (Mumbai) (ap-south-1)
  - Asia Pacific (Osaka) (ap-northeast-3)
  - Asia Pacific (Seoul) (ap-northeast-2)
  - Asia Pacific (Singapore) (ap-southeast-1)
  - Asia Pacific (Sydney) (ap-southeast-2)
  - Asia Pacific (New Zealand) (ap-southeast-6)
  - Asia Pacific (Thailand) (ap-southeast-7)
  - Asia Pacific (Tokyo) (ap-northeast-1)
  - Canada (Central) (ca-central-1)
  - China (Beijing) (cn-north-1)
  - China (Ningxia) (cn-northwest-1)
  - Europe (Frankfurt) (eu-central-1)
  - Europe (Ireland) (eu-west-1)
  - Europe (London) (eu-west-2)
  - Europe (Milan) (eu-south-1)
  - Europe (Paris) (eu-west-3)
  - Europe (Spain) (eu-south-2)
  - Europe (Stockholm) (eu-north-1)
  - Europe (Zurich) (eu-central-2)
  - Israel (Tel Aviv) (il-central-1)
  - Mexico (Central) (mx-central-1)
  - Middle East (Bahrain) (me-south-1)
  - Middle East (UAE) (me-central-1)
  - South America (São Paulo) (sa-east-1)
  - AWS GovCloud (US-East) (us-gov-east-1)
  - AWS GovCloud (US-West) (us-gov-west-1)

- Publicly accessible Multi-AZ data warehouses support 1 less VPC security
  group than Single-AZ and privately accessible Multi-AZ warehouses.
