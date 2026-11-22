

# Incident response in Amazon OpenSearch Memory

Security is the highest priority at AWS. As part of the AWS Cloud shared responsibility model, AWS manages a data center, network, and software architecture that meets the requirements of the most security-sensitive organizations. AWS is responsible for any incident response with respect to the Amazon OpenSearch Memory service itself. As an AWS customer, you are responsible for incident response on your side of the shared responsibility model: the access you grant, the data you store, and the agents that use it.

If you suspect that a principal has accessed a space without authorization, you can take the following actions:

1. **Find out what happened.** Review the space's CloudTrail events to see which operations the principal called, on which space, and when. Data events for the event and memory operations must be enabled on your trail to be recorded. For more information, see [Monitoring Amazon OpenSearch Memory with AWS CloudTrail](memory-cloudtrail.md).

1. **Stop the access.** Remove or restrict the principal's IAM permissions. For a space that uses a customer managed key, you can also remove the principal's access to the key, which makes every request from that principal fail immediately.

1. **Clean up.** Delete events or memories that shouldn't have been written, with [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html) and [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html), or delete the space. Deleting a space doesn't delete its events right away; they are removed when they reach their expiry. To remove events sooner, delete them before you delete the space.

To help you understand the impact that incident response and your choices have on your corporate goals, we encourage you to review the following resources:
+ [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html)
+ [AWS Best Practices for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)
+ [Security Perspective of the AWS Cloud Adoption Framework (CAF) whitepaper](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html)