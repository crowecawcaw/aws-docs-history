

# Evaluation with Inspect AI
<a name="nova-eval-inspect-ai"></a>

You can evaluate your customized Amazon Nova models using [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai), an open-source evaluation framework. Inspect AI supports standardized benchmarks from the AI research community, enabling you to measure model performance across knowledge, reasoning, coding, and safety tasks.

Choose the evaluation approach that best fits your workflow:
+ **Inspect AI SDK** – Run evaluations interactively from a notebook or local environment against your SageMaker inference endpoint. Best for development, iteration, and quick testing.
+ **Inspect AI container** – Run evaluations at scale as SageMaker Training Jobs. Best for production evaluation pipelines, chaining multiple benchmarks, and automated workflows.

**Recommended workflow:** Start with the Inspect AI SDK to build and test your custom evaluation benchmarks using the [AI assistant onboarding prompt](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/sagemaker-inspect-ai/ai_assisted_benchmark_creation.md), then run evaluations against your preferred inference solution. Once your benchmarks are fully validated, you can seamlessly switch to job-based evaluation using the Inspect AI container — no code changes required. Simply move your benchmark files and recipe file to S3 and launch the job.

**Topics**
+ [Evaluate with Inspect AI SDK](nova-eval-on-sagemaker-inference.md)
+ [Evaluate with Inspect AI Container](nova-eval-inspect-ai-container.md)