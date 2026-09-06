

# Financial Advisor Chat Assistant
<a name="financial-advisor-chat-assistant"></a>

Publication date: **January 10, 2022 ([Diagram history](#diagram-history))**

Financial advisors often work outside of normal business hours, when head office teams might not be available to answer questions. This architecture enables you to use AWS to create a sophisticated conversational chatbot to help financial advisors get answers to their queries 24/7.

## Financial Advisor Chat Assistant Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing a financial advisor chat assistannt.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-advisor-chat-assistant/images/financial-advisor-chat-assistant.png)


To enhance the security of this architecture, you shoulduse the following additional services: **AWS CloudTrail** to track API usage, **Amazon CloudWatch** to monitor the AWS resources, and **AWS Key Management Service** (AWS KMS) to help securely generate and manage AWS encryption keys. You should also enable secure headers in **AWS Amplify**.

1. The user’s browser resolves domain names through **Amazon Route 53** to IP address for **Amazon Simple Storage Service** (Amazon S3) and **Amazon CloudFront**.

1. **Amazon Cognito** provides user authentication and access control to the chat assistant and returns temporary credentials to the user’s browser or app to grant access to Amazon Lex . AWS recommends that you enable a strong password policy in **Amazon Cognito**. **Amazon Route 53**, **CloudFront**, **Amazon S3**, and **Amazon Cognito** are managed by **Amplify**, which aids rapid application development.

1. The user’s browser uses the temporary credentialsto call the **Amazon Lex** API.

1. **Amazon Lex** uses a built - in **Amazon Kendra** search intent to query **Amazon Kendra**. Access to **Amazon Kendra** is controlled by an **AWS Identity and Access Management** (IAM) role.

1. **Amazon Kendra** indexes objects in **Amazon S3** using the **Amazon Kendra** **Amazon S3** connector. You should enable **Amazon S3** at rest encryption.

1. **Amazon Kendra** indexes all objects in Salesforce, which are then available through the **Amazon Kendra** Salesforce connector.

1. Before connecting **Amazon Kendra** to the user’s Salesforce server, you must create a Salesforce connected app with OAuth enabled.

1. **Amazon Kendra** indexes Salesforce (API version48) with the Salesforce consumer and secret key.

1. Salesforce keys are stored in **AWS Secrets Manager** and use key rotation.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 10, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.