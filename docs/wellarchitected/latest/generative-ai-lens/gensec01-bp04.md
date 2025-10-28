# GENSEC01-BP04 Implement access monitoring to generative AI

services and foundation models

Generative AI services and foundation models can be resource
intensive to use and can be misused. Implementing access monitoring
on these services and models helps to identify, triage and resolve
unintended access quickly.

**Desired outcome:** When
implemented, this current guidance monitors access to sensitive
generative AI systems and foundation models. Unintended and
unauthorized use of generative AI services and foundation models can
be identified quickly and further action can be taken if
appropriate.

**Benefits of establishing this current
guidance:** [Maintain
traceability](../framework/sec-design.md "../framework/sec-design.md") - Access monitoring traces access to generative
AI services and foundation models.

**Level of risk exposed if this current
guidance is not established:** High

## Implementation guidance

AWS CloudTrail can be used to monitor access to AWS services.
To track service-level access to generative AI services such as
Amazon Bedrock, customers can utilize AWS CloudTrail. In Amazon Bedrock, customers can additionally turn on model invocation
logging to collect metadata, requests and responses for model
invocations in an AWS account. Similar capabilities exist for the
Amazon Q family of services.

For additional controls, consider implementing guardrails to mask
or remove sensitive data elements (like personal data) in the prompts
before foundation model invocations are made. This additional step
helps to mitigate the unintended or unauthorized access to private
or restricted data and makes sure your organization policies and
responsible AI governance are followed.

### Implementation steps

1. In Amazon Bedrock, configure model invocation logging to track
   model invocations and store the logs in Amazon S3, Amazon CloudWatch Logs, or both.
2. In Amazon Q Developer, capture user activity by enabling
   user activity capture in the settings.
3. In Amazon Q Business, configure log delivery for analysis
   and review into Amazon S3, Amazon CloudWatch Logs, or Amazon Data Firehose.
4. For self-hosted models on Amazon SageMaker AI Inference
   Endpoints, configure logging using your preferred logging
   solution.
5. Introduce logging, monitoring and telemetry capture in
   additional application layers, depending on your specific
   workload.

## Resources

**Related practices:**

- [SEC03-BP08](../security-pillar/sec_permissions_share_securely.md "../security-pillar/sec_permissions_share_securely.md")

**Related guides, videos, and documentation:**

- [Monitoring
  Amazon Q Business and Q Apps](../../../amazonq/latest/qbusiness-ug/monitoring-overview.md "../../../amazonq/latest/qbusiness-ug/monitoring-overview.md")
- [Monitoring
  Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/monitoring-overview.md "../../../amazonq/latest/qdeveloper-ug/monitoring-overview.md")

**Related examples:**

- [Monitoring
  Generative AI Applications using Amazon Bedrock and Amazon CloudWatch Integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/ "https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/")
- [Overseeing
  AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/ "https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/")
