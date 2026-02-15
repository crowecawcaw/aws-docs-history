# Reasoning model evaluation

## Overview

Reasoning model support enables evaluation with reasoning-capable Nova models that perform explicit internal reasoning before generating final responses. This feature uses API-level control via the `reasoning_effort` parameter to dynamically enable or disable reasoning functionality, potentially improving response quality for complex analytical tasks.

**Supported models**

- amazon.nova-2-lite-v1:0:256k

## Recipe configuration

Enable reasoning by adding the `reasoning_effort` parameter to the `inference` section of your recipe:

```
run:
  name: reasoning-eval-job-name                          # [MODIFIABLE] Unique identifier for your evaluation job
  model_type: amazon.nova-2-lite-v1:0:256k               # [FIXED] Must be a reasoning-supported model
  model_name_or_path: nova-lite-2/prod                   # [FIXED] Path to model checkpoint or identifier
  replicas: 1                                            # [MODIFIABLE] Number of replicas for SageMaker Training job
  data_s3_path: ""                                       # [MODIFIABLE] Leave empty for SageMaker Training job; optional for SageMaker HyperPod job
  output_s3_path: ""                                     # [MODIFIABLE] Output path for SageMaker HyperPod job (not compatible with SageMaker Training jobs)

evaluation:
  task: mmlu                                             # [MODIFIABLE] Evaluation task
  strategy: zs_cot                                       # [MODIFIABLE] Evaluation strategy
  metric: accuracy                                       # [MODIFIABLE] Metric calculation method

inference:
  reasoning_effort: high                                 # [MODIFIABLE] Enables reasoning mode; options: low/high or null to disable
  max_new_tokens: 32768                                  # [MODIFIABLE] Maximum tokens to generate, recommended value when reasoning_effort set to high
  top_k: -1                                              # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0                                             # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0                                         # [MODIFIABLE] Sampling temperature (0 = deterministic)
```

## Using the reasoning_effort parameter

The `reasoning_effort` parameter controls the reasoning behavior for reasoning-capable models.

### Prerequisites

- **Model compatibility** – Set `reasoning_effort` only when `model_type` specifies a reasoning-capable model (currently `amazon.nova-2-lite-v1:0:256k`)
- **Error handling** – Using `reasoning_effort` with unsupported models will fail with `ConfigValidationError: "Reasoning mode is enabled but model '{model_type}' does not support reasoning. Please use a reasoning-capable model or disable reasoning mode."`

### Available options

| Option         | Behavior                              | Token limit                          | Use case                                                                 |
| -------------- | ------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------ |
| null (default) | Disables reasoning mode               | N/A                                  | Standard evaluation without reasoning overhead                           |
| low            | Enables reasoning with constraints    | 4,000 tokens for internal reasoning  | Scenarios requiring concise reasoning; optimizes for speed and cost      |
| high           | Enables reasoning without constraints | No token limit on internal reasoning | Complex problems requiring extensive analysis and step-by-step reasoning |

| Training method                 | Available options | How to configure                                                            |
| ------------------------------- | ----------------- | --------------------------------------------------------------------------- |
| SFT (Supervised Fine-Tuning)    | High or Off only  | Use reasoning_enabled: true (high) or reasoning_enabled: false (off)        |
| RFT (Reinforcement Fine-Tuning) | Low, High, or Off | Use reasoning_effort: low or reasoning_effort: high. Omit field to disable. |
| Evaluation                      | Low, High, or Off | Use reasoning_effort: low or reasoning_effort: high. Use null to disable.   |

### When to enable reasoning

**Use reasoning mode (`low` or `high`) for**

- Complex problem-solving tasks (mathematics, logic puzzles, coding)
- Multi-step analytical questions requiring intermediate reasoning
- Tasks where detailed explanations or step-by-step thinking improve accuracy
- Scenarios where response quality is prioritized over speed

**Use non-reasoning mode (`null` or omit parameter) for**

- Simple Q&A or factual queries
- Creative writing tasks
- When faster response times are critical
- Performance benchmarking where reasoning overhead should be excluded
- Cost optimization when reasoning doesn't improve task performance

### Troubleshooting

**Error: "Reasoning mode is enabled but model does not support reasoning"**

**Cause**: The `reasoning_effort` parameter is set to a non-null value, but the specified `model_type` doesn't support reasoning.

**Resolution**:

- Verify your model type is `amazon.nova-2-lite-v1:0:256k`
- If using a different model, either switch to a reasoning-capable model or remove the `reasoning_effort` parameter from your recipe
