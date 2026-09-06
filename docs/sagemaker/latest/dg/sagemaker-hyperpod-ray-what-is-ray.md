

# What is Ray
<a name="sagemaker-hyperpod-ray-what-is-ray"></a>

Ray is an open source unified framework for scaling AI and Python applications. It provides the compute layer for parallel processing, so you do not need to be a distributed systems expert to run work across a cluster. You keep writing PyTorch, JAX, or vLLM, and Ray handles the scaling. For the full overview, see [Overview](https://docs.ray.io/en/latest/ray-overview/index.html) in the Ray documentation.

## The Ray framework
<a name="sagemaker-hyperpod-ray-what-is-ray-framework"></a>

Ray has three layers:
+ **Ray AI Libraries**, a set of Python libraries for common machine learning tasks.
+ **Ray Core**, a general-purpose distributed computing library that scales Python applications.
+ **Ray clusters**, a set of worker nodes connected to a head node. A cluster can be fixed-size, or it can autoscale to the resources your applications request.

## Ray AI libraries
<a name="sagemaker-hyperpod-ray-what-is-ray-libraries"></a>
+ **Ray Data** for distributed data preprocessing and batch inference.
+ **Ray Train** for distributed training, data-parallel and model-parallel.
+ **Ray Tune** for parallel hyperparameter tuning.
+ **Ray Serve** for online model serving.
+ **RLlib** for reinforcement learning.

## Reinforcement learning on Ray
<a name="sagemaker-hyperpod-ray-what-is-ray-rl"></a>

RLlib is the reinforcement learning library Ray ships. Beyond it, the reinforcement learning frameworks used for large language model post-training build on Ray for their distributed layer, because a single run has to place and coordinate several different roles across GPUs at once: rollout generation, reward scoring, and policy training. Ray Core gives them the actor placement and scheduling to do that.

Frameworks that run on Ray include verl, OpenRLHF, and NVIDIA NeMo-RL. Each runs as an ordinary Ray workload, so anything Ray supports runs the same way here.

## What Ray handles for you
<a name="sagemaker-hyperpod-ray-what-is-ray-handles"></a>

Ray manages the distributed systems work that would otherwise be yours:
+ **Orchestration** of the components of a distributed application.
+ **Scheduling** of when and where tasks run.
+ **Fault tolerance**, so tasks complete despite failures.
+ **Autoscaling** of resources to match demand.

## Ray on HyperPod
<a name="sagemaker-hyperpod-ray-what-is-ray-unchanged"></a>

HyperPod runs open source Ray through the KubeRay operator, unchanged. It does not fork Ray, modify the Ray runtime, or introduce a proprietary scheduler. `RayCluster`, `RayJob`, `RayCronJob`, and `RayService` behave as they do upstream, and manifests you already run continue to work. For what to set up, see [Getting started](sagemaker-hyperpod-ray-getting-started.md).