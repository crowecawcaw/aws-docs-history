# LSOPS04-BP02 Enforce controls in IT tooling and

automation

Implement quality controls and automation in the standard IT
tooling used by the development teams whenever possible to enable
continuous validation.

**Desired outcome:**

- Automated enforcement of quality and regulatory controls within
  development workflows.
- Reduced manual oversight burden while maintaining regulatory
  adherence.
- Early detection of regulatory issues during the development
  process.

**Common anti-patterns:**

- Relying primarily on manual reviews and approvals for
  verification.
- Inconsistent application of controls across different teams or
  environments.
- Adding audit checks only at the end of development cycles.

**Benefits of establishing this best
practice:**

- Increased development velocity through automated audit
  verification.
- Improved quality through consistent application of controls.
- Greater scalability of processes across growing organizations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Identify key control points in your development and operational
processes where automated verification can replace manual checks.
Implement infrastructure as code templates with pre-validated
configurations, automated testing for regulatory requirements, and
continuous monitoring for drift from approved baselines. These
automated controls should generate appropriate evidence for audit
purposes while remaining transparent to developers.

Consider an automated approach where you translate regulatory
requirements into automated tests and policies. This allows teams
to validate adherence continuously throughout the development
lifecycle rather than as a separate activity. When properly
implemented, automated controls can provide greater assurance than
manual processes while reducing the compliance burden on teams.

### Implementation steps

1. Identify key control points in development and operational
   workflows:

- Use AWS Glue Data Quality for data pipelines.

1. Integrate automated testing into CI/CD pipelines:

- Use AWS CodePipeline with validation gates.
- Use AWS CodeBuild for running automated tests.

1. Deploy continuous monitoring solutions for configuration
   drift:

- Use AWS Config Rules to detect non-compliant resources.
- Use Amazon EventBridge for automated remediation of issues.

## Resources

**Related documents:**

- [Compliance
  and Auditing](https://aws.amazon.com/cloudops/compliance-and-auditing/ "https://aws.amazon.com/cloudops/compliance-and-auditing/")

**Related examples:**

- [Measure
  performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/ "https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/")

**Related tools:**

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/ "https://aws.amazon.com/glue/features/data-quality/")
