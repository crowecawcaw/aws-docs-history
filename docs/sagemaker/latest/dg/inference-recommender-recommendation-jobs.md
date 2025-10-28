# Recommendation jobs with

Amazon SageMaker Inference Recommender

Amazon SageMaker Inference Recommender can make two types of recommendations:

1. Inference recommendations (`Default` job type) run a set of load
   tests on the recommended instance types. You can also load test for a serverless
   endpoint.. You only need to provide a model package Amazon Resource Name (ARN)
   to launch this type of recommendation job. Inference recommendation jobs
   complete within 45 minutes.
2. Endpoint recommendations (`Advanced` job type) are based on a
   custom load test where you select your desired ML instances or a serverless
   endpoint, provide a custom traffic pattern, and provide requirements for latency
   and throughput based on your production requirements. This job takes an average
   of 2 hours to complete depending on the job duration set and the total number of
   inference configurations tested.
   Both types of recommendations use the same APIs to create, describe, and stop jobs.
   The output is a list of instance configuration recommendations with associated
   environment variables, cost, throughput, and latency metrics. Recommendation jobs also
   provide an initial instance count, which you can use to configure an autoscaling policy.
   To differentiate between the two types of jobs, when you’re creating a job through
   either the SageMaker AI console or the APIs, specify `Default` to create preliminary
   endpoint recommendations and `Advanced` for custom load testing and endpoint
   recommendations.

###### Note

You do not need to do both types of recommendation jobs in your own workflow. You
can do either independently of the other.

Inference Recommender can also provide you with a list of prospective instances, or the top five
instance types that are optimized for cost, throughput and latency for model deployment,
along with a confidence score. You can choose these instances when deploying your model.
Inference Recommender automatically performs benchmarking against your model for you to provide the
prospective instances. Since these are preliminary recommendations, we recommend that
you run further instance recommendation jobs to get more accurate results. To view the
prospective instances, go to your SageMaker AI model details page. For more information, see
[Get instant prospective
instances](inference-recommender-prospective.md "inference-recommender-prospective.md").

###### Topics

- [Get instant prospective
  instances](inference-recommender-prospective.md "inference-recommender-prospective.md")
- [Inference
  recommendations](inference-recommender-instance-recommendation.md "inference-recommender-instance-recommendation.md")
- [Get an inference
  recommendation for an existing endpoint](inference-recommender-existing-endpoint.md "inference-recommender-existing-endpoint.md")
- [Stop your inference
  recommendation](instance-recommendation-stop.md "instance-recommendation-stop.md")
- [Compiled recommendations
  with Neo](inference-recommender-neo-compilation.md "inference-recommender-neo-compilation.md")
- [Recommendation
  results](inference-recommender-interpret-results.md "inference-recommender-interpret-results.md")
- [Get autoscaling policy
  recommendations](inference-recommender-autoscaling.md "inference-recommender-autoscaling.md")
- [Run a custom load test](inference-recommender-load-test.md "inference-recommender-load-test.md")
- [Stop your load test](load-test-stop.md "load-test-stop.md")
- [Troubleshoot Inference Recommender
  errors](inference-recommender-troubleshooting.md "inference-recommender-troubleshooting.md")
