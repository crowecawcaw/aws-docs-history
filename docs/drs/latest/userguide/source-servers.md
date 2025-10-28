# AWS DRS source servers

You must add your source servers to the AWS Elastic Disaster Recovery console in order to
replicate them into AWS. Source servers are added by installing the AWS Replication Agent on each
individual server. The following documentation provides installation paths for both Linux and
Windows servers. Ensure that your servers are supported by AWS Elastic Disaster Recovery by reviewing
the [supported Windows operating systems](Supported-Operating-Systems-Windows.md "Supported-Operating-Systems-Windows.md")
and [supported Linux operating systems](Supported-Operating-Systems-Linux.md "Supported-Operating-Systems-Linux.md") documentation.

Once your source servers have been added to AWS Elastic Disaster Recovery, you can monitor and interact with
them from the **Source Servers** page. The source servers page is the default view in the AWS Elastic Disaster Recovery
Console, and is the page that you interact with the most. On the **Source Servers** page you can
view all of your source servers, monitor their recovery readiness and data replication state,
see the last recovery result, see any pending actions, and sort your servers by column contents.
The command menus on the page allow you to perform source server actions such as adding source servers, editing settings, disconnecting, and deleting source servers.

You can choose the hostname of any individual source server on the source servers page in
order to access the server details view. This view allows you to see the details for individual
servers. Here you are able to see an in-depth overview of the server's recovery state, view the
server's technical details, manage tags, manage disks, and most importantly, configure the
individual replications settings and launch settings for the server.

###### Topics

- [Adding source servers to AWS DRS](adding-servers.md "adding-servers.md")
- [AWS DRS source servers page](server-list.md "server-list.md")
- [View server details with AWS DRS](server-details.md "server-details.md")
