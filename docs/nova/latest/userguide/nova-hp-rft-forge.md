# Reinforcement Learning

###### Note

Detailed documentation is provided once subscribed

Nova Forge provides advanced reinforcement learning capabilities with the option to use remote reward functions in your own environment. Customers can choose to integrate their own endpoint to execute validation for immediate real-world feedback, or even use their own orchestrator to coordinate agentic multi-turn evaluations in your environment.

## Bring your own orchestrator for agentic multi-turn evaluations

For Forge users requiring multi-turn conversations or reward functions exceeding
15-minute timeouts, Nova Forge provides Bring Your Own Orchestration (BYOO)
capabilities. This allows you to coordinate agentic multi-turn evaluations in your environment (e.g., using chemistry tools to score molecular designs, or robotics simulations that reward efficient task completion and penalize collisions).

###### Topics

- [Architecture overview](#nova-hp-rft-forge-architecture "#nova-hp-rft-forge-architecture")
- [BYOO setup](#nova-hp-rft-forge-setup "#nova-hp-rft-forge-setup")
- [Data preparation for custom RL
  environments](#nova-hp-rft-forge-data-prep "#nova-hp-rft-forge-data-prep")
- [BYOO recipe configuration](#nova-hp-rft-forge-recipe "#nova-hp-rft-forge-recipe")
- [BYOO request and response
  formats](#nova-hp-rft-forge-formats "#nova-hp-rft-forge-formats")
- [BYOO environment](#nova-hp-rft-forge-environment "#nova-hp-rft-forge-environment")

### Architecture overview

The BYOO architecture provides full control over the rollout and generation
process through customer-managed infrastructure.

**Training VPC:**

- **Rollout**: Coordinates training by
  delegating rollout generation to customer infrastructure
- **Trainer**: Performs model weight
  updates based on received rollouts

**Customer VPC (such as ECS on EC2):**

- **Proxy Lambda**: Receives rollout
  requests and coordinates with customer infrastructure
- **Rollout Response SQS**: Queue for
  returning completed rollouts to training infrastructure
- **Generate Request SQS**: Queue for model
  generation requests
- **Generate Response SQS**: Queue for
  model generation responses
- **Customer Container**: Implements custom
  orchestration logic (can use provided starter kit)
- **DynamoDB**: Stores and retrieves state
  across the orchestration process

**Workflow:**

1. Rollout delegates rollout generation to Proxy Lambda
2. Proxy Lambda pushes rollout API request to Generate Request SQS
3. Customer container processes requests, manages multi-turn
   interactions, and calls reward functions
4. Container stores and retrieves state from DynamoDB as needed
5. Container pushes rollout responses to Rollout Response SQS
6. Rollout sends completed rollouts to Trainer for weight updates

### BYOO setup

**Prerequisites:**

- Install SAM CLI: [Amazon Web Services Serverless Application Model (AWS SAM)
  documentation](../../../serverless-application-model/latest/developerguide/install-sam-cli.md "../../../serverless-application-model/latest/developerguide/install-sam-cli.md")
- Get SAM code from NovaRFTBundles repository:
  `NovaRFTEnvBundles/trees/mainline/—/lambda_proxy#`

**Deployment steps:**

Deploy this for every new environment you are running in parallel. Three
Lambda functions and four SQS queues will be created using this code. The
deployment corresponds to the middle portion of the architecture diagram, to
enable communication between the training cluster and the client.

```
sam build
sam deploy --guided \
  --stack-name <Your Stack Name> \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides ProjectName=<your-project-name>
```

### Data preparation for custom RL

environments

###### Important

Custom RL environments with BYOO are configured during **training** using the `rollout.delegate:
 true` setting and BYOO infrastructure parameters. The
`rl_env` field mentioned in some examples is only used during
**evaluation** to specify how to evaluate
the trained model, not during training itself.

For use cases requiring custom RL environments or agents, the
`messages` and `tools` fields are optional. Use this
format to build your dataset:

```
{
  "id": "wordle_001",
  "messages": [],
  "tools": [],
  "metadata": {
    "answer": "crane",
    "problem": "Guess: crane"
  }
}
```

The metadata will be passed as-is in the rollout request. For more details,
refer to the Rollout Request documentation.

### BYOO recipe configuration

###### Note

Remote reward functions in your own Amazon Web Services environment do **not** use the `rl_env` field. Instead,
they use `rollout.delegate: true` to hand off orchestration to
your custom infrastructure. The `rl_env` field is only used
during evaluation to specify how to evaluate the trained model. Note that
`data_s3_path` is mandatory, and corresponds to the initial
prompts that will be used to start the conversation between the Nova model
and the environment.

The `max_seq_length` includes the full context length the model is
expected to get during the multi-turn conversation. The number of tokens builds
up quickly with each turn, and should be set taking into consideration the
response length.

Similarly, the `rollout.timeout` is the maximum time in seconds the
entire conversation between the trainer and environment is expected to take. A
timeout will result in training failure.

The recipe is designed for high throughput communication between the trainer
and environment. By design, the training cluster will create many requests to
the environment in parallel, and the BYOO environment should be designed to
handle such requests.

```
run:
  name: <run-name>
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://<bucket-name>/train.jsonl # required
  output_s3_path: s3://path/to/output/checkpoint
  replicas: 4
  generation_replicas: 2
  rollout_worker_replicas: 1
  rollout_request_arn: <rollout-proxy-lambda-arn>
  rollout_response_sqs_url: <rollout-response-queue-url>
  generate_request_sqs_url: <generate-request-queue-url>
  generate_response_sqs_url: <generate-response-queue-url>

training_config:
  max_steps: 100
  max_seq_length: 9392
  global_batch_size: 1024
  reasoning_effort: high                               # Options: low, high, or omit for no reasoning

  data:                                 # Or multi-turn for multi-turn conversations
    shuffle: false

  rollout:
    delegate: true                                     # Enables BYOO mode
    timeout: 600                                       # 10 minutes timeout for rollout completion
    rollout_strategy:
      type: off_policy_async
      age_tolerance: 2
    advantage_strategy:
      number_generation: 16
    generator:
      server_count: ${run.generation_replicas}
      timeout: 1000
      max_model_len: ${training_config.max_seq_length}
      max_new_tokens: 18000
      set_random_seed: true
      temperature: 1
      top_k: 0

  train:
    replicas: ${run.replicas}
    max_steps: ${training_config.max_steps}
    global_batch_size: ${training_config.global_batch_size}
    save_steps: 10
    save_top_k: 5

    # RL parameters [Advanced]
    clip_ratio_high: 0.2
    ent_coeff: 0.001
    loss_scale: 1

    # Optimizer settings
    optim:
      lr: 1e-7
      optimizer: 'adam'
      weight_decay: 0.01
      adam_beta1: 0.9
      adam_beta2: 0.95
      warmup_steps: 5
      min_lr: 1e-5
```

Launch the recipe with the `hyperpod start-job` command similar to
other HyperPod recipes. Run the BYOO environment in parallel, details of which
are given below.

### BYOO request and response

formats

**Rollout request:**

Sent from training infrastructure to your Proxy Lambda:

```
{
  "version": "v0",
  "timestamp": "2025-10-28T...",
  "sample_id": "sample-000_0",
  "max_length": 10240,
  "rewards": {
    "range": [0.0, 1.0]
  },
  "data": {
    "problem": "How many six-digit numbers are there in which all digits are odd? Let's think step by step and output the final answer within \\boxed{}.",
    "answer": "15625"
  }
}
```

**Generate request:**

Sent from your orchestration logic to request model generation:

```
{
  "version": "v0",
  "sample_id": "sample-000_0",
  "step_id": "sample-000_0_0",
  "messages": [
    {
      "role": "user",
      "content": "How many six-digit numbers are there in which all digits are odd? Let's think step by step and output the final answer within \\boxed{}."
    }
  ]
}
```

**Generate response:**

Returned from model generation service:

```
{
  "version": "v0",
  "sample_id": "sample-000_0",
  "step_id": "sample-000_0_0",
  "data": {
    "choices": [{
      "message": {
        "content": "To determine how many six-digit numbers..."
      },
      "finish_reason": "stop",
      "logprobs": {
        "content": [
          {"token": "token_id:123", "logprob": -0.5}
        ]
      }
    }],
    "serving_model_num": 0
  },
  "finish_reason": "stop"
}
```

**Rollout response:**

Sent from your orchestration logic back to training infrastructure:

```
{
  "version": "v0",
  "sample_id": "sample-000_0",
  "stop_reason": "end_of_conversation",
  "rewards": {
    "aggregate_score": 0.85
  }
}
```

### BYOO environment

To facilitate setting up your own environment, Nova Forge includes examples of
sample environments along with code to launch the environment with appropriate
configuration.

**Installation:**

- Install the `verifiers` package provided with Nova Forge.
  You can also install the environments you are interested in testing such
  as `wordle` by navigating to
  `verifiers/environments/wordle/` and running `pip
install -e .`
- Navigate to `NovaRFTEnvBundles/nova-rl-async-client` and
  run `pip install -e .`
- Navigate to `NovaRFTEnvBundles/nova-rl-async-client/src` to
  see examples of training and evaluation clients. A sample configuration
  is given below for wordle environment.

**Train client configuration:**

```
@chz.chz
class CLIConfig:
    # SQS configuration
    # rollout request queue
    queue_url: str = "https://sqs.us-east-1.amazonaws.com/<account_id>/<project-name>-SageMaker-RolloutRequestQueue.fifo"
    region_name: str = "us-east-1"
    groups_per_batch: int = 4
    max_messages_per_poll: int = 10

    # Client configuration (for model inference)
    # proxy lambda
    client_base_url: str = "https://<proxy-lambda-id>.lambda-url.<region>.on.aws/"
    client_region: str = "us-east-1"
    client_service: str = "lambda"
    client_timeout: float = 600.0
    client_poll_interval: float = 0.5

    # environment configuration
    vf_env_id: str = "wordle"
    vf_env_args: str | None = None

    # rollout configuration
    group_size: int = 1
    model_name: str = "nova-rl"

    # processing control
    max_batches: int | None = None  # None = process until queue empty
    continuous: bool = True  # If True, keep polling forever
```

**Evaluation client configuration:**

```
@chz.chz
class CLIConfig:
    # Model configuration
    model_name: str = "nova"

    # Environment configuration
    vf_env_id: str = "wordle"
    vf_env_args: str | None = None # '{"max_examples": 1, "max_turns": 5}'  # JSON string

    # Evaluation configuration
    num_examples: int = 1
    rollouts_per_example: int = 1
    max_concurrent: int = 32

    # Sampling configuration
    max_tokens: int = 1024
    temperature: float = 0.0

    # Client configuration
    # proxy lambda
    client_base_url: str = "https://<proxy-lambda-id>.lambda-url.us-east-1.on.aws/"
    client_region: str = "us-east-1"
    client_service: str = "lambda"
    client_timeout: float = 3000.0
    client_poll_interval: float = 0.5
```
