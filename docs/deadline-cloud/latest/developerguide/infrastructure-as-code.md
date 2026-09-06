

# Manage Deadline Cloud infrastructure as code
<a name="infrastructure-as-code"></a>

You can define AWS Deadline Cloud (Deadline Cloud) farms, queues, and fleets as code. Deploy them with AWS CloudFormation (CloudFormation), the AWS Cloud Development Kit (AWS CDK), or Terraform. All three tools build on the same Deadline Cloud resource types, so they create equivalent infrastructure. Choose the tool your team already uses to manage the rest of your AWS infrastructure.

The following table compares the three tools. The sections after the table describe each tool and link to a working starter template in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples) repository on the GitHub website.


| Aspect | CloudFormation | AWS CDK | Terraform | 
| --- | --- | --- | --- | 
| Authoring | YAML or JSON template | A programming language such as TypeScript or Python, compiled to a CloudFormation template | HCL configuration | 
| Provider | AWS native | AWS native | HashiCorp AWSCC | 
| Deadline Cloud resource names | `AWS::Deadline::*` | `CfnFarm`, `CfnQueue`, `CfnFleet`, and so on | `awscc_deadline_*` | 
| State | Managed by AWS | Managed by AWS | Local or remote backend | 

## CloudFormation
<a name="infrastructure-as-code-cfn"></a>

CloudFormation provides native resource types for Deadline Cloud in the `AWS::Deadline` namespace. For the properties and return values of each resource type, see [AWS Deadline Cloud](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Deadline.html) in the *CloudFormation Template Reference*.

For working templates that deploy a complete farm, connect fleets to private VPC resources, and manage capacity, see [CloudFormation template examples for Deadline Cloud](examples-cloudformation.md).

## AWS CDK
<a name="infrastructure-as-code-cdk"></a>

With the AWS CDK, you define Deadline Cloud resources using L1 constructs, such as `CfnFarm`, `CfnQueue`, and `CfnFleet`, from the [`aws-cdk-lib/aws-deadline`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_deadline-readme.html) module. The constructs are generated from the CloudFormation resource types, and your AWS CDK app deploys as a CloudFormation stack.

For a working TypeScript app with four example farm stacks built from reusable constructs, see [Deploy Deadline Cloud farms with the AWS CDK](examples-cdk.md).

## Terraform
<a name="infrastructure-as-code-terraform"></a>

Terraform supports Deadline Cloud through the [AWS Cloud Control (AWSCC) provider](https://registry.terraform.io/providers/hashicorp/awscc/latest) on the Terraform Registry website, which exposes resources such as `awscc_deadline_farm`, `awscc_deadline_queue`, and `awscc_deadline_fleet`. The AWSCC provider is generated from the CloudFormation resource types through AWS Cloud Control API, so it covers the same resources as CloudFormation. The `hashicorp/aws` provider doesn't include Deadline Cloud resources.

For working configurations, including a starter farm equivalent to the CloudFormation and AWS CDK versions, see [Deploy Deadline Cloud farms with Terraform](examples-terraform.md).

## Resources outside your templates
<a name="infrastructure-as-code-coverage"></a>

The Deadline Cloud resource types cover farms, queues, fleets, queue environments, storage profiles, limits, license endpoints, metered products, monitors, and the associations between queues and fleets or limits. For the full list, see [AWS Deadline Cloud](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Deadline.html) in the *CloudFormation Template Reference*.

A few resources don't have resource types, so you manage them with the console, the AWS CLI, or the API after your deployment completes:
+ **Budgets** – Create budgets for your farms and queues with budget manager. For more information, see [Managing budgets and usage](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/using-budget-manager.html) in the *Deadline Cloud User Guide*.
+ **Memberships** – Grant users and groups access to farms, fleets, queues, and jobs. For more information, see [Managing users](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html) in the *Deadline Cloud User Guide*.