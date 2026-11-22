

# Prerequisites for SageMaker HyperPod cluster observability

Complete these prerequisites if you use Amazon Managed Grafana to view the metrics, with either metric store, or Amazon Managed Service for Prometheus as the metric store. For the extension's own prerequisites, see [Prerequisites for the observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md#sagemaker-hyperpod-cluster-observability-slurm-extension-prerequisites).

## Enable IAM Identity Center
<a name="sagemaker-hyperpod-cluster-observability-slurm-prerequisites-iam-id-center"></a>

To enable observability for your SageMaker HyperPod cluster, you must first enable IAM Identity Center. This is a prerequisite for deploying an CloudFormation stack that sets up the Amazon Managed Grafana workspace and Amazon Managed Service for Prometheus. Both of these services also require the IAM Identity Center for authentication and authorization, ensuring secure user access and management of the monitoring infrastructure.

For detailed guidance on enabling IAM Identity Center, see the [Enabling IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) section in the *AWS IAM Identity Center User Guide*. 

After successfully enabling IAM Identity Center, set up a user account that will serve as the administrative user throughout the following configuration precedures.

## Create and deploy an CloudFormation stack for SageMaker HyperPod observability
<a name="sagemaker-hyperpod-cluster-observability-slurm-prerequisites-cloudformation-stack"></a>

Create and deploy a CloudFormation stack for SageMaker HyperPod observability to monitor HyperPod cluster metrics in real time using Amazon Managed Service for Prometheus and Amazon Managed Grafana. To deploy the stack, note that you also should enable your [IAM Identity Center](https://console.aws.amazon.com/singlesignon) beforehand.

Use the sample CloudFormation script [`cluster-observability.yaml`](https://github.com/awslabs/awsome-distributed-ai/blob/main/observability/prometheus-grafana/cluster-observability.yaml), which creates an Amazon Managed Service for Prometheus workspace and an Amazon Managed Grafana workspace that uses IAM Identity Center, with Amazon CloudWatch and Amazon Managed Service for Prometheus as data sources. To use a workspace that you already have, pass its ID to the stack. If you send metrics to Amazon Managed Service for Prometheus, set `prometheus.remoteWriteUrl` to the stack's `AMPRemoteWriteURL` output when you install the extension.