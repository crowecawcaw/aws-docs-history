# Evaluate the performance of optimized

models

After you use an optimization job to create an optimized model, you can run an evaluation
of model performance. This evaluation yields metrics for latency, throughput, and price. Use
these metrics to determine whether the optimized model meets the needs of your use case or
whether it requires further optimization.

You can run performance evaluations only by using Studio. This feature is not
provided through the Amazon SageMaker AI API or Python SDK.

## Before you begin

Before you can create a performance evaluation, you must first optimize a model by
creating an inference optimization job. In Studio, you can evaluate only the models
that you create with these jobs.

## Create the performance evaluation

Complete the following steps in Studio to create a performance evaluation for an
optimized model.

1. In the Studio navigation menu, under **Jobs**, choose
   **Inference optimization**.
2. Choose the name of the job that created the optimized model that you want to
   evaluate.
3. On the job details page, choose **Evaluate
   performance**.
4. On the **Evaluate performance** page, some JumpStart
   models require you to sign an end-user license agreement (EULA) before you can
   proceed. If requested, review the license terms in the **License
   agreement** section. If the terms are acceptable for your use case,
   select the checkbox for **I accept the EULA, and read the terms and
   conditions.**
5. For **Select a model for tokenizer**, accept the default, or
   a choose a specific model to act as the tokenizer for your evaluation.
6. For **Input datasets**, choose whether to:
   - Use the default sample datasets from SageMaker AI.
   - Provide an S3 URI that points to your own sample datasets.

7. For **S3 URI for performance results**, provide a URI that
   points to the location in Amazon S3 where you want to store the evaluation
   results.
8. Choose **Evaluate**.

Studio shows the **Performance evaluations** page, where
your evaluation job is shown in the table. The **Status**
column shows the status of your evaluation. 9. When the status is **Completed**, choose the name of the job
to see the evaluation results.

The evaluation details page shows tables that provide the performance metrics for
latency, throughput, and price. For more information about each metric, see the [Metrics reference for inference
performance evaluations](#performance-eval-metrics-reference "#performance-eval-metrics-reference").

## Metrics reference for inference

performance evaluations

After you successfully evaluate the performance of an optimized model, the evaluation
details page in Studio shows the following metrics.

### Latency metrics

The **Latency** section shows the following metrics

**Concurrency**

The number of concurrent users that the evaluation simulated to invoke
the endpoint simultaneously.

**Time to first token (ms)**

The time that elapsed between when request is sent and when the first
token of a streaming response is received.

**Inter-token latency (ms)**

The time to generate an output token for each request.

**Client latency (ms)**

The request latency from the time the request is sent to the time the
entire response is received.

**Input tokens/sec (count)**

The total number of generated input tokens, across all requests,
divided by the total duration in seconds for the concurrency.

**Output tokens/sec (count)**

The total number of generated output tokens, across all requests,
divided by total duration in seconds for the concurrency.

**Client invocations (count)**

The total number of inference requests sent to the endpoint across all
users at a concurrency.

**Client invocation errors (count)**

The total number of inference requests sent to the endpoint across all
users at a given concurrency that resulted in an invocation
error.

**Tokenizer failed (count)**

The total number of inference requests where the tokenizer failed to
parse the request or the response.

**Empty inference response (count)**

The total number of inference requests that resulted in zero output
tokens or the tokenizer failing to parse the response.

### Throughput metrics

The **Throughput** section shows the following metrics.

**Concurrency**

The number of concurrent users that the evaluation simulated to invoke
the endpoint simultaneously.

**Input tokens/sec/req (count)**

The total number of generated input tokens per second per
request.

**Output tokens/sec/req (count)**

The total number of generated output tokens per second per
request.

**Input tokens (count)**

The total number of generated input tokens per request.

**Output tokens (count)**

The total number of generated output tokens per request.

### Price metrics

The **Price** section shows the following metrics.

**Concurrency**

The number of concurrent users that the evaluation simulated to invoke
the endpoint simultaneously.

**Price per million input tokens**

Cost of processing 1M input tokens.

**Price per million output tokens**

Cost of generating 1M output tokens.
