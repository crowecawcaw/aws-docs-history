# How Advanced Prompt Optimization works

## Overview

Advanced Prompt Optimization (AdvPO) allows you to optimize your prompts for any
model on Bedrock while comparing your original prompts to optimized prompts across up to 5
models simultaneously. You can use this if you are migrating to a new model or just want to
get better performance on your current model. If you are changing models, select your current
model as a baseline and up to 4 other models. If you are not changing models, just select
your current model to see before and after optimization. The optimizer takes your prompt
templates (up to 10 per job), example user inputs for variable values (evaluation samples, up to 100 per prompt
template), ground truth answers, and an evaluation metric to guide the optimization. It's
even compatible with multimodal inputs such as JPG, JPEG, PNG, GIF, WebP, or PDF. You can provide an
LLM-as-a-judge rubric, a Lambda function, or short natural language steering criteria. The
evaluation steers the prompt optimization. The optimizer works in an evaluation-based
feedback loop to optimize the prompt and resulting model responses, and outputs the original
and final prompt templates with evaluation scores, cost estimates, and latency.

If you want to migrate prompts from a non-Bedrock model and still want to have side-by-side
comparisons, one way you can do that is to run inference on your non-Bedrock model separately,
then apply a [Custom Lambda evaluator](advanced-prompt-optimization-evaluation.md#advanced-prompt-optimization-evaluation-lambda "advanced-prompt-optimization-evaluation.md#advanced-prompt-optimization-evaluation-lambda") to score those results. Then, create an
Advanced Prompt Optimization job with the same Lambda function evaluator for your Bedrock target models.
That way, you can have a direct comparison of your old model to your new model before and after
prompt optimization.

## How the optimization loop works

Your evaluation samples are injected into the placeholder variables in your prompt
template, then sent for inference with your target model(s). Multimodal inputs (images
and PDFs) are sent in the payload to the model along with the prompt but should not be
referenced in a double curly bracket `{{placeholder}}` variable. The responses are graded
according to your evaluation method. The service analyzes the evaluation results and
automatically rewrites your prompts, then sends them back to the models. This feedback
loop repeats and completes according to proprietary internal optimization
parameters.

It is important that you define your evaluation method and criteria as precisely as
possible, because the evaluation steers the prompt optimization.

Both the dataset and the metric/lambda code shape the optimization quality. The system
uses your dataset to test prompt candidates, and reads your metric code (source text and
docstrings) to understand what "good" means and to diagnose where prompts fail.

By default, the optimizer rewrites any part of your entire prompt template. To limit optimization
to specific sections of your template, use `<advpo:optimize>` or
`<advpo:exclude>` tags. For example, the following template optimizes only the
response instructions while preserving the rest:

```
You are a customer service agent. Always be polite and professional.

<advpo:optimize>When responding to a complaint, summarize the issue and propose one resolution.</advpo:optimize>

Never disclose internal pricing or employee information.
```

For more information, see
[Selective optimization](advanced-prompt-optimization-selective.md "advanced-prompt-optimization-selective.md").

## What you receive

At the end of the optimization job, you receive:

- Your prompt templates before and after optimization
- Evaluation scores for each evaluation sample
- Latency (time to first token, or TTFT) for each model
- Cost estimates for each model

## Cost

All inference and Lambda function invocations run in your AWS account. Lambda
operations are charged at Lambda's public pricing. Inference pricing (including
LLM-as-a-judge evaluations) is charged according to Bedrock's public pricing for
on-demand inference. There is no separate Advanced Prompt Optimization service charge
beyond inference costs. The current default LLM-as-a-judge model is Anthropic Claude
Sonnet 4.6, unless you select a different one for your custom LLMJ prompt.

See the Bedrock public pricing page under Prompt Optimization, then Advanced Prompt
Optimization for a calculation method to estimate the cost of running an
optimization.

## Expected duration

For a single prompt with only a few evaluation samples, the job could run for 15 to 20
minutes. For many prompts, each with a large number of evaluation samples, the job could
run for over an hour, potentially for multiple hours. This is because each prompt
template goes through multiple rounds of inference, evaluation, and rewriting loops based
on every evaluation sample record you provide.
