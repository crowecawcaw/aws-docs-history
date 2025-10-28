# Create a connection to GitHub Enterprise

Server

You use connections to associate your AWS resources with a third-party repository. You
can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to create a connection to GitHub Enterprise
Server.

Connections only provide access to repositories owned by the GitHub Enterprise Server
account that is used during connection creation to authorize installation of the GitHub
app.

Before you begin:

- You must already have a GitHub Enterprise Server instance and a repository in
  it.
- You need to be an administrator of the GitHub Enterprise Server instance in order
  to create GitHub apps and create a host resource as shown in this section.

###### Important

When you set up your host for GitHub Enterprise Server, a VPC endpoint for webhooks
event data is created for you. If you created your host before November 24, 2020, and
you want to use VPC PrivateLink webhook endpoints, you must first [delete](connections-host-delete.md "connections-host-delete.md") your
host and then [create](connections-host-create.md "connections-host-create.md") a new host.

###### Note

For organizations in GitHub Enterprise Server or GitLab self-managed, you don’t pass
an available host. You create a new host for each connection in your organization, and
you must be sure to enter the same information in the network fields (VPC ID, Subnet
IDs, and Security Group IDs) for the host. For more information, see [Connection and host setup for installed providers supporting organizations](troubleshooting-connections.md#troubleshooting-organization-host "troubleshooting-connections.md#troubleshooting-organization-host").

###### Topics

- [Create a connection to GitHub
  Enterprise Server (console)](connections-create-gheserver-console.md "connections-create-gheserver-console.md")
- [Create a connection to GitHub
  Enterprise Server (CLI)](connections-create-gheserver-cli.md "connections-create-gheserver-cli.md")
