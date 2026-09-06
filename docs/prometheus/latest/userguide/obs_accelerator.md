

# Set up Amazon Managed Service for Prometheus with AWS Observability Accelerator
<a name="obs_accelerator"></a>

AWS provides observability tools, including monitoring, logging, alerting, and dashboards, for your Amazon Elastic Kubernetes Service (Amazon EKS) projects. This includes Amazon Managed Service for Prometheus, [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html), [AWS Distro for OpenTelemetry](https://aws-otel.github.io/), and other tools. To help you use these tools together, AWS provides Terraform modules that configure observability with these services, called the [AWS Observability Accelerator](https://github.com/aws-observability/terraform-aws-observability-accelerator).

AWS Observability Accelerator provides two collector profiles for Amazon Managed Service for Prometheus:
+ **Managed metrics (agentless)** – Uses the [Amazon Managed Service for Prometheus collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector.html), a fully managed, agentless scraper that runs outside your cluster. No collector pods to manage. Metrics only.
+ **Self-managed** – Deploys an OpenTelemetry Collector via Helm in your cluster. Supports metrics, traces (AWS X-Ray), and logs (Amazon CloudWatch).

This section walks through both options, starting with the recommended agentless approach.

The Terraform templates and detailed instructions can be found on the [AWS Observability Accelerator for Terraform GitHub page](https://github.com/aws-observability/terraform-aws-observability-accelerator).

## Prerequisites
<a name="obs-accelerator-prereq"></a>

To use AWS Observability Accelerator, you must have an existing Amazon EKS cluster, and the following prerequisites:
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) – used to call AWS functionality from the command line.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/) – used to control your EKS cluster from the command line.
+ [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (>= 1.5.0) – used to automate creation of the resources for this solution. You must have the AWS provider set up with an IAM role that has access to create and manage Amazon Managed Service for Prometheus, Amazon Managed Grafana, and IAM within your AWS account. For more information about how to configure the AWS provider for Terraform, see [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) in the *Terraform documentation*.

## Using the managed metrics (agentless) example
<a name="obs-accelerator-managed-metrics"></a>

This example uses the Amazon Managed Service for Prometheus collector to scrape Prometheus metrics from your Amazon EKS cluster without deploying any collector pods. The collector requires at least two subnets in two distinct Availability Zones. For more details, see the [eks-amp-managed](https://github.com/aws-observability/terraform-aws-observability-accelerator/tree/main/examples/eks-amp-managed) example on GitHub.

**To use the agentless infrastructure monitoring Terraform module**

1. From the folder you want to create your project in, clone the repo using the following command.

   ```
   git clone https://github.com/aws-observability/terraform-aws-observability-accelerator.git
   ```

1. Initialize Terraform with the following commands.

   ```
   cd examples/eks-amp-managed
   
   terraform init
   ```

1. Create a new `terraform.tfvars` file, as in the following example. Use the AWS Region, cluster ID, and VPC networking details for your Amazon EKS cluster. The collector requires at least two subnets in two distinct Availability Zones.

   ```
   # (mandatory) AWS Region where your resources will be located
   aws_region = "{{eu-west-1}}"
   
   # (mandatory) EKS Cluster name
   eks_cluster_id = "{{my-eks-cluster}}"
   
   # (mandatory) Subnets for the managed scraper (>= 2 AZs)
   scraper_subnet_ids = ["{{subnet-aaa}}", "{{subnet-bbb}}"]
   
   # (mandatory) Security group allowing scraper access to the EKS API
   scraper_security_group_ids = ["{{sg-xxx}}"]
   ```

1. Create an Amazon Managed Grafana workspace, if you don't already have one that you want to use. For information about how to create a new workspace, see [Create your first workspace](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html#AMG-getting-started-workspace-create) in the *Amazon Managed Grafana User Guide.*

1. Create two variables for Terraform to use your Grafana workspace by running the following commands at the command line. You will need to replace the {{grafana-workspace-id}} with the ID from your Grafana workspace.

   ```
   export TF_VAR_managed_grafana_workspace_id={{grafana-workspace-id}}
   export TF_VAR_grafana_api_key=`aws grafana create-workspace-api-key --key-name "observability-accelerator-$(date +%s)" --key-role ADMIN --seconds-to-live 1200 --workspace-id $TF_VAR_managed_grafana_workspace_id --query key --output text`
   ```

1. [Optional] To use an existing Amazon Managed Service for Prometheus workspace, add the ID to the `terraform.tfvars` file, as in the following example, replacing the {{prometheus-workspace-id}} with your Prometheus workspace ID. If you do not specify an existing workspace, then a new Prometheus workspace will be created for you.

   ```
   # (optional) Leave it empty for a new workspace to be created
   managed_prometheus_workspace_id = "{{prometheus-workspace-id}}"
   ```

1. Deploy the solution with the following command.

   ```
   terraform apply -var-file=terraform.tfvars
   ```

This will create resources in your AWS account, including the following:
+ A new Amazon Managed Service for Prometheus workspace (unless you opted to use an existing workspace).
+ An Amazon Managed Service for Prometheus collector (agentless scraper) configured to scrape Prometheus metrics from your Amazon EKS cluster.
+ Prometheus recording and alerting rules in your Amazon Managed Service for Prometheus workspace.
+ kube-state-metrics and node-exporter deployed in your Amazon EKS cluster for infrastructure metrics.
+ New Amazon Managed Grafana data source and dashboards in your current workspace. The dashboards will be listed under **EKS Monitoring**.

## Alternative: Self-managed OpenTelemetry Collector
<a name="obs-accelerator-self-managed"></a>

If you need traces, logs, or full control over the collection pipeline, use the self-managed profile. This deploys an OpenTelemetry Collector via Helm in your Amazon EKS cluster, configured to scrape Prometheus metrics and remote-write to Amazon Managed Service for Prometheus. It also supports traces (AWS X-Ray) and logs (Amazon CloudWatch). For more details, see the [eks-amp-otel](https://github.com/aws-observability/terraform-aws-observability-accelerator/tree/main/examples/eks-amp-otel) example on GitHub.

**To use the self-managed Terraform module**

1. Clone the repo and initialize Terraform.

   ```
   git clone https://github.com/aws-observability/terraform-aws-observability-accelerator.git
   cd examples/eks-amp-otel
   terraform init
   ```

1. Create a new `terraform.tfvars` file, as in the following example.

   ```
   # (mandatory) AWS Region where your resources will be located
   aws_region = "{{eu-west-1}}"
   
   # (mandatory) EKS Cluster name
   eks_cluster_id = "{{my-eks-cluster}}"
   ```

1. Set up your Amazon Managed Grafana workspace and API key using the same steps as the managed metrics example (steps 4–6 above).

1. Deploy the solution with the following command.

   ```
   terraform apply -var-file=terraform.tfvars
   ```

This will create the following resources in your AWS account (unlike the agentless approach, the collector runs inside your cluster):
+ An Amazon Managed Service for Prometheus workspace (if not provided).
+ An Amazon Managed Grafana workspace with data source and dashboards.
+ An OpenTelemetry Collector deployed via Helm in your Amazon EKS cluster, configured to scrape Prometheus metrics and remote-write to Amazon Managed Service for Prometheus.
+ An IAM role for service accounts (IRSA) for the OpenTelemetry Collector.
+ Traces pipeline to AWS X-Ray (enabled by default).
+ Logs pipeline to Amazon CloudWatch (enabled by default).

## Viewing dashboards
<a name="obs-accelerator-dashboards"></a>

To view your new dashboards, open the specific dashboard in your Amazon Managed Grafana workspace. The infrastructure dashboards are provisioned automatically by Terraform. For more information about using Amazon Managed Grafana, see [Working in your Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-working-with-Grafana-workspace.html), in the *Amazon Managed Grafana User Guide*.