# Tutorial prerequisites and considerations

Before you start this tutorial, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md "accessing.md"). These steps include signing up for
AWS and creating an AWS Identity and Access Management (IAM) principal with access to Amazon Keyspaces. Take note of the
name of the IAM user and the access keys because you'll need them later in this
tutorial.

Create a keyspace with the name `myKeyspace`and at least one table to test
the connection using the VPC endpoint later in this tutorial. You can find detailed
instructions in [Getting started with Amazon Keyspaces (for Apache Cassandra)](getting-started.md "getting-started.md").

After completing the prerequisite steps, proceed to [Step 1: Launch an Amazon EC2
instance](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md").
