

# FND05-BP01 Shift compliance checks left with proactive controls

 Proactive controls evaluate infrastructure and configuration against your organization's standards before resources are provisioned, so non-compliant resources are blocked at deploy time. Shifting these checks into pipelines, templates, and provisioning flows shortens the feedback loop for builders, shrinks the backlog that detective tooling has to work through, and reduces the volume of remediation work that lands on downstream teams. 

 **Desired outcome:** 
+  Your organization's compliance standards are codified as machine-readable policies that run against infrastructure as code before it is deployed. 
+  Your delivery pipelines reject templates that violate required controls and surface the failure in the same place developers already see build errors. 
+  Your provisioning services (CloudFormation, Service Catalog, CDK) run proactive checks at the point of resource creation so non-compliant resources cannot be created even through the console. 
+  Your detective tooling sees a shrinking volume of findings for classes of issue that proactive controls now prevent, freeing it to focus on unusual or emergent problems. 
+  Your foundation team measures proactive coverage alongside detective coverage as a core input to the organization's compliance posture. 

 **Common anti-patterns:** 
+  Relying on detective tooling alone, so every misconfiguration becomes a ticket and a remediation action rather than being prevented at provisioning time. 
+  Writing custom scripts that scan templates locally but never wiring them into the pipeline or the provisioning flow, so the checks are optional and inconsistent. 
+  Duplicating the same rules across Config, CloudFormation Guard, CDK Aspects, and third-party scanners with no source of truth, so the rules drift apart and teams learn to ignore some of them. 
+  Running proactive scans only at merge time, missing the opportunity to give developers feedback while they are still writing the template and the fix is cheapest. 
+  Treating proactive checks as advisory warnings that teams routinely waive, so the controls exist on paper but have no real effect on what gets deployed. 
+  Putting proactive controls in place without an exception process, so legitimate cases where a rule does not apply turn into permanent workarounds that undermine the control. 

 **Benefits of establishing this best practice:** 
