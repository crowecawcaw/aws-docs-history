# Migrations (including VMware)

AWS Transform can help you migrate your virtual and bare metal server environments to Amazon EC2
by using generative AI, including VMware, Hyper-V, and other sources.
This chapter provides an overview of AWS Transform migration capabilities and of the workflow of the migration
process.

## Capabilities and key features

AWS Transform offers the following capabilities and key features for migrating your
server environments to AWS.

- Multiple discovery options:

  - Assisted discovery of your VMware environment by using collectors from
    AWS Application Discovery Service.
  - Use the open-source [Export for
    vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter") tool (VMware environments).
  - Importing independently collected discovery data (any source environment).

- AI-driven conversion of your source network configuration to an
  Amazon VPC network architecture.
- AI-driven generation of migration plans, including application grouping and
  suggested migration waves.
- Rehosting your servers to run natively on Amazon EC2.
- Localized web application interface, allowing you to use AWS Transform for
  migrations in your preferred language. For more information, see
  [Language settings](transform-environment.md#transform-environment-language "transform-environment.md#transform-environment-language").

AWS Transform supports migrating Windows and Linux servers of supported operating systems.
For the full list of supported operating systems, see [Supported operating
systems](../../../mgn/latest/ug/Supported-Operating-Systems.md "../../../mgn/latest/ug/Supported-Operating-Systems.md") in the _AWS Transform MGN User
Guide_.

## AWS Transform migration architecture

This diagram displays an overview of AWS Transform migration architecture.

![AWS Transform VMware architecture](images/atx-vm-architecture_v2.png)
