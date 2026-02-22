# [DL.EAC.6] Use general-purpose programming languages to generate Infrastructure-as-Code

**Category:** RECOMMENDED

Developing infrastructure as code (IaC) using general-purpose programming languages
aligns closely with modern software development practices and DevOps principles. IaC has
traditionally been implemented as predefined templates modeled through domain-specific
languages using markup languages like JSON or YAML. During deployment, these templates are
provided parameters which specify environment-specific details. While parameterized
templates are still a best practice for traditional IaC templates, this approach can
become difficult to develop, troubleshoot, and manage as infrastructure and environments
become more complex.

Using general-purpose programming languages changes how we develop, manage, and
deploy IaC. It is no longer a collection of parameterized templates, but instead
infrastructure is written in common programming languages such as TypeScript, Python, or
Java, and can be treated the same as other code throughout the development lifecycle.
Instead of providing environment-specific configuration during deployment, tools
like [AWS Cloud Development Kit (AWS CDK)](../../../cdk/v2/guide/best-practices.md#best-practices-apps-stages "../../../cdk/v2/guide/best-practices.md#best-practices-apps-stages")
generate separate templates for each environment using configurations defined in source
code. This provides a more predictable, consistent, and reproducible deployment process.

Transitioning to using general-purpose programming languages
for IaC can also change how you govern IaC at scale. For
example, AWS CDK includes the ability to consume, publish, and
version software components called AWS CDK
[constructs](../../../cdk/v2/guide/constructs.md "../../../cdk/v2/guide/constructs.md")
through private artifact registries or the
open-source [Construct
Hub](https://constructs.dev/ "https://constructs.dev/") registry.

**Related information:**

- [Best
  practices for developing and deploying cloud
  infrastructure with the AWS CDK](../../../cdk/v2/guide/best-practices.md "../../../cdk/v2/guide/best-practices.md")
- [CDK
  for Terraform (CDKtf)](https://www.terraform.io/docs/cdktf/index.html "https://www.terraform.io/docs/cdktf/index.html")
- [CDK for Kubernetes
  (CDK8s)](https://cdk8s.io/ "https://cdk8s.io/")
- [AWS Solutions Constructs](../../../solutions/latest/constructs/welcome.md "../../../solutions/latest/constructs/welcome.md")
- [Artifact
  Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/ "https://aws.amazon.com/codeartifact/")
- [Infrastructure
  IS Code with the AWS CDK](https://www.youtube.com/watch?v=Lh-kVC2r2AU "https://www.youtube.com/watch?v=Lh-kVC2r2AU")
- [Best
  practices for using the AWS CDK in TypeScript to create
  IaC projects](../../../prescriptive-guidance/latest/best-practices-cdk-typescript-iac/introduction.md "../../../prescriptive-guidance/latest/best-practices-cdk-typescript-iac/introduction.md")
- [Adding
  the "AWS CDK bootstrap" action in Amazon CodeCatalyst](../../../codecatalyst/latest/userguide/cdk-boot-action.md "../../../codecatalyst/latest/userguide/cdk-boot-action.md")
