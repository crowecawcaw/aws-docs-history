# Amazon SageMaker HyperPod Inference release notes

This topic covers release notes that track updates, fixes, and new features for
Amazon SageMaker HyperPod Inference. SageMaker HyperPod Inference enables you to deploy and scale machine
learning models on your HyperPod clusters with enterprise-grade reliability. For general
Amazon SageMaker HyperPod platform releases, updates, and improvements, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

For information about SageMaker HyperPod Inference capabilities and deployment options, see
[Deploying models on
Amazon SageMaker HyperPod](sagemaker-hyperpod-model-deployment.md "sagemaker-hyperpod-model-deployment.md").

## SageMaker HyperPod Inference release notes:

v2.3

**What's new**

This release introduces new optional fields in the Custom Resource Definitions (CRDs)
to enhance deployment configuration flexibility.

**Features**

- **Multi Instance Types**
  - **Enhanced deployment reliability** – Supports
    multi-instance type configurations with automatic failover to alternative
    instance types when preferred options lack capacity
  - **Intelligent resource scheduling** – Uses
    Kubernetes node affinity to prioritize instance types while guaranteeing
    deployment even when preferred resources are unavailable
  - **Optimized cost and performance** – Maintains
    your instance type preferences and prevents capacity-related failures during
    cluster fluctuations

**Bug Fixes**

Changes to the field `invocationEndpoint` in the spec of the
`InferenceEndpointConfig` will now take effect:

- If the `invocationEndpoint` field is patched or updated, dependent
  resources, such as the `Ingress`, the Load Balancer,
  `SageMakerEndpointRegistration`, and SageMaker Endpoint, will be
  updated with normalisation.
- The value for `invocationEndpoint` provided will be stored as-is
  in the `InferenceEndpointConfig` spec itself. When this value is used
  to create a Load Balancer and— if enabled— a SageMaker Endpoint, it will be
  normalised to have one leading forward slash.
  - `v1/chat/completions` will be normalised to
    `/v1/chat/completions` for the `Ingress`, AWS Load
    Balancer, and SageMaker Endpoint. For the
    `SageMakerEndpointRegistration`, it will be displayed in its
    spec as `v1/chat/completions`.
  - `///invoke` will be normalised to `/invoke` for
    the `Ingress`, AWS Load Balancer, and SageMaker Endpoint. For
    the `SageMakerEndpointRegistration`, it will be displayed in
    its spec as `invoke`.

**Installing Helm:**

Follow: [https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart")

If you are focused on only installing the inference operator, after step 1 i.e.
`Set Up Your Helm Environment`, do
`cd HyperPodHelmChart/charts/inference-operator`. Since you are in the
inference operator chart directory itself, in the commands, wherever you see
`helm_chart/HyperPodHelmChart`, replace with `.` .

**Upgrade Operator to v2.3 in case already installed:**

```
cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

helm upgrade hyperpod-inference-operator . \
  -n kube-system \
  -f current-values.yaml \
  --set image.tag=v2.3
```
