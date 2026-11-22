

# sns-topic-message-delivery-notification-enabled

Checks if an Amazon SNS topic has IAM roles for both successful and failed deliveries set for any endpoint type. The rule is NON\_COMPLIANT otherwise, including email/SMS-only topics. The rule does not check subscriptions, role existence, or log delivery. 



**Identifier:** SNS\_TOPIC\_MESSAGE\_DELIVERY\_NOTIFICATION\_ENABLED

**Resource Types:** AWS::SNS::Topic

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1575c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).