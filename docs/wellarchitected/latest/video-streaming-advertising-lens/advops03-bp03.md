

# ADVOPS03-BP03 Design publisher workloads to reduce defects and improve flow

 Design Prebid, SGAI, FAST channel, and ad format workloads to minimize defects through automated testing, configuration validation, and progressive delivery. Treat all workload configurations as code. Use version control, automated linting, and integration testing to prevent configuration errors from reaching production. 

 **Desired outcome:** 
+  All publisher workload configurations (Prebid adapters, SGAI manifest templates, FAST channel schedules) are managed in version-controlled repositories with automated validation gates. 
+  Pre-deployment validation catches configuration errors before they reach production, including SCTE-35 marker schema validation for SGAI and EPG schedule completeness checks for FAST channels. 
+  Integration test suites validate behavior across the full pipeline in staging before production deployment. 

 **Common anti-patterns:** 
+  Manually editing Prebid adapter configurations without version control, making it impossible to audit what changed when a fill rate drop coincides with a configuration update. 
+  Deploying SGAI manifest generation changes without schema validation. SCTE-35 marker formatting errors that pass staging may fail in production for specific message types. 
+  Lacking automated integration tests for publisher workload changes, discovering defects only after production impact. 
+  Not treating FAST channel schedule files as code subject to validation. Schedule gaps and missing asset references are discovered at broadcast time rather than during pre-validation. 

 **Benefits of establishing this best practice:** 
+  Reduced production defect frequency. 
+  Faster feedback on configuration quality through automated validation at commit time. 
+  Improved flow of changes into production through validated, automated pipelines. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Configuration files for advertising workloads are code. They have the same ability to break production systems as application code changes. However, they often receive less engineering rigor. For example, adapter configuration updates may be made directly through an operations UI without version control, SGAI manifest templates may be edited in place without testing, and FAST channel schedule files may be uploaded without validation. 

 Apply infrastructure as code practices to advertising configuration to give changes the same rigor as application code. Version control captures who changed what and when to identify the configuration change that caused a fill rate drop. Automated linting validates syntax, required fields, and constraint conformance before the change is committed, removing errors that would otherwise appear in production only under specific traffic or content conditions. Integration tests validate behavior across the full pipeline in a staging environment that mirrors production, catching semantic errors that linting can't detect. 

 For Prebid Server, automated linting must validate that timeout thresholds fall within acceptable ranges, that required parameters for each adapter type are present and correctly formatted, and that identity-signal parameters (UID2 endpoint URLs, LiveRamp account configuration) are specified. For SGAI, SCTE-35 schema validation must cover all message types used in the deployment (spliceinsert, timesignal, splicenull, and privatecommand) with type-specific validation rules for each. For FAST channel schedules, EPG completeness checks must verify that all time slots have assigned content, referenced asset IDs exist in the content origin, and asset durations match their scheduled slot durations. 

 AWS CodePipeline orchestrates automated validation gates as pipeline stages, so no change proceeds to the next stage without passing validation. AWS Config rules detect configuration drift between the deployed state and the version-controlled source of truth, and alert when manual changes cause drift. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Migrate all publisher workload configurations to version-controlled repositories:** Move Prebid adapter configurations, SGAI manifest templates, and FAST channel schedule files from operational UIs and shared drives into Git repositories. Require pull request review for all configuration changes. Add .gitignore entries for any auto-generated files that should not be tracked. This creates the audit trail that enables rapid identification of configuration changes correlated with production incidents. 

1.  **Implement automated linting and schema validation as pipeline gates:** Create AWS CodePipeline stages that run linting and schema validation on configuration changes before deployment. For Prebid adapters, use JSON Schema validation against adapter-specific schemas. For SGAI manifest templates, implement SCTE-35 schema validation covering all message types used in the deployment. For FAST channel schedules, implement EPG completeness validation using a Lambda function that checks asset availability and slot coverage. 

1.  **Build integration test suites for staging validation:** Create integration tests that validate behavior across the full pipeline for each configuration change type in a staging environment that mirrors production. For Prebid adapter changes, run a 15-minute auction simulation and verify that the modified adapter's bid response rate, latency, and response format meet requirements. For SGAI changes, run a synthetic live stream through the updated manifest generation pipeline and validate SCTE-35 marker output. For FAST channel schedule changes, validate that all referenced assets are accessible and that no scheduling gaps exist. 

1.  **Configure AWS Config rules for configuration drift detection:** Create AWS Config rules that compare deployed Prebid adapter configurations, SGAI manifest templates, and FAST channel schedule files against the version-controlled source of truth in your Git repository. Configure rules to evaluate on configuration change and notify through SNS when drift is detected. This catches manual emergency changes that bypass the validated pipeline so they are captured for review. 

1.  **Establish feedback loops from production defects to validation coverage:** After each production defect caused by a configuration error, add a new validation rule to the pipeline that would have caught the defect. Track validation coverage metrics: the number of defect classes covered by automated validation compared to the total classes observed in production. Report this metric in the monthly operational health review as a leading indicator of defect frequency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS03-BP01 Mitigate deployment risks for publisher workload changes](advops03-bp01.md) 

 **Related documents:** 
+  [AWS Config rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html) 
+  [AWS CodePipeline automated validation](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html) 
+  [ANSI/SCTE 35 specification reference](https://www.scte.org/standards/library/catalog/scte-35-digital-program-insertion-cueing-message/) 

 **Related services:** 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS Config](https://aws.amazon.com/config/) 