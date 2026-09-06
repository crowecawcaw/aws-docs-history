

# Digital sovereignty controls
<a name="digital-sovereignty-controls"></a>

*Digital sovereignty* means control over digital assets. AWS Control Tower offers a group of controls that are designed to enhance your digital sovereignty governance posture. The pillars of this posture are as follows:
+ *Data residency:* Control over the location of your data.

  For more information, see [Controls that enhance data residency protection](data-residency-controls.md).
+ *Granular access:* Access restrictions that limit all access to your data, unless the access is requested by you, or by a partner whom you trust.

  For more information, see [Region deny control applied to the OU](ou-region-deny.md).
+ *Encryption:* Features and controls that help you encrypt data, whether in transit, at rest, or in memory.

  For example, see the control [CT.APPSYNC.PR.5: Require an AWS AppSync GraphQL API cache to have encryption at rest enabled](https://docs.aws.amazon.com/controltower/latest/controlreference/appsync-rules.html#ct-appsync-pr-5-description).
+ *Resiliency:* Ability to sustain operations through disruption or disconnection, which is essential in the case of events such as supply chain disruption, network interruption, and natural disaster.

  For example see the control [CT.NETWORK-FIREWALL.PR.5: Require an AWS Network Firewall firewall to be deployed across multiple Availability Zones](https://docs.aws.amazon.com/controltower/latest/controlreference/network-firewall-rules.html#network-firewall-pr-5-description).

You can read more about digital sovereignty and AWS in the blog: [AWS Digital Sovereignty Pledge: Control without compromise.](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/)

**The Data residency subgroup**  
Although the digital sovereignty group is primarily a group of preventive controls, it includes *preventive* and *detective* controls in the **Data residency** subgroup.