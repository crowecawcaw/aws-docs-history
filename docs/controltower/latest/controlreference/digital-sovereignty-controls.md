# Digital sovereignty

controls

_Digital sovereignty_ means control over digital assets. AWS Control Tower
offers a group of controls that are designed to enhance your digital sovereignty governance
posture. The pillars of this posture are as follows:

- _Data residency:_ Control over the location of your
  data.

For more information, see [Controls that enhance data residency
protection](data-residency-controls.md "data-residency-controls.md").

- _Granular access:_ Access restrictions that limit all access to
  your data, unless the access is requested by you, or by a partner whom you
  trust.

For more information, see [Region deny control applied to the OU](ou-region-deny.md "ou-region-deny.md").

- _Encryption:_ Features and controls that help you encrypt data,
  whether in transit, at rest, or in memory.

For example, see the control [CT.APPSYNC.PR.5: Require an AWS AppSync GraphQL API cache to have encryption at rest enabled](appsync-rules.md#ct-appsync-pr-5-description "appsync-rules.md#ct-appsync-pr-5-description").

- _Resiliency:_ Ability to sustain operations through disruption
  or disconnection, which is essential in the case of events such as supply chain
  disruption, network interruption, and natural disaster.

For example see the control [CT.NETWORK-FIREWALL.PR.5: Require an AWS Network Firewall firewall to be deployed across multiple Availability Zones](network-firewall-rules.md#network-firewall-pr-5-description "network-firewall-rules.md#network-firewall-pr-5-description").
You can read more about digital sovereignty and AWS in the blog: [AWS
Digital Sovereignty Pledge: Control without compromise.](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/ "https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/")

###### The Data residency subgroup

Although the digital sovereignty group is primarily a group of preventive controls, it includes _preventive_ and _detective_ controls in the **Data residency** subgroup.
