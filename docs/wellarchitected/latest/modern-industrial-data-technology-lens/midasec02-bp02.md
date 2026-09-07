

# MIDASEC02-BP02 Enable multi-factor authentication (MFA) and token authorization (TA)
<a name="midasec02-bp02"></a>

 Strengthen identity verification by enforcing MFA for human users and implementing token-based authorization for machines and services. 

 **Desired outcome:** Stronger authentication for both human users and industrial systems accessing AWS resources. 

 **Benefits of establishing this best practice:** Reduces risks associated with credential theft and replay attacks across IT/OT boundaries. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-11"></a>

 Enable MFA across all accounts, and integrate token services for secure, time-bound access. 

### Implementation steps
<a name="implementation-steps-12"></a>
+  Require MFA for all AWS accounts and IAM users using virtual or hardware devices. 
+  Implement SSO with MFA enforcement using AWS IAM Identity Center. 
+  Use temporary credentials and tokens through AWS Security Token Service for federated and service access. 
+  Enable and monitor MFA usage compliance with AWS Config rules. 

## Resources
<a name="resources-12"></a>
+  [ Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) 
+  [ What is AWS Identity and Access Management Access Analyzer? ](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) 
+  [ Welcome to the AWS Security Token Service API Reference ](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) 