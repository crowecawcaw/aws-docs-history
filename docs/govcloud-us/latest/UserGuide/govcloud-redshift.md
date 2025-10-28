# Amazon Redshift in AWS GovCloud (US)

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools. It is optimized for datasets ranging from a few hundred gigabytes to a petabyte or more and costs less than $1,000 per terabyte per year, a tenth the cost of most traditional data warehousing solutions.

## How Amazon Redshift differs for AWS GovCloud (US)

- To connect to Amazon Redshift with SSL, you must download the Amazon Redshift certificate bundle from [https://s3.us-gov-west-1.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt](https://s3.us-gov-west-1.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt "https://s3.us-gov-west-1.amazonaws.com/redshift-downloads/amazon-trust-ca-bundle.crt"). For more information, see [Configure Security Options for Connections.](../../../redshift/latest/mgmt/connecting-ssl-support.md "../../../redshift/latest/mgmt/connecting-ssl-support.md")
- The COPY EXPLICIT_IDS parameter is not available.

## Documentation for Amazon Redshift

[Amazon Redshift documentation](http://aws.amazon.com/documentation/redshift/ "http://aws.amazon.com/documentation/redshift/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Redshift metadata is not permitted to contain export-controlled data. This metadata
  includes all configuration data that you enter when creating and maintaining your Amazon Redshift
  clusters except the master password.
- Do not enter export-controlled data in the following fields:
  - Database instance identified
  - Master user name
  - Database name
  - Database snapshot name
  - Database security group name
  - Database security group description
  - Database parameter group name
  - Database parameter group description
  - Option group name
  - Option group description
  - Database subnet group name
  - Database subnet group description
  - Event subscription name
  - Resource tags

If you are processing export-controlled data with Amazon Redshift, follow these guidelines in order to
maintain export
compliance:

- When
  you use the console or the AWS APIs, the only data field that is protected as
  export-controlled data is the Amazon Redshift Master Password.
- After you create your database, change the master password of your Amazon Redshift cluster by
  directly using the database client.
- You can enter export-controlled data into any data fields by using your database
  client-side tools. Do not pass export-controlled data by using the web service APIs that are
  provided by Amazon Redshift.
- To secure export-controlled data in your VPC, set up access control lists (ACLs) to
  control traffic entering and exiting your VPC. If you have multiple databases configured
  with different ports, set up ACLs on all the ports.
  - For example, if you're running an application server on an Amazon EC2 instance that
    connects to an Amazon Redshift cluster,
    a
    non-U.S. person could reconfigure the DNS to redirect
    export-controlled data out of the VPC and into any server that could possibly be outside
    of the AWS GovCloud (US) Regions.

  To prevent this type of attack and to maintain export compliance, use network ACLs
  to prevent network traffic from exiting the VPC on the database port. For more
  information, see [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md") in the
  _Amazon VPC User Guide_.

- For each cluster that contains export-controlled data, ensure that only specific CIDR
  ranges and Amazon EC2 security groups can access the cluster, especially when an Internet
  gateway is attached to the VPC. Only allow connections that are from the
  AWS GovCloud (US) Regions or other export-controlled environments to export-controlled
  clusters.

If you are processing export-controlled data with this service,
use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
