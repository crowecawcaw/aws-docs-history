

# elbv2-acm-certificate-required
<a name="elbv2-acm-certificate-required"></a>

Checks if Application Load Balancers and Network Load Balancers have listeners that are configured to use certificates from AWS Certificate Manager (ACM). This rule is NON\_COMPLIANT if at least 1 load balancer has at least 1 listener that is configured without a certificate from ACM or is configured with a certificate different from an ACM certificate.



**Identifier:** ELBV2\_ACM\_CERTIFICATE\_REQUIRED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

AcmCertificatesAllowed (Optional)Type: CSV  
Comma-separated list of certificate Amazon Resource Names (ARNs).

## AWS CloudFormation template
<a name="w2aac20c16c17b7d775c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).