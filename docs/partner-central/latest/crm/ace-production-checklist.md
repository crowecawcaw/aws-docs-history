# Production checklist

Follow these steps to complete the production installation of your AWS Partner CRM
connector.

1. Confirm that you completed the [onboarding
   process](crm-integration-getting-started.md "crm-integration-getting-started.md") for the CRM integration. In [stage 6](stage-6-production-approval.md "stage-6-production-approval.md") of
   this process, you set up your production environment and perform data migration so you can
   manage opportunities and leads through the integration.
2. Install and configure the CRM connector. For more information, refer to [Installing the connector](install-connector.md "install-connector.md").
3. Map opportunities and lead objects by choosing one of the following mapping options.
   For reference, see this list of [required fields](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv") on GitHub.
   - Use the AWS ACE opportunity custom object provided with AWS Partner CRM connector to
     log opportunities and share them with AWS. Using this option, you can automatically
     map AWS fields to Salesforce fields.
   - Use the standard Salesforce object and map the required AWS fields.
   - Use an ACE custom opportunity object. You first create a workflow to populate an
     intermediate table of ACE opportunity objects and then map the Salesforce fields to
     AWS.

4. For additional details and guidance about mapping options, refer to [Mapping ACE objects](crm-connector-mapping.md "crm-connector-mapping.md").
5. (Optional) Set up inbound and outbound synchronization schedules between the AWS Partner
   Network and Salesforce. For details, refer to [Creating synchronization schedules](crm-connector-scheduling.md "crm-connector-scheduling.md").
6. To validate a partner-originated opportunity in production, raise a [support
   case](crm-integration-faq.md#troubleshooting "crm-integration-faq.md#troubleshooting") with Partner Central Operations (PCO) in your Partner Central account. In
   this process, you create a dummy opportunity, sync it with AWS, and ask the AWS
   support agent to confirm that AWS received the opportunity. At the end of testing, ask
   your AWS support agent to reject the opportunity request so you can delete it from your
   side.
7. (Optional) Perform data backfill. This process ensures that both AWS Originated and
   Partner Originated opportunity referrals can be identified during future updates. For more
   information, refer to [Stage 6: Production
   approval](stage-6-production-approval.md "stage-6-production-approval.md") in the CRM onboarding process.
8. Activate the production integration to allow the exchange of files through the Amazon
   S3 bucket. For details, refer to [Stage 7: Launch](stage-7-launch.md "stage-7-launch.md").
