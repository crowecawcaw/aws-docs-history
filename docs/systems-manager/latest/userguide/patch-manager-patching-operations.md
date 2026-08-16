# How Patch Manager operations work

This section provides technical details that explain how Patch Manager, a tool in
AWS Systems Manager, determines which patches to install and how it installs them on each
supported operating system. For Linux operating systems, it also provides information
about specifying a source repository, in a custom patch baseline, for patches other than
the default configured on a managed node. This section also provides details about how
patch baseline rules work on different distributions of the Linux operating
system.

###### Note

The information in the following topics applies no matter which method or type of
configuration you are using for your patching operations:

- A patch policy configured in Quick Setup
- A Host Management option configured in Quick Setup
- A maintenance window to run a patch `Scan` or
  `Install` task
- An on-demand **Patch now** operation
