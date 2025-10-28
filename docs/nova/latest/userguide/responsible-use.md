# Responsible use

Building safety, security, and trust measures with AI models is a shared responsibility
between AWS and our customers. Our goal is to align our models to the [AWS Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") and mitigate
undesired outcomes while providing a delightful customer experience. Our approach to
Responsible AI (RAI) is structured around our [core dimensions of responsible
AI](https://aws.amazon.com/ai/responsible-ai/ "https://aws.amazon.com/ai/responsible-ai/"), which are covered in the following list. For each of these dimensions, we
developed guidelines that govern our decision-making throughout the entire model development
life cycle. This life cycle encompasses every stage, from initial data collection and
pre-training, to the implementation of post-deployment runtime mitigations.

- _Fairness_ - Considering impacts on different groups of
  stakeholders
- _Explainability_ - Understanding and evaluating system
  outputs
- _Privacy and Security_ - Appropriately obtaining, using, and
  protecting data and models
- _Safety_ - Preventing harmful output and misuse
- _Controllability_ - Having mechanisms to monitor and steer AI
  system behavior
- _Veracity and robustness_ - Achieving correct system outputs,
  even with unexpected or adversarial inputs
- _Governance_ - Incorporating best practices into the AI supply
  chain, including providers and deployers
- _Transparency_ - Enabling stakeholders to make informed choices
  about their engagement with an AI system

###### Topics

- [Guidelines](#responsible-guidelines "#responsible-guidelines")
- [Recommendations](#responsible-recommendations "#responsible-recommendations")
- [Amazon Nova Lite and Pro Customizable Content Moderation Settings](customizable-content-moderation.md "customizable-content-moderation.md")

## Guidelines

The guidelines we use to direct our model development includes but is not limited to
moderating content that glorifies, facilitates, or promotes the following:

- Participation in dangerous activities, self harm, or use of dangerous
  substances.
- Use, misuse, or trade of controlled substances, tobacco, or alcohol.
- Physical violence or gore.
- Child abuse or child sexual abuse material.
- Animal abuse or animal trafficking.
- Misinformation that positions individuals or groups as responsible for
  deliberate deception, undermining an institution with general public
  credibility, or endangering human health or livelihood.
- Malware, malicious content, or any content that facilitates
  cyber-crime.
- Disrespect, discrimination, or stereotype towards an individual or
  group.
- Insults, profanity, obscene gestures, sexually explicit language, pornography,
  hate symbols, or hate groups.
- Full nudity that is outside of a scientific, educational, or reference
  context.
- Bias against a group based on a demographic characteristic.

## Recommendations

**Appropriateness for Use:** Because AI model outputs are
probabilistic, Amazon Nova may produce inaccurate or inappropriate content. Customers
should evaluate outputs for accuracy and appropriateness for their use case, especially
if they will be directly surfaced to end users. Additionally, if Amazon Nova is used in
customer workflows that produce consequential decisions, customers must evaluate the
potential risks of their use case and implement appropriate human oversight, testing,
and other use-case specific safeguards to mitigate such risks.

**Prompt Optimizations:** In the event of encountering
moderation by Amazon Nova, consider examining the prompts used with respect to the
guidelines above. Optimizing the prompts to reduce the likelihood of generating
undesired outcomes is the recommended strategy to produce the expected outputs using
Amazon Nova models. Pay attention where the input is controlled by users, including pixel
content that could impact the performance of the model. Please see the
prompt guidelines section in this user guide for further
details.

**Privacy:** Amazon Nova is available in
Amazon Bedrock. Amazon Bedrock is a managed service and does not store
or review customer prompts or customer prompt completions, and prompts and completions
are never shared between customers, or with Amazon Bedrock partners. AWS does
not use inputs or outputs generated through the Amazon Bedrock service to train
Amazon Bedrock models, including Amazon Nova. See Section [50.3](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") of the AWS Service Terms
and the AWS [Data
Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/") for more information. For service-specific privacy information,
see the Privacy and Security section of the [Amazon Bedrock FAQs](https://aws.amazon.com/bedrock/faqs/ "https://aws.amazon.com/bedrock/faqs/")
documentation. Amazon Nova takes steps to avoid completing prompts that could be construed
as requesting private information. If a user is concerned that their private information
has been included in a Amazon Nova completion, the user should contact us [here](https://titan.aws.com/privacy "https://titan.aws.com/privacy").

**Security:** All Amazon Bedrock models,
including Amazon Nova, come with enterprise security that enables customers to build
generative AI applications that support common data security and compliance standards,
including GDPR and HIPAA. Customers can use AWS PrivateLink to establish private
connectivity between customized Amazon Nova and on-premise networks without exposing
customer traffic to the internet. Customer data is always encrypted in transit and at
rest, and customers can use their own keys to encrypt the data, e.g., using AWS Key Management Service.
Customers can use AWS Identity and Access Management to securely control access to Amazon Bedrock
resources, including customized Amazon Nova. Also, Amazon Bedrock offers
comprehensive monitoring and logging capabilities that can support customer governance
and audit requirements. For example, Amazon CloudWatch can help track usage metrics that are
required for audit purposes, and AWS CloudTrail can help monitor API activity and troubleshoot
issues as Amazon Nova is integrated with other AWS systems. Customers can also choose to
store the metadata, prompts, and completions in their own encrypted Amazon Simple Storage Service (Amazon S3)
bucket.

**Intellectual Property:** AWS offers uncapped
intellectual property (IP) indemnity coverage for outputs of generally available
Amazon Nova models (see Section 50.10 of the [Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/")). This means that
customers are protected from third-party claims alleging IP infringement or
misappropriation (including copyright claims) by the outputs generated by these
Amazon Nova models. In addition, our standard IP indemnity for use of the Services
protects customers from third-party claims alleging IP infringement (including copyright
claims) by the Services (including Amazon Nova models) and the data used to train
them.
