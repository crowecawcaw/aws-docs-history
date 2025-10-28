# Use AMS SSP to provision Amazon Connect in your AMS account

###### Note

After careful consideration, we decided to end support for Amazon Connect Voice ID, effective May 20, 2026. Amazon Connect Voice ID
will no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025,
you can continue to use Amazon Connect Voice ID features. After May 20, 2026, you will no longer be able to use Amazon Connect Voice ID.

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Connect capabilities directly in your AMS managed account. Amazon Connect is an omnichannel cloud contact center that helps companies provide
superior customer service at a lower cost. Amazon Connect provides a seamless experience across voice
and chat for customers and agents. This includes one set of tools for skills-based routing,
powerful real-time and historical analytics, and easy-to-use intuitive management tools – all
with pay-as-you-go pricing.

You can create one or more instances of the virtual contact center instances in either AMS multi-account
landing zone or single-account landing zone accounts. You can use existing SAML 2.0 identity providers
for agent access or use Amazon Connect native support for user life cycle management.

Additionally, you can claim toll free/direct dial phone numbers for each Amazon Connect instance from the
Amazon Connect console. You can create rich contact flows to achieve the desired customer experience and
routing using an easy-to-use graphical user interface. The contact flows can leverage AWS Lambda functions
to integrate with on-premises data stores and API’s. You can also enable data streaming using
Kinesis Streams and Firehose.

The call recordings, chat transcripts, and reports, are stored in an Amazon S3 bucket
encrypted using an AWS KMS key. The contact flow logs can be saved to CloudWatch log groups.

To learn more, see
[Amazon Connect](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/").

## Amazon Connect in AWS Managed Services FAQ

**Q: How do I request access to Amazon Connect in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM roles to your account:
`customer_connect_console_role` and
`customer_connect_user_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Connect in my AMS account?**

There are no restrictions. Full functionality of Amazon Connect is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Connect in my AMS account?**

- You must create an AWS KMS Key and an Amazon S3 bucket using standard AMS RFCs; the Amazon S3 bucket is
  required for storing call recordings and chat transcripts.
- If you want to integrate with Active Directory (AD), an AD Connector is required for
  integration between AMS-hosted Amazon Connect instances and your on-premises directory services. AD Connector
  can be configured in your account by requesting a 'Management | Other | Other' RFC.
- You can enable the following optional self-provisioned services based on your contact flow requirements.
  - **AWS Lambda**: You can use Lambda functions to extend the contact flows to
    leverage existing on-premises data stores or APIs. You can use the Lambda self-provisioned service to create the Lambda functions.
  - **Amazon Kinesis Data Streams**: You can create data streams
    to enable Data streaming to external applications. You can stream contact trace records or Agent Events.
  - **Amazon Kinesis Data Firehose**: You can create
    Data Firehose to stream high volume contact trace records to external applications.
  - **Amazon Lex**: You can leverage Amazon Lex Chatbots to create
    smart contact flows leveraging Amazon Alexa services for rich customer experience and automation.

- **Q: How do I request to add list of countries for outbound or inbound calls?**

To add a list of countries for outbound or inbound calls, submit a service request to AMS.
