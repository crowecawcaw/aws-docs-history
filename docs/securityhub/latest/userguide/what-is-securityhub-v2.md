# Introduction to AWS Security Hub

###### Note

Security Hub is in preview release and is subject to change.

AWS Security Hub is a unified cloud security solution that prioritizes your critical security issues and helps you respond at scale.
Security Hub detects security issues by automatically correlating and enriching security signals from multiple sources, such as posture management, vulnerability management (Amazon Inspector), sensitive data (Amazon Macie), and threat detection (Amazon GuardDuty).
This enables security teams to prioritize active risks in their cloud environments through automated analyses and contextual insights.
Through intuitive visualizations, Security Hub transforms complex security signals into actionable insights, which enables you to make informed decisions about your security quickly.
Security Hub also includes automated response workflows to help you remediate risks, improve team productivity, and minimize operational disruptions.

## Features

###### Unified security solution

Gain broader visibility across your cloud environment through centralized management in a unified cloud security solution.

###### Actionable security insights

Gain actionable security insights through advanced analytics to learn about security risks associated with your environment.

###### Reduced response times

Streamline response times with automated workflows and an integrated ticketing system.

###### Exposure findings

Security Hub correlates findings from Security Hub CSPM control checks, Amazon Inspector, and other AWS services to detect exposures associated with AWS resources.

######

Findings are formatted in the Open Cybersecurity Schema Framework (OCSF)

Security Hub generates findings in OCSF and receives findings in OCSF from Security Hub CSPM and other AWS services:

- Amazon GuardDuty
- Amazon Macie
- Amazon Inspector

###### Dashboard

The Security Hub console provides a comprehensive view of your exposures, threats, security coverage, and resources, as well as an interactive visualization called the attack path graph, which shows how potential attackers can access and take control of resources associated with an exposure finding.

###### Integrations with third-party products

You can enhance your security posture with Security Hub integrations.
For example, if you use Jira Cloud or ServiceNow ITSM, you can use this feature to create tickets from findings.

## Integrations

Security Hub receives findings from the following AWS services.

- AWS Security Hub CSPM
- Amazon GuardDuty
- Amazon Inspector
- Amazon Macie

## AWS Regions supported for public preview

Security Hub supports the following AWS Regions for this public preview release.

- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Stockholm)
- Europe (Ireland)
- US West (N. California)
- US West (Oregon)
- Europe (London)
- Europe (Paris)
- South America (São Paulo)
- US East (N. Virginia)
- US East (Ohio)

The following are opt-in AWS Regions, which require that you enable them before you can access them.

- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Jakarta)
- Europe (Milan)
- Middle East (Bahrain)

For information about these AWS Regions, see [Opt-in status](../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status "../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status") in the _AWS Regions and Availability Zones User Guide_.

## Accessibility

Security Hub is available in the AWS Regions listed above.
You can enable Security Hub for individual accounts or accounts in your organization.
You can access Security Hub through the following:

**Security Hub console**

The Security Hub console is a browser-based interface you can use to create and manage AWS resources.
In this console, you can access your account, data, and resources.

**Security Hub API**

The Security Hub API gives you programmatic access to your account, data, and resources.
You can send HTTPS requests directly to Security Hub.

**AWS CLI**

With [the AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"), you can run commands in your system command line to perform tasks and build scripts that perform tasks.
In some cases, the AWS CLI can be more useful than the Security Hub console.

**AWS SDKs**

[AWS SDKs](https://aws.amazon.com/developertools/ "https://aws.amazon.com/developertools/") consist of libraries and sample code for various programming languages and platforms (C++, Go, Java, .NET, and Python).
They provide programmatic access to Security Hub and other AWS services in your preferred language and can help you manage tasks such as managing errors, signing requests, and retrying requests.

## Pricing

There is no cost to use Security Hub.
Security Hub is free during this public preview.
