# Kiro in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) and AWS GovCloud (US-East).

Kiro is an AI-powered development platform that accelerates software development from prototype to production through spec-driven development. The platform transforms natural language prompts into structured requirements, architectural designs, and discrete implementation tasks, enabling developers to build complex features with precision and speed.

Kiro provides both an integrated development environment (IDE) and command-line interface (CLI) that help developers maintain control throughout the development process. The platform converts requirements into clear specifications, analyzes codebases to recommend optimal architectures, and creates sequenced implementation plans with comprehensive tests. Developers can automate repetitive workflows through hooks that trigger on events, generating documentation and unit tests in the background.

## How Kiro differs for AWS GovCloud (US)

The following differences apply to Kiro in AWS GovCloud (US) Region:

- Kiro Plugins: IDE integrations, including the Visual Studio Code plugin, are not available. Users must access Kiro through the standalone IDE or CLI.
- Inline Suggestions: Real-time code suggestions and inline completions are not available.
- Autonomous Agent is not available.
- Social or BuilderID Login: Authentication through social providers and AWS Builder ID is not supported.
- Data Storage for Service Improvement: Content collection for service improvement (prompts, responses, generated code) is disabled.
- User Activity Metrics and S3 Reporting: Collection of user activity metrics and generation of daily reports in Amazon S3 is not available. Enterprise administrators cannot enable telemetry or activity reporting.
- Cross-Region Inference (CRIS): For customers in AWS GovCloud (US-East) (us-gov-east-1), inference requests are processed using Amazon Bedrock in AWS GovCloud (US-West) (us-gov-west-1). Your content remains stored in the region where your Kiro profile was created. All cross-region communication is encrypted in transit using TLS 1.2 or higher.
- Auto: Automated model selection is disabled at launch. Claude Sonnet 4.5 is the default foundation model in AWS GovCloud (US).

## Documentation for Kiro

- [Kiro Documentation](https://kiro.dev/docs/ "https://kiro.dev/docs/")
- [Kiro VPC Endpoint Documentation](https://kiro.dev/docs/privacy-and-security/vpc-endpoints/ "https://kiro.dev/docs/privacy-and-security/vpc-endpoints/")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

Kiro metadata is not permitted to contain export-controlled data. This metadata includes:

- Authentication and authorization tokens (IAM Identity Center integration).
