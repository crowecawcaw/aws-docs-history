

# Cloud-native Contact Center for Multilingual IT Service Desk

Publication date: **January 6, 2021 ([Diagram history](diagram-history.md))**

This reference architecture diagram shows how to modernize the IT service desk with an intelligent, omnichannel contact center by using [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/).

## Cloud-native Contact Center for Multilingual IT Service Desk diagram
<a name="cloud-native-contact-center-multilingual-diagram1"></a>

![Reference architecture diagram showing a cloud-native contact center for a multilingual IT service desk by using Amazon Connect Customer, Amazon Lex, AWS Lambda, and Amazon Simple Storage Service.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/contact-center/images/cloud-native-contact-center-multilingual.png)


1. End users contact the IT Service Desk through voice (PSTN or softphone), web chat, or smartphone. SD agents connect through a web-based softphone (CCP) from a browser.

1. Connect Customer provides inbound and outbound voice, web chat, and mobile chat with skills-based routing. Configure phone numbers, support queues, contact flows, and routing profiles.

1. Connect Customer integrates with CRM or ITSM ticketing tools (like ServiceNow) by using connectors from the AWS Partner ecosystem or custom integrations with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/).

1. Integrate Connect Customer with [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/) to create intelligent conversational chatbots. Automate high-volume contacts without increasing SD agents.

1. Connect Customer stores call recordings in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/) and [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/) for speech-to-text conversion. Use [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) to analyze key topics and sentiments.

1. [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/) protects sensitive data stored in call recordings. Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) to analyze relationships in the converted text.

1. Connect Customer provides real-time metrics (agents logged in, abandon rates, calls handled). Analyze contact trace records (CTRs) by using [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) and Lambda, store in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), and view in [Quick](https://docs.aws.amazon.com/quick/latest/userguide/) dashboards.

**Note**  
**A.** Connect Customer is an open platform, providing out-of-the-box integrations for leading CRM tools such as Salesforce and Zendesk, Workforce Management (WFM) tools, and analytics tools. With Lambda, you can create your own integration to existing ITSM or CRM products. To learn more about APN partners who have created custom integration connectors, see [Connect Customer Partners](https://aws.amazon.com/products/connect/customer/partners/).  
**B.** Connect Customer Integration offers a Quick Start guide to organizations using [ServiceNow](https://www.servicenow.com/) as their ticketing tool. You can use Lambda functions to jumpstart integration of ServiceNow and Connect Customer, resulting in one unified ITSM UI for SD agents and end users.

## Further reading
<a name="cloud-native-contact-center-multilingual-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect Customer product page](https://aws.amazon.com/connect/)