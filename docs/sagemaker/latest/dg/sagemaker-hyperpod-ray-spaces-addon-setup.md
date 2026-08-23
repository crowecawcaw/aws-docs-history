# Setting up the Spaces add-on

The SageMaker Spaces add-on provides the IDE and notebook spaces that attach to a Ray
cluster. You install it from the console, then configure web browser access so users open a
space in a browser.

## Prerequisites

- A HyperPod cluster orchestrated by Amazon EKS. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").

The following are optional. You need them for web browser access to a space, and for Ray
Dashboard access through the Ray Endpoint Operator:

- A customer-owned domain with a public Amazon Route 53 hosted zone, an AWS
  Certificate Manager certificate for that domain, and an AWS AWS KMS key that
  signs access tokens.

## Install the add-on

###### To install the Spaces add-on

1. In the console, open your HyperPod cluster and choose the **IDE and
   Notebooks** tab.
2. For the Spaces add-on, choose **Quick Install** to apply the
   default configuration, or **Custom install** to change
   it.

For the detailed steps and the options each path exposes, see [Install SageMaker
AI Spaces Add-on](operator-install.md "operator-install.md") and [Customize add-on](customization.md "customization.md").

###### Important

Ray interactive development requires version 0.2.0 or later of the Spaces add-on.
Earlier versions do not include it. If you already installed an earlier version,
upgrade it before you attach a space to a Ray cluster.

## Ray integration configuration

The add-on turns on Ray integration with the following defaults. Change them in the
add-on configuration when your workload needs different values.

```
{
  "jupyter-k8s-aws-hyperpod": {
    "rayIntegration": {
      "enabled": true,
      "objectStoreMemory": "1073741824",
      "devShmSizeLimit": "1Gi",
      "sidecar": {
        "runAsUser": 1000,
        "runAsGroup": 100,
        "resources": {
          "requests": { "cpu": "250m", "memory": "512Mi" },
          "limits": { "cpu": "1", "memory": "1536Mi" }
        }
      }
    }
  }
}
```

## Configure web browser access

Web browser access is optional. Configure it when you want users to open a space in a
browser, or to reach the Ray Dashboard from a browser.

###### Important

Web browser access requires a customer-owned domain and a public Route 53 hosted
zone. Without them you cannot open a space in a browser, and the Ray Endpoint Operator
cannot serve the Ray Dashboard. For more information about dashboard access, see
[Ray Dashboard access and remote job submission](sagemaker-hyperpod-ray-dashboard.md "sagemaker-hyperpod-ray-dashboard.md").

Web browser access needs the Route 53 hosted zone, the ACM certificate, and the AWS KMS
key from the prerequisites. For the configuration steps, see [Web browser access](browser-access.md "browser-access.md"). For the
domain and certificate setup, see [Custom certificates and Route 53 DNS](sagemaker-hyperpod-model-deployment-custom-certs.md "sagemaker-hyperpod-model-deployment-custom-certs.md").

## Verify

Confirm the add-on reports **Active** on the **IDE and
Notebooks** tab before you attach a space. Check that its version is 0.2.0 or
later.
