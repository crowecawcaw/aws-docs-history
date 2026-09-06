

# Accelerated inference
<a name="sagemaker-hyperpod-ray-accelerated-inference"></a>

Ray Serve is the open source model-serving library for Ray. You deploy a model as a Serve application, and Ray Serve handles request routing, batching, and replica scaling. On HyperPod, Ray Serve runs on KubeRay through a `RayService` resource, so your Serve code and deployment graph are unchanged.

## Requirements
<a name="sagemaker-hyperpod-ray-accelerated-inference-requirements"></a>

Ray Serve on HyperPod requires only the KubeRay operator. KubeRay reconciles the `RayService` resource, creates the Ray cluster that backs it, and manages the Serve applications on it. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md).

You do not install a separate inference operator to serve models with Ray Serve. The JumpStart deployment path additionally uses the `toolkit-for-ray-on-sagemaker-ai` library, which you install with `pip`.

## What you can do
<a name="sagemaker-hyperpod-ray-accelerated-inference-capabilities"></a>
+ Deploy a model from your own code as a `RayService` and reach it over HTTP.
+ Deploy an JumpStart model into a Ray Serve deployment.
+ Lower time to first token for long-context and multi-turn workloads with a managed tiered KV cache and prefix-aware routing.
+ Scale serving replicas within the cluster, and scale cluster capacity with managed Karpenter.

For the Ray Serve API and deployment concepts, see [Ray Serve: Scalable and Programmable Serving](https://docs.ray.io/en/latest/serve/index.html) in the Ray documentation.

**Topics**
+ [Requirements](#sagemaker-hyperpod-ray-accelerated-inference-requirements)
+ [What you can do](#sagemaker-hyperpod-ray-accelerated-inference-capabilities)
+ [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md)
+ [Deploying a JumpStart model with Ray Serve](sagemaker-hyperpod-ray-deploy-jumpstart-model.md)
+ [Managed tiered KV cache and routing](sagemaker-hyperpod-ray-kv-cache.md)
+ [Setting up tiered KV cache](sagemaker-hyperpod-ray-kv-cache-setup.md)
+ [Autoscaling serving capacity](sagemaker-hyperpod-ray-serving-autoscaling.md)