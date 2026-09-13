

# SMSEC05-BP01 Use distributed denial of service (DDoS) protection service to maintain content availability
<a name="smsec05-bp01"></a>

It is important to respond to threats and other attacks by protecting your origin and using tools to block or mitigate malicious requests.

**Desired outcome:**
+ Amazon CloudFront helps protect against network-level and application level DDoS attacks and maintains content availability
+ You have observability into traffic patterns to protect and mitigate

**Common anti-patterns:**
+ Organizations expose media origin servers directly to the internet without DDoS protection, leaving live streaming events vulnerable to volumetric attacks that disrupt service during peak viewership.
+ Teams deploy streaming infrastructure without AWS Shield Advanced, relying only on basic network-level protections that can't mitigate sophisticated application-layer attacks targeting video APIs and manifest endpoints.
+ Organizations fail to place content delivery network (CDN) distributions in front of origin infrastructure, allowing attackers to target origin servers directly with traffic volumes that overwhelm available capacity.
+ Teams don't configure DDoS alerting or monitoring, discovering attacks only after viewers report service degradation or complete outages during live events.
+ Organizations lack a DDoS response plan specific to streaming workloads, resulting in ad-hoc mitigation attempts that extend the duration and impact of attacks on content availability.

**Benefits of establishing this best practice:**
+ DDoS protection keeps live streaming events and video on demand (VOD) services available during volumetric or application-layer attacks, protecting viewer experience and advertising revenue.
+ CloudFront absorbs attack traffic at edge locations globally, stopping malicious requests from reaching origin infrastructure and consuming processing capacity.
+ AWS Shield Advanced provides automatic detection and mitigation of DDoS attacks without manual intervention, reducing response time from minutes to seconds during live events.
+ Shield Advanced cost protection stops unexpected scaling charges from DDoS-driven traffic spikes that would otherwise inflate CDN and origin compute costs.
+ Shield Response Team engagement provides specialized support during active attacks on high-value live streaming events.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

A DDoS attack is when multiple systems intentionally flood your resources, which can render your content origin unavailable or hidden to your viewers. It is important to use a DDoS protection tool, such as AWS Shield, to protect your resources. AWS Shield helps protect AWS resources such as Amazon CloudFront distributions and Amazon Route 53 so that your content can be located and reached globally. AWS Shield Advanced helps protect resources built upon services such as Elastic Load Balancing, Amazon EC2, and AWS Global Accelerator against common and most frequently occurring infrastructure (layer 3 and 4) attacks like SYN floods, UDP floods, reflection attacks, and others to support high availability of your applications on AWS. If you need to protect resources that you are hosting privately, put a CDN, such as a CloudFront distribution, in front of it.

### Implementation steps
<a name="implementation-steps"></a>

1. **Activate AWS Shield:** Activate AWS Shield and optionally AWS Shield Advanced for DDoS protection and mitigation.

1. **Implement monitoring and alerting:** Implement monitoring and alerting for DDoS attack detection and mitigation status.

1. **Perform a security analysis:** [Perform a security analysis with AWS Shield](https://aws.amazon.com/shield/getting-started/) to begin strengthening your security posture.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC05-BP02 Restrict content origin access to only allow known entities](smsec05-bp02.html)
+ [SMSEC05-BP03 Use a web application firewall to monitor and control content access](smsec05-bp03.html)

**Related documents**
+ [AWS Shield Getting Started](https://aws.amazon.com/shield/getting-started/)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Shield](https://aws.amazon.com/shield/)