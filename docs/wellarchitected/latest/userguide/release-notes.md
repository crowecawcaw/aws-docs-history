

AWS Well-Architected Agent is in preview release and is subject to change.

# Release notes
<a name="release-notes"></a>

This page describes changes to the AWS Well-Architected user guide. For notification about updates to this documentation, you can subscribe to the RSS feed.

## AWS Well-Architected Agent released (10-1-2026)
<a name="update-2026-10-01"></a>

### AWS Well-Architected Agent (preview)
<a name="release-notes-waa-preview"></a>

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

## Historic AWS Well-Architected releases
<a name="release-notes-historic"></a>

The following table describes earlier updates to this guide.


| Change | Description | Date | 
| --- | --- | --- | 
| Added Well-Architected Framework Review (WAFR) section | Added a new section with guidance on performing a WAFR using the AWS Well-Architected Tool. | October 13, 2025 | 
| New lens | This release added one new lens to the Lens Catalog. | April 17, 2025 | 
| New and updated lenses | This release added one new lens to the Lens Catalog and updated one other lens. | June 27, 2024 | 
| Jira | This release added the AWS Well-Architected Tool Connector for Jira. | April 16, 2024 | 
| New lenses | This release added new lenses to the Lens Catalog. | March 26, 2024 | 
| Updated functionality | This release adds the Lens Catalog feature to AWS WA Tool. | November 26, 2023 | 
| Updated functionality | This release adds the Review Templates feature to AWS WA Tool. | October 3, 2023 | 
| Updated functionality | This release adds the Profiles feature to AWS WA Tool. | June 13, 2023 | 
| Updated functionality | This release enhances the AWS Trusted Advisor and AWS Service Catalog AppRegistry integration, and adds the `AWSWellArchitectedDiscoveryServiceRolePolicy` to AWS managed policies. | May 3, 2023 | 
| Content update | Corrected name of WellArchitectedConsoleReadOnlyAccess policy. | January 19, 2023 | 
| Updated functionality | This release removes the FTR lens from the tool. | December 14, 2022 | 
| Updated functionality | This release adds the AWS Trusted Advisor and AWS Service Catalog AppRegistry integration. | November 7, 2022 | 
| Content update | Corrected a problem in the custom lens JSON example for `choices`. | September 29, 2022 | 
| Content update | The `choices` section of the custom lens JSON specification was updated. | August 2, 2022 | 
| Updated functionality | This release adds the ability to specify additional resources for choices in a custom lens, to preview a custom lens before publishing it, and add tags to custom lenses. | June 21, 2022 | 
| Updated functionality | This release adds the ability to access the AWS Well-Architected community on AWS re:Post. | May 31, 2022 | 
| Updated functionality | This release adds the sustainability pillar and minor updates to Tutorial. | March 31, 2022 | 
| Updated functionality | Individual best practices can now be marked as not applicable. | July 14, 2021 | 
| Updated functionality | This release adds the FTR and SaaS lenses to the tool. | December 3, 2020 | 
| Content update | Clarified that after you upgrade a workload to use a new lens that you cannot go back to the previous version. | July 8, 2020 | 
| Content update | Clarified sharing in AWS Regions introduced after March 20, 2019. | June 24, 2020 | 
| Updated functionality | Access to a workload share is removed immediately when a workload share invitation is rejected. Shared access is granted when the share is accepted. | June 17, 2020 | 
| Updated functionality | This release adds a review owner to the workload. | April 1, 2020 | 
| Updated functionality | This release adds an architectural diagram link to the workload. | March 10, 2020 | 
| Content update | Clarified that workload shares are AWS Region-specific. | January 10, 2020 | 
| Updated functionality | This release adds workload sharing. | January 9, 2020 | 
| Content update | Security section updated with latest guidance. | December 6, 2019 | 
| Updated functionality | This release makes the industry fields optional when defining a workload. | August 19, 2019 | 
| Updated functionality | This release adds improvement plan items to the workload report. | July 29, 2019 | 
| Updated functionality | The release adds the DeleteWorkload action to the policy. | July 18, 2019 | 
| Content update | The content in this guide has been updated with minor fixes. | June 19, 2019 | 
| Content update | The content in this guide has been updated with minor fixes. | May 30, 2019 | 
| Updated functionality | This release supports upgrading the version of the framework used for a workload review. | May 1, 2019 | 
| Updated functionality | This release adds the ability to specify non-AWS Regions when defining a workload. | February 14, 2019 | 
| AWS Well-Architected Tool general availability | This release introduces the AWS Well-Architected Tool. | November 29, 2018 | 