# GENOPS04-BP01 Automate generative AI application lifecycle with

infrastructure as code (IaC)

Implementing and managing IaC is crucial for consistent,
version-controlled, and automated infrastructure deployment across
environments. This practice streamlines deployment, reduces errors,
and enhances team collaboration. IaC helps customers achieve
efficiency, reliability, and scalability in infrastructure
management, which allows for rapid iteration, straightforward
rollback, and improved governance and results in secure deployments
aligned with compliance standards.

**Desired outcome:** After
implementing the practice of automating the lifecycle management of
generative AI workloads using IaC, customers have version control
infrastructure automated through CI/CD pipelines.

**Benefits of establishing this best
practice:**
[Safely
automate where possible](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Define your entire workload and its
operations (applications, infrastructure, configuration, and
procedures) as code, facilitating infrastructure level change
management, infrastructure version control, and advanced paradigms
such as self-healing infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Automate your application development and migration through stages
using IaC principles. When selecting your tool stack, consider
your team's skills and project requirements. Use tools such as AWS Cloud Development Kit (AWS CDK), AWS CloudFormation, or Terraform
to define and manage the infrastructure resources required for
your application. These resources may include Amazon Bedrock,
Amazon API Gateway, AWS Lambda functions, and AWS Data Pipelines, all of which help you create a reproducible and
version-controlled stack.

Store your IaC templates in a version control system like Git.
This practice facilitates collaboration among team members, allows
for tracking changes over time, and enables rolling back to
previous versions if necessary.

Implement a CI/CD pipeline using AWS CodePipeline, Jenkins, or a
similar tool. This pipeline should initiate on code changes, run
tests on your IaC templates, and automatically deploy
infrastructure changes.

Manage your IaC templates to handle multiple environments such as
development, testing and staging, and production. To maintain
consistency across environments, use the same templates with
different parameters.

Establish practices and controls to help you maintain compliance
of your resources, like using AWS Config to track resource
configurations. Implement Service Catalog for standardized
resource provisioning, and regularly audit your IaC templates for
security best practices and compliance.

### Implementation steps

1. Select your IaC tool stack.
   - Evaluate AWS CDK, AWS CloudFormation, or Terraform
   - Consider team skills and project needs
   - Assess learning curve and maintainability

2. Define your infrastructure resources.
   - Include each component, such as Amazon Bedrock, Amazon API Gateway, AWS Lambda, and AWS Data Pipelines
   - Create reproducible, version-controlled stacks
   - Use modular design for reusability

3. Version control your IaC templates.
   - Use a code repository Git tool
   - Implement branching strategy aligned with environments

4. Implement a CI/CD pipeline.
   - Consider AWS CodePipeline or Jenkins for orchestration
   - Configure initiation events for code changes
   - Set up automated testing for IaC templates
   - Enable automatic deployment of changes
   - Implement approval gates for production deployments

5. Manage multiple environments.
   - Use the same templates with different parameters for
     development, test, and production
   - Implement environment-specific security controls

6. Establish governance and compliance.
   - Use AWS Config for tracking resource configurations and
     automate remediations
   - Implement Service Catalog for standardized
     provisioning
   - Set up automated compliance checks and reporting

7. Regularly audit your IaC templates.
   - Focus on security best practices
   - Conduct periodic third-party security assessments

## Resources

**Related practices:**

- [OPS05-BP10](../framework/ops_dev_integ_auto_integ_deploy.md "../framework/ops_dev_integ_auto_integ_deploy.md")
- [OPS06-BP03](../framework/ops_mit_deploy_risks_deploy_mgmt_sys.md "../framework/ops_mit_deploy_risks_deploy_mgmt_sys.md")
- [OPS06-BP04](../framework/ops_mit_deploy_risks_auto_testing_and_rollback.md "../framework/ops_mit_deploy_risks_auto_testing_and_rollback.md")
- [OPS05-BP08](../framework/ops_dev_integ_multi_env.md "../framework/ops_dev_integ_multi_env.md")
- [OPS05-BP01](../framework/ops_dev_integ_version_control.md "../framework/ops_dev_integ_version_control.md")

**Related guides, videos, and documentation:**

- [Operationalize
  generative AI applications on AWS](https://aws.amazon.com/blogs/gametech/operationalize-generative-ai-applications-on-aws-part-ii-architecture-deep-dive/ "https://aws.amazon.com/blogs/gametech/operationalize-generative-ai-applications-on-aws-part-ii-architecture-deep-dive/")
- [AWS CloudFormation Amazon Bedrock resources](../../../bedrock/latest/userguide/creating-resources-with-cloudformation.md "../../../bedrock/latest/userguide/creating-resources-with-cloudformation.md")
- [AWS re:Invent 2024 - Generative AI in action: From prototype to
  production (AIM276)](https://www.youtube.com/watch?v=aFQFiVOh3P0 "https://www.youtube.com/watch?v=aFQFiVOh3P0")

**Related examples:**

- [Walkthrough:
  Building a pipeline for test and production stacks](../../../AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.md "../../../AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.md")
- [AWS CDK Examples](https://github.com/aws-samples/aws-cdk-examples "https://github.com/aws-samples/aws-cdk-examples")
- [AWS CDK Developer Guide](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")
- [Terraform
  AWS Provider Examples](https://github.com/terraform-providers/terraform-provider-aws/tree/main/examples "https://github.com/terraform-providers/terraform-provider-aws/tree/main/examples")
- [Amazon SageMaker AI model endpoint creation with CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.md#aws-resource-sagemaker-model--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.md#aws-resource-sagemaker-model--examples")

**Related tools:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
