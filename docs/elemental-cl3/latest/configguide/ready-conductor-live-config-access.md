# Accessing the

nodes

The procedures in this guide require you to access the AWS Elemental Conductor Live nodes and the worker
nodes. You might need to work with a node using the web interface or using the CLI (command line
interface).

## Working from the web

interface

At your workstation, open a web browser and enter the IP address or
hostname of the node.

**Limitations on using the web
interface**

You can't use the web interface to perform some configuration tasks. You must always use
the CLI. The affected configuration tasks are:

- DNS server. If at least one Ethernet interface on the node uses
  DHCP, you can only use the CLI to work with DNS. Otherwise, you can
  work with DNS using the web interface or the CLI.
- Ethernet interfaces: You can't create or modify an Ethernet
  interface using the web interface.
- Ethernet interface bonds: You can't create or modify a bond using
  the web interface.

## Working from the CLI

At your workstation, start a remote terminal session to the AWS Elemental Conductor Live node. For example,
use SSH and connect to the node using the IP address or hostname:

```
$ ssh myConductorLive
```

Log in to the node using the credentials for an administrator that has
been set up on the node. If you haven't set up users yet, use the user
credentials of the default _elemental_
user.
