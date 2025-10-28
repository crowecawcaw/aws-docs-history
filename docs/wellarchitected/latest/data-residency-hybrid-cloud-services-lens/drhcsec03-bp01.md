# DRHCSEC03-BP01 Implement controls that enhance your digital sovereignty governance posture

Consider implementing controls which are not data residency
specific as these controls help enable a defense in depth approach
to security and are often easy to enable without requiring
customization.

**Desired outcome:** Preventative
controls deny storage of data in locations that lack compliance
with data residency regulations.

**Common anti-patterns:**

- Attempting to author and maintain all the controls within your
  organization rather than using controls maintained by AWS, AWS
  partners, or others who invest continuously in maintaining
  controls focused on digital sovereignty

**Benefits of establishing this best
practice:** Rigorously tested controls are deployed
through automated procedures that improve your ability to securely
scale more rapidly and cost-effectively.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- Enable the AWS Control Tower
  [digital
  sovereignty group](../../../controltower/latest/controlreference/digital-sovereignty-controls.md "../../../controltower/latest/controlreference/digital-sovereignty-controls.md") of controls. Evaluate each
  control's applicability to your scenario, as some controls
  have very limited use cases where they should be applied.
  One of the most commonly deployed controls is the
  [OU
  Region deny control](../../../controltower/latest/controlreference/ou-region-deny.md "../../../controltower/latest/controlreference/ou-region-deny.md").  
  - While the same set of preventative and detective
    controls can be reproduced without deployment through
    Control Tower, it is highly recommended to use Control
    Tower to eliminate the undifferentiated heavy lifting of
    maintaining these controls yourself. This practice also
    facilitates easier deployment of new controls as they
    become available.

- Disable any Local Zones (at the account level) that are
  currently enabled but not required.
- Deploy an SCP to deny the ec2:ModifyAvailabilityZoneGroup
  IAM action to all principals that do not have explicit
  approval to opt in to Local Zones for the account.
- Establish a data perimeter as discussed in
  [SEC03-BP08
  Share resources securely within your organization](../security-pillar/sec_permissions_share_securely.md "../security-pillar/sec_permissions_share_securely.md"), as
  controlling which principals have access to data is a
  foundational step to controlling the location where data can
  be stored.
- Deploy encryption controls to enforce usage of encryption.
  Where supported, require AWS KMS customer-managed keys, and
  implement fine grained AWS KMS key policies to promote
  security-in-depth and add another level of data access
  control.

## Resources

**Related best practices:**

- [SEC03-BP05
  Define permission guardrails for your organization](../security-pillar/sec_permissions_define_guardrails.md "../security-pillar/sec_permissions_define_guardrails.md")
- [SEC03-BP08
  Share resources securely within your organization](../security-pillar/sec_permissions_share_securely.md "../security-pillar/sec_permissions_share_securely.md")
- [SEC08-BP01
  Implement secure key management](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md")

**Related documentation:**

- [Digital
  sovereignty controls](../../../controltower/latest/controlreference/digital-sovereignty-controls.md "../../../controltower/latest/controlreference/digital-sovereignty-controls.md")
- [Region
  deny control applied to the OU](../../../controltower/latest/controlreference/ou-region-deny.md "../../../controltower/latest/controlreference/ou-region-deny.md")
- [Evaluating
  Resources with AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
- [Building
  Data Perimeter on AWS](../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md "../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md")
- [Establishing
  a data perimeter on AWS: Allow only trusted identities to
  access company data](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-allow-only-trusted-identities-to-access-company-data/ "https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-allow-only-trusted-identities-to-access-company-data/")
- [Data
  Perimeter Policy Examples](https://github.com/aws-samples/data-perimeter-policy-examples "https://github.com/aws-samples/data-perimeter-policy-examples")
