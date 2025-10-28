# Connections concepts

Setting up and using the connections feature is easier if you understand the concepts and
terms. Here are some concepts to know about as you use connections in the
Developer Tools console:

installation

An instance of the AWS app on a third-party account. Installing the AWS CodeStar
Connector app allows AWS to access resources within the third-party account.
An installation can only be edited on the third-party provider’s website.

connection

An AWS resource used to connect third-party source repositories to other
AWS services.

third-party repository

A repository that is provided by a service or company that is not part of
AWS. For example, a
Bitbucket
repository is a third-party repository.

provider type

A service or company that provides the third-party source repository you want
to connect to. You connect your AWS resources to external _provider types_. A provider type where the source
repository is installed on the network and infrastructure is an installed
provider type. For example, GitHub Enterprise Server is an installed provider
type.

host

A resource that represents the infrastructure where a third-party provider is
installed. Connections use the host to represent the server where your
third-party provider is installed, such as GitHub Enterprise Server. You create
one host for all connections to that provider type.

###### Note

When you use the console to create a connection to GitHub Enterprise
Server, the console creates a host resource for you as part of the
process.
