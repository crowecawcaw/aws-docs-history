

# Enterprise Frontier Safeguards (EFS) for Anthropic models
<a name="efs-anthropic"></a>

The [Enterprise Frontier Safeguards on the Anthropic website](https://www.anthropic.com/news/enterprise-frontier-safeguards) (EFS) program was built in collaboration between AWS and Anthropic to ensure that customers can access Anthropic's most intelligent models safely, from both a model use and a customer data perspective. EFS applies to Anthropic Claude models on Amazon Bedrock that Anthropic requires data retention for safety review, called "Covered Models". Covered Models are a category of Claude models that carry additional data retention, safety review, and access policies wherever they're offered.

For the current list of covered models and their requirements, see [Amazon Bedrock abuse detection](abuse-detection.html) and [Covered Models on the Anthropic website](https://support.claude.com/en/articles/15425695-covered-models).

If you are eligible, EFS provides the following:
+ You receive zero data retention (ZDR) for internal use through at least June 30, 2027 on Amazon Bedrock and Claude Platform on AWS. Your prompts and outputs are not retained during this period.
+ After the ZDR period, your traffic will be subject to retention with automated safety monitoring. Automated safety monitoring is a process of pattern detection that will look for signals of serious misuse across many requests, rather than reacting to any single prompt.
+ One approval covers all Claude Fable models. You don't need to reapply for each model, and ZDR applies to all of them.

Later this year, you will be able to store your data within your own AWS infrastructure, where you can manage your encryption keys, access policies, networking, and audit logging. Once launched, you can set up your storage and encryption during the ZDR period, so your storage is ready when retention begins.

ZDR runs alongside any existing data retention commitments in your agreements with Anthropic. To understand how to control your data, see [Amazon Bedrock data retention](data-retention.html).

Eligibility is determined under the EFS program. To find out whether your organization is eligible, contact your AWS account team or [AWS Support](https://aws.amazon.com/support).

Claude Mythos models are not covered by EFS. Access to Mythos models is handled separately. For details, contact your AWS account team.