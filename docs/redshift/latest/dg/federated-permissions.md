Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift federated permissions

Amazon Redshift federated permissions simplifies permissions management across multiple Redshift data warehouses by enabling you to
define data permissions once and automatically enforce them across all warehouses in your AWS account.
This eliminates the need to redefine, manage permissions and fine grained access control policies across multiple warehouses.

When you register Redshift warehouse namespace/cluster with AWS Glue Data Catalog, all databases from registered warehouse namespaces/clusters are automatically mounted
in every warehouse, providing seamless data discovery without manual configuration.

You define permissions on database objects using familiar Redshift SQL commands, specifying global identities through AWS Identity and Access Management (IAM) or AWS IAM Identity Center.
These permissions are stored along with the warehouse data and enforced consistently regardless of which warehouse executes the query.

## Key concepts

- **Redshift warehouse with federated permissions**: The producer warehouse that is registered with Data Catalog and where data and Redshift permissions are stored.
- **Consuming Redshift warehouse**: Any warehouse that queries data from remote warehouse. Consuming warehouse can optionally be enabled for Redshift federated permissions.
- **Global identity**: IAM and IAM Identity Center provides global identity across all warehouses enabled for Redshift federated permissions. Users authenticate once through their
  existing identity provider and receive consistent access based on their global identity, regardless of which warehouse they connect to.
- **Auto-mounting**: All warehouses enabled for Redshift federated permissions are automatically visible in all warehouses within your account. This auto-mounting
  capability enables catalog and database discovery for cross-warehouse analytics.
- **Identity propagation**: When you execute a cross-warehouse query, Redshift propagates your global identity (IAM role or IAM Identity Center user) to the remote warehouse.
- **Authorization across warehouses**: The remote warehouse enabled Redshift federated permissions validates your permissions for cross-warehouse queries and are enforced in the consuming warehouses.
- **Fine grained access control**: Policies for Row Level Security (RLS), Column Level Policies (CLP), and Dynamic Data Masking (DDM) that can be enforced across warehouses.

## Benefits

**Simplified administration**

- Define permissions once on the warehouse
- Automatically enforce same permissions across all consuming warehouses
- Eliminate the need to redefine, manage permissions and fine-grained access control policies across multiple warehouses
- Reduce administrative overhead and potential for configuration errors

**Enhanced security and compliance**

- Ensure consistent security policy enforcement across all warehouses
- Implement fine-grained access controls at table, and column level
- Audit permissions from any warehouse
- Enhanced compliance tooling with additional SHOW commands

**Improved user experience**

- Register once and no need to manually create data shares
- Single sign-on across all warehouses and consistent access based on global identity
- Seamless namespace discovery without manual catalog configuration
- No need to manage separate local user accounts in each warehouse

**Horizontal scalability**

- Add new warehouses without increasing governance complexity
- New consuming warehouses automatically enforce permission policies
- Analysts immediately see all databases from registered warehouses

## Use Cases

**Workload isolation with unified governance**

Separate compute resources for different workloads (ETL, analytics, reporting) while maintaining consistent security policies across all warehouses.

**Multi-team data access**

Enable multiple teams to access shared data from their own warehouses with appropriate access controls automatically enforced.

**Data mesh architecture**

Implement a data mesh approach where multiple independent compute resources operate on shared data with unified governance.

**Cost optimization**

Scale compute resources independently for different use cases while maintaining centralized permission management.
