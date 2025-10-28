# Regional data

considerations

Amazon Cognito user pools are each created in one AWS Region, and they store the user profile
data only in that region. User pools can send user data to a different AWS Region,
depending on how optional features are configured.

- If the default `no-reply@verificationemail.com` email address setting is used
  for routing verification of emails addresses with Amazon Cognito user pools, emails are
  routed through the same region as the associated user pool.
- If a different email address is used to configure Amazon Simple Email Service (Amazon SES) with
  Amazon Cognito user pools, that email address is routed through the AWS Region
  associated with the email address in Amazon SES.
- SMS messages from Amazon Cognito user pools are routed through the same region Amazon SNS
  unless noted otherwise on [Configuring email or phone verification](user-pool-settings-email-phone-verification.md "user-pool-settings-email-phone-verification.md").
- If Amazon Pinpoint analytics are used with Amazon Cognito user pools, the event data is
  routed to the US East (N. Virginia) Region.

###### Note

Amazon Pinpoint is available in several AWS Regions in North America, Europe, Asia, and
Oceania. Amazon Pinpoint regions include the Amazon Pinpoint API. If a Amazon Pinpoint region is supported by
Amazon Cognito, then Amazon Cognito will send events to Amazon Pinpoint projects within the _same_ Amazon Pinpoint region. If a region _isn't_ supported by Amazon Pinpoint, then Amazon Cognito will _only_ support sending events in us-east-1. For Amazon Pinpoint
detailed region information, see [Amazon Pinpoint endpoints and
quotas](../../../general/latest/gr/pinpoint.md "../../../general/latest/gr/pinpoint.md") and [Using Amazon Pinpoint analytics with amazon cognito user pools](cognito-user-pools-pinpoint-integration.md "cognito-user-pools-pinpoint-integration.md").
