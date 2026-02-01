Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with using federated queries to

PostgreSQL

To create a federated query, you follow this general approach:

1. Set up connectivity from your Amazon Redshift cluster to your Amazon RDS or Aurora PostgreSQL DB instance.

To do this, make sure that your RDS PostgreSQL or Aurora PostgreSQL DB instance can
accept connections from your Amazon Redshift cluster. We recommend that your Amazon Redshift cluster and
Amazon RDS or Aurora PostgreSQL instance be in the same virtual private cloud (VPC) and subnet
group. This way, you can add the security group for the Amazon Redshift cluster to the inbound
rules of the security group for your RDS or Aurora PostgreSQL DB instance.

You can also set up VPC peering or other networking that allows Amazon Redshift to make
connections to your RDS or Aurora PostgreSQL instance.

For more information about VPC networking, see the following.

    * [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") in the
     *Amazon VPC Peering Guide*
    * [Working with a DB instance in a VPC](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md")  in the
     *Amazon RDS User Guide*

###### Note

There are cases where you must enable enhanced VPC routing: For example, if your Amazon Redshift cluster is in a different
VPC than your RDS or Aurora PostgreSQL instance, or if they're in the same VPC and your routes require it. Otherwise,
you might receive timeout errors when you run a federated query. 2. Set up secrets in AWS Secrets Manager for your RDS PostgreSQL and Aurora PostgreSQL
databases. Then reference the secrets in AWS Identity and Access Management (IAM) access policies and roles.
For more information, see [Creating a secret and an IAM role to use
federated queries](federated-create-secret-iam-role.md "federated-create-secret-iam-role.md").

###### Note

If your cluster uses enhanced VPC routing, you might need to configure an interface VPC endpoint for AWS Secrets Manager.
This is necessary when the VPC and subnet of your Amazon Redshift cluster don’t have access to the public AWS Secrets Manager endpoint.
When you use a VPC interface endpoint, communication between the Amazon Redshift cluster in your VPC and AWS Secrets Manager is routed privately
from your VPC to the endpoint interface. For more information,
see [Creating an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the
_Amazon VPC User Guide_. 3. Apply the IAM role that you previously created to the Amazon Redshift cluster. For more information, see
[Creating a secret and an IAM role to use
federated queries](federated-create-secret-iam-role.md "federated-create-secret-iam-role.md"). 4. Connect to your RDS PostgreSQL and Aurora PostgreSQL databases with an external schema. For more information,
see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md"). For examples on how to use federated query, see [Examples of using a federated query](federated_query_example.md "federated_query_example.md"). 5. Run your SQL queries referencing the external schema that references your RDS PostgreSQL and
Aurora PostgreSQL databases.
