

# Deploying a JumpStart model with Ray Serve
<a name="sagemaker-hyperpod-ray-deploy-jumpstart-model"></a>

You can deploy JumpStart models into Ray Serve on HyperPod without manually downloading model weights, writing model-loading code, or configuring a serving container. The [toolkit-for-ray-on-sagemaker-ai](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/) library on the PyPI website provides a `JumpStartModelLoaderCallback` that integrates with Ray Serve's LLM API to handle model artifact download from JumpStart at deployment time.

## Prerequisites
<a name="sagemaker-hyperpod-ray-deploy-jumpstart-model-prereq"></a>
+ A running Ray cluster or a `RayService` you deploy in the following steps. For more information, see [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md).
+ The KubeRay operator installed. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md).
+ The Amazon EKS Pod Identity Agent add-on installed on your cluster. For more information, see [Set up the EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) in the *Amazon EKS User Guide*.

## Configure IAM permissions
<a name="sagemaker-hyperpod-ray-deploy-jumpstart-model-iam"></a>

The `JumpStartModelLoaderCallback` calls the SageMaker AI API to retrieve presigned URLs for downloading model artifacts. Your Ray Serve pods need an IAM role with the following permissions.

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

Create a Pod Identity association that maps a Kubernetes service account to this IAM role. For more information, see [Configuring a Kubernetes service account to assume an IAM role with EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-association.html) in the *Amazon EKS User Guide*.

```
aws eks create-pod-identity-association \
  --cluster-name {{eks-cluster-name}} \
  --namespace {{namespace}} \
  --service-account {{jumpstart-ray-serve}} \
  --role-arn arn:aws:iam::{{account-id}}:role/{{role-name}}
```

Reference this service account in your `RayService` manifest using the `serviceAccountName` field (shown in the following example).

## Deploy the model
<a name="sagemaker-hyperpod-ray-deploy-jumpstart-model-deploy"></a>

The following example deploys a JumpStart model using Ray Serve's `LLMConfig` with the `JumpStartModelLoaderCallback`. The callback downloads model artifacts from JumpStart using presigned URLs when the serve replica starts and loads them into the serving engine (vLLM), exposing an OpenAI-compatible API.

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

Reference `app` from the `import_path` in your `RayService` manifest, then deploy it as described in [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md). Make sure both `headGroupSpec` and `workerGroupSpecs` set `serviceAccountName` to the service account associated with the IAM role created in the previous step.

**Note**  
For information about model licensing and EULA requirements, see [Choose a foundation model](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html).

## Reaching the endpoint
<a name="sagemaker-hyperpod-ray-deploy-jumpstart-model-endpoint"></a>

The deployment exposes an OpenAI-compatible chat completions API on port 8000 through the KubeRay service created for the `RayService`. For quick testing, use `kubectl port-forward`:

```
kubectl port-forward svc/{{ray-service-head-svc}} 8000:8000
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