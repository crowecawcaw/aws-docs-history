

# Pricing for MediaConnect
<a name="what-is-pricing"></a>

As with other AWS products, there are no contracts or minimum commitments for using MediaConnect. Pricing varies by resource type.

MediaConnect router  
You are charged an hourly rate for each active input and output, based on maximum bitrate capacity. Base rates include uptime and same-Region transfers. Outputs that receive content from a different Region or that egress to the internet incur additional hourly charges. You are not charged for inputs and outputs that are stopped or idle.

Transport stream flows  
You are charged an hourly rate for each running flow, plus per-GB data transfer charges or reserved outbound bandwidth pricing for internet delivery. Standby flows don't incur active resource costs. Reserved outbound bandwidth requires a 12-month commitment.

NDI® flows  
You are charged an hourly rate for each running flow. NDI outputs are included with no data transfer charges within a VPC. If you add transport stream outputs, transport stream output data transfer charges apply.

AWS CDI and JPEG XS flows  
You are charged an hourly rate for each running flow, plus an hourly rate per output. Rates depend on the maximum video size that you define when you create the flow. Reserved outbound bandwidth is not available for these flow types.

AWS Elemental MediaConnect Gateway  
The gateway software is available at no cost. You supply your own hardware and use Amazon Elastic Container Service Anywhere to run a container in on-premises infrastructure. Amazon ECS Anywhere pricing and MediaConnect transport stream flow and data transfer charges apply.

For more information, see [AWS Elemental MediaConnect Pricing](https://aws.amazon.com/mediaconnect/pricing/).