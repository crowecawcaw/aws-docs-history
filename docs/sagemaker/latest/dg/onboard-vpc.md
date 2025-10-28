# Choose an Amazon VPC

This topic provides detailed information about choosing an Amazon Virtual Private Cloud (Amazon VPC) when you
onboard to Amazon SageMaker AI domain. For more information about onboarding to SageMaker AI domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

By default, SageMaker AI domain uses two Amazon VPCs. One Amazon VPC is managed by Amazon SageMaker AI and provides
direct internet access. You specify the other Amazon VPC, which provides encrypted traffic between
the domain and your Amazon Elastic File System (Amazon EFS) volume.

You can change this behavior so that SageMaker AI sends all traffic over your specified Amazon VPC.
When you choose this option, you must provide the subnets, security groups, and interface
endpoints that are necessary to communicate with the SageMaker API and SageMaker AI runtime, and various
AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon CloudWatch, that are used by Studio.

When you onboard to SageMaker AI domain, you tell SageMaker AI to send all traffic over your Amazon VPC by
setting the network access type to **VPC only**.

###### To specify the Amazon VPC information

When you specify the Amazon VPC entities (that is, the Amazon VPC, subnet, or security group) in
the following procedure, one of three options is presented based on the number of entities
you have in the current AWS Region. The behavior is as follows:

- One entity – SageMaker AI uses that entity. This can't be changed.
- Multiple entities – You must choose the entities from the dropdown
  list.
- No entities – You must create one or more entities in order to use
  domain. Choose **Create <entity>** to open the VPC console in a
  new browser tab. After you create the entities, return to the domain **Get
  started** page to continue the onboarding process.
  This procedure is part of the Amazon SageMaker AI domain onboarding process when you choose
  **Set up for organizations**. Your Amazon VPC information is specified under
  the **Network** section.

1. Select the network access type.

###### Note

If **VPC only** is selected, SageMaker AI automatically applies the
security group settings defined for the domain to all shared spaces created in the
domain. If **Public internet only** is selected, SageMaker AI does not
apply the security group settings to shared spaces created in the domain.

    * **Public internet only** – Non-Amazon EFS traffic goes through
     a SageMaker AI managed Amazon VPC, which allows internet access. Traffic between the domain and
     your Amazon EFS volume is through the specified Amazon VPC.
    * **VPC only** – All SageMaker AI traffic is through the specified
     Amazon VPC and subnets. You must use a subnet that does not have direct internet access in
     **VPC only** mode. Internet access is disabled by default.

2. Choose the Amazon VPC.
3. Choose one or more subnets. If you don't choose any subnets, SageMaker AI uses all the subnets
   in the Amazon VPC. We recommend that you use multiple subnets that are not created in
   constrained Availability Zones. Using subnets in these constrained Availability Zones can
   result in insufficient capacity errors and longer application creation times. For more
   information about constrained Availability Zones, see [Constrained Availability Zones](../../../global-infrastructure/latest/regions/aws-availability-zones.md#constrained-zones "../../../global-infrastructure/latest/regions/aws-availability-zones.md#constrained-zones") in the _AWS Regions and Availability
   Zones User Guide_.
4. Choose the security groups. If you chose **Public internet only**,
   this step is optional. If you chose **VPC only**, this step is
   required.

###### Note

For the maximum number of allowed security groups, see [UserSettings](../APIReference/API_UserSettings.md "../APIReference/API_UserSettings.md").
For Amazon VPC requirements in **VPC only** mode, see [Connect Studio notebooks in
a VPC to external resources](studio-notebooks-and-internet-access.md "studio-notebooks-and-internet-access.md").
