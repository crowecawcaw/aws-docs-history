# Financial Advisor Chat Assistant

Publication date: **January 10, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

Financial advisors often work outside of normal business hours, when head office teams might
not be available to answer questions. This architecture enables you to use AWS to create a
sophisticated conversational chatbot to help financial advisors get answers to their queries
24/7.

## Financial Advisor Chat Assistant Diagram

![Reference architecture diagram showing a financial advisor chat assistannt.](images/financial-advisor-chat-assistant.png)

To enhance the security of this architecture, you shoulduse the following additional
services: **AWS CloudTrail** to track API usage, **Amazon CloudWatch** to monitor the AWS resources, and **AWS Key Management Service** (AWS KMS) to help securely generate and manage AWS encryption keys.
You should also enable secure headers in **AWS Amplify**.

1. The user’s browser resolves domain names through **Amazon Route 53** to IP address for **Amazon Simple Storage Service** (Amazon S3)
   and **Amazon CloudFront**.
2. **Amazon Cognito** provides user authentication and access control
   to the chat assistant and returns temporary credentials to the user’s browser or app to
   grant access to Amazon Lex . AWS recommends that you enable a strong password policy in
   **Amazon Cognito**. **Amazon Route 53**,
   **CloudFront**, **Amazon S3**, and
   **Amazon Cognito** are managed by **Amplify**, which aids rapid application development.
3. The user’s browser uses the temporary credentialsto call the **Amazon Lex** API.
4. **Amazon Lex** uses a built - in **Amazon Kendra** search intent to query **Amazon Kendra**. Access
   to **Amazon Kendra** is controlled by an **AWS Identity and Access Management** (IAM) role.
5. **Amazon Kendra** indexes objects in **Amazon S3** using the **Amazon Kendra**
   **Amazon S3** connector. You should enable **Amazon S3** at rest encryption.
6. **Amazon Kendra** indexes all objects in Salesforce, which are
   then available through the **Amazon Kendra** Salesforce
   connector.
7. Before connecting **Amazon Kendra** to the user’s Salesforce
   server, you must create a Salesforce connected app with OAuth enabled.
8. **Amazon Kendra** indexes Salesforce (API version48) with the
   Salesforce consumer and secret key.
9. Salesforce keys are stored in **AWS Secrets Manager** and use key
   rotation.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/financial-advisor-chat-assistant.md "samples/financial-advisor-chat-assistant.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- |
| Initial publication | Reference architecture diagram first published. | January 10, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
