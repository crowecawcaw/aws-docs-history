# Supported Regions

This topic describes the AWS Regions where you can use AWS DevOps Agent. For more information about AWS Regions, see [Specify which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management Reference Guide_.

## Cross-Region resource monitoring

AWS DevOps Agent can monitor and investigate resources in AWS accounts located in any AWS Region, regardless of which supported Region you create your Agent Space in. When you associate an AWS account with an Agent Space, the agent discovers and maps resources across all Regions within that account. This means you do not need an Agent Space in every Region where your workloads run.

Choose a supported Region based on your preferred data residency, proximity to your operations team, or organizational requirements.

## Supported Regions

AWS DevOps Agent is available in the following AWS Regions.

| Region Name               | Region Code    | Console Link                                                                                                                                                                          |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | us-east-1      | [Open console](https://us-east-1.console.aws.amazon.com/aidevops/home?region=us-east-1 "https://us-east-1.console.aws.amazon.com/aidevops/home?region=us-east-1")                     |
| US West (Oregon)          | us-west-2      | [Open console](https://us-west-2.console.aws.amazon.com/aidevops/home?region=us-west-2 "https://us-west-2.console.aws.amazon.com/aidevops/home?region=us-west-2")                     |
| Canada (Central)          | ca-central-1   | [Open console](https://ca-central-1.console.aws.amazon.com/aidevops/home?region=ca-central-1 "https://ca-central-1.console.aws.amazon.com/aidevops/home?region=ca-central-1")         |
| South America (São Paulo) | sa-east-1      | [Open console](https://sa-east-1.console.aws.amazon.com/aidevops/home?region=sa-east-1 "https://sa-east-1.console.aws.amazon.com/aidevops/home?region=sa-east-1")                     |
| Asia Pacific (Mumbai)     | ap-south-1     | [Open console](https://ap-south-1.console.aws.amazon.com/aidevops/home?region=ap-south-1 "https://ap-south-1.console.aws.amazon.com/aidevops/home?region=ap-south-1")                 |
| Asia Pacific (Singapore)  | ap-southeast-1 | [Open console](https://ap-southeast-1.console.aws.amazon.com/aidevops/home?region=ap-southeast-1 "https://ap-southeast-1.console.aws.amazon.com/aidevops/home?region=ap-southeast-1") |
| Asia Pacific (Sydney)     | ap-southeast-2 | [Open console](https://ap-southeast-2.console.aws.amazon.com/aidevops/home?region=ap-southeast-2 "https://ap-southeast-2.console.aws.amazon.com/aidevops/home?region=ap-southeast-2") |
| Asia Pacific (Tokyo)      | ap-northeast-1 | [Open console](https://ap-northeast-1.console.aws.amazon.com/aidevops/home?region=ap-northeast-1 "https://ap-northeast-1.console.aws.amazon.com/aidevops/home?region=ap-northeast-1") |
| Europe (Frankfurt)        | eu-central-1   | [Open console](https://eu-central-1.console.aws.amazon.com/aidevops/home?region=eu-central-1 "https://eu-central-1.console.aws.amazon.com/aidevops/home?region=eu-central-1")         |
| Europe (Ireland)          | eu-west-1      | [Open console](https://eu-west-1.console.aws.amazon.com/aidevops/home?region=eu-west-1 "https://eu-west-1.console.aws.amazon.com/aidevops/home?region=eu-west-1")                     |
| Europe (London)           | eu-west-2      | [Open console](https://eu-west-2.console.aws.amazon.com/aidevops/home?region=eu-west-2 "https://eu-west-2.console.aws.amazon.com/aidevops/home?region=eu-west-2")                     |

## Service endpoints

| Region Name               | Region Code    | Endpoint                              | Protocol |
| ------------------------- | -------------- | ------------------------------------- | -------- |
| US East (N. Virginia)     | us-east-1      | aidevops.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | aidevops.us-west-2.amazonaws.com      | HTTPS    |
| Canada (Central)          | ca-central-1   | aidevops.ca-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | aidevops.sa-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | aidevops.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | aidevops.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | aidevops.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | aidevops.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | aidevops.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | aidevops.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | aidevops.eu-west-2.amazonaws.com      | HTTPS    |

## Feature availability by Region

Not all AWS DevOps Agent features are available in every Region. The following table shows which features are available in each supported Region.

| Feature                                                                     | Available Regions                      |
| --------------------------------------------------------------------------- | -------------------------------------- |
| Production operations (investigations, recommendations, prevention)         | All supported Regions                  |
| On-demand DevOps tasks                                                      | All supported Regions                  |
| Custom agents                                                               | All supported Regions                  |
| Release management (release readiness review and release testing) — preview | US East (N. Virginia) `us-east-1` only |

## Considerations

- **Release management preview availability** — Release management capabilities

(release readiness review and autonomous release testing) are available only in US East (N. Virginia) `us-east-1` during preview. Support for all Regions listed above will be added at general availability.

- **Agent Space Region selection** — An Agent Space and its data (investigations,

topology, recommendations) are stored in the Region where you create it. Choose a Region that meets your data residency requirements.

- **Cross-Region monitoring** — Resources in AWS accounts associated with an Agent

Space are monitored regardless of which Region those resources are deployed in. You do not need to create separate Agent Spaces in each Region where your workloads run.

- **Third-party integrations** — Connections to CI/CD providers (GitHub, GitLab),

observability tools (Dynatrace, Datadog, New Relic, Splunk), and MCP servers are configured per Agent Space and are not Region-dependent.
