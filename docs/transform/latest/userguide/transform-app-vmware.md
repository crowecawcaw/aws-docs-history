# VMware migration

AWS Transform can help you migrate your VMware environment to Amazon EC2 by using generative AI.
This document provides an overview of AWS Transform and of the workflow of the migration
process.

## Capabilities and key features

AWS Transform offers the following capabilities and key features for migrating your VMware
environment to AWS.

- Three discovery options:
  - Assisted discovery of your VMware environment by using collectors from
    AWS Application Discovery Service.
  - Use the open-source [Export for
    vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter") tool.
  - Importing independently collected discovery data.

- AI-driven conversion of your source VMware network configuration to an
  Amazon VPC network architecture.
- AI-driven generation of migration plans, including application grouping and
  suggested migration waves.
- Rehosting your servers to run natively on Amazon EC2.

AWS Transform supports migrating Windows and Linux servers of supported operating systems.
For the full list of supported operating systems, see [Supported operating
systems](../../../mgn/latest/ug/Supported-Operating-Systems.md "../../../mgn/latest/ug/Supported-Operating-Systems.md") in the _AWS Transform MGN User
Guide_.

## AWS Transform VMware migration architecture

This diagram displays an overview of AWS Transform VMware migration architecture.

![AWS Transform VMware architecture](images/atx-vm-architecture_v2.png)
