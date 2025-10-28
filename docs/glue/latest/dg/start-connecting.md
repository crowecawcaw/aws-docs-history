# Setting up network access to data stores

To run your extract, transform, and load (ETL) jobs, AWS Glue must be able to access your data
stores. If a job doesn't need to run in your virtual private cloud (VPC) subnet—for
example, transforming data from Amazon S3 to Amazon S3—no additional configuration is
needed.

If a job needs to run in your VPC subnet—for
example, transforming data from a JDBC data store in a private subnet—AWS Glue

sets up [elastic network
interfaces](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") that enable your jobs to connect securely to other resources within
your VPC. Each elastic network interface is assigned a private IP address from the IP
address range within the subnet you specified. No public IP addresses are assigned.
Security groups specified in the AWS Glue connection are applied on each of the elastic network interfaces.
For more information, see [Setting up Amazon VPC for JDBC connections to Amazon RDS data stores from
AWS Glue](setup-vpc-for-glue-access.md "setup-vpc-for-glue-access.md").

All JDBC data stores that are accessed by the job must be available from the VPC subnet. To
access Amazon S3 from within your VPC, a [VPC endpoint](vpc-endpoints-s3.md "vpc-endpoints-s3.md") is
required. If your job needs to access both VPC resources and the public internet,

the VPC needs to have a Network Address Translation (NAT) gateway inside the VPC.

A job or development endpoint can only access one VPC (and subnet) at a time. If you need to access data stores in different VPCs, you have the following options:

- Use VPC peering to access the data stores.
  For more about VPC peering, see [VPC Peering Basics](../../../vpc/latest/peering/vpc-peering-basics.md "../../../vpc/latest/peering/vpc-peering-basics.md")
- Use an Amazon S3 bucket as an intermediary storage location. Split the work into two jobs, with the Amazon S3 output of job 1 as the input to job 2.
  For details on how to connect to a Amazon Redshift data store using Amazon VPC, see [Configuring Redshift connections](aws-glue-programming-etl-connect-redshift-home.md#aws-glue-programming-etl-connect-redshift-configure "aws-glue-programming-etl-connect-redshift-home.md#aws-glue-programming-etl-connect-redshift-configure").

For details on how to connnect to Amazon RDS data stores using Amazon VPC, see [Setting up Amazon VPC for JDBC connections to Amazon RDS data stores from
AWS Glue](setup-vpc-for-glue-access.md "setup-vpc-for-glue-access.md").

Once necessary rules are set in Amazon VPC, you create a connection in AWS Glue with the necessary properties to connect to your data stores.
For more information about the connection, see
[Connecting to data](glue-connections.md "glue-connections.md").

###### Note

Make sure you set up your DNS environment for AWS Glue. For more information,
see [Setting up DNS in your VPC](set-up-vpc-dns.md "set-up-vpc-dns.md").

###### Topics

- [Setting up a VPC to connect to PyPI for
  AWS Glue](setup-vpc-for-pypi.md "setup-vpc-for-pypi.md")
- [Setting up DNS in your VPC](set-up-vpc-dns.md "set-up-vpc-dns.md")
