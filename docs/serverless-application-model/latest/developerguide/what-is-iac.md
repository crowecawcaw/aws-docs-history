# Infrastructure as Code (IaC)

With Infrastructure as Code (IaC), you can automate the deployment and management of your AWS resources, including serverless applications. IaC allows you to define your infrastructure using code, making it easier to version, share, and replicate your deployments. This approach helps you:

- Speed up your development cycle
- Simplify configuration management
- Improve reliability and consistency of your deployments

## IaC tools for AWS serverless applications

AWS offers several IaC tools to help you build, deploy, and manage your cloud resources. This section explains how AWS SAM fits within this ecosystem and works with other AWS IaC tools.

**AWS CloudFormation**

Using [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/"), you can model and provision your entire AWS infrastructure with YAML or JSON templates. AWS CloudFormation handles resource creation, updates, and deletion automatically. When you deploy AWS SAM applications, AWS CloudFormation processes the transformed templates to create and manage your resources.

**AWS Serverless Application Model (AWS SAM)**

AWS SAM helps you build serverless applications with simplified syntax for defining serverless resources. You can use AWS SAM templates to provision Lambda functions, APIs, databases, and event sources using concise YAML syntax. AWS SAM transforms these templates into AWS CloudFormation templates during deployment.

###### Note

While AWS SAM specializes in serverless applications, you can use any AWS CloudFormation resource types in your AWS SAM templates. This gives you the flexibility to include non-serverless resources when needed.

**AWS Cloud Development Kit (AWS CDK)**

With [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/"), you can define your serverless infrastructure using familiar programming languages like TypeScript, Python, Java, C#/.Net, or Go. You can use programming constructs such as loops and conditions to define your infrastructure, and AWS CDK generates AWS CloudFormation templates for deployment. You can use the AWS SAM CLI to locally test and debug applications created with AWS CDK.
To learn more, see [Testing CDK applications locally](../../../cdk/v2/guide/testing-locally.md "../../../cdk/v2/guide/testing-locally.md").

## Comparing IaC tools for Serverless Applications

When choosing an IaC tool for your serverless applications, consider your team's preferences, project requirements, and existing workflows. The following table compares the key characteristics of AWS IaC tools for serverless development:

| **Tool**               | **Primary use**                                       | **Best for**                                             | **Works with AWS SAM**                                                          | **When to choose**                                                                                                          |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **AWS CloudFormation** | Managing complex AWS infrastructure                   | Applications requiring detailed control of AWS resources | AWS SAM templates transform into AWS CloudFormation templates during deployment | For fine-grained control over non-serverless resources                                                                      |
| **AWS SAM**            | Serverless application development                    | Teams building serverless applications using Lambda      | Native functionality                                                            | When focusing primarily on serverless architectures with Lambda functions, API Gateway APIs, and other serverless resources |
| **AWS CDK**            | Infrastructure definition using programming languages | Teams preferring typed languages and code-first approach | Generate AWS SAM templates and use AWS SAM CLI for testing                      | When you need programmatic infrastructure definition or complex resource configuration logic                                |

###### Note

While this guide focuses on AWS-native IaC tools, Terraform is another popular IaC solution that can be used to define serverless applications. The AWS SAM CLI supports local testing of Lambda functions defined in Terraform. For more information, see [AWS SAM CLI Terraform support](terraform-support.md "terraform-support.md").

## Learn more

- To learn more about DevOps practices on AWS, see [Introduction to DevOps on AWS](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- For information about using Lambda with different IaC tools, see [Using Lambda with infrastructure as code (IaC)](../../../lambda/latest/dg/foundation-iac.md "../../../lambda/latest/dg/foundation-iac.md")
