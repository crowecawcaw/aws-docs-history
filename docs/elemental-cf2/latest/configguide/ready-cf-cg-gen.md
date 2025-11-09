This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# General Information

###### CPU-only and GPU-enabled

There are two processing architectures for AWS Elemental Server: CPU-only and GPU-enabled.

In an AWS Elemental Conductor File cluster, the Conductor File nodes and the AWS Elemental Server nodes must be either all running CPU-only versions of software, or all running GPU-enabled versions of software. So both Conductor File and all AWS Elemental Server nodes must all be running CPU-only software versions, or all be running GPU-enabled software.

###### Redundancy and Non-Redundant Clusters

The AWS Elemental Conductor File cluster can be set up in a redundant or non-redundant Conductor configuration.

- A redundant configuration involves setting up two Conductor File nodes. Only one Conductor node controls the cluster at a time, but both are active and performing database replication.
- In a non-redundant configuration, there is only one Conductor node.
  This table summarizes the available cluster options for AWS Elemental Conductor File:

| Workers       | Conductor                               |
| ------------- | --------------------------------------- |
| Non-redundant | Non-redundant (only one Conductor node) |
| Non-redundant | Redundant (two Conductor nodes)         |

This guide describes how to set-up all of these configurations.
