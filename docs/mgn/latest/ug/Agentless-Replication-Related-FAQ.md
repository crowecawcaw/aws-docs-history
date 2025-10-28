NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Agentless replication related

This section contains answers to questions about agentless replication.

###### Topics

- [In which situations would you recommend using
  agentless replication (snapshot shipping)?](#faq-agentless-situations "#faq-agentless-situations")
- [In which situations would you recommend using
  agent-based replication?](#faq-agentless-situations-agent "#faq-agentless-situations-agent")
- [How does agentless replication work?](#faq-agentless-work "#faq-agentless-work")
- [Does agentless replication require installing
  any component in the customer's source data center?](#faq-agentless-component "#faq-agentless-component")
- [Is the agentless feature available in all
  Regions that AWS MGN service supports?](#faq-agentless-regions "#faq-agentless-regions")
- [Does agentless replication support the same
  source operating systems that are supported by agent-based replication?](#faq-agentless-os "#faq-agentless-os")
- [Is the agentless feature supported in
  CloudEndure migration?](#faq-agentless-cloudendure "#faq-agentless-cloudendure")
- [Which virtualization environments are supported
  by the agentless feature?](#faq-agentless-virtualization "#faq-agentless-virtualization")
- [On which operating systems can the MGN vCenter
  Client be installed?](#faq-agentless-os-client "#faq-agentless-os-client")
- [Do I need to generate special credentials to
  install the MGN vCenter Client?](#faq-agentless-credentials "#faq-agentless-credentials")
- [What are the agentless replication
  prerequisites?](#faq-agentless-credentials-prereques "#faq-agentless-credentials-prereques")
- [How do I install the MGN vCenter Client?](#faq-agentless-how-install "#faq-agentless-how-install")
- [Can a proxy server be used between the source server
  and the AWS Application Migration Service console?](#faq-agentless-proxy "#faq-agentless-proxy")

## In which situations would you recommend using

agentless replication (snapshot shipping)?

Agentless replication best serves customers whose company's security policies do not
allow installing an agent on each of their source servers, or for operating systems that are
only supported by agentless replication. This solution is only available for data centers
using vCenter version 6.7, 7.0 and 8.0.

## In which situations would you recommend using

agent-based replication?

Agent-based replication is our default recommendation for all use cases, except when
your company's security policies prevent you from using this method or if the OS is not
supported. Using agent-based replication provides Continuous Data Replication, and ensures a
cutover window of minutes . When using agentless replication, the data is transferred using
snapshot shipping. Upon cutover, you may need to wait to have a fully updated snapshot, and
your cutover window may be longer.

## How does agentless replication work?

You can learn more about how agentless replication works and see a high-level diagram of
the agentless replication framework in the [agentless
replication documentation](agentless-mgn.md "agentless-mgn.md").

## Does agentless replication require installing

any component in the customer's source data center?

Yes. In order to use agentless replication, customers must install the MGN vCenter
Client in their source data center. The client discovers the source servers and replicates
their data to AWS.

## Is the agentless feature available in all

Regions that AWS MGN service supports?

Yes. Both agent-based and agentless replication is supported in AWS Application Migration Service (AWS MGN) in all
Regions.

## Does agentless replication support the same

source operating systems that are supported by agent-based replication?

Agentless replication supports all of the [supported Windows operating systems](Supported-Operating-Systems.md#Supported-Operating-Systems-Windows "Supported-Operating-Systems.md#Supported-Operating-Systems-Windows") and [supported Linux operating systems](Supported-Operating-Systems.md#Supported-Operating-Systems-Linux "Supported-Operating-Systems.md#Supported-Operating-Systems-Linux") of agent-based replication.

## Is the agentless feature supported in

CloudEndure migration?

No. This feature is only available on AWS Application Migration Service.

## Which virtualization environments are supported

by the agentless feature?

The agentless replication feature is available for vCenter versions 6.7, 7.0 and 8.0. Other
virtualization environments are not supported.

## On which operating systems can the MGN vCenter

Client be installed?

The MGN vCenter Client can be installed on the following 64 bit Linux versions:

- Ubuntu 18.x+ (64 bit) - 22.04
- Amazon Linux 2
- RHEL 8.x

## Do I need to generate special credentials to

install the MGN vCenter Client?

Yes. In order to use the AWS MGN vCenter Client, you must first generate the correct IAM
credentials. Learn more in the [agentless replication documentation](vcenter-credentials-mgn.md "vcenter-credentials-mgn.md").

## What are the agentless replication

prerequisites?

The only prerequisite for agentless replication is to ensure that you have initialized AWS Application Migration Service.

## How do I install the MGN vCenter Client?

You can learn more about installing the MGN vCenter Client as well as installation
requirements in the [agentless replication
documentation](installing-vcenter-appliance-mgn.md "installing-vcenter-appliance-mgn.md").

## Can a proxy server be used between the source server

and the AWS Application Migration Service console?

Yes. You can configure transparent proxy either by using an environment variable prior to the installation (Linux and Windows),
or by using the --proxy-address flag in the Linux installer:

- Using the installer: ./aws-vcenter-client-installer-init.py --proxy-address http://PROXY:PORT/
- Using environment variable: export https_proxy=http://PROXY:PORT/; ./aws-vcenter-client-installer-init.py

Make sure the proxy has a trailing forward slash (/).
