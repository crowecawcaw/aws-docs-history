

# DRHCSEC03-BP01 Implement controls that enhance your digital sovereignty governance posture
<a name="drhcsec03-bp01"></a>

 Consider implementing controls which are not data residency specific as these controls help enable a defense in depth approach to security and are often easy to enable without requiring customization. 

 **Desired outcome:** Preventative controls deny storage of data in locations that lack compliance with data residency regulations. 

 **Common anti-patterns:** 
+  Attempting to author and maintain all the controls within your organization rather than using controls maintained by AWS, AWS partners, or others who invest continuously in maintaining controls focused on digital sovereignty 

 **Benefits of establishing this best practice:** Rigorously tested controls are deployed through automated procedures that improve your ability to securely scale more rapidly and cost-effectively. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-20"></a>
+  Enable the AWS Control Tower [digital sovereignty group](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html) of controls. Evaluate each control's applicability to your scenario, as some controls have very limited use cases where they should be applied. One of the most commonly deployed controls is the [OU Region deny control](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html).   
  +  While the same set of preventative and detective controls can be reproduced without deployment through Control Tower, it is highly recommended to use Control Tower to eliminate the undifferentiated heavy lifting of maintaining these controls yourself. This practice also facilitates easier deployment of new controls as they become available. 
+  Disable any Local Zones (at the account level) that are currently enabled but not required. 
+  Deploy an SCP to deny the ec2:ModifyAvailabilityZoneGroup IAM action to all principals that do not have explicit approval to opt in to Local Zones for the account. 
+  Establish a data perimeter as discussed in [SEC03-BP08 Share resources securely within your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html), as controlling which principals have access to data is a foundational step to controlling the location where data can be stored. 
+  Deploy encryption controls to enforce usage of encryption. Where supported, require AWS KMS customer-managed keys, and implement fine grained AWS KMS key policies to promote security-in-depth and add another level of data access control. 

## Resources
<a name="resources-6"></a>

 **Related best practices:** 
+  [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html) 
+  [SEC03-BP08 Share resources securely within your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 

 **Related documentation:** 
+  [Digital sovereignty controls](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html) 
+  [Region deny control applied to the OU](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html) 
+  [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) 
+  [Building Data Perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) 
+  [Establishing a data perimeter on AWS: Allow only trusted identities to access company data](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-allow-only-trusted-identities-to-access-company-data/) 
+  [Data Perimeter Policy Examples](https://github.com/aws-samples/data-perimeter-policy-examples) 