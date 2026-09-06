

# mq-active-single-instance-broker-storage-type-efs
<a name="mq-active-single-instance-broker-storage-type-efs"></a>

Checks if an Amazon MQ for ActiveMQ single-instance broker using the mq.m5 instance type family is configured with Amazon Elastic File System (EFS) for broker storage. The rule is NON\_COMPLIANT if configuration.StorageType is not 'efs'. 



**Identifier:** MQ\_ACTIVE\_SINGLE\_INSTANCE\_BROKER\_STORAGE\_TYPE\_EFS

**Resource Types:** AWS::AmazonMQ::Broker

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1107c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).