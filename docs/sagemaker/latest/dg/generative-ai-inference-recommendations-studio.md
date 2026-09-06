

# Get inference recommendations by using Amazon SageMaker Studio
<a name="generative-ai-inference-recommendations-studio"></a>

With Amazon SageMaker Studio, you get a guided, end-to-end console experience for generative AI inference recommendations. Instead of writing code to call the API, you configure an optimization job through a visual workflow: choose a preset use case profile, set an optimization goal, select your model and compute, and then review and deploy ranked, deployment-ready configurations. This experience uses the same benchmarking infrastructure as the API. When you use the API, the same workflow is called an AI recommendation job. For more information about the API workflow, see [Get generative AI inference deployment recommendations](generative-ai-inference-recommendations-get-started.md).

The inference recommendations experience is available in Studio under **Jobs**, **Inference optimization**.

## Prerequisites
<a name="generative-ai-inference-recommendations-studio-prereqs"></a>

You don't need prior experience with Amazon SageMaker Studio or generative AI model deployment to complete this task. Before you create an inference optimization job in Studio, you need the following:
+ An AWS account with a Amazon SageMaker Studio domain.
+ IAM permissions for SageMaker AI inference optimization operations.
+ An IAM execution role that grants SageMaker AI access to your model artifacts in Amazon S3. For more information, see [How to use SageMaker AI execution roles](sagemaker-roles.md).

**Pricing**  
Generating recommendations incurs no additional cost. Standard compute costs apply for the optimization jobs and the endpoints that SageMaker AI provisions during benchmarking. SageMaker AI automatically deletes these endpoints when the job completes. For pricing information, see [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/).

## Step 1: Create an optimization job
<a name="generative-ai-inference-recommendations-studio-create"></a>

1. Open the Amazon SageMaker Studio application.

1. In the left navigation pane, under **Jobs**, choose **Inference optimization**.

   The **Inference optimization** page lists your existing jobs, sorted newest first, with their **Name**, **Status**, **Base model**, and **Created on** date.

1. Choose **Create**. Studio opens the job configuration page, which contains the **Strategy**, **Model**, and **Compute** sections that you complete in the following steps.

![The Inference optimization landing page in Studio, showing the list of existing jobs and the Create button.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-landing.png)


## Step 2: Configure your strategy
<a name="generative-ai-inference-recommendations-studio-strategy"></a>

In the **Strategy** section, you select a preset use case profile and an optimization goal. The profile determines the traffic pattern that SageMaker AI benchmarks against, so you don't have to specify token distributions and concurrency manually.

1. For **Use-case**, choose the profile that best describes your primary workload's traffic:  
**Generate**  
Optimized for short inputs and long outputs, such as code generation.  
**Interact**  
Optimized for fast, multi-turn exchanges with balanced input and output, such as multi-turn chat.  
**Summarize**  
Optimized for long inputs and short outputs. Condenses lengthy documents into concise summaries.  
**Custom**  
Bring your own dataset and parameters. Manually add your data and enter your concurrency and output token length.

1. For **Optimization goal**, choose how SageMaker AI balances cost, latency, and throughput for the optimized model:  
**Minimize cost**  
Finds the cheapest infrastructure cost for low-volume workloads.  
**Minimize latency**  
Prioritizes responsiveness over throughput and cost.  
**Maximize throughput**  
Serves the maximum number of tokens per second for high-volume workloads.

![The Strategy section showing the Use-case presets and Optimization goal options.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-strategy.png)


If you choose **Custom**, additional fields appear so that you can benchmark against your own representative data:

**Data (S3)**  
Enter or browse to the Amazon S3 URI of your evaluation dataset, in JSON Lines (JSONL) format. SageMaker AI uses this data for model optimization and benchmarking.

**Concurrency**  
Enter the number of concurrent users (simultaneous requests) to simulate.

**Output tokens**  
Enter the mean number of output tokens per request.

![The Custom use-case fields: Data (S3), Concurrency, and Output tokens.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-custom.png)


## Step 3: Select your model
<a name="generative-ai-inference-recommendations-studio-model"></a>

In the **Model** section, choose **Select**. The **Select model** dialog box opens with a tab for each supported model source. Choose the tab for your model source, provide the requested information, and then choose **Select**.

**JumpStart**  
Browse the JumpStart catalog and choose a foundation model (for example, `gpt-oss-20b` or `meta-textgeneration-llama-3-1-8b-instruct`). Use the search box to filter by name; the table shows the model **Name**, **Provider**, and **Task**. If the model requires it, accept the end-user license agreement (EULA) when prompted.

**Logged**  
Search for a registered model package group from your SageMaker AI Model Registry. Models that you customized with a model customization job also appear here. The artifact URI resolves automatically.

**Deployable**  
Search for an existing SageMaker AI model by name (for example, a model from a previous deployment or training job). The artifact URI resolves from the model metadata.

**S3**  
Bring your own model artifact. For **Name**, enter a name for the model. For **Artifact (S3)**, enter or browse to the Amazon S3 URI of your model artifact (for example, `s3://{{amzn-s3-demo-bucket}}/model.tar.gz`).

![The Select model dialog box on the JumpStart tab, with tabs for JumpStart, Logged, Deployable, and S3.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-model-jumpstart.png)


![The Select model dialog box on the S3 tab, showing the Name and Artifact (S3) fields.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-model-s3.png)


