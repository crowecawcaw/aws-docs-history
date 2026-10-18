

# Getting started with the training session APIs
<a name="training-sessions-getting-started"></a>

This guide walks you through setting up and running your first training session. Start here if you are new to the training session APIs and want to get a working training loop running quickly. Before you begin, make sure you have completed the [Prerequisites](training-sessions-prereqs.md).

For conceptual background, see [Training session APIs](customizing-models-training-sessions.md). For the full API, see [Python SDK reference](training-sessions-sdk.md).

## Quickstart: supervised fine-tuning
<a name="training-sessions-getting-started-quickstart"></a>

The following example opens a session, runs one supervised fine-tuning (SFT) step on two prompt and response pairs with the `cross_entropy` loss, saves a checkpoint, and stops the session.

Install the SDK. The `tokenizer` extra provides the `get_tokenizer()` method the example uses.

```
pip install 'sagemaker-train[tokenizer]>=1.25.0'
```

Then run:

```
from sagemaker.train.training_session import ServiceClient, AdamParams
from sagemaker.train.training_session._utils import _serialize_loss_fn_inputs

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
tc = svc.create_lora_training_client(base_model="<name from list_base_models()>", rank=32, alpha=64)
tok = tc.get_tokenizer()

batch = []
for prompt, response in PAIRS:
    prompt_ids = tok.encode(prompt, add_special_tokens=False)
    ids = tok.encode(prompt + response, add_special_tokens=False)
    prompt_len = len(prompt_ids)
    eos = tok.eos_token_id if tok.eos_token_id is not None else ids[-1]
    target_tokens = ids[1:] + [eos]
    weights = [0.0] * prompt_len + [1.0] * (len(ids) - prompt_len)
    batch.append({
        "modelInput": {"chunks": [{"tokens": ids, "type": "encoded_text"}]},
        "lossFnInputs": _serialize_loss_fn_inputs(
            {"target_tokens": target_tokens, "weights": weights}
        ),
    })

fwd_bwd = tc.forward_backward(batch, loss_fn="cross_entropy")
step = tc.optim_step(AdamParams(learning_rate=5e-5))
print(fwd_bwd.result().metrics, step.result().metrics)

print(tc.save_state().result().model_package_arn)
tc.stop()
```

Each entry in `batch` is one training example: the token IDs of the prompt and response, the next token to predict at each position, and a weight per position. A weight of `0.0` excludes the prompt from the loss, so the model learns only the response. `forward_backward` and `optim_step` each return a future immediately, so the optimizer step is queued behind the forward-backward pass; call `.result()` to wait for the metrics.

Available base models vary by Region — call `list_base_models()` instead of hard-coding a list.

**Important**  
You are charged for the tokens a session processes (prefill, sample, and train). An active session also counts against your concurrent-session quota. Call `tc.stop()` when you finish, including in error paths, so an abandoned session does not hold quota or accept further billable operations. For pricing details, see [Supported models, pricing, and Regions](customizing-models-training-sessions.md#training-sessions-models-pricing-regions).

## Training sessions cookbook
<a name="training-sessions-getting-started-cookbook"></a>

The [training sessions cookbook](https://github.com/aws/sagemaker-training-sessions-cookbook) on GitHub provides complete training loops with logging, evaluation, and helper utilities. For the list of recipes, see [End-to-end examples](training-sessions-example.md).