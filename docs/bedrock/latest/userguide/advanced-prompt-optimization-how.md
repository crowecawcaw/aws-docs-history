# How Advanced Prompt Optimization works

## Overview

Advanced Prompt Optimization takes your prompt templates, evaluation samples, and an
evaluation method, then runs iterative inference, evaluate, and rewrite loops. It outputs
optimized prompts with evaluation metrics for each target model. It supports multimodal
inputs including png, jpg, and PDF files.

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
