End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Use AMS SSP to provision Connect Customer in your AMS account

###### Note

After careful consideration, we decided to end support for Connect Customer Voice ID, effective May 20, 2026. Connect Customer Voice ID
will no longer accept new customers beginning May 20, 2025. As an existing customer with an account signed up for the service before May 20, 2025,
you can continue to use Connect Customer Voice ID features. After May 20, 2026, you will no longer be able to use Connect Customer Voice ID.

Use AMS Self-Service Provisioning (SSP) mode to access Connect Customer capabilities directly in your AMS managed account. Connect Customer is an omnichannel cloud contact center that helps companies provide
superior customer service at a lower cost. Connect Customer provides a seamless experience across voice
and chat for customers and agents. This includes one set of tools for skills-based routing,
powerful real-time and historical analytics, and easy-to-use intuitive management tools – all
with pay-as-you-go pricing.

You can create one or more instances of the virtual contact center instances in either AMS multi-account
landing zone or single-account landing zone accounts. You can use existing SAML 2.0 identity providers
for agent access or use Connect Customer native support for user life cycle management.

Additionally, you can claim toll free/direct dial phone numbers for each Connect Customer instance from the
Connect Customer console. You can create rich contact flows to achieve the desired customer experience and
routing using an easy-to-use graphical user interface. The contact flows can leverage AWS Lambda functions
to integrate with on-premises data stores and API’s. You can also enable data streaming using
Kinesis Streams and Firehose.

The call recordings, chat transcripts, and reports, are stored in an Amazon S3 bucket
encrypted using an AWS KMS key. The contact flow logs can be saved to CloudWatch log groups.

To learn more, see
[Connect Customer](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/").

## Connect Customer in AWS Managed Services FAQ

**Q: How do I request access to Connect Customer in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM roles to your account:
`customer_connect_console_role` and
`customer_connect_user_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Connect Customer in my AMS account?**

There are no restrictions. Full functionality of Connect Customer is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Connect Customer in my AMS account?**

- You must create an AWS KMS Key and an Amazon S3 bucket using standard AMS RFCs; the Amazon S3 bucket is
  required for storing call recordings and chat transcripts.
- If you want to integrate with Active Directory (AD), an AD Connector is required for
  integration between AMS-hosted Connect Customer instances and your on-premises directory services. AD Connector
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
