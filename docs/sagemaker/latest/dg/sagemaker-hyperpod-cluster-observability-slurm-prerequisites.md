# Prerequisites for SageMaker HyperPod cluster observability

Before proceeding with the steps to [Installing metrics exporter packages on your HyperPod cluster](sagemaker-hyperpod-cluster-observability-slurm-install-exporters.md "sagemaker-hyperpod-cluster-observability-slurm-install-exporters.md"), ensure that
the following prerequisites are met.

## Enable IAM Identity Center

To enable observability for your SageMaker HyperPod cluster, you must first enable IAM
Identity Center. This is a prerequisite for deploying an AWS CloudFormation stack that sets up
the Amazon Managed Grafana workspace and Amazon Managed Service for Prometheus. Both of these services also require the IAM
Identity Center for authentication and authorization, ensuring secure user access
and management of the monitoring infrastructure.

For detailed guidance on enabling IAM Identity Center, see the [Enabling IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") section in the _AWS IAM
Identity Center User Guide_.

After successfully enabling IAM Identity Center, set up a user account that will
serve as the administrative user throughout the following configuration
precedures.

## Create and deploy an AWS CloudFormation stack for SageMaker HyperPod observability

Create and deploy a CloudFormation stack for SageMaker HyperPod observability to monitor
HyperPod cluster metrics in real time using Amazon Managed Service for Prometheus and Amazon Managed Grafana. To deploy the
stack, note that you also should enable your [IAM Identity Center](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon") beforehand.

Use the sample CloudFormation script [`cluster-observability.yaml`](https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/4.prometheus-grafana/cluster-observability.yaml "https://github.com/aws-samples/awsome-distributed-training/blob/main/4.validation_and_observability/4.prometheus-grafana/cluster-observability.yaml") that helps you set up Amazon VPC
subnets, Amazon FSx for Lustre file systems, Amazon S3 buckets, and IAM roles required to
create a HyperPod cluster observability stack.
