# Set up Amazon Managed Service for Prometheus with AWS Observability Accelerator

AWS provides observability tools, including monitoring, logging, alerting, and
dashboards, for your Amazon Elastic Kubernetes Service (Amazon EKS) projects. This includes Amazon Managed Service for Prometheus, [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md"), [AWS Distro for
OpenTelemetry](https://aws-otel.github.io/ "https://aws-otel.github.io/"), and other tools. To help you use these tools together, AWS
provides Terraform modules that configure observability with these services, called the
[AWS Observability Accelerator](https://github.com/aws-observability/terraform-aws-observability-accelerator "https://github.com/aws-observability/terraform-aws-observability-accelerator").

AWS Observability Accelerator provides examples for monitoring infrastructure, [NGINX](https://nginx.org/en/ "https://nginx.org/en/") deployements, and other scenarios. This
section gives an example of monitoring infrastructure within your Amazon EKS cluster.

The Terraform templates and detailed instructions can be found on the [AWS Observability Accelerator for Terraform GitHub page](https://github.com/aws-observability/terraform-aws-observability-accelerator "https://github.com/aws-observability/terraform-aws-observability-accelerator"). You can also read the [blog post announcing AWS Observability Accelerator](https://aws.amazon.com/blogs/mt/announcing-aws-observability-accelerator-to-configure-comprehensive-observability-for-amazon-eks/ "https://aws.amazon.com/blogs/mt/announcing-aws-observability-accelerator-to-configure-comprehensive-observability-for-amazon-eks/").

## Prerequisites

To use AWS Observability Accelerator, you must have an existing Amazon EKS cluster, and the following
prerequisites:

- [AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – used to call AWS functionality from the command line.
- [kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/") –
  used to control your EKS cluster from the command line.
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli "https://learn.hashicorp.com/tutorials/terraform/install-cli") – used to automate creation of the resources for
  this solution. You must have the AWS provider setup with an IAM role that
  has access to create and manage Amazon Managed Service for Prometheus, Amazon Managed Grafana, and IAM within your
  AWS account. For more information about how to configure the AWS provider
  for Terraform, see [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs "https://registry.terraform.io/providers/hashicorp/aws/latest/docs") in the _Terraform
  documentation_.

## Using the infrastructure monitoring example

AWS Observability Accelerator provides example templates that use the included Terraform modules to set
up and configure observability for your Amazon EKS cluster. This example demonstrates using
AWS Observability Accelerator to set up infrastructure monitoring. For more details about using this
template and additional capabilities that it includes, see [Existing Cluster with the AWS Observability Accelerator base and Infrastructure monitoring](https://github.com/aws-observability/terraform-aws-observability-accelerator/tree/main/examples/existing-cluster-with-base-and-infra "https://github.com/aws-observability/terraform-aws-observability-accelerator/tree/main/examples/existing-cluster-with-base-and-infra")
page on GitHub.

###### To use the infrastructure monitoring Terraform module

1. From the folder you want to create your project in, clone the repo using the
   following command.

```
git clone https://github.com/aws-observability/terraform-aws-observability-accelerator.git
```

2. Initialize Terraform with the following commands.

```
cd examples/existing-cluster-with-base-and-infra

terraform init
```

3. Create a new `terraform.tfvars` file, as in the following example.
   Use the AWS Region and cluster ID for your Amazon EKS cluster.

```
# (mandatory) AWS Region where your resources will be located
aws_region = "`eu-west-1`"

# (mandatory) EKS Cluster name
eks_cluster_id = "`my-eks-cluster`"
```

4. Create an Amazon Managed Grafana workspace, if you don't already have one that you want to
   use. For information about how to create a new workspace, see [Create your first workspace](../../../grafana/latest/userguide/getting-started-with-AMG.md#AMG-getting-started-workspace-create "../../../grafana/latest/userguide/getting-started-with-AMG.md#AMG-getting-started-workspace-create") in the _Amazon Managed Grafana User
   Guide._
5. Create two variables for Terraform to use your Grafana workspace by running
   the following commands at the command line. You will need to replace the
   `grafana-workspace-id` with the ID from your
   Grafana workspace.

```
export TF_VAR_managed_grafana_workspace_id=`grafana-workspace-id`
export TF_VAR_grafana_api_key=`aws grafana create-workspace-api-key --key-name "observability-accelerator-$(date +%s)" --key-role ADMIN --seconds-to-live 1200 --workspace-id $TF_VAR_managed_grafana_workspace_id --query key --output text`
```

6. [Optional] To use an existing Amazon Managed Service for Prometheus workspace, add the ID to the
   `terraform.tfvars` file, as in the following example, replacing
   the `prometheus-workspace-id` with your Prometheus
   workspace ID. If you do not specify an existing workspace, then a new Prometheus
   workspace will be created for you.

```
# (optional) Leave it empty for a new workspace to be created
managed_prometheus_workspace_id = "`prometheus-workspace-id`"
```

7. Deploy the solution with the following command.

```
terraform apply -var-file=terraform.tfvars
```

This will create resources in your AWS account, including the following:

- A new Amazon Managed Service for Prometheus workspace (unless you opted to use an existing
  workspace).
- Alert manager configuration, alerts, and rules in your Prometheus
  workspace.
- New Amazon Managed Grafana data source and dashboards in your current workspace. The data
  source will be called `aws-observability-accelerator`. The dashboards
  will be listed under **Observability Accelerator
  Dashboards**.
- An [AWS Distro for
  OpenTelemetry](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/") operator set up in the provided Amazon EKS cluster, to send
  metrics to your Amazon Managed Service for Prometheus workspace.

To view your new dashboards, open the specific dashboard in your Amazon Managed Grafana workspace.
For more information about using Amazon Managed Grafana, see [Working in
your Grafana workspace](../../../grafana/latest/userguide/AMG-working-with-Grafana-workspace.md "../../../grafana/latest/userguide/AMG-working-with-Grafana-workspace.md"), in the _Amazon Managed Grafana User
Guide_.
