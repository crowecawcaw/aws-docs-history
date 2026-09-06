

# guardduty-ecs-protection-runtime-enabled
<a name="guardduty-ecs-protection-runtime-enabled"></a>

Checks if ECS Runtime Monitoring with automated agent management is enabled for Amazon GuardDuty detector. The rule is NON\_COMPLIANT if the feature is not enabled for your account or at least one member account in your organization. 



**Identifier:** GUARDDUTY\_ECS\_PROTECTION\_RUNTIME\_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d893c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).