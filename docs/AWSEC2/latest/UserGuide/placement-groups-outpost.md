# Placement groups on AWS Outposts

AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs,
and tools to customer premises. By providing local access to AWS managed
infrastructure, AWS Outposts enables customers to build and run applications on premises using
the same programming interfaces as in AWS Regions, while using local compute and
storage resources for lower latency and local data processing needs.

An Outpost is a pool of AWS compute and storage capacity deployed at a customer
site. AWS operates, monitors, and manages this capacity as part of an AWS Region.

You can create placement groups on Outposts that you have created in your account.
This allows you to spread out instances across underlying hardware on an Outpost at your
site. You create and use placement groups on Outposts in the same way that you create
and use placement groups in regular Availability Zones. When you create a placement
group with a spread strategy on an Outpost, you can choose to have the placement group
spread instances across hosts or racks. Spreading instances across hosts allows you to
use a spread strategy with a single rack Outpost.

**Considerations**

- A rack level spread placement group can hold as many instances as you have
  racks in your Outpost deployment.
- A host level spread placement group can hold as many instances as you have
  hosts in your Outpost deployment.

###### Prerequisite

You must have an Outpost installed at your site. For more information, see [Create an Outpost and order Outpost capacity](../../../outposts/latest/userguide/order-outpost-capacity.md "../../../outposts/latest/userguide/order-outpost-capacity.md") in the _AWS Outposts
User Guide_.

###### To use a placement group on an Outpost

1. Create a subnet on the Outpost. For more information, see [Create a
   subnet](../../../outposts/latest/userguide/launch-instance.md#create-subnet "../../../outposts/latest/userguide/launch-instance.md#create-subnet") in the _AWS Outposts User Guide_.
2. Create a placement group in the associated Region of the Outpost. If you
   create a placement group with a spread strategy, you can choose host or rack
   level spread to determine how the group will spread instances across the
   underlying hardware on your Outpost. For more information, see [Create a placement group for your EC2 instances](create-placement-group.md "create-placement-group.md").
3. Launch an instance into the placement group. For **Subnet**
   choose the subnet that you created in Step 1, and for **Placement group
   name**, select the placement group that you created in Step 2. For
   more information, see [Launch
   an instance on the Outpost](../../../outposts/latest/userguide/launch-instance.md#launch-instances "../../../outposts/latest/userguide/launch-instance.md#launch-instances") in the _AWS Outposts User
   Guide_.
