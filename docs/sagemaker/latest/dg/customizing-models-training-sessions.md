

# Training session APIs
<a name="customizing-models-training-sessions"></a>

The SageMaker AI training session APIs run model customization on stateful, serverless GPU sessions where you orchestrate training operations directly. Existing high-level fine-tuning APIs constrain your training loop to predefined workflows such as supervised fine-tuning (SFT). You cannot write custom loss functions or run frontier reinforcement learning (RL) with elastic rollouts. You are also locked into the infrastructure decisions those APIs make for you.

Teams building production AI systems need to iterate on algorithms, experiment with novel training objectives, and scale RL across Regions without rewriting distributed training code. Training session APIs give you that level of control.

**Note**  
Training session APIs require you to write Python code that drives the training loop. If you want a managed workflow that does not require programming, see [Serverless model customization](customize-model.md). If you want to submit a complete training script as a job instead, see [SageMaker AI Training Jobs](customizing-models-training-jobs.md).

With the training session APIs, instead of submitting a complete training script, you open a session and call operations like `forward_backward()`, `optim_step()`, and `sample()` as API calls, and compose them into whatever training procedure your technique requires. The model stays loaded on GPUs across calls, and the service handles distributed execution, gradient synchronization, and tenant isolation.

```
from sagemaker.train.training_session import ServiceClient, AdamParams

svc = ServiceClient(region="us-west-2", role_arn="arn:aws:iam::111122223333:role/MyRole")
tc = svc.create_lora_training_client(base_model="gpt-oss-20b", rank=32, alpha=64)

# Custom reinforcement learning loop with on-policy sampling
sc = tc.create_sampling_client()
for step in range(num_steps):
    ops = [sc.sample(p, num_samples=4, sampling_params=params) for p in prompts]
    rollouts = [op.result() for op in ops]
    tc.forward_backward(build_batch(rollouts), loss_fn="ppo").result()
    tc.optim_step(AdamParams(learning_rate=5e-5)).result()
    sc = tc.save_weights_and_get_sampling_client()

tc.stop()
```

Use the training session APIs when you need:
+ Full control over a custom training loop (SFT, RL, or novel techniques).
+ Multi-stage pipelines that chain multiple procedures in one session.
+ Step-by-step debugging of loss divergence or reward hacking.
+ Multi-turn RL where rollout generation and policy updates share model state.

## Who it is for
<a name="training-sessions-who"></a>
+ ML researchers experimenting with novel training techniques.
+ Advanced ML teams running production RL systems.
+ Teams building custom loss functions, such as group relative policy optimization (GRPO), DRO, and DAPO.
+ Organizations needing multi-Region training and elastic rollout inference.
+ Teams that own their data and want to own their models.

## Key differentiators
<a name="training-sessions-differentiators"></a>


| Capability | What it means | 
| --- | --- | 
| Operation-level API | You orchestrate forward\_backward(), sample(), and optim\_step() individually rather than submitting a monolithic training script. | 
| Stateful sessions | The model stays loaded on GPUs across calls. No cold starts between rollout generation and policy updates. | 
| Serverless | No instance selection, no cluster management, no capacity planning. The service provisions and manages GPU infrastructure. | 
| Technique-agnostic | Implement SFT, proximal policy optimization (PPO), GRPO, multi-turn RL, or any custom procedure. You choose the algorithm; the service does not limit your technique. | 

## Supported models, pricing, and Regions
<a name="training-sessions-models-pricing-regions"></a>

**Supported models**


| Model | Region | 
| --- | --- | 
| GPT-OSS-20B | us-east-1, us-west-2, ap-south-1 | 
| Gemma-4-31B-it | us-west-2, ap-south-1 | 
| Qwen-3.6-27B | us-west-2, ap-south-1 | 

**Pricing**

For full pricing details, see the [SageMaker AI pricing](https://aws.amazon.com/sagemaker/ai/pricing/) page. Charges are based on three dimensions:
+ **Prefill** – the cost of processing the input tokens fed into the model at the start of each training step. This includes the prompt, conversation history, and any context the model receives before generating a response.
+ **Sample** – the cost of the tokens the model generates during the training rollout. This is where the model produces its responses, which are then evaluated and used to compute the reward signal.
+ **Train** – the cost of the backward pass, where the model weights are updated based on the reward signal. This is the core learning step in the RL process.

**Quotas**

The following quotas apply to the training session APIs. These quotas are adjustable. To request an increase, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas). For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Maximum number of concurrent fine-tuning training sessions | 2 | Yes | 

## Topics
<a name="training-sessions-topics"></a>
+ [Prerequisites](training-sessions-prereqs.md)
+ [AWS managed policies for SageMaker AI training session APIs](training-sessions-security-iam-awsmanpol.md)
+ [Core operations](training-sessions-primitives.md)
+ [Getting started with the training session APIs](training-sessions-getting-started.md)
+ [Python SDK reference](training-sessions-sdk.md)
+ [API reference](training-sessions-api.md)
+ [End-to-end examples](training-sessions-example.md)
+ [Troubleshooting and best practices](training-sessions-troubleshooting.md)
+ [Security in SageMaker AI Training Sessions](training-sessions-security.md)