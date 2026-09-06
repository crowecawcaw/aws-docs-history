

# redshift-serverless-workgroup-routes-within-vpc
<a name="redshift-serverless-workgroup-routes-within-vpc"></a>

Checks if Amazon Redshift Serverless workgroups route the network traffic through a VPC. The rule is NON\_COMPLIANT if workgroups have 'Turn on Enhanced VPC routing' disabled. 



**Identifier:** REDSHIFT\_SERVERLESS\_WORKGROUP\_ROUTES\_WITHIN\_VPC

**Resource Types:** AWS::RedshiftServerless::Workgroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1329c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).