## Step 4: Select compute (optional)
<a name="generative-ai-inference-recommendations-studio-compute"></a>

If you chose **Minimize latency** or **Maximize throughput** as your optimization goal, you can optionally expand the **Compute** section to control which instances SageMaker AI evaluates.

**Source**  
Choose between default on-demand compute and reserved capacity. If you have reserved capacity from a SageMaker AI flexible training plan, it appears in this dropdown list.

**Instance(s)**  
Select up to three instance types for SageMaker AI to evaluate and benchmark (for example, `ml.g6e.2xlarge` and `ml.g7e.2xlarge`). If you don't select any instances, SageMaker AI chooses compatible instances based on your model's requirements.

**Instance selection**  
For the **Minimize cost** goal, SageMaker AI selects a recommended instance for you, so you can't select instances.

![The Compute section showing the Source dropdown and selected instance types under Instance(s).](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-compute.png)


## Step 5: Launch the job
<a name="generative-ai-inference-recommendations-studio-launch"></a>

When you complete the job configuration, choose **Optimize** to submit it. SageMaker AI opens the job's detail page, where the **Status** transitions from **Running** to **Completed**. For preset use cases such as **Interact**, SageMaker AI matches your workload against pre-validated configurations, which can return recommendations faster than a custom benchmark. For custom benchmarks, jobs typically take one to three hours.

Use the tabs on the detail page to inspect the job:

**Overview**  
The ranked recommendations with their performance metrics. This tab populates when the job completes.

**Settings**  
The configuration you submitted, including the base model, use case, goal, and compute.

**Details**  
Job metadata, timestamps, and output artifacts.

To stop a running job, choose **Actions**, and then choose **Stop**.

![A running optimization job detail page showing the Actions button, the Settings tab, and the Running status.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-running.png)


## Step 6: Monitor and troubleshoot
<a name="generative-ai-inference-recommendations-studio-monitor"></a>

After you submit the job, the **Status** shows **Running** for a period that depends on the number of instance types you selected, whether you provided a custom dataset, and the optimization goal. The job can take anywhere from a few minutes to several hours. Depending on the optimization goal, the job runs different steps that you can monitor from other Studio pages:

**Minimize cost**  
SageMaker AI creates an endpoint using the recommended instance type and runs benchmark jobs. To check the endpoint, in **Deployments**, choose **Endpoints** and look for the **InService** status. To review the benchmark runs, in **Jobs**, choose **Training** and find your job under **Training Jobs**.

**Minimize latency**  
SageMaker AI creates one or more endpoints, one per instance type. If the model architecture and instance type support a kernel-tuned deployment, SageMaker AI uses that deployment type. Otherwise, SageMaker AI uses a standard deployment. SageMaker AI then runs a benchmark training job for each combination. Monitor both the **Endpoints** and **Training** pages to view the logs.

**Maximize throughput**  
If the model architecture and instance type support speculative decoding, a training job runs first to train the draft model, and then SageMaker AI deploys the endpoints. Monitor both the **Endpoints** and **Training** pages to view the logs. For more information, see [Speculative decoding](model-optimize.md#speculative-decoding).

**Endpoint cleanup**  
SageMaker AI automatically deletes the endpoints that the optimization job creates after the job completes.

![The Endpoints page showing InService endpoints created by the inference optimization job for each selected instance type.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-endpoints.png)


![The Training Jobs page showing In progress benchmark training jobs for each benchmark test configuration.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-training.png)


## Step 7: Review recommendations and deploy
<a name="generative-ai-inference-recommendations-studio-review"></a>

When the job completes, the **Overview** tab displays the ranked inference packages that SageMaker AI generated from benchmarks performed by [NVIDIA AIPerf](https://github.com/ai-dynamo/aiperf) on the GitHub website. Each package shows its optimized configuration, its performance metrics (such as Time to First Token (TTFT), inter-token latency (ITL), throughput, and cost), the recommended instance type, and a **Deploy** button.

![A completed job showing the ranked, optimized inference packages with their metrics and Deploy buttons.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/gen-ai-rec-studio-results.png)


1. Review the ranked packages and their metrics, and choose **Deploy** on your preferred package.

1. In the deployment dialog box, SageMaker AI pre-fills the endpoint name and instance type. Choose to deploy to a new endpoint or to update an existing endpoint.

   When you confirm, SageMaker AI runs the following operations for you:
   + `CreateModel` — Registers the optimized model.
   + `CreateEndpointConfig` — Sets up the endpoint configuration.
   + `CreateEndpoint` — Provisions the endpoint.

1. Wait for the endpoint to reach the **InService** status. You can then invoke it to serve inference requests.

## Manage optimization jobs
<a name="generative-ai-inference-recommendations-studio-manage"></a>

The **Jobs**, **Inference optimization** page provides centralized management of your jobs:
+ **Search and filter.** Use the search bar to filter jobs by name.
+ **Stop a running job.** Select a job, choose **Actions**, choose **Stop**, and then confirm.
+ **Delete a job.** Select a completed or failed job, choose **Actions**, choose **Delete**, and then confirm.
+ **Inspect details.** Choose any job to open its detail page with the **Overview**, **Settings**, and **Details** tabs.

Consider re-running an optimization job after you fine-tune or update your model, when new instance types become available in your AWS Region, when your traffic patterns change significantly, or after a serving container or framework upgrade. You can also re-run jobs on a regular cadence, such as every two weeks, to pick up the latest optimizations as SageMaker AI adds them.