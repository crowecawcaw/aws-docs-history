# DSSEC05-BP01 Control unauthorized remote access to

infrastructure

Implement access controls to make sure only authorized support staff from verified
locations can access infrastructure resources. This includes identity verification, location
validation, and continuous monitoring of access activities.

Securing access to infrastructure resources is critical for maintaining a robust digital
sovereignty posture. Organizations must implement controls that verify user identity, validate
location, and enforce appropriate access levels. This approach combines identity management,
network controls, and automated monitoring to limit access to authorized personnel from trusted
locations.

**Desired outcome:** Organizations maintain visibility and control
over infrastructure access with detailed audit trails of support activities. Security risks are
reduced through granular access controls with real-time detection and response to potential
security threats. Support operations remain efficient while maintaining strict sovereignty
boundaries.

**Common anti-patterns**:

- Granting overly broad permissions for support roles and using shared accounts instead
  of individual identities, violating least privilege principles.
- Relying solely on IP-based access without multi-factor authentication or [just-in-time access](../../../singlesignon/latest/userguide/temporary-elevated-access.md "../../../singlesignon/latest/userguide/temporary-elevated-access.md") for elevated privileges.
- Failing to regularly review and rotate access credentials while storing sensitive keys
  in plain text or version control systems.
- Using the same access controls across each environment without differentiating
  requirements and allowing direct SSH/RDP (Secure Socket Shell / Remote Desktop Protocol)
  access without proper monitoring.

**Benefits of establishing this best practice**:

- Reduced risk of unauthorized access and security breaches with faster incident
  detection and response capabilities.
- Automated controls and standardized processes improve operational efficiency.
- Enhanced audit trails demonstrate regulatory adherence with better visibility into
  infrastructure access patterns.
- Improved processes while maintaining strict security boundaries.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Organizations should assess their current infrastructure, support requirements, and
compliance obligations before implementing access controls. Identify critical systems, map
existing access patterns, and document regulatory requirements that influence your approach.
The following practices establish secure access controls while maintaining operational
efficiency.

**Digital sovereignty considerations:**

- When remote access is required, verify that access originates from within approved
  jurisdictions using secure connectivity mechanisms such as [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"), VPN
  connections, or [AWS Verified Access](../../../verified-access/latest/ug/what-is-verified-access.md "../../../verified-access/latest/ug/what-is-verified-access.md") that
  terminate within sovereign boundaries. This verifies that even remote infrastructure
  management maintains jurisdictional adherence.
- Make sure support staff operate from approved jurisdictions and use network access
  controls to enforce geographic restrictions.
- Combine location-based and identity-based access controls using [Zero Trust Architecture](https://aws.amazon.com/security/zero-trust/ "https://aws.amazon.com/security/zero-trust/") principles
  aligned to data residency requirements.
- Maintain audit trails that demonstrate adherence to local regulations.
- Use encryption keys managed within sovereign boundaries.

### Implementation steps

**Identity and access management**:

1. **Implement strong identity and access management:**
   - Use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") to create individual user accounts for support staff.
   - Assign the least privilege necessary for each role, following the principle of
     least privilege.
   - Regularly review and audit IAM permissions to verify they remain appropriate.

2. **Enforce multi-factor authentication (MFA):**
   - Require [MFA](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") for support staff
     accounts, especially those with elevated privileges.
   - Use hardware tokens or virtual MFA devices for added security.

3. **Implement just-in-time access:**
   - Use [AWS
     IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to grant temporary, elevated permissions only when needed.
   - Implement automated processes to revoke access after a specified time or when
     no longer required.

**Network and access controls**:

1. **Implement network access controls:**
   - Use [AWS Virtual Private Cloud
     (VPC)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") to create isolated network environments.
   - Implement [Network Access Control Lists
     (NACLs)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") and [Security Groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") to
     restrict inbound and outbound traffic.
   - Use VPN or [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") for secure
     access from authorized locations.

2. **Use AWS Systems Manager for secure access:**
   - Use [Session
     Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") for browser-based access to EC2 instances without the need for
     open inbound ports.
   - Implement fine-grained permissions for Session Manager access.

3. **Implement IP-based restrictions:**
   - Use [IAM
     policy conditions](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") to restrict access based on source IP addresses or
     ranges.
   - Regularly review and update allowed IP ranges to verify they remain current.

**Governance and compliance**:

1. **Use AWS Organizations:**
   - Implement a [multi-account
     strategy](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") to segregate environments and limit the blast radius of potential
     security incidents.
   - Use [service
     control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") to enforce guardrails across your organization.

2. **Use AWS Config:**
   - Set up [AWS Config rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") to
     continuously monitor and assess the compliance of your AWS resources.
   - Create custom rules to enforce organization-specific security policies.

3. **Use AWS Control Tower:**
   - Implement [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") to set up and govern a secure, multi-account AWS
     environment.
   - Consider using [_Customizations
     for AWS Control Tower_ (CfCT)](../../../controltower/latest/userguide/cfct-overview.md "../../../controltower/latest/userguide/cfct-overview.md") to further customize your landing
     zone account structure and access controls.

**Monitoring and logging**:

1. **Enable and monitor AWS CloudTrail:**
   - Use [CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to
     log API calls and management events across your AWS accounts.
   - Set up alerts for suspicious activities or unauthorized access attempts.

2. **Regular security assessments:**
   - Conduct periodic vulnerability assessments and penetration testing.
   - Use [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") to
     get a centralized view of your security posture.

**Data protection and key management**:

1. **Implement secure key management:**
   - Use [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") for centralized management of encryption keys.
   - Implement [key rotation policies](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") and
     access controls for sensitive data.

2. **Implement data protection measures:**
   - Use [AWS Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md") to discover, classify, and protect sensitive data stored in
     S3 buckets.
   - Implement [encryption at rest](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md")
     and [in transit](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") for sensitive data.

**Automation and DevOps security**:

1. **Centralized package and dependency management:**
   - Use [AWS
     CodeArtifact](../../../codeartifact/latest/ug/welcome.md "../../../codeartifact/latest/ug/welcome.md") to implement centralized artifact repositories for secure
     package management.
   - Use [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md") for automated
     dependency scanning and vulnerability detection.
   - Maintain versioned and validated packages with approval workflows.

2. **Automated software deployment:**
   - Use infrastructure as code (IaC) with [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md"), [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md"), or [Terraform](https://www.terraform.io/ "https://www.terraform.io/") for each deployment.
   - Implement [AWS CodePipeline](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") and [AWS CodeBuild](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md") for automated testing and security validation.
   - Create standardized deployment pipelines with [AWS CodeDeploy](../../../codedeploy/latest/userguide/welcome.md "../../../codedeploy/latest/userguide/welcome.md") for consistent
     releases.

3. **Reduced interactive access:**
   - Use [AWS Systems Manager
     Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") to automate routine administrative tasks.
   - Implement [AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") with [temporary
     elevated access](../../../singlesignon/latest/userguide/temporary-elevated-access.md "../../../singlesignon/latest/userguide/temporary-elevated-access.md") for just-in-time access controls.
   - Create automated approval workflows using [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") and [Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

4. **Automated compute protection:**
   - Deploy [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") for automated
     threat detection and continuous monitoring.
   - Implement [AWS Systems Manager Patch
     Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md") for automated patch management across your fleet.
   - Enable [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
     for centralized security findings and automated remediation.

**Training and continual improvement**:

1. Provide regular security awareness training to support staff.
2. Keep the team updated on the latest AWS security features and best practices.

## Resources

**Related best practices**:

- [SEC02-BP02 Use
  temporary credentials](../security-pillar/sec_identities_unique.md "../security-pillar/sec_identities_unique.md")
- [SEC02-BP03
  Store and use secrets securely](../security-pillar/sec_identities_secrets.md "../security-pillar/sec_identities_secrets.md")
- [SEC02-BP04 Rely on a centralized identity provider](../security-pillar/sec_identities_identity_provider.md "../security-pillar/sec_identities_identity_provider.md")
- [SEC03-BP01
  Define access requirements](../security-pillar/sec_permissions_define.md "../security-pillar/sec_permissions_define.md")
- [SEC03-BP02 Grant least privilege access](../security-pillar/sec_permissions_least_privileges.md "../security-pillar/sec_permissions_least_privileges.md")
- [SEC03-BP07 Analyze public and cross-account access](../security-pillar/sec_permissions_analyze_cross_account.md "../security-pillar/sec_permissions_analyze_cross_account.md")
- [SEC05-BP01 Create network layers](../security-pillar/sec_network_protection_create_layers.md "../security-pillar/sec_network_protection_create_layers.md")
- [SEC05-BP02 Control traffic flow within your network layers](../security-pillar/sec_network_protection_layered.md "../security-pillar/sec_network_protection_layered.md")
- [SEC06-BP01 Perform vulnerability management](../security-pillar/sec_protect_compute_vulnerability_management.md "../security-pillar/sec_protect_compute_vulnerability_management.md")
- [SEC06-BP02 Provision compute from hardened images](../security-pillar/sec_protect_compute_hardened_images.md "../security-pillar/sec_protect_compute_hardened_images.md")
- [SEC04-BP01 Configure service and application logging](../security-pillar/sec_detect_investigate_events_app_service_logging.md "../security-pillar/sec_detect_investigate_events_app_service_logging.md")
- [SEC04-BP02 Capture logs, findings, and metrics in standardized
  locations](../security-pillar/sec_detect_investigate_events_logs.md "../security-pillar/sec_detect_investigate_events_logs.md")
- [SEC04-BP04 Initiate remediation for non-compliant resources](../security-pillar/sec_detect_investigate_events_noncompliant_resources.md "../security-pillar/sec_detect_investigate_events_noncompliant_resources.md")

**Related documents**:

- [AWS Security
  Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/")
- [AWS Identity and Access Management
  Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md")

**Related videos**:

- [AWS re:Inforce 2025 - Integrate
  Zero Trust into your cloud network (NIS304)](https://www.youtube.com/watch?v=AMSkou99Fus "https://www.youtube.com/watch?v=AMSkou99Fus")
- [AWS re:Invent 2025 -
  Innovations in Infrastructure Protection to strengthen your network (SEC310)](https://www.youtube.com/watch?v=qt9kaqiOYbQ "https://www.youtube.com/watch?v=qt9kaqiOYbQ")
- [AWS re:Invent 2025 - Advanced
  VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw "https://www.youtube.com/watch?v=40QfxdvDGsw")
- [AWS re:Inforce 2022 - Security
  best practices with AWS IAM (IAM201)](https://www.youtube.com/watch?v=SMjvtxXOXdU "https://www.youtube.com/watch?v=SMjvtxXOXdU")
- [Intro to Network Security - best
  practices for securing your network](https://www.youtube.com/watch?v=pwkyzElfJZc "https://www.youtube.com/watch?v=pwkyzElfJZc")

**Related services**:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/")
- [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/")
