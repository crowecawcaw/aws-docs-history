

# Production checklist
<a name="ace-production-checklist"></a>

Follow these steps to complete the production installation of your AWS Partner CRM connector.

1. Confirm that you completed the [onboarding process](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-getting-started.html) for the CRM integration. In [stage 6](https://docs.aws.amazon.com/partner-central/latest/crm/stage-6-production-approval.html) of this process, you set up your production environment and perform data migration so you can manage opportunities and leads through the integration. 

1. Install and configure the CRM connector. For more information, refer to [Installing the connector](install-connector.md).

1.  Map opportunities and lead objects by choosing one of the following mapping options. For reference, see this list of [required fields](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv) on GitHub.
   + Use the AWS ACE opportunity custom object provided with AWS Partner CRM connector to log opportunities and share them with AWS. Using this option, you can automatically map AWS fields to Salesforce fields.
   + Use the standard Salesforce object and map the required AWS fields.
   + Use an ACE custom opportunity object. You first create a workflow to populate an intermediate table of ACE opportunity objects and then map the Salesforce fields to AWS.

1. For additional details and guidance about mapping options, refer to [Mapping ACE objects](crm-connector-mapping.md).

1. (Optional) Set up inbound and outbound synchronization schedules between the AWS Partner Network and Salesforce. For details, refer to [Creating synchronization schedules](crm-connector-scheduling.md).

1. To validate a partner-originated opportunity in production, raise a [support case](https://docs.aws.amazon.com/partner-central/latest/crm/crm-integration-faq.html#troubleshooting) with Partner Central Operations (PCO) in your Partner Central account. In this process, you create a dummy opportunity, sync it with AWS, and ask the AWS support agent to confirm that AWS received the opportunity. At the end of testing, ask your AWS support agent to reject the opportunity request so you can delete it from your side.

1. (Optional) Perform data backfill. This process ensures that both AWS Originated and Partner Originated opportunity referrals can be identified during future updates. For more information, refer to [Stage 6: Production approval](https://docs.aws.amazon.com/partner-central/latest/crm/stage-6-production-approval.html) in the CRM onboarding process.

1. Activate the production integration to allow the exchange of files through the Amazon S3 bucket. For details, refer to [Stage 7: Launch](https://docs.aws.amazon.com/partner-central/latest/crm/stage-7-launch.html).