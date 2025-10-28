# Setting up vertical autoscaling for Amazon EMR on EKS

This topic helps you get your Amazon EKS cluster ready to submit Amazon EMR Spark jobs with
vertical autoscaling. The setup process requires you to confirm or complete the tasks in the
following sections:

###### Topics

- [Prerequisites](#jobruns-vas-prereqs "#jobruns-vas-prereqs")
- [Install the Operator Lifecycle Manager (OLM) on
  your Amazon EKS cluster](#jobruns-vas-install-olm "#jobruns-vas-install-olm")
- [Install the Amazon EMR on EKS vertical autoscaling
  operator](#jobruns-vas-install-operator "#jobruns-vas-install-operator")

## Prerequisites

Complete the following tasks before you install the vertical autoscaling Kubernetes
operator on your cluster. If you've already completed any of the prerequisites, you can
skip those and move on to the next one.

- [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
  – If you've already installed the
  AWS CLI, confirm that you have the latest version.
- [Install kubectl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md") – kubectl is a command line tool that you
  use to communicate with the Kubernetes API server. You need kubectl to install and
  monitor vertical autoscaling-related artifacts on your Amazon EKS cluster.
- [Install the Operator
  SDK](https://sdk.operatorframework.io/docs/installation/ "https://sdk.operatorframework.io/docs/installation/") – Amazon EMR on EKS uses the Operator SDK as a package manager
  for the life of the vertical autoscaling operator that you install on your
  cluster.
- [Install
  Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") – You need access to the Docker CLI to authenticate
  and fetch the vertical autoscaling-related Docker images to install on your Amazon EKS
  cluster.
- [Install
  the Kubernetes Metrics server](../../../eks/latest/userguide/metrics-server.md "../../../eks/latest/userguide/metrics-server.md")– You must first install metrics server so the vertical
  pod autoscaler can fetch metrics from the Kubernetes API server.
- [Get started with Amazon EKS – eksctl](../../../eks/latest/userguide/getting-started-eksctl.md "../../../eks/latest/userguide/getting-started-eksctl.md")
  (version 1.24 or higher)
  – Vertical autoscaling is supported with Amazon EKS versions 1.24 and higher. Once
  you create the cluster, [register it for use
  with Amazon EMR](setting-up-registration.md "setting-up-registration.md").
- [Select an Amazon EMR
  base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md") (release 6.10.0 or higher) – Vertical
  autoscaling is supported with Amazon EMR releases 6.10.0 and higher.

## Install the Operator Lifecycle Manager (OLM) on

your Amazon EKS cluster

Use the Operator SDK CLI to install the Operator Lifecycle Manager (OLM) on the
Amazon EMR on EKS cluster where you want to set up vertical autoscaling, as shown in the following
example. Once you set it up, you can use OLM to install and manage the lifecycle of the
[Amazon EMR vertical autoscaling
operator](#jobruns-vas-install-operator "#jobruns-vas-install-operator").

```
operator-sdk olm install
```

To validate installation, run the `olm status` command:

```
operator-sdk olm status
```

Verify that the command returns a successful result, similar to the following example
output:

```
INFO[0007] Successfully got OLM status for version `X.XX`
```

If your installation doesn't succeed, see [Troubleshooting Amazon EMR on EKS vertical
autoscaling](troubleshooting-vas.md "troubleshooting-vas.md").

## Install the Amazon EMR on EKS vertical autoscaling

operator

Use the following steps to install the vertical autoscaling operator on your Amazon EKS
cluster:

1. Set up the following environment variables that you will use to complete the
   installation:
   - **`$REGION`** points to the
     AWS Region for your cluster. For example, `us-west-2`.
   - **`$ACCOUNT_ID`** points to the Amazon ECR
     account ID for your Region. For more information, see [Amazon ECR registry accounts by Region](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR").
   - **`$RELEASE`** points to the Amazon EMR
     release that you want to use for your cluster. With vertical autoscaling, you must
     use Amazon EMR release 6.10.0 or higher.

2. Next, get authentication tokens to the [Amazon ECR registry](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR") for the operator.

```
aws ecr get-login-password \
 --region `region-id` | docker login \
 --username AWS \
 --password-stdin $ACCOUNT_ID.dkr.ecr.`region-id`.amazonaws.com
```

3. Install the Amazon EMR on EKS vertical autoscaling operator with the following
   command:

```
ECR_URL=$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com && \
REPO_DEST=dynamic-sizing-k8s-operator-olm-bundle && \
BUNDLE_IMG=emr-$RELEASE-dynamic-sizing-k8s-operator && \
operator-sdk run bundle \
$ECR_URL/$REPO_DEST/$BUNDLE_IMG\:latest
```

This will create a release of the vertical autoscaling operator in the default
namespace of your Amazon EKS cluster. Use this command to install in a different
namespace:

```
operator-sdk run bundle \
$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/dynamic-sizing-k8s-operator-olm-bundle/emr-$RELEASE-dynamic-sizing-k8s-operator:latest \
-n `operator-namespace`
```

###### Note

If the namespace that you specify doesn't exist, OLM won't install the operator.
For more information, see [Kubernetes namespace not
found](troubleshooting-vas.md "troubleshooting-vas.md"). 4. Verify that you successfully installed the operator with the kubectl Kubernetes
command-line tool.

```
kubectl get csv -n `operator-namespace`
```

The `kubectl` command should return your newly-deployed vertical
autoscaler operator with a **Phase** status of **Succeeded**. If you've trouble with installation or setup, see
[Troubleshooting Amazon EMR on EKS vertical
autoscaling](troubleshooting-vas.md "troubleshooting-vas.md").
