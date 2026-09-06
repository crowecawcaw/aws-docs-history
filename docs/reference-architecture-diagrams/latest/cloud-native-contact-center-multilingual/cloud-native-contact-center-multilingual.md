

# Cloud-native Contact Center for Multilingual IT Service Desk
<a name="cloud-native-contact-center-multilingual"></a>

Publication date: **January 6, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to modernize the IT service desk with an intelligent, omnichannel contact center by using [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html).

## Cloud-native Contact Center for Multilingual IT Service Desk
<a name="diagram1"></a>

![Reference architecture diagram showing a cloud-native contact center for a multilingual IT service desk by using Amazon Connect, Amazon Lex, AWS Lambda, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cloud-native-contact-center-multilingual/images/cloud-native-contact-center-multilingual.png)


1. End users contact the IT Service Desk through voice (PSTN or softphone), web chat, or smartphone. SD agents connect through a web-based softphone (CCP) from a browser.

1. Amazon Connect provides inbound and outbound voice, web chat, and mobile chat with skills-based routing. Configure phone numbers, support queues, contact flows, and routing profiles.

1. Amazon Connect integrates with CRM or ITSM ticketing tools (like ServiceNow) by using connectors from the AWS Partner ecosystem or custom integrations with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

1. Integrate Amazon Connect with [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) to create intelligent conversational chatbots. Automate high-volume contacts without increasing SD agents.

1. Amazon Connect stores call recordings in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). Use Amazon Transcribe and Amazon Translate for speech-to-text conversion. Use Amazon Comprehend to analyze key topics and sentiments.

1. Amazon Macie protects sensitive data stored in call recordings. Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) to analyze relationships in the converted text.

1. Amazon Connect provides real-time metrics (agents logged in, abandon rates, calls handled). Analyze contact trace records (CTRs) by using [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) and Lambda, store in [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html), and view in [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) dashboards.

**Note**  
**A.** Amazon Connect is an open platform, providing out-of-the-box integrations for leading CRM tools such as Salesforce and Zendesk, Workforce Management (WFM) tools, and analytics tools. With Lambda, you can create your own integration to existing ITSM or CRM products. To learn more about APN partners who have created custom integration connectors, see [Amazon Connect Partners](https://aws.amazon.com/products/connect/customer/partners/).  
**B.** Amazon Connect Integration offers a Quick Start guide to organizations using [ServiceNow](https://www.servicenow.com/) as their ticketing tool. You can use Lambda functions to jumpstart integration of ServiceNow and Amazon Connect, resulting in one unified ITSM UI for SD agents and end users.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect product page](https://aws.amazon.com/connect/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 6, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.