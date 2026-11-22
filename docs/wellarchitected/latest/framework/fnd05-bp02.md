

# FND05-BP02 Establish emergency access mechanisms

 Establish processes that provide emergency access to your workloads when your centralized identity provider is unavailable or misconfigured. When federation fails, authorized administrators need an alternate path to cloud resources to resolve critical issues. Design emergency access processes for specific failure modes so administrators have the right tools without creating shortcuts around normal controls. 

 **Desired outcome:** 
+  You have defined and documented the failure modes that qualify as emergencies, considering your normal operating conditions and the systems your users depend on to manage their workloads. 
+  You have documented clear steps to confirm and declare an emergency. For example, identity administrators must check the status of both primary and standby identity providers and declare an emergency only when both are unavailable. 
+  You have defined specific emergency access processes for each failure mode. Process specificity reduces the risk of users overusing a general process for situations that don't warrant emergency access. 
+  Your emergency access processes clearly describe when each process applies and does not apply, and point to alternate processes when applicable. 
+  Your processes include detailed instructions and playbooks that can be followed quickly. Emergency events are stressful and time-sensitive, so processes must be short and direct to run under pressure. 

 **Common anti-patterns:** 
+  Lacking well-documented and well-tested emergency access processes, leaving users unprepared and following improvised procedures when emergencies arise. 
+  Building emergency access processes that depend on the same systems (such as a centralized identity provider) as normal access mechanisms. A failure of such a system affects both normal and emergency paths. 
+  Permitting emergency access processes to be used in non-emergency situations, for example because users find it faster to make changes directly than to submit changes through a pipeline. 
+  Operating emergency access processes that do not generate sufficient logs to audit the processes, or leaving those logs unmonitored so potential misuse is not alerted on. 

 **Benefits of establishing this best practice:** 
+  Reduced time to respond to and resolve emergencies, resulting in less downtime and higher service availability. 
+  Improved security and accountability through tracking of each emergency access request, with alerts on unauthorized misuse. 
+  Clear separation between routine and emergency procedures, reducing the likelihood that emergency mechanisms are abused as shortcuts. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Emergency access processes are a safety net when your organization's daily systems are unavailable. The architectural principle is isolation, meaning that your emergency access path must not depend on the same components as your primary access path. This includes the identity provider itself, the infrastructure hosting it, the network paths to reach it, and the configuration data that supports it. 

 Design emergency access processes around specific failure modes. A failure in your identity provider infrastructure requires a different response than a misconfigured SAML federation in AWS. When you define processes for specific scenarios, you reduce the risk of misuse because users understand when each process applies. Specific processes are also more straightforward to test. You can validate that each process addresses its intended failure mode without relying on components that should be unavailable in that scenario. 

 Pre-create the IAM resources needed by the emergency access process. This removes dependencies on AWS [control plane](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) APIs that might be unavailable during an emergency, and avoids [eventual consistency delays](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html) in resource propagation. Emergency access belongs in your [SEC10-BP02 Develop incident management plans](sec10-bp02.md) and service request workflow. Include all-hours approval paths, secondary approvers, and escalation routes that do not depend on the failed system. The approval workflow itself must be independent of the failed component. If granting emergency access requires approvers to authenticate through the same identity provider that is down, you have created a circular dependency. Correlate the telemetry from every access attempt with declared emergencies. Activity outside a declared event is an indicator of misuse and must trigger alerts. Rotate credentials after each emergency use, and exercise the processes periodically as part of incident response simulations and [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel13-bp03.md). 

**Important**  
 The emergency access account must remain dormant during normal operations. Any sign-in or API activity in this account outside a documented emergency event indicates unauthorized use or misuse and must trigger immediate investigation. 

 **Failure mode one: Identity provider used to federate to AWS is unavailable.** 

 When your centralized identity provider is unavailable, workforce users cannot federate to AWS accounts. The emergency access process relies on a pre-created emergency access AWS account. The account has IAM roles with permissions to assume cross-account roles in AWS accounts that require emergency access. Two approaches work: 
+  **Pre-created [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html):** Create as few IAM users as possible, each assigned to a single emergency administrator, with strong passwords and MFA tokens. Advantage: per-user attribution in CloudTrail. Disadvantage: multiple sets of long-lived credentials to maintain. 
+  **Emergency account [root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html):** Set a strong password and multiple MFA tokens, store them in a secure enterprise credential vault with strong authentication. Secure the password and MFA reset factors (email distribution list, shared phone number monitored by security). Advantage: single set of credentials. Disadvantage: multiple administrators share the user, so attribution depends on vault audit logs. 

 **Failure mode two: Identity provider configuration on AWS is modified or has expired.** 

 AWS-side configurations (IAM Identity Center or IAM Identity Provider) might be modified by mistake, or the X.509 certificate imported into AWS might expire without a replacement. Either scenario breaks federation. The emergency access process follows the same patterns as failure mode one. Identity administrators only need least-privilege access to the Identity Center administrator account to update the federation configuration. 

 **Failure mode three: IAM Identity Center disruption.** 

 For an IAM Identity Center or AWS Region disruption, set up direct SAML federation from your identity provider to IAM in the emergency account. This provides temporary access to the AWS Management Console. Identity administrators add members to pre-created emergency operations groups in your identity provider, and those users then federate directly to AWS IAM roles, bypassing IAM Identity Center. See [Set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html) for process and design considerations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create a dedicated emergency access AWS account:** Create an AWS account dedicated to emergency access processes. Pre-create the IAM resources needed in the account such as IAM roles or IAM users, and optionally IAM Identity Providers. Also pre-create cross-account IAM roles in the workload AWS accounts with trust relationships with corresponding IAM roles in the emergency access account. Use [AWS CloudFormation StackSets with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) to create these resources in the member accounts. 

1.  **Protect cross-account roles with SCPs:** Create AWS Organizations [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to prevent deletion or modification of the cross-account IAM roles in the member AWS accounts. 

1.  **Enable centralized CloudTrail logging:** Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for the emergency access AWS account and send trail events to a central [Amazon S3](https://aws.amazon.com/s3/) bucket in your log collection account. If using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), CloudTrail is enabled by default and logs are sent to a dedicated log archive account. 

1.  **Monitor emergency account activity:** Create [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that match on console login and API activity by the emergency IAM roles. Send notifications to your security operations center when activity happens outside of an ongoing emergency event tracked in your incident management system. 

1.  **Pre-create authentication resources for identity provider failures:** For failure modes one and two, pre-create the authentication resources the mechanism you chose requires. If you use [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html), pre-create each user with a strong password and associated [MFA device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html). If you use the emergency account root user, configure the root user with a strong password stored in your enterprise credential vault, and associate multiple physical MFA devices with the root user. Store those devices in locations quickly accessible by members of your emergency administrator team. 

1.  **Configure direct SAML federation for IAM Identity Center disruption:** For failure mode three, in the emergency access AWS account, create an IAM Identity Provider to enable direct SAML federation from your identity provider, following [Set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html). 

1.  **Create empty emergency operations groups for IAM Identity Center disruption:** For failure mode three, in your identity provider, create emergency operations groups with no members during normal operations. These groups map to IAM roles for direct SAML federation when IAM Identity Center is disrupted. Membership is added only when an emergency is declared and removed as soon as the event is resolved. 

1.  **Create corresponding IAM roles for SAML federation:** For failure mode three, create [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the emergency access account that correspond to the emergency operations groups, with a trust policy that trusts your SAML identity provider. Scope the permissions to only what is needed to resolve IAM Identity Center disruptions, such as assuming cross-account roles or managing resources during the emergency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 

 **Related documents:** 
+  [Set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html) 
+  [Enabling SAML 2.0 federated users to access the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) 
+  [Break glass access](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/) 
+  [AWS fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) 

 **Related examples:** 
+  [AWS Break Glass Role](https://github.com/awslabs/aws-break-glass-role) 
+  [AWS customer playbook framework](https://github.com/aws-samples/aws-customer-playbook-framework) 
+  [AWS incident response playbook samples](https://github.com/aws-samples/aws-incident-response-playbooks) 