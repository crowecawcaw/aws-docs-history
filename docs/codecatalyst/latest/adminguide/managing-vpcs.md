Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Connecting an Amazon VPC to an Amazon CodeCatalyst space

_Amazon Virtual Private Clouds_ (Amazon VPCs) are virtual networks that provide extra security to your application by
isolating it from the public internet. By connecting to an Amazon VPC, users can securely run workflow actions and create Dev Environments
linked to your VPC in CodeCatalyst. You can set a default VPC connection for a space, so that all workflow runs and Dev Environments will run
connected to that VPC.

A _VPC connection_ is a CodeCatalyst resource which contains all of the configurations
needed for your workflow to access a VPC. Space administrators can add their own VPC connections in the
Amazon CodeCatalyst console on behalf of space members. By adding a VPC connection, space members can run
workflow actions and create Dev Environments that adhere to network rules and can access resources in the associated VPC.

For more information about setting up a VPC, see the [Amazon VPC User
Guide](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md").

**Considerations for administering VPC connections**

- You must have the **Space administrator** role or **Power user** role to manage VPC connections at the space level.
- **Project administrators** can associate a VPC connection to their environment and **Contributors**
  can associate that VPC-connected environment with a workflow. When administering VPC connections as a **Space administrator**, you
  are maintaining these resources on behalf of space members.

###### Topics

- [Use cases](#managing-vpcs.use-cases "#managing-vpcs.use-cases")
- [How do I get started with VPC connections?](#managing-vpcs.how-to "#managing-vpcs.how-to")
- [Limitations of VPC connections in CodeCatalyst](#managing-vpcs.limitations "#managing-vpcs.limitations")
- [Setting up an Amazon VPC](managing-vpcs.md "managing-vpcs.md")
- [Adding VPC connections for a space](managing-vpcs.md "managing-vpcs.md")
- [Configuring VPC endpoints for a space](managing-vpcs.md "managing-vpcs.md")
- [Managing a default VPC connection for a space](managing-vpcs.md "managing-vpcs.md")
- [Editing VPC connections for a space](managing-vpcs.md "managing-vpcs.md")
- [Removing VPC connections for a space](managing-vpcs.md "managing-vpcs.md")

## Use cases

VPC connectivity from CodeCatalyst actions makes it possible to:

- Run a workflow action that follows the network rules of a VPC connection.
- Run a workflow action that accesses resources running in a VPC.
- Deploy an update to an Amazon EKS cluster running in a VPC.

## How do I get started with VPC connections?

The high-level steps to add and use a VPC connection are as follows:

1. In the AWS Management Console, **create an Amazon Virtual Private Cloud (VPC)** or use an existing VPC. A VPC is a virtual network that provides extra
   security to your application by isolating it from the public internet and allows you to securely run your workflow actions in CodeCatalyst. In order for
   your VPC to work with CodeCatalyst, it must have a certain configuration. For more information, see [Amazon VPC setup requirements](managing-vpcs.md#managing-vpcs.requirements "managing-vpcs.md#managing-vpcs.requirements").
2. In your CodeCatalyst space settings, **create a VPC connection**. A
   _VPC connection_ is a CodeCatalyst resource which contains all of the configurations needed for a workflow to access a VPC. For more information,
   see [Adding VPC connections for a space](managing-vpcs.md "managing-vpcs.md").
3. Associate this VPC connection with an **environment** to use with your workflow actions. For more information,
   see [Associating a VPC connection with an environment](../userguide/deploy-environments-associate-vpc.md "../userguide/deploy-environments-associate-vpc.md") in the _CodeCatalyst User Guide_.
4. Within a workflow, associate the VPC-connected environment to your **workflow action**. When an action is configured with an environment
   that has a VPC connection, the action will run connected to the VPC, adhere to the network rules, and access resources specified by the associated VPC.
   For more information, see [Associating an environment, account connection, and IAM role with a workflow action](../userguide/deploy-environments-add-app-to-environment.md "../userguide/deploy-environments-add-app-to-environment.md") in the _CodeCatalyst User Guide_.
5. Create a **Dev Environment** associated to your VPC connection. For more information, see [Creating a Dev Environment](../userguide/devenvironment-create.md "../userguide/devenvironment-create.md") in the _CodeCatalyst User Guide_.

## Limitations of VPC connections in CodeCatalyst

- CodeCatalyst only supports creating VPC connections in the same region. For more information on the available regions, see [CodeCatalyst VPC endpoint service names](managing-vpcs.md#managing-vpcs.endpoint-service-names "managing-vpcs.md#managing-vpcs.endpoint-service-names").
- CodeCatalyst does not support VPC connectivity with the Lambda compute type. Instead, use the Amazon EC2 compute type.
- CodeCatalyst does not support VPC connectivity with Windows. Instead, use Linux.
- VPC connectivity may lead to longer action run times.
