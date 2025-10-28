# SEC11-BP07 Regularly assess security properties of the

pipelines

Apply the principles of the Well-Architected Security Pillar to
your pipelines, with particular attention to the separation of
permissions. Regularly assess the security properties of your
pipeline infrastructure. Effectively managing the security
_of_ the pipelines allows you to deliver the
security of the software that passes _through_
the pipelines.

**Desired outcome:** The pipelines
you use to build and deploy your software follow the same
recommended practices as any other workload in your environment. The
tests that you implement in your pipelines are not editable by the
teams who use them. You give the pipelines only the permissions
needed for the deployments they are doing using temporary
credentials. You implement safeguards to prevent pipelines from
deploying to the wrong environments. You configure your pipelines to
emit state so that the integrity of your build environments can be
validated.

**Common anti-patterns:**

- Security tests that can be bypassed by builders.
- Overly broad permissions for deployment pipelines.
- Pipelines not being configured to validate inputs.
- Not regularly reviewing the permissions associated with your
  CI/CD infrastructure.
- Use of long-term or hardcoded credentials.
  **Benefits of establishing this best practice:**

- Greater confidence in the integrity of the software that is
  built and deployed through the pipelines.
- Ability to stop a deployment when there is suspicious
  activity.
  **Level of risk exposed if this best practice is not
  established:** High

## Implementation guidance

Your deployment pipelines are a critical component of your
software development lifecycle and should follow the same security
principles and practices as any other workload in your
environment. This includes implementing proper access controls,
validating inputs, and regularly reviewing and auditing the
permissions associated with your CI/CD infrastructure.

Verify that the teams responsible for building and deploying
applications do not have the ability to edit or bypass the
security tests and checks implemented in your pipelines. This
separation of concerns helps maintain the integrity of your build
and deployment processes.

As a starting point, consider employing the
[AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/ "https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/"). This reference
architecture provides a secure and scalable foundation for
building your CI/CD pipelines on AWS.

Additionally, you can use services like
[AWS Identity and Access Management Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to generate least-privilege IAM
policies for both your pipeline permissions and as a step in your
pipeline to verify workload permissions. This helps verify that
your pipelines and workloads have only the necessary permissions
required for their specific functions, which reduces the risk of
unauthorized access or actions.

### Implementation steps

- Start with the
  [AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/ "https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/").
- Consider using
  [AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to programmatically generate
  least privilege IAM policies for the pipelines.
- Integrate your pipelines with monitoring and alerting so
  that you are notified of unexpected or abnormal activity,
  for AWS managed services
  [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") allows you to route data to targets such
  as [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") or
  [Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") (Amazon SNS).

## Resources

**Related documents:**

- [AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/ "https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/")
- [Monitoring
  AWS CodePipeline](../../../codepipeline/latest/userguide/monitoring.md "../../../codepipeline/latest/userguide/monitoring.md")
- [Security
  best practices for AWS CodePipeline](../../../codepipeline/latest/userguide/security-best-practices.md "../../../codepipeline/latest/userguide/security-best-practices.md")

**Related examples:**

- [DevOps
  monitoring dashboard](https://github.com/aws-solutions/aws-devops-monitoring-dashboard "https://github.com/aws-solutions/aws-devops-monitoring-dashboard") (GitHub)
