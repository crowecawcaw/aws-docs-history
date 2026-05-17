# Optimize and migrate prompts in Amazon Bedrock

Amazon Bedrock offers prompt optimization, a model migration and optimization tool that helps you
get the best performance from foundation models. Amazon Bedrock provides two prompt optimization
options. [Simple optimization](prompt-management-optimize.md "prompt-management-optimize.md") performs a fast, heuristic rewrite of a single short prompt for
one model. [Advanced Prompt Optimization](advanced-prompt-optimization-how.md "advanced-prompt-optimization-how.md") (AdvPO) allows you to optimize your prompts for any
model on Bedrock while comparing your original prompts to optimized prompts across up to 5
models simultaneously. You can use this if you are migrating to a new model or just want to
get better performance on your current model. If you are changing models, select your current
model as a baseline and up to 4 other models. If you are not changing models, just select
your current model to see before and after optimization. The optimizer takes your prompt
templates (up to 10 per job), example user inputs for variable values (up to 100 per prompt
template), ground truth answers, and an evaluation metric to guide the optimization. It's
even compatible with multimodal inputs such as jpg, png, or PDF. You can provide an
LLM-as-a-judge rubric, a Lambda function, or short natural language steering criteria. The
evaluation steers the prompt optimization. The optimizer works in an evaluation-based
feedback loop to optimize the prompt and resulting model responses, and outputs the original
and final prompt templates with evaluation scores, cost estimates, and latency.

## Choose an optimization method

|                     | Simple optimization                                          | Advanced Prompt Optimization                                                                                                   |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **Use case**        | Basic single-prompt rewrite for short prompts                | Flexible, iterative optimization where your evaluation steers the prompt rewriting, for model migration and performance tuning |
| **Best for**        | Short prompts (approximately 1k tokens or less)              | Prompt templates of any length that fits in the model's context window                                                         |
| **Input**           | Single prompt text                                           | Up to 10 prompt templates with evaluation samples, including multimodal                                                        |
| **Models**          | 1 model                                                      | Up to 5 models compared simultaneously                                                                                         |
| **Evaluation**      | None (heuristic rewrite)                                     | Your choice: steering criteria, LLM-as-judge rubric, or custom Lambda function                                                 |
| **Output**          | Rewritten prompt (instant)                                   | Optimized templates with evaluation scores, cost estimates, and latency per model                                              |
| **Execution**       | Synchronous (seconds)                                        | Asynchronous job (15 min to hours, depending on number of prompt templates and evaluation samples)                             |
| **Multimodal**      | No                                                           | Yes (images, PDFs)                                                                                                             |
| **Model migration** | Partial: can rewrite prompts, but no side by side comparison | Yes, compare current model against candidates side by side                                                                     |

###### Topics

- [How Advanced Prompt Optimization works](advanced-prompt-optimization-how.md "advanced-prompt-optimization-how.md")
- [Prerequisites and permissions](advanced-prompt-optimization-prereqs.md "advanced-prompt-optimization-prereqs.md")
- [Prepare your input dataset](advanced-prompt-optimization-input.md "advanced-prompt-optimization-input.md")
- [Create and manage optimization jobs](advanced-prompt-optimization-jobs.md "advanced-prompt-optimization-jobs.md")
- [Define evaluation methods](advanced-prompt-optimization-evaluation.md "advanced-prompt-optimization-evaluation.md")
- [View and interpret results](advanced-prompt-optimization-results.md "advanced-prompt-optimization-results.md")
- [Supported Regions, models, and quotas](advanced-prompt-optimization-quotas.md "advanced-prompt-optimization-quotas.md")
- [Troubleshooting](advanced-prompt-optimization-troubleshooting.md "advanced-prompt-optimization-troubleshooting.md")

- [Simple optimization](prompt-management-optimize.md "prompt-management-optimize.md") (Optimize a prompt in Prompt management)