+  Fixing a misconfiguration in a template during code review is much cheaper than fixing a live resource in production after a detective rule has flagged it. 
+  Compliance errors surface in the pull request or pipeline the developer is already watching, in the same cadence as build and test failures, rather than hours or days later. 
+  Classes of finding that proactive controls prevent disappear from the detective queue, so the security team's attention shifts toward novel issues. 
+  Rules codified once and applied in pipelines and provisioning flows run uniformly across every workload, every account, and every Region. 
+  A demonstrable pre-deploy enforcement layer produces evidence that compliance is built into the path to production, not bolted on afterward. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Controls fall into four types: 
+  *Preventive* controls stop non-compliant actions and configurations from being possible at all (service control policies, resource control policies, IAM policies, permission boundaries). 
+  *Proactive* controls evaluate infrastructure before it is provisioned and block non-compliant resources from being created. 
+  *Detective* controls find and report non-compliance in resources that already exist. 
+  *Reactive* controls remediate or contain what detection finds. 

 All four control types work together to catch issues throughout the development, build, and release pipeline. A detective finding starts a workflow (triage, assignment, change approval, deployment, verification) that takes days and involves multiple teams. When the same rule runs against a template at pull request time, it returns a failure in minutes, and one developer resolves it with a small edit. As the environment grows, this difference dominates the total cost of compliance. 

 Enforce at three points in the development flow: 1. During IDE and local development, linting rules, pre-commit hooks, and framework-native checks like [AWS CDK Aspects](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html) and [cdk-nag](https://github.com/cdklabs/cdk-nag) catch issues while the developer is still writing the code. 2. In the delivery pipeline, [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) and policy-as-code runners evaluate templates in [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) or equivalent, and failing policies fail the build. 3. At the provisioning service, [AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) evaluate resources at the point of creation and can block stack operations that would produce non-compliant resources. 

 [AWS Config proactive rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_components.html#proactive-rules) extend existing Config rule logic to pre-deploy evaluation. Pipelines catch most issues early, but hooks and proactive Config rules enforce policies even for resources created through the console, the CLI, or out-of-band automation that bypasses the pipeline. 

 Start from a landing zone and reference architecture baseline. Modern landing zones ([AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), [Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/landing-zone-accelerator-on-aws/), and the patterns in the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/)) deliver a substantial preventive and proactive posture through SCPs, managed controls, and account baselines. Build on that foundation, and focus your proactive investment on the rules specific to your workloads, regulatory scope, and internal standards. [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) products and curated IaC modules also serve as proactive controls: a builder who consumes a vetted pattern inherits its compliance. 

 Author rules in a single source of truth. Store the rules as code: version-controlled, reviewed, tested against sample templates (both passing and failing cases), and released through a pipeline. Don't copy rules between Guard, Config, CDK-nag, and third-party scanners. When rules drift apart, coverage fragments and teams lose trust in the controls. Where the same rule logic needs to run in multiple places (pre-commit, pipeline, hook, detective), generate the variants from the single source. Pair every rule with a clear failure message that tells the developer *what* is wrong, *why* it matters, and *how* to fix it. 

 Every proactive control needs an exception path. Rules will not fit every resource, workload, or time window, and if the only options are "pass" or "block," teams work around the control. Define how teams request exceptions, who approves them, how long they last, and how they are tracked. Tag exceptions on the resources or stacks they apply to so auditors and security teams can see where rules were waived and why. A healthy exception rate is low and shrinking. A rising exception rate signals that a rule is wrong or missing context and needs review. 

**Important**  
 Proactive controls block deployments when they fail, which means a poorly written rule can halt the flow of changes across the organization. Test every rule against a representative corpus of real templates before enforcing it, and stage new rules in report-only mode before switching them to blocking mode. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Baseline preventive and proactive posture from your landing zone:** Inventory the controls already delivered by your landing zone before authoring new ones. [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) and [Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/) deploy a substantial set of SCPs, managed controls, and account baselines out of the box. Map these controls to your organization's compliance requirements so you can target your proactive authoring effort on the gaps rather than reimplementing what the landing zone already enforces. 

1.  **Codify organization-specific rules in a single source of truth:** Establish a version-controlled repository that holds the organization's proactive rules as code, with each rule paired to the compliance requirement it satisfies, sample templates expected to pass, sample templates expected to fail, and a clear failure message. Use [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) as the common policy language for CloudFormation and CDK-synthesized templates, and generate variants for other enforcement points (CDK Aspects, pre-commit hooks, Config proactive rules) from the same source. 

1.  **Integrate policy evaluation into delivery pipelines:** Add a policy evaluation stage to pipelines that synthesize or submit CloudFormation templates, typically as an [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) step in [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) or the equivalent in other CI systems. Fail the build when required rules fail and surface the failure message, the offending resource, and a link to the rule source in the build output. For CDK projects, adopt [cdk-nag](https://github.com/cdklabs/cdk-nag) to run rule packs during synthesis so violations surface before templates are ever produced. 

1.  **Enforce at the provisioning service with CloudFormation Hooks:** Deploy [AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) to evaluate resources at the point of stack operations, so non-compliant resources are blocked even when they bypass the pipeline. Use [Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html) to reuse your existing Guard rules as hooks without writing separate handler code. Activate hooks across the organization through [CloudFormation hook configuration at the Organizations level](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/) so a single activation covers every member account. 

1.  **Extend detective rules to proactive evaluation where supported:** For [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html) that support proactive evaluation, enable proactive mode so the same rule logic that detects non-compliant resources also evaluates resources before they are created. See [Evaluation modes for AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_components.html). With proactive mode, developers can test their templates against the same rule set that evaluates them in production, using the [StartResourceEvaluation API](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) from CI or local tooling. 

1.  **Publish curated patterns as a proactive control layer:** Make compliant-by-construction templates, modules, and [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) products the default path for common workloads, so builders consuming a vetted pattern cannot easily produce a non-compliant variant. Treat the curated pattern library as part of the proactive control surface: rule failures against a pattern must trigger a pattern update, not dozens of individual team fixes. 

1.  **Roll out new rules in report-only mode before enforcing:** Stage every new rule in a non-blocking mode first, such as pipeline warnings, hook NON\_COMPLIANT results published to [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) without blocking, or Config proactive evaluations surfaced in dashboards. Review the signal against real workloads, refine the rule, and switch to blocking mode only after the false-positive rate is acceptable and owners of any preexisting violations have been engaged. Communicate the change window clearly so teams know when report-only becomes blocking. 

1.  **Define an exception process with time bounds:** Document how teams request an exception, who approves it based on the rule's risk level, how the exception is recorded on the resource or stack (typically through a tag), and how long it remains valid before it must be re-reviewed. Track exceptions in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html) custom insights or an equivalent so rising exception volume on a specific rule surfaces as a signal that the rule needs attention. 

1.  **Measure proactive coverage and feed findings back into the rule set:** Track the proportion of compliance rules that have a proactive enforcement point, the distribution of detective findings by rule (to identify candidates for proactive enforcement), and the volume of exceptions per rule. Review the metrics on a regular cadence and use them to prioritize the next set of rules to author, tighten, or retire. Feed recurring detective findings back to the rule authors so repeated issues get upgraded into proactive controls over time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP03 Establish standard repositories of shared resources and patterns](fnd04-bp03.md) 
+  [FND05-BP06 Remediate non-compliant resources](fnd05-bp06.md) 
+  [FND05-BP08 Employ vulnerability and patch management controls](fnd05-bp08.md) 
+  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md) 
+  [SEC01-BP07 Evaluate and implement new security services and features regularly](sec01-bp07.md) 

 **Related documents:** 
+  [AWS CloudFormation Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) 
+  [AWS CloudFormation Guard User Guide](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [Evaluation modes for AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_components.html) 
+  [AWS Control Tower controls reference](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html) 
+  [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) 
+  [Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/) 

 **Related examples:** 
+  [Proactively keep resources compliant by using AWS CloudFormation Hooks and AWS CloudFormation Guard](https://aws.amazon.com/blogs/mt/proactively-keep-resources-secure-and-compliant-with-aws-cloudformation-hooks/) 
+  [Introducing AWS CloudFormation Guard 2.0](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/) 
+  [Using cdk-nag to check AWS CDK applications for compliance](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/) 
+  [Proactive compliance with AWS Config rules](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-proactive-rules-and-aws-cloudformation-hooks-to-prevent-creation-of-non-complaint-cloud-resources/) 

 **Related tools:** 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [cdk-nag](https://github.com/cdklabs/cdk-nag) 

 **Related services:** 
+  [AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 