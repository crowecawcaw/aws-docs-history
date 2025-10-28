# Amazon Virtual Andon

Publication date: **October 15, 2021 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture provides a scalable Andon system to help optimize processes, support the transition to predictive maintenance, and prevent future equipment issues. This architecture can also be [deployed on AWS](../../../solutions/latest/amazon-virtual-andon/welcome.md "../../../solutions/latest/amazon-virtual-andon/welcome.md") using an AWS CloudFormation template that launches, configures, and runs the AWS services required to deploy this solution using AWS best practices for security and availability.

## Amazon Virtual Andon

![Reference architecture diagram showing a scalable Andon system to help optimize processes, support the transition to predictive maintenance, and prevent future equipment issues.](images/amazon-virtual-andon.png)

1. An **Amazon CloudFront** web interface deploys into an **Amazon Simple Storage Service** (Amazon S3) bucket configured for web hosting.
2. An **Amazon Cognito** user pool allows the solution’s
   administrators to register users and groups using the web interface.
3. **AWS AppSync** GraphQL APIs and **AWS Amplify** power the web interface. **Amazon DynamoDB** tables store the factory data.
4. An **AWS IoT** rule engine helps users monitor
   manufacturing workstations or devices for events, and then routes the events to the
   correct engineer for resolution in real-time.
5. Authorized users can interact with and receive notifications from this solution. An
   **AWS Lambda** function and **Amazon Simple Notification Service** (Amazon SNS) send email messages and SMS notifications.
6. Issues created, acknowledged, and closed in the web interface are recorded and updated
   using **AWS AppSync** and **DynamoDB**.
7. The **AWS AppSync** GraphQL APIs can be called directly with
   HTTP POST requests.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/amazon-virtual-andon.md "samples/amazon-virtual-andon.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [IoT Lens Checklist — AWS
  Well-Architected](../../../wellarchitected/latest/iot-lens-checklist/overview.md "../../../wellarchitected/latest/iot-lens-checklist/overview.md")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Reviewed            | Reviewed for technical accuracy                 | October 15, 2021 |
| Initial publication | Reference architecture diagram first published. | July 3, 2021     | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
