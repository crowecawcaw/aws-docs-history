

# SMSEC07-BP01 Establish your plan for incident response
<a name="smsec07-bp01"></a>

To prepare for incidents, have a plan in place to educate and use your team so that incidents are quickly dealt with and don't cause undue degradation.

**Desired outcome:**
+ Establishing a plan for Incident Response will allow your team to react quickly, take effective action, and restore services in a timely manner

**Common anti-patterns:**
+ Organizations operate streaming infrastructure without documented incident response procedures, leading to ad-hoc responses during content leaks or service disruptions that extend downtime and increase impact.
+ Teams lack defined escalation paths for streaming-specific incidents such as digital rights management (DRM) key compromise, unauthorized stream redistribution, or live event disruption, resulting in delayed response while ownership is determined.
+ Organizations don't conduct incident response drills or tabletop exercises for streaming scenarios, leaving teams unprepared when real incidents occur during high-viewership live events.
+ Teams fail to maintain up-to-date infrastructure documentation and service dependency maps, making it difficult to isolate affected components and restore service during incidents.
+ Organizations don't establish communication protocols with content licensors for security incidents, missing contractual notification deadlines when content breaches occur.

**Benefits of establishing this best practice:**
+ Documented procedures and trained teams reduce mean time to recovery during streaming service incidents, minimizing viewer impact and revenue loss from service disruptions.
+ Predefined response playbooks for content security incidents—such as DRM key compromise or unauthorized redistribution—enable immediate containment actions that limit the spread of leaked content.
+ Demonstrated incident response capability satisfies content licensor security requirements and provides assurance that breaches will be handled within contractual notification timelines.
+ Post-incident reviews identify gaps in security controls and response procedures, driving iterative improvements to content protection and infrastructure resilience.
+ Regular drills and tabletop exercises prepare response teams to execute effectively under pressure during high-stakes live events where downtime has immediate financial impact.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Your organization should take care to create a plan around incident response. Know how to identify issues at different stages of your workflow, who will be in charge of clearing specific issues, which teams will handle communications that come up, and so on. The [AWS Security whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html) outlines the steps to take to plan your incident response strategy.

### Implementation steps
<a name="implementation-steps"></a>

1. **Document your infrastructure:** Outline and record your infrastructure and make notes on critical services.

1. **Create restoration documentation:** Set up documentation on how to restore services during known issues.

1. **Establish response teams:** Set up teams and responsibilities so that someone can respond around the clock.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC02-BP01 Monitor for fraudulent access attempts](smsec02-bp01.html)

**Related documents**
+ [Aspects of AWS Incident Response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aspects-of-aws-incident-response.html)
+ [AWS Well-Architected Framework Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
+ [Secure Content Delivery with Amazon CloudFront](https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/secure-content-delivery-with-amazon-cloudfront.html)
+ [AWS Motion Picture Association of America (MPAA) and Studio Compliance](https://aws.amazon.com/compliance/mpaa/)
+ [Serving Private Content Using Amazon CloudFront and AWS Lambda@Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/serving-private-content-using-amazon-cloudfront-aws-lambdaedge/)

**Related videos**
+ [Secure Media Streaming and Delivery](https://www.youtube.com/watch?v=zzeho2uLpHM)