

# Python SDK reference

Use the SDK for the training session APIs (`sagemaker.train.training_session`) to drive a training loop from your own Python process. Your code issues each step — a forward and backward pass, an optimizer step, sampling, saving or loading a checkpoint — and SageMaker AI manages the infrastructure and the base model. This page describes the behavior you need to write a correct loop.

```shell
pip install sagemaker-train
```

## At a glance
<a name="training-sessions-sdk-glance"></a>

```python
from sagemaker.train.training_session import ServiceClient, AdamParams, Datum, ModelInput

PAIRS = [
    ("Question: 2+2?\nAnswer:", " 4"),
    ("Capital of France?", " Paris"),
]

svc = ServiceClient(
    region="us-west-2",
    role_arn="arn:aws:iam::111122223333:role/MyRole",
    model_package_group_arn="arn:aws:sagemaker:us-west-2:111122223333:model-package-group/my-training-session-checkpoints",
    s3_output_path="s3://amzn-s3-demo-bucket/training-sessions/",
)
print(svc.list_base_models())              # base models you can fine-tune in this Region
tc = svc.create_lora_training_client(base_model="<name from list_base_models()>", rank=32, alpha=64)
tok = tc.get_tokenizer()                   # the service takes token IDs, so tokenize client-side

batch = []
for prompt, response in PAIRS:
    prompt_len = len(tok.encode(prompt, add_special_tokens=False))
    ids = tok.encode(prompt + response, add_special_tokens=False) + [tok.eos_token_id]
    batch.append(Datum(
        model_input=ModelInput.from_ints(ids[:-1]),
        loss_fn_inputs={
            "target_tokens": ids[1:],
            "weights": [0.0] * (prompt_len - 1) + [1.0] * (len(ids) - prompt_len),
        },
    ))

# Both calls return an APIFuture immediately, so optim_step is queued behind
# forward_backward. Resolve both once they are submitted.
fwd_bwd = tc.forward_backward(batch, loss_fn="cross_entropy")
step = tc.optim_step(AdamParams(learning_rate=5e-5))
print(fwd_bwd.result().metrics, step.result().metrics)

print(tc.save_state().result().model_package_arn)
tc.stop()
```

Each datum in a batch carries the loss inputs its loss function requires — see [Training data](#training-sessions-sdk-training-data). `get_tokenizer()` requires the tokenizer extra (`pip install 'sagemaker-train[tokenizer]'`); pass token IDs directly to skip it. Available base models vary by Region. Call `list_base_models()` instead of hard-coding a list.

## Clients
<a name="training-sessions-sdk-clients"></a>


| Client | Use it to | Get one from | 
| --- | --- | --- | 
| ServiceClient | Create sessions. List sessions, base models, and checkpoints. | Construct it directly. | 
| TrainingClient | Drive the training loop. | ServiceClient.create\_lora\_training\_client or either restore factory. | 
| SamplingClient | Generate tokens from one fixed set of weights. | A TrainingClient, or a ServiceClient when no session is running. | 

The following diagram shows which factory method creates each client:
+ A `ServiceClient` creates a `TrainingClient` through `create_lora_training_client`, `create_training_client_from_state`, or `create_training_client_from_state_with_optimizer`.
+ A `ServiceClient` creates a `SamplingClient` directly through `create_sampling_client`.
+ A `TrainingClient` creates a `SamplingClient` through `create_sampling_client` or `save_weights_and_get_sampling_client`.

![Diagram of the factory methods that create TrainingClient and SamplingClient objects.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/training-sessions/training-sessions-clients.png)


`ServiceClient` requires `role_arn`, the IAM role each session assumes. Set `model_package_group_arn`, `s3_output_path`, `kms_key_arn`, and `vpc_config` on the client to apply them to every session it creates, or pass them per call to override. When you omit them, SageMaker AI supplies account defaults.

Each factory has an `*_async` twin that takes the same arguments and returns the same client. Creating a session waits for it to become ready, which takes from seconds to several minutes depending on the model. The `_async` form performs that wait without blocking the event loop.

```python
tc = await svc.create_lora_training_client_async(base_model="...", rank=32)
```

## Operations and results
<a name="training-sessions-sdk-operations"></a>

Every operation submits when you call it and returns an `APIFuture`. `future.result()` blocks until the operation finishes, then returns the result or raises `OperationError`. It accepts `timeout` and `poll_interval`. `await future` does the same inside an event loop without blocking it.

Submit successive operations before collecting the earlier one. They pipeline, and both run in the same cycle.

The following diagram compares two ways to run `forward_backward` and `optim_step`:
+ *Sequential*: you collect each result before you submit the next operation. Each operation costs one full round trip.
+ *Pipelined*: you submit both operations, then collect both results. Both operations are in flight in the same cycle.

The following loop uses the pipelined pattern.

```python
for batch in data_loader:
    fwd_bwd = tc.forward_backward(batch, loss_fn="ppo")
    optim = tc.optim_step()
    fwd_bwd.result()
    optim.result()
```

![Sequence diagram comparing sequential and pipelined submission of forward_backward and optim_step.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/training-sessions/training-sessions-pipelining.png)


### Async variants
<a name="training-sessions-sdk-async"></a>

What an `*_async` method returns depends on whether the operation is ordered.


| Operations | `*_async` returns | 
| --- | --- | 
| forward\_backward, forward, optim\_step, save\_state, save\_weights\_for\_sampler, load\_state, load\_state\_with\_optimizer | An APIFuture. Await it again for the result. | 
| sample, compute\_logprobs | The result: SampleResponse or list[float \| None]. | 

Training operations run in the order you submit them, so the coroutine returns a future and you choose when to wait. Sampling operations are independent, so the coroutine returns the result directly.

```python
# Training: two awaits
fwd_bwd = await tc.forward_backward_async(batch, loss_fn="ppo")
result = await fwd_bwd

# Sampling: one await
response = await sc.sample_async(prompt, num_samples=4, sampling_params=params)
```

### Concurrent sampling
<a name="training-sessions-sdk-concurrent-sampling"></a>

Each `sample` call takes one prompt. `SamplingParams.max_tokens` defaults to 512, which is also the smallest value the service accepts. Sampling operations are independent, so keep many in flight to raise throughput.

```python
results = await asyncio.gather(*(
    sc.sample_async(p, num_samples=4, sampling_params=params)
    for p in prompts
))
```

Synchronous code achieves the same by submitting every call before collecting any:

```python
ops = [sc.sample(p, num_samples=4, sampling_params=params) for p in prompts]
results = [op.result() for op in ops]
```

## Model source
<a name="training-sessions-sdk-model-source"></a>

`create_training_client_from_state`, `create_training_client_from_state_with_optimizer`, and `create_sampling_client` accept a base model, saved weights, or both.


| You pass | Result | 
| --- | --- | 
| model\_package\_arn only | The base model comes from the package, at the version the weights were trained on. | 
| base\_model only | Resolved to its latest version. | 
| Both | They must name the same base model, or the call raises ValueError. The version still comes from the package. | 

Because only the model name is compared, a `base_model` that resolves to a newer version than the checkpoint is accepted, and the checkpoint version is used. `base_model` accepts a name from `list_base_models()`, a HuggingFace model ID, or a full hub content ARN to pin an exact version.

## Checkpoints
<a name="training-sessions-sdk-checkpoints"></a>

Both checkpoint calls register a versioned SageMaker AI model package. They differ in what they contain.


| Call | Contains | Use it to | 
| --- | --- | --- | 
| save\_state() | Weights and optimizer state | Resume training where it stopped. | 
| save\_weights\_for\_sampler() | Weights only | Sample from or deploy a snapshot. Pass merge\_weights=True to also write a self-contained merged model to the same package version. | 

The following diagram shows the two save paths and how you use what each one produces. `save_state` writes a `ModelPackageKind.CHECKPOINT` package that contains the weights and the optimizer state. Restore it with `load_state_with_optimizer` to resume exactly where training stopped, or with `load_state` to resume training with a new optimizer. `save_weights_for_sampler` writes a `ModelPackageKind.MODEL` package that contains the weights only. You can sample from it or deploy it.

![Diagram of the save and restore paths for checkpoint and model packages.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/training-sessions/training-sessions-save-restore.png)


The diagram shows the following paths:
+ `save_state` writes a `ModelPackageKind.CHECKPOINT` package that contains the weights and the optimizer state.
+ `save_weights_for_sampler` writes a `ModelPackageKind.MODEL` package that contains the weights only. You can sample from it or deploy it.
+ `load_state_with_optimizer` restores a checkpoint package with its optimizer state, so training resumes exactly where it stopped.
+ `load_state` restores the weights from a checkpoint package and resets the optimizer.

Restore with the method that names what you want:

```python
tc.load_state(arn).result()                 # weights only; optimizer resets
tc.load_state_with_optimizer(arn).result()  # weights and optimizer
```

### Resume a run
<a name="training-sessions-sdk-resume"></a>

A session is compute and cannot be reattached by name. The checkpoint is durable on its own, so checkpoint periodically and resume by starting a new session from the latest one.

```python
if step % checkpoint_every == 0:
    tc.save_state(description=f"step {step}").result()

# Later, or in a new process
from sagemaker.train.training_session import ModelPackageKind, ServiceClient

svc = ServiceClient(region="us-west-2", role_arn=role_arn, model_package_group_arn=my_group)
ckpt = svc.get_latest_model_package(ModelPackageKind.CHECKPOINT)
tc = svc.create_training_client_from_state_with_optimizer(model_package_arn=ckpt.model_package_arn)
```

Pass your own `model_package_group_arn` for runs you intend to resume. `get_latest_model_package` searches the group set on the client or passed per call, and raises `ValueError` when neither is set. One group per experiment also keeps the result exact, because an unnamed group is shared across your account.

Each saved package consumes Amazon S3 storage until you remove it. `delete_model_package(arn)` removes the package; add `delete_artifacts=True` to remove the stored weights as well. The package holds the only reference to its Amazon S3 location, so deleting the package alone leaves the objects in place.

## Training data
<a name="training-sessions-sdk-training-data"></a>

`forward_backward` accepts token ID lists or strings. For control over the loss, pass `Datum` objects.

```python
from sagemaker.train.training_session import Datum, ModelInput, TensorData, TensorDtype

# Prompt [101, 2023], response [3456, 7890]. Input drops the last token.
tokens = [101, 2023, 3456, 7890]
Datum(
    model_input=ModelInput.from_ints(tokens[:-1]),
    loss_fn_inputs={
        "target_tokens": TensorData(tokens[1:], dtype=TensorDtype.INT64, shape=[3]),
        "weights": TensorData([0.0, 1.0, 1.0], shape=[3]),
        "logprobs": TensorData(logprobs_tensor),   # torch or numpy
        "advantages": TensorData([0.0, 1.5, 1.5], shape=[3]),
    },
)
```

Each loss function requires specific `loss_fn_inputs` keys. Omitting one fails the operation.


| `loss_fn` | Required keys | 
| --- | --- | 
| cross\_entropy | target\_tokens, weights | 
| ppo, importance\_sampling, cispo | target\_tokens, weights, logprobs, advantages | 

Every value in `loss_fn_inputs` follows two rules:
+ **One value for each input token.** Use `0` at positions to skip.
+ **`weights` masks the prompt.** `weights[i]` scores `target_tokens[i]`, the token after position `i`. Use `0` for prompt targets and `1` for response targets.

`TensorData` takes torch tensors and numpy arrays. You can also pass strings instead of token IDs, and the SDK tokenizes them for you. This needs `pip install 'sagemaker-train[tokenizer]'`. To get token IDs yourself, call `get_tokenizer()`.

For reinforcement learning, build one datum for each sampled response, adding the sampled `logprobs` and an advantage for each response token. The advantage here is each response's reward minus its group's mean, so swap in your own. The following Python example defines `build_batch`, which you can adapt:

```python
from sagemaker.train.training_session import Datum, ModelInput

def build_batch(prompts, responses, rewards):
    batch = []
    for prompt, response, group_rewards in zip(prompts, responses, rewards):
        baseline = sum(group_rewards) / len(group_rewards)
        for seq, reward in zip(response.sequences, group_rewards):
            tokens = prompt + seq.tokens
            prompt_len = len(prompt)
            response_len = len(tokens) - prompt_len
            batch.append(Datum(
                model_input=ModelInput.from_ints(tokens[:-1]),
                loss_fn_inputs={
                    "target_tokens": tokens[1:],
                    "weights": [0.0] * (prompt_len - 1) + [1.0] * response_len,
                    "logprobs": [0.0] * (prompt_len - 1) + list(seq.logprobs),
                    "advantages": [0.0] * (prompt_len - 1) + [reward - baseline] * response_len,
                },
            ))
    return batch
```

## On-policy sampling
<a name="training-sessions-sdk-on-policy"></a>

A `SamplingClient` samples from the weights it was created with, so each client holds one fixed policy. To sample from the latest weights, call `save_weights_and_get_sampling_client()` after each update. It saves the weights and returns a client bound to them.

The following Python example runs the loop with `build_batch` from [Training data](#training-sessions-sdk-training-data). Each prompt is a list of token IDs built from your `questions`, and `answers` holds the expected answer for each question. `reward_fn` scores one response against its answer and returns a float. Replace it with your own check:

```python
from sagemaker.train.training_session import AdamParams, SamplingParams

tok = tc.get_tokenizer()
prompts = [tok.encode(q, add_special_tokens=False) for q in questions]
params = SamplingParams(max_tokens=512)
num_steps = 100

def reward_fn(response_tokens, answer):
    # 1.0 when the response ends with the expected answer, else 0.0.
    text = tok.decode(response_tokens, skip_special_tokens=True)
    return 1.0 if text.strip().endswith(answer) else 0.0

sc = tc.create_sampling_client()
for step in range(num_steps):
    ops = [sc.sample(p, num_samples=4, sampling_params=params) for p in prompts]
    responses = [op.result() for op in ops]
    rewards = [[reward_fn(seq.tokens, a) for seq in response.sequences]
               for a, response in zip(answers, responses)]
    tc.forward_backward(build_batch(prompts, responses, rewards), loss_fn="ppo").result()
    tc.optim_step(AdamParams(learning_rate=1e-5)).result()
    sc = tc.save_weights_and_get_sampling_client()
```

For more information about complete loops with evaluation and checkpointing, see [End-to-end examples](training-sessions-example.md).

## Sessions
<a name="training-sessions-sdk-sessions"></a>


| Call | Effect | 
| --- | --- | 
| tc.stop() | Stop the session. The session record is retained. | 
| tc.delete(stop\_if\_active=False) | Delete the session. Pass stop\_if\_active=True to stop it first. | 
| svc.stop\_session(name), svc.delete\_session(name) | The same, addressed by name. | 
| svc.list\_sessions(status\_equals=...) | List sessions, paginating automatically. | 

A session supports one `TrainingClient` at a time. A second client on the same session raises `ConcurrentAccessError`. Call `stop()` when you finish, or scope the client to a `with` block.