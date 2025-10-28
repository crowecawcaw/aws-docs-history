# Using Terraform to deploy state machines in Step Functions

[Terraform](https://www.terraform.io/intro/ "https://www.terraform.io/intro/") by HashiCorp is a framework for building applications using infrastructure as code (IaC). With Terraform, you can create state machines and use features, such as previewing infrastructure deployments and creating reusable templates. Terraform templates help you maintain and reuse the code by breaking it down into smaller chunks.

If you're familiar with Terraform, you can follow the development lifecycle described in this topic as a model for creating and deploying your state machines in Terraform. If you aren't familiar with Terraform, we recommend that you first complete the workshop [Introduction to Terraform on AWS](https://catalog.workshops.aws/terraform101/en-US "https://catalog.workshops.aws/terraform101/en-US") for getting acquainted with Terraform.

###### Tip

To deploy an example of a state machine built using Terraform, see [Deploy with Terraform](https://catalog.workshops.aws/stepfunctions/iac/deploy-with-terraform "https://catalog.workshops.aws/stepfunctions/iac/deploy-with-terraform") in _The AWS Step Functions Workshop_.

###### In this topic

- [Prerequisites](#terraform-sfn-prerequisites "#terraform-sfn-prerequisites")
- [Development lifecycle with Terraform](#terraform-sfn-dev-lifecycle "#terraform-sfn-dev-lifecycle")
- [IAM roles and policies for your state machine](#terraform-sfn-iam-policy "#terraform-sfn-iam-policy")

## Prerequisites

Before you get started, make sure you complete the following prerequisites:

- Install Terraform on your machine. For information about installing Terraform, see [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli").
- Install Step Functions Local on your machine. We recommend that you install the Step Functions Local Docker image to use Step Functions Local. For more information, see [Testing state machines with Step Functions Local (unsupported)](sfn-local.md "sfn-local.md").
- Install AWS SAM CLI. For installation information, see [Installing the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/install-sam-cli.md "../../../serverless-application-model/latest/developerguide/install-sam-cli.md") in the _AWS Serverless Application Model Developer Guide_.
- Install the AWS Toolkit for Visual Studio Code to view the workflow diagram of your state machines. For installation information, see [Installing the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md "../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md") in the _AWS Toolkit for Visual Studio Code User Guide_.

## State machine development lifecycle with Terraform

The following procedure explains how you can use a state machine prototype that you build using [Workflow Studio](workflow-studio.md "workflow-studio.md") in the Step Functions console as a starting point for local development with Terraform and the [AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md").

To view the complete example that discusses the state machine development with Terraform and presents the best practices in detail, see [Best practices for writing Step Functions Terraform projects](https://aws.amazon.com/blogs/devops/best-practices-for-writing-step-functions-terraform-projects/ "https://aws.amazon.com/blogs/devops/best-practices-for-writing-step-functions-terraform-projects/").

###### To start the development lifecycle of a state machine with Terraform

1. Bootstrap a new Terraform project with the following command.

```
terraform init
```

2. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") to create a prototype for your state machine.
3. In Workflow Studio, do the following:
   1. Create your workflow prototype.
   2. Export the [Amazon States Language (ASL)](concepts-amazon-states-language.md "concepts-amazon-states-language.md") definition of your workflow. To do this, choose the **Import/Export** dropdownlist, and then select **Export JSON definition**.

4. Save the exported ASL definition within your project directory.

You pass the exported ASL definition as an input parameter to the [`aws_sfn_state_machine`](https://registry.terraform.io/modules/terraform-aws-modules/step-functions/aws/latest "https://registry.terraform.io/modules/terraform-aws-modules/step-functions/aws/latest") Terraform resource that uses the [`templatefile`](https://developer.hashicorp.com/terraform/language/functions/templatefile "https://developer.hashicorp.com/terraform/language/functions/templatefile") function. This function is used inside the definition field that passes the exported ASL definition and any variable substitutions.

###### Tip

Because the ASL definition file can contain lengthy blocks of text, we recommend you avoid the inline EOF method. This makes it easier to substitute parameters into your state machine definition. 5. (Optional) Update the ASL definition within your IDE and visualize your changes using the AWS Toolkit for Visual Studio Code.

![Screenshot of the ASL definition of a workflow in Visual Studio Code and its visual representation.](images/visualize-sm-terraform-iac.png)

To avoid continuously exporting your definition and refactoring it into your project, we recommend that you make updates locally in you IDE and track these updates with [Git](https://git-scm.com/ "https://git-scm.com/"). 6. Test your workflow using [Step Functions Local](sfn-local.md "sfn-local.md").

###### Tip

You can also locally test service integrations with Lambda functions and API Gateway APIs in your state machine using [AWS SAM CLI Local](sfn-local-lambda.md "sfn-local-lambda.md"). 7. Preview your state machine and other AWS resources before deploying the state machine. To do this, run the following command.

```
terraform plan
```

8. Deploy your state machine from your local environment or through [CI/CD pipelines](https://aws.amazon.com/blogs/developer/build-infrastructure-ci-for-terraform-code-leveraging-aws-developer-tools-and-terratest/ "https://aws.amazon.com/blogs/developer/build-infrastructure-ci-for-terraform-code-leveraging-aws-developer-tools-and-terratest/") using the following command.

```
terraform apply
```

9. (Optional) Clean up your resources and delete the state machine using the following command.

```
terraform destroy
```

## IAM roles and policies for your state machine

Use the [Terraform service integration policies](https://registry.terraform.io/modules/terraform-aws-modules/step-functions/aws/latest#service-integration-policies "https://registry.terraform.io/modules/terraform-aws-modules/step-functions/aws/latest#service-integration-policies") to add necessary IAM permissions to your state machine, for example, permission to invoke Lambda functions. You can also define explicit roles and policies and associate them with your state machine.

The following IAM policy example grants your state machine access to invoke a Lambda function named `myFunction`.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`myFunction`"
 }
 ]
}`

```

We also recommend using the [`aws_iam_policy_document`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document") data source when defining IAM policies for your state machines in Terraform. This helps you check if your policy is malformed and substitute any resources with variables.

The following IAM policy example uses the `aws_iam_policy_document` data source and grants your state machine access to invoke a Lambda function named `myFunction`.

```
data "aws_iam_policy_document" "state_machine_role_policy" {

  statement {
    effect = "Allow"

    actions = [
      "lambda:InvokeFunction"
    ]

    resources = ["${aws_lambda_function.`function-1`.arn}:*"]
  }

}
```

###### Tip

To view more advanced AWS architectural patterns deployed with Terraform, see [Terraform examples at Serverless Land Workflows Collection](https://serverlessland.com/workflows?framework=Terraform "https://serverlessland.com/workflows?framework=Terraform").
