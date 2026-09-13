

# SMOPS01-BP01 Assess trade-offs between streaming architecture options and associated risks
<a name="smops01-bp01"></a>

When designing streaming video infrastructure, carefully evaluate the trade-offs between different architectural approaches and their associated risks. This includes considering factors such as performance, scalability, availability, security, and cost to determine the optimal solution for different streaming scenarios.

**Desired outcome:**
+ A well-informed decision-making process that results in streaming video architectures optimized for specific use cases (video on demand (VOD), live streaming, low-latency, interactive) with clear understanding of trade-offs and mitigated risks.

**Benefits of establishing this best practice:**
+ Improved alignment between business requirements and technical implementation
+ Reduced operational issues through proactive risk identification
+ Better resource utilization and cost management
+ Enhanced ability to meet quality and performance expectations

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Each streaming scenario presents distinct architectural trade-offs that affect performance, cost, reliability, and operational complexity. Understanding these trade-offs before committing to an architecture avoids costly rework and confirms the chosen approach matches business priorities.

For VOD workloads, the primary trade-off is between managed services and self-managed infrastructure for batch processing components that convert media into distribution formats. Managed services like AWS Elemental MediaConvert reduce operational overhead but may offer less customization than self-managed encoding fleets on Amazon EC2. For Live Streaming workloads, redundancy requirements, contribution feed quality, and encoding options must be weighed against cost to maintain reliability during high-value live events. Ad-supported content architectures require evaluating server-side compared to client-side ad insertion approaches, balancing viewer experience, ad blocker resistance, and personalization capabilities against implementation complexity. Low-latency streaming introduces trade-offs between specialized protocols and scalability, while interactive streaming requires balancing real-time communication technologies against audience size requirements.

### Implementation steps
<a name="implementation-steps"></a>

1. **Document streaming workload requirements:** Capture the following for each streaming scenario in your portfolio:
+ Audience size
+ Quality expectations
+ Latency requirements
+ Monetization approach

1. **Evaluate managed compared to self-managed options:** Compare managed service options against self-managed infrastructure for each component of your streaming workflow, considering:
+ Operational overhead
+ Cost
+ Customization needs

1. **Conduct proof-of-concept testing:** Perform proof-of-concept testing for critical components to validate feasibility and compatibility with your existing workflows and device environment.

1. **Document architectural decisions:** Record architectural decisions and their rationales, including identified risks and mitigation strategies, to maintain institutional knowledge.

1. **Define monitoring criteria:** Establish monitoring criteria to validate that architectural decisions meet performance and reliability targets over time.

## Resources
<a name="resources"></a>

**Related documents**
+ [Video on Demand on AWS Solution](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/)
+ [Live Streaming on AWS Solution](https://aws.amazon.com/solutions/implementations/live-streaming-on-aws/)
+ [AWS Media Services Overview](https://aws.amazon.com/media-services/)
+ [Amazon Interactive Video Service (IVS) Low-Latency Streaming](https://aws.amazon.com/ivs/)

**Related services**
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [Amazon Interactive Video Service](https://aws.amazon.com/ivs/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)