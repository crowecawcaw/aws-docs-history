NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Source Servers in AWS Application Migration Service

You must add your source servers to the AWS Application Migration Service console in order to migrate them into
AWS. Source servers are added by installing the AWS Replication Agent on each individual
server. This documentation provides installation paths for both Linux and Windows
servers. Ensure that your servers are supported by AWS Application Migration Service by reviewing the [Supported operating systems](Supported-Operating-Systems.md "Supported-Operating-Systems.md")

In addition, AWS Application Migration Service allows you to perform [agentless snapshot
replication](agentless-mgn.md "agentless-mgn.md") from your vCenter source environment into AWS. This is achieved by
installing the Application Migration Service vCenter Client in your vCenter environment. Agentless snapshot replication
has its own unique credentials, installation, and replication mechanisms. AWS Application Migration Service recommends
using agent-based replication when possible, as it supports CDP (Continuous Data Protection) and
provides the shortest cutover window. Agentless replication should be used when your company's
policies or technical issues prevent you from installing the AWS Replication Agent on each
individual server.

Once your source servers have been added to AWS Application Migration Service, you can monitor and interact with them
from the Source servers page. The Source servers page is the default view in the AWS Application Migration Service
console, and is the page that you interact with the most. On the Source servers page, you can
view all of your source servers, monitor their migration lifecycle and data replication state, see
the next step in the migration process for each server, and sort your servers by a variety of
categories. You can also perform a variety of commands from the Source servers page through the
command menus. These menus allow you to full control your servers by managing data replication,
launching test and cutover instances, and disconnecting servers from AWS Application Migration Service.

You can click on any individual source server on the Source servers page in order to access
the server details view. This view allows you to see the details for individual servers. Here
you are able to see an in-depth view of the server's migration lifecycle, browse an overview
of the server's technical details, manage tags, manage disks, and most importantly, configure the
individual replication settings and launch settings for the server.

###### Topics

- [Adding source servers](adding-servers.md "adding-servers.md")
- [Installing the AWS Application Migration Service vCenter Client for Agentless Replication on vCenter source
  environments](agentless-mgn.md "agentless-mgn.md")
- [Manage source servers](server-list.md "server-list.md")
- [Access details on a source server](server-details.md "server-details.md")
