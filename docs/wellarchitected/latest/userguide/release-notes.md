

AWS Well-Architected Agent is in preview release and is subject to change.

# Release notes
<a name="release-notes"></a>

## AWS Well-Architected Agent preview released (October 1, 2026)
<a name="update-2026-10-01"></a>

AWS Well-Architected Agent is an AI-powered cloud optimization service that continuously analyzes your AWS environment and delivers personalized, prioritized recommendations across cost, security, performance, and resilience. The agent generates recommendations at three levels (resource, application, and architecture) with ready-to-deploy SSM runbooks so you can act immediately.

Key capabilities added with this release:
+ **Automated, ongoing analysis:** Unlike point-in-time architecture reviews, AWS WA Agent analyzes your environment on a weekly cadence and refreshes recommendations automatically.
+ **Ready-to-deploy remediation:** Recommendations include AI-generated SSM runbooks, not only findings.
+ **Goal-aligned prioritization:** Recommendations are ranked against the business goals you define in your agent profile.
+ **Cross-pillar impact and trade-off analysis:** Every recommendation shows positive impacts on other pillars, as well as trade-offs with risk level and mitigation strategies.
+ **IaC architecture reviews:** On-demand architecture reviews of CloudFormation and Terraform templates, returning findings aligned to AWS Well-Architected best practices.
+ **Multi-account scale:** A single agent profile can analyze multiple AWS accounts and scan resources across multiple AWS Regions.

AWS WA Agent is available to customers with a Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations support plan. Agent profiles are hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon), and scan resources across all commercial AWS Regions.

For more information, see [What is AWS Well-Architected Agent (preview)?](agent.md).