# Securing access to an Amazon Neptune cluster

There are multiple ways for you to secure your Amazon Neptune clusters.

## Using IAM policies to restrict

access to a Neptune DB cluster

To control who can perform Neptune management actions on Neptune DB clusters and DB
instances, use AWS Identity and Access Management (IAM).

When you use an IAM account to access the Neptune console, you must first sign
in to the AWS Management Console using your IAM account before opening the Neptune console at
[https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").

When you connect to AWS using IAM credentials, your IAM account must have
IAM policies that grant the permissions required to perform Neptune management
operations. For more information, see [Using different kinds of IAM policies for
controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").

## Using VPC security groups to restrict

access to a Neptune DB cluster

Neptune DB clusters must be created in an Amazon Virtual Private Cloud (Amazon VPC). To control which devices
and EC2 instances can open connections to the endpoint and port of the DB instance for
Neptune DB clusters in a VPC, you use a VPC security group.
For more information about VPCs, see [Create a security group using the VPC console](get-started-vpc.md#security-vpc-security-group "get-started-vpc.md#security-vpc-security-group").

###### Note

To connect to your Neptune cluster you must expose the cluster's Database port (default of 8182) for
both the inbound and outbound rules to allow for proper connectivity.

## Using IAM authentication to restrict

access to a Neptune DB cluster

If you enable AWS Identity and Access Management (IAM) authentication in a Neptune DB cluster, anyone
accessing the DB cluster must first be authenticated. See [Authenticating your Amazon Neptune database with AWS Identity and Access Management](iam-auth.md "iam-auth.md") for information about setting up IAM authentication.

For information about using temporary credentials to authenticate, including examples for
the AWS CLI, AWS Lambda, and Amazon EC2, see [Using temporary credentials to connect to Amazon Neptune](iam-auth-temporary-credentials.md "iam-auth-temporary-credentials.md").

The following links provide additional information about connecting to Neptune
using IAM authentication with the individual query languages:

###### Using Gremlin with IAM authentication

- [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
- [Connecting to Amazon Neptune databases using IAM with
  Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")

###### Note

This example applies to both Gremlin and SPARQL.

###### Using openCypher with IAM authentication

- [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md")
- [Connecting to Amazon Neptune databases using IAM with
  Gremlin Java](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")

###### Note

This example applies to both Gremlin and SPARQL.

###### Using SPARQL with IAM authentication

- [Connecting to Amazon Neptune databases using IAM authentication with Java and
  SPARQL](iam-auth-connecting-sparql-java.md "iam-auth-connecting-sparql-java.md")
- [Connecting to Amazon Neptune databases using IAM authentication with Python](iam-auth-connecting-python.md "iam-auth-connecting-python.md")

###### Note

This example applies to both Gremlin and SPARQL.
