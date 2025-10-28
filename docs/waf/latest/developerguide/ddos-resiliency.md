**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Building basic DDoS resilient architectures with Shield Advanced

This page explains Distributed Denial of Service (DDoS) resiliency and introduces two example architectures.

DDoS resiliency is the ability of your application architecture to withstand DDoS
attacks while continuing to serve legitimate end users. An application that is highly
resilient can remain available during an attack with minimal impact on performance metrics
such as errors or latency. This section shows some common example architectures and
describes how to use the DDoS detection and mitigation capabilities that are provided by
AWS and Shield Advanced to increase their DDoS resiliency.

The example architectures in this section highlight the
AWS services that provide the greatest DDoS resiliency benefits for your deployed applications.
The benefits of the highlighted services include the following:

- **Access to globally distributed network capacity** –
  The services Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 provide you with access to internet
  and DDoS mitigation capacity across the AWS global edge network. This is useful in
  mitigating larger volumetric attacks, which can reach terabits in scale. You can run
  your application in any AWS Region and use these services to protect availability
  and optimize performance for your legitimate users.
- **Protection against web application layer DDoS attack
  vectors** – Web application layer DDoS attacks are best
  mitigated using a combination of application scale and a web application firewall
  (WAF). Shield Advanced uses web request inspection logs from AWS WAF to detect anomalies
  that can be mitigated either automatically or via engagement with the AWS
  Shield Response Team (SRT). Automatic mitigation is available through deployed AWS WAF
  rate-based rules and also through the Shield Advanced automatic application layer DDoS mitigation.
  In addition to reviewing these examples, review and follow the applicable best practices at [AWS
  Best Practices for DDoS Resiliency](../../../whitepapers/latest/aws-best-practices-ddos-resiliency.md "../../../whitepapers/latest/aws-best-practices-ddos-resiliency.md").

###### Topics

- [Example Shield Advanced DDoS resiliency architecture for common web
  applications](ddos-resiliency-example-web.md "ddos-resiliency-example-web.md")
- [Example Shield Advanced DDoS resiliency architecture for TCP and UDP
  applications](ddos-resiliency-example-tcp-udp.md "ddos-resiliency-example-tcp-udp.md")
