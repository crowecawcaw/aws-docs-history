

# s3-bucket-policy-grantee-check
<a name="s3-bucket-policy-grantee-check"></a>

Checks that the access granted by the Amazon S3 bucket is restricted by any of the AWS principals, federated users, service principals, IP addresses, or VPCs that you provide. The rule is COMPLIANT if a bucket policy is not present.

For example, if the input parameter to the rule is the list of two principals: `111122223333` and `444455556666` and the bucket policy specifies that only `111122223333` can access the bucket, then the rule is COMPLIANT. With the same input parameters: If the bucket policy specifies that `111122223333` and `444455556666` can access the bucket, it is also COMPLIANT.

However, if the bucket policy specifies that `999900009999` can access the bucket, the rule is NON\_COMPLIANT. 

**Note**  
If a bucket policy contains more than one statement, each statement in the bucket policy is evaluated against this rule.



**Identifier:** S3\_BUCKET\_POLICY\_GRANTEE\_CHECK

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

servicePrincipals (Optional)Type: CSV  
Comma-separated list of service principals, for example 'cloudtrail.amazonaws.com, lambda.amazonaws.com'.

federatedUsers (Optional)Type: CSV  
Comma-separated list of identity providers for web identity federation such as Amazon Cognito and SAML identity providers. For example 'cognito-identity.amazonaws.com, arn:aws:iam::111122223333:saml-provider/my-provider'.

awsPrincipals (Optional)Type: CSV  
Comma-separated list of principals such as IAM User ARNs, IAM Role ARNs, and AWS accounts. You must provide the full ARN or use partial matching. For example, "arn:aws:iam::{{AccountID}}:role/{{role\_name}}" or "arn:aws:iam::{{AccountID}}:role/\*". If the provided value is not an exact match with the principal ARN specified in the bucket policy, the rule is NON\_COMPLIANT.

ipAddresses (Optional)Type: CSV  
Comma-separated list of CIDR formatted IP addresses, for example '10.0.0.1, 192.168.1.0/24, 2001:db8::/32'.

vpcIds (Optional)Type: CSV  
Comma-separated list of Amazon Virtual Private Clouds (Amazon VPC) IDs, for example 'vpc-1234abc0, vpc-ab1234c0'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1399c25"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).