

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Document history
<a name="doc-history"></a>

The following table describes the important changes to the documentation since the last release of AMS.
+ **API version: 2019-05-21**
+ **Latest documentation update: **September 23, 2025



| Change | Description | Date | 
| --- | --- | --- | 
| Removed deprecated drift remediation change type references | [RFC updates and drift detection](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-updates-and-dd.html).<br />Removed references to the deprecated managed automation drift remediation change type (ct-34sxfo53yuzah) from the drift remediation FAQs. | August 18, 2026 | 
| Updated drift remediation FAQs for CloudFormation-ingested stacks | [RFC updates and drift detection](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ex-rfc-updates-and-dd.html).<br />Clarified that drift remediation is supported for standard AMS change types (ct-3kinq0u4l33zf) but is not supported for stacks provisioned through the CloudFormation ingest change type (ct-36cn2avfrrj9v). | August 18, 2026 | 
| Updated Log retention and rotation defaults in SALZ: Default settings section |  [ Log retention and rotation defaults ](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/log-defaults.html).<br />Updated information about AWS CloudTrail logs. | February 11, 2026 | 
| Updated change type for endpoint autoscaling in SageMaker AI in AWS Managed Services FAQ section |  [ Use AMS SSP to provision Amazon SageMaker AI in your AMS account](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/sagemaker.html#set-sagemaker-faqs).<br />Submit a RFC with Management \| Advanced stack components \| Identity and Access Management (IAM) \| Update entity or policy (managed automation) change type (ct-27tuth19k52b4) to elevate autoscaling permissions temporarily, or permanently, as autoscaling requires permissive access on CloudWatch service. | September 25, 2025 | 
| Precise change type references |  [ Create, Change, or Delete Security Groups](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/about-security-groups.html#create-security-group).<br />To add a user: Submit an RFC using Management \| Directory Service \| Users and groups \| Add user to group [ct-24pi85mjtza8k] and To remove a user: Submit an RFC using Management \| Directory Service \| Users and groups \| Remove user from group [ct-2019s9y3nfml4] | August 08, 2025 | 
| TOC link removed | TOC [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) link removed. | August 08, 2025 | 
| Added link for prescription guidance | [Set up consolidated billing–link new account to Payer account](set-up-consolidated-billing.md). | May 08, 2025 | 
| Updated instructions to activate IAM access to the AWS Management Console | Clarified the instructions for activating IAM access to the AWS Management Console. | [Activate IAM access to the AWS console](activate-iam-access-to-console.md) | 
| Updated number of allowed transit virtual interfaces on Direct Connect dedicated connections | Direct Connect dedicated connections now have a limit of 4 transit virtual interfaces per connection  | [Connecting Direct Connect to Transit Gateway](setup-net-connect-to-tg.md) | 
| Improve wording. | Specified that "only used as a "Deny" list " must include "Allow All" to ensure AMS monitoring and management operations. | [Network configuration](core-questions-network.md) | 
| Additional information on using the AMS CLI. | "Added note that the `--region` option may be needed for some CLI commands" | [Install the AMS CLIs](install-cli.md) | 
| Updated: Chapter headings for consistency and readabiliy, moved some topic sub-sections into more appropriate sections | "Modes for change management" is the new heading for "Change management" | [Change management modes](using-change-management.md) | 
| Updated content | The AMS mode previously known as "Change Management mode" or "Standard CM mode" is now known as "RFC mode." The modes section has been expanded. | [RFC mode](rfc-mode.md). | 
| Updated content | The AMS mode previously known as "Change Management mode" or "Standard CM mode" is now known as "RFC mode." The modes section has been shortened and links to the *AMS Advanced User Guide* sections on modes added. | [AMS modes](ams-modes-og.md). | 
| MALZ: Updated network architecture diagram | [Networking account architecture](malz-network-arch.md)m | June 16, 2022 | 
| Moved topic list to below opening paragraphs | [AWS Managed Services Onboarding Introduction](og-intro.md) | June 16, 2022 | 
| Updated content, inclusive language initiative | "Management account" not "Master account. | [IAM user role in AMS](defaults-user-role.md), "Policy examples" section | 
| Updated content, Tools account role names | Updated role name CustomerMigrationAccessRole to AWSManagedServicesMigrationRole. | [AWS Application Migration Service (AWS MGN)](tools-account-mgn.md) | 
| SALZ: Continuity management defaults | Updated link and removed obsolete information from [VPC tag and defaults](vpc-tag-and-defaults.md)  | February 28, 2022 | 