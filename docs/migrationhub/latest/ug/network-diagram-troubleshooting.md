AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Troubleshooting the AWS Migration Hub network

diagram

Use the information here to help you troubleshoot and fix issues that you might encounter
when working with the network diagram in AWS Migration Hub.

###### Topics

- [Message that you need to install
  Discovery Agent](#troubleshooting-problem-need-agent "#troubleshooting-problem-need-agent")
- [Problems when adding servers or
  expanding diagram](#troubleshooting-problem-expand-diagram "#troubleshooting-problem-expand-diagram")

## Message that you need to install

Discovery Agent

The following topics describe scenarios when you get a message that you need to install
Discovery Agent.

### After choosing one or more servers on

the server list page, and then choosing **Visualize network**, you get a
message that you need to install a discovery agent on the server.

Add AWS Application Discovery Service Discovery Agent to the servers that you that want mapped in the network diagram.
For more information, see [Setting up Agent Based
Discovery](../../../application-discovery/latest/userguide/setting-up-agents.md "../../../application-discovery/latest/userguide/setting-up-agents.md") the _Application Discovery Service User Guide_.

### When trying add a server that doesn't

have discovery agent installed to a group, you get a message that you need to install
discovery agent on the server.

Add the Discovery Agent to the servers that you that want to be able to add to a group.

## Problems when adding servers or

expanding diagram

The following topics describe scenarios when you get a message when adding new servers or
expanding existing servers.

### When adding new servers or expanding

existing servers on the network diagram, you get a message that your choices will cause the
diagram to exceed its visual limit of 1,500 server nodes.

Retry adding fewer servers.

### When adding new servers or expanding

existing servers on the network diagram, you experience high latency that leads to a time
out.

Retry adding fewer servers.
