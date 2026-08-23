# Deploying a JumpStart model with Ray Serve

You can deploy JumpStart models into Ray Serve on HyperPod without manually
downloading model weights, writing model-loading code, or configuring a serving container.
The [toolkit-for-ray-on-sagemaker-ai](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/ "https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/")
library on the PyPI website provides a `JumpStartModelLoaderCallback` that integrates with Ray
Serve's LLM API to handle model artifact download from JumpStart at deployment
time.

## Prerequisites

- A running Ray cluster or a `RayService` you deploy in the
  following steps. For more information, see [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md "sagemaker-hyperpod-ray-deploy-model.md").
- The KubeRay operator installed. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md").
- The Amazon EKS Pod Identity Agent add-on installed on your cluster. For more
  information, see [Set up the EKS Pod
  Identity Agent](../../../eks/latest/userguide/pod-id-agent-setup.md "../../../eks/latest/userguide/pod-id-agent-setup.md") in the _Amazon EKS User
  Guide_.

## Configure IAM permissions

The `JumpStartModelLoaderCallback` calls the SageMaker AI API to retrieve
presigned URLs for downloading model artifacts. Your Ray Serve pods need an IAM role
with the following permissions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sagemaker:CreateHubContentPresignedUrls",
      "Resource": "*"
    }
  ]
}
```

Create a Pod Identity association that maps a Kubernetes service account to this
IAM role. For more information, see [Configuring a Kubernetes service
account to assume an IAM role with EKS Pod Identity](../../../eks/latest/userguide/pod-id-association.md "../../../eks/latest/userguide/pod-id-association.md") in the _Amazon EKS
User Guide_.

```
aws eks create-pod-identity-association \
  --cluster-name `eks-cluster-name` \
  --namespace `namespace` \
  --service-account `jumpstart-ray-serve` \
  --role-arn arn:aws:iam::`account-id`:role/`role-name`
```

Reference this service account in your `RayService` manifest using the
`serviceAccountName` field (shown in the following example).

## Deploy the model

The following example deploys a JumpStart model using Ray Serve's
`LLMConfig` with the `JumpStartModelLoaderCallback`. The callback
downloads model artifacts from JumpStart using presigned URLs when the serve replica
starts and loads them into the serving engine (vLLM), exposing an OpenAI-compatible
API.

```
from ray.serve.llm import LLMConfig, build_openai_app
from ray.llm._internal.common.callbacks.base import CallbackConfig
from toolkit_for_ray_on_sagemaker_ai import JumpStartModelLoaderCallback

llm_config = LLMConfig(
    model_loading_config={
        "model_id": "my-llm",
        "model_source": "placeholder",
    },
    callback_config=CallbackConfig(
        callback_class=JumpStartModelLoaderCallback,
        callback_kwargs={
            "jumpstart_model_id": "huggingface-reasoning-qwen3-4b",
            "region": "us-east-1",
            "accept_eula": False,  # Set to True after reviewing the model's EULA
        },
    ),
    accelerator_type="A10G",
)

app = build_openai_app({"llm_configs": [llm_config]})
```

Reference `app` from the `import_path` in your
`RayService` manifest, then deploy it as described in [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md "sagemaker-hyperpod-ray-deploy-model.md"). Make sure both
`headGroupSpec` and `workerGroupSpecs` set
`serviceAccountName` to the service account associated with the IAM role
created in the previous step.

###### Note

For information about model licensing and EULA requirements, see [Choose a
foundation model](jumpstart-foundation-models-choose.md "jumpstart-foundation-models-choose.md").

## Reaching the endpoint

The deployment exposes an OpenAI-compatible chat completions API on port 8000
through the KubeRay service created for the `RayService`. For quick testing,
use `kubectl port-forward`:

```
kubectl port-forward svc/`ray-service-head-svc` 8000:8000
```

Then send requests to `http://localhost:8000`:

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "my-llm",
    "messages": [{"role": "user", "content": "What is Ray Serve?"}]
  }'
```
