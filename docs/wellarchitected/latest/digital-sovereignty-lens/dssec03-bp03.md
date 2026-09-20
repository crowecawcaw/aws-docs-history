

# DSSEC03-BP03 Validate resource configurations for sovereignty compliance
<a name="dssec03-bp03"></a>

 Sovereignty configuration validation verifies that resources are provisioned and maintained in line with jurisdictional constraints: Region placement, key residency, replication scope, and classification tagging. Validate resource configurations against sovereignty baselines before and after deployment using rules-based evaluation. 

 **Desired outcome:** 
+  Resources are validated against sovereignty-specific configuration baselines before they are provisioned and are monitored continuously for configuration drifts after deployment. 

 **Common anti-patterns:** 
+  Deploying resources without checking whether the underlying resources are configured to meet sovereignty requirements. 
+  Relying solely on detective controls to find misconfigured resources after deployment, rather than blocking noncompliant configurations before provisioning. 

 **Benefits of establishing this best practice:** 
+  Noncompliant resource configurations are blocked before provisioning, reducing remediation effort and compliance risk. 
+  Continuous configuration monitoring detects drift from sovereignty baselines after deployment. 
+  Reusable rule libraries reduce the effort to validate new workloads against sovereignty requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Use [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) rules to validate resource configurations against sovereignty requirements. CloudFormation Guard is an [open source](https://github.com/aws-cloudformation/cloudformation-guard), general-purpose, policy-as-code evaluation tool for defining compliance-aligned rules in a human-readable, declarative format. To get started, refer to the [setup instructions](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up.html). Its domain-specific language (known as Guard DSL) provides reusable rules that can be applied at multiple stages of your DevOps lifecycle, from pre-deployment validation in CI/CD pipelines to runtime compliance checks with AWS Config. The stages and application methods are: 

1.  **Local unit testing (developer workstation)** - Use cfn-guard test for local development, and [unit testing](https://docs.aws.amazon.com/cfn-guard/latest/ug/testing-rules.html) of your guard rules. 

1.  **Local validation (developer workstation and CI/CD pipelines)** - Run cfn-guard validate against CloudFormation templates, CloudFormation change sets, JSON-based Terraform configuration files, or Kubernetes configurations. 

1.  **CloudFormation Guard Hooks (at provisioning time, server-side)** - Guard alone doesn't provide server-side enforcement. To enforce compliance proactively, develop, unit test, and validate your Guard rules locally, then deploy them as [CloudFormation Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html). Guard Hooks enforce Guard rules automatically before CloudFormation create, update, or delete operations. You can also configure a Guard Hook when you create, update, and delete a resource using the [AWS Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html) (with IaC providers such as [Terraform](https://github.com/hashicorp/terraform-provider-awscc) and [Pulumi](https://github.com/pulumi/pulumi-aws-native)). 

1.  **AWS AWS Control Tower proactive controls (at provisioning time, server-side)** - Use [AWSAWS Control Tower proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) to block noncompliant resources before they are created. Proactive controls are implemented as CloudFormation Hooks and evaluate resource configurations during provisioning. These proactive controls are implemented as preCreate and preUpdate hook handlers. Be aware that these controls **might not evaluate requests** made through the AWS console, AWS APIs, SDKs, or other IaC tools. 

1.  **AWS Config custom policy rules (post-deployment, continuous)** - Use [AWS Config custom rules with Guard](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html) to continuously evaluate resource configurations after deployment. Config evaluates resources against your Guard rules and generates compliance findings when configurations drift from sovereignty baselines. 

 Develop, unit test, and validate new rule files locally. Then, based on your needs, deploy them on the server-side as CloudFormation Guard Hooks or AWS Config custom rules. Before writing a new Guard rule, check the [proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) already provided by AWS Control Tower, and the [AWS Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry), for reusable starting points. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define sovereignty configuration baselines**: Document the resource configuration requirements that support your sovereignty posture. Common sovereignty configuration rules include: 
   +  KMS keys should be single-Region (multi-Region keys disallowed for data residency) 
   +  S3 buckets should not have cross-Region replication configured 
   +  Secrets Manager secrets should not replicate to other Regions 
   +  Resources should carry sovereignty tags (data-classification, data-residency-requirement, compliance-framework) 
   +  RDS instances should not have cross-Region read replicas outside approved jurisdictions 

    Map each rule to the regulatory requirement it supports and document in your compliance catalog from [DSOPS02-BP01 Baseline your compliance requirements](dsops02-bp01.html). 

    Layer controls across different enforcement surfaces so that no single bypass defeats the baseline. For example, the [AWS Control Tower Region deny control](https://docs.aws.amazon.com/controltower/latest/controlreference/primary-region-deny-policy.html) blocks AWS API calls in non-approved Regions regardless of how they are invoked, while a Guard Hook on CloudFormation stack operations additionally catches sovereignty violations *within* an approved Region, such as an S3 bucket with cross-Region replication configured to a non-approved destination. 

1.  **Write CloudFormation Guard rules for sovereignty requirements**: Implement Guard rules that validate resource configurations. The following examples illustrate common sovereignty rules: 

    **Note:** The code snippets shown here are for illustration only and may not be accurate. Validate against your own environment and requirements unique to your workload. 
   +  **Validate KMS key residency:** 

     ```
     # Verify KMS keys are single-region only
     rule check_kms_single_region {
       Resources[ Type == 'AWS::KMS::Key' ].Properties {
         MultiRegion != true
           << Violation: Multi-region KMS keys are not permitted.
              KMS keys must be single-region for data residency compliance.
              Fix: Set MultiRegion to false or remove the property entirely. >>
       }
     }
     ```
   +  **Validate S3 replication restrictions:** 

     ```
     # Verify S3 buckets do not have cross-region replication
     rule check_s3_no_cross_region_replication {
       Resources[ Type == 'AWS::S3::Bucket' ].Properties {
         ReplicationConfiguration not exists
           << Violation: S3 buckets must not have replication configuration
              for data residency compliance.
              Fix: Remove the ReplicationConfiguration property. >>
       }
     }
     ```
   +  **Validate sovereignty tags:** 

     ```
     # Verify resources have required sovereignty tags
     rule check_sovereignty_tags {
       Resources[ Type in ['AWS::S3::Bucket', 'AWS::DynamoDB::Table'] ].Properties {
         Tags exists
           << Violation: Resource missing Tags. Must include sovereignty tags:
              data-classification, data-residency-requirement, compliance-framework. >>
     
         when Tags exists {
           some Tags[*].Key == 'data-classification'
             << Violation: Missing required tag 'data-classification'. >>
     
           some Tags[*].Key == 'data-residency-requirement'
             << Violation: Missing required tag 'data-residency-requirement'. >>
     
           some Tags[*].Key == 'compliance-framework'
             << Violation: Missing required tag 'compliance-framework'. >>
         }
       }
     }
     ```
   +  **Validate Secrets Manager replication:** 

     ```
     # Verify Secrets Manager secrets are not replicated to other regions
     rule check_secrets_manager_no_replication {
       Resources[ Type == 'AWS::SecretsManager::Secret' ].Properties {
         ReplicaRegions not exists
           << Violation: Secrets Manager secrets must not be replicated to other regions
              for data residency compliance.
              Fix: Remove the ReplicaRegions property entirely. >>
       }
     }
     ```

1.  **Test rules locally**: Unit test Guard rules locally using cfn-guard test with both passing and failing test cases. Test edge cases, for example, test that specific resource types without Tags correctly trigger a violation. Review and update rules when regulations change or new resource types are adopted. For guidance on tracking regulatory changes, see [DSOPS06-BP01 Track regulatory changes across jurisdictions](dsops06-bp01.html). 

1.  **Integrate rules into CI/CD pipelines (pre-deployment)**: Run cfn-guard validate against infrastructure templates in your CI/CD pipeline before deployment. Consider failing the pipeline stage if sovereignty rules are violated. For guidance on embedding compliance validation into pipelines, see [DSOPS02-BP02 Establish an automated path to compliance](dsops02-bp02.html). 

1.  **Deploy rules as proactive controls (pre-provisioning)**: Use [AWSAWS Control Tower proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) to block noncompliant resources before they are created. For custom sovereignty rules not covered by built-in proactive controls, deploy your Guard rules as [CloudFormation Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html). Consider the following: 
   +  **Start in WARN mode:** Guard Hooks support WARN and FAIL modes. Start with WARN mode to assess which deployments would be blocked, then switch to FAIL mode for enforcement. Guard Hooks have a 30-second timeout per invocation with 3 retries, so optimize rules before enabling FAIL mode to avoid blocking legitimate deployments. 
   +  **Understand coverage boundaries:** AWS Control Tower proactive controls evaluate resources provisioned through CloudFormation stack operations. CloudFormation Guard Hooks can additionally evaluate CloudFormation initiated stack operations, resource changes, change-set-based invocations, and Cloud Control API initiated resource operations. Resources created directly through the AWS console, AWS APIs, or SDKs may not be evaluated by either mechanism. 
   +  **Layer detective controls for complete coverage:** Guard rules evaluate template definitions, not runtime state: a template may pass validation but the deployed resource could drift. And resources created outside IaC workflows may not be detected with proactive controls. Deploy AWS Config custom rules (Step 6) using the same Guard DSL syntax to provide continuous runtime monitoring regardless of how resources were created. 

1.  **Deploy rules as detective controls (post-deployment)**: When you create and deploy [custom AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html#config-custom-policy-rules) using the Guard DSL syntax, you can enable both proactive evaluation (checking resource properties for compliance before they are deployed) and detective evaluation (detecting drift after deployment). You can scope evaluations to "all changes", "changes to specific resource types, resource identifiers" or "resources with specific tags". Route findings to [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) for aggregation and to [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) for automated alerting or remediation. AWS Config rule evaluations are priced per evaluation. At scale, dozens of sovereignty rules across thousands of resources can accumulate costs. Scope rules to specific resource types or tags. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSSEC03-BP01 Validate policy effectiveness through automated analysis](dssec03-bp01.html) 
+  [DSSEC03-BP02 Verify network security posture through automated analysis](dssec03-bp02.html) 
+  [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.html) 
+  [DSOPS02-BP02 Establish an automated path to compliance](dsops02-bp02.html) 
+  [SEC01-BP06 Automate deployment of standard security controls](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_automate_security_controls.html) 

 **Related documents:** 
+  [AWS CloudFormation Guard User Guide](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [Creating AWS Config custom rules with Guard](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html) 
+  [AWSAWS Control Tower proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) 
+  [Create AWS Config custom rules by using AWS CloudFormation Guard policies](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies.html) 

 **Related examples:** 
+  [AWS Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry) 
+  [AWS Config Conformance Pack Samples](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8) 

 **Related services:** 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 