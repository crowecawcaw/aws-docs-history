

# ADVCOST03-BP01 Consider private communication channels between SSP and DSP
<a name="advcost03-bp01"></a>

 Private communication channels can help keep traffic secure while also reducing internet egress charges. 

## Implementation guidance
<a name="implementation-guidance-63"></a>

 With [AWS PrivateLink](https://aws.amazon.com/privatelink/), you can establish secure, private communication channels between your SSPs, DSPs, and other AWS services or on-premises resources. This approach enhances security, reduces data exposure risks, and can improve performance for your programmatic advertising workloads, while simplifying your network architecture and reducing operational overhead. In cases where PrivateLink cannot be used, then Amazon VPC Peering, AWS Direct Connect, and AWS Global Accelerator can be considered. 

## Resources
<a name="resources-57"></a>
+  [AWS lowers data processing charges for AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2021/07/aws-lowers-data-processing-charges-aws-privatelink/) 
+  [Get started with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html) 