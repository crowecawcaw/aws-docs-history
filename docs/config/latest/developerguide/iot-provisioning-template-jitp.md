# iot-provisioning-template-jitp

Checks if AWS IoT provisioning templates are using just-in-time provisioning (JITP). The rule is NON_COMPLIANT if configuration.TemplateType is not 'JITP'.

**Identifier:** IOT_PROVISIONING_TEMPLATE_JITP

**Resource Types:** AWS::IoT::ProvisioningTemplate

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
