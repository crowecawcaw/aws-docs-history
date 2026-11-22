

# ADVPERF01-BP04 Evaluate AI/ML-based architecture for optimization

 Use AWS services to implement a low-latency, high-throughput inference and MLOps framework for advertising workloads. AI/ML is central to advertising. Contextual targeting, dynamic creative optimization, bid price prediction, and fraud detection all rely on model inference that must complete within auction deadlines. 

 **Desired outcome:** 
+  Your machine learning inference pipeline delivers consistent, low-latency predictions at scale, from model training through production serving. 
+  Foundation model inference, custom model hosting, and MLOps automation run on purpose-built AWS services. 
+  Observability is built in from the start, with CloudWatch metrics tracking invocation latency, token consumption, and error rates. 
+  Repeated inference results are cached to avoid redundant model invocations for identical inputs. 

 **Common anti-patterns:** 
+  Invoking [Amazon Bedrock](https://aws.amazon.com/bedrock/) over public internet endpoints instead of through [AWS PrivateLink](https://aws.amazon.com/privatelink/), which adds network hops and TLS handshake overhead to every inference call on the critical path. 
+  Re-running inference for identical inputs on every request without caching, when the model output for those inputs is deterministic and reusable. 
+  Using a single general-purpose instance type for all ML workloads without evaluating purpose-built accelerators (Trainium for training, Inferentia for inference). 
+  Calling foundation models synchronously in the bid evaluation path without measuring their contribution to end-to-end bid response latency. 

 **Benefits of establishing this best practice:** 
+  A well-architected ML inference framework reduces bid and classification response times, improving bid win rates and campaign performance. 
+  Combining private networking, intelligent caching, and purpose-built inference infrastructure gives you predictable latency at scale without managing undifferentiated hosting complexity. 
+  Automated MLOps pipelines (SageMaker AI Pipelines) reduce the time between model improvement and production deployment, accelerating the feedback loop on campaign performance. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising AI/ML workloads don't share a single latency budget, so the first decision is which tier each model belongs to. Real-time bid scoring must return a prediction within the few milliseconds an auction allows. Contextual classification of a page or video asset can take hundreds of milliseconds, because it runs before bid requests arrive. Attribution and campaign-performance models run in batch and tolerate minutes. Decide the tier first, and keep inference that can't meet the deadline off the synchronous bid path. 

 Self-hosted inference and foundation-model access trade control against operational overhead. When you host your own bid-scoring or segment-classification model, you control instance type, batching, and model compilation, but you own capacity and scaling. When you call a managed foundation model, you remove the hosting burden and give up that low-level control. Within self-hosted inference, treat the accelerator choice as an economic decision. Purpose-built training and inference accelerators return more performance per dollar than general-purpose GPU instances for models that compile to their instruction sets. That advantage repays the compilation and validation effort only at sustained volume. A classifier invoked on every bid request qualifies as opposed to a model called a few times an hour. 

 Network path becomes a latency variable once inference runs on or near the bid path. A call that crosses the public internet inherits routing variability. That variability appears at p99 and p999, the tail percentiles that decide whether a response arrives before the auction closes. Private network paths remove that source of tail variance. Treat this as an architectural decision made up front, because changing it after launch means re-validating every inference call on the critical path. 

 Caching inference results pays off when the model returns the same output for a repeated input. Contextual classification of recurring content fits that condition. A FAST-channel asset or a frequently requested page produces an identical classification each time you evaluate it. Recomputing it wastes both latency and inference spend. A cache entry's time-to-live must track how often the underlying content changes. A stale classification can be worse than a slow one when creative-to-content matching depends on it. Inference with input-dependent or non-deterministic output (real-time bid pricing, generative creative) gains little from caching and doesn't justify its complexity. 

 Inference shape determines which latency signal is meaningful. Total round-trip time captures a short categorical classification. Time-to-first-token captures a streaming generation, because that is what the downstream consumer waits on. Measure a streaming workload only on round-trip time, or a classification workload only on token counts. The dashboard can look healthy while the metric that governs auction fit goes unmeasured. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy custom model inference on managed compute:** Run custom bid scoring and classification models on Amazon ECS, Amazon EKS, or Amazon SageMaker AI based on your orchestration preferences. Use SageMaker AI Pipelines to build, train, evaluate, and deploy models in a repeatable, automated workflow. Configure auto scaling on SageMaker AI inference endpoints to maintain consistent performance as bid request volume fluctuates. 

1.  **Run foundation model inference on Amazon Bedrock through PrivateLink:** For contextual classification and ad creative generation use cases, configure Amazon Bedrock access through a VPC interface endpoint (PrivateLink). This removes public internet routing from the inference call entirely. Verify that DNS resolution within your VPC resolves the Bedrock endpoint to a private IP address before enabling production traffic. 

1.  **Cache repeated inference results in Amazon ElastiCache:** For contextual classification of recurring content (video segments, page URLs, or creative assets that appear repeatedly), implement a cache-aside pattern. Check ElastiCache before invoking Bedrock. If the result is cached, return it immediately. If not, invoke Bedrock, return the result, and write it to the cache with a TTL appropriate to how often the content changes. This is particularly effective for FAST channel content that plays on a rotating schedule. 

1.  **Monitor inference performance with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Bedrock metrics:** Enable CloudWatch metrics for Amazon Bedrock and monitor InvocationLatency for classification requests and TimeToFirstToken for streaming generation requests. Set alarms on p99 latency thresholds aligned to your bid response latency budget. Use InputTokenCount and OutputTokenCount to track inference costs and detect unexpected model usage patterns. 

1.  **Use SageMaker AI predictive scaling for known peak periods:** Train SageMaker AI Pipelines scaling policies on historical inference traffic patterns to proactively add inference capacity before anticipated demand peaks. For advertising workloads with predictable peak windows (primetime, major live events), configure scheduled scaling actions to pre-scale inference endpoints before traffic arrives rather than reacting after latency increases. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP06 Use a managed serverless runtime for AI agent compute](advperf02-bp06.md) 
+  [ADVPERF06-BP07 Pre-classify publisher content for contextual targeting at ingest time](advperf06-bp07.md) 

 **Related documents:** 
+  [Use interface VPC endpoints (AWS PrivateLink) for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) 
+  [Monitor Amazon Bedrock with CloudWatch](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-cloudwatch.html) 
+  [Guidance for Machine Learning for Near Real-Time Advertising on AWS](https://aws.amazon.com/solutions/guidance/machine-learning-for-near-real-time-advertising-on-aws/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 