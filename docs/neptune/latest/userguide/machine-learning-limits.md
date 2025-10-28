# Neptune ML limits

- The types of inference currently supported are node classification,
  node regression, edge classification, edge regression and link prediction
  (see [Neptune ML capabilities](machine-learning.md#machine-learning-capabilities "machine-learning.md#machine-learning-capabilities")).
- The maximum graph size that Neptune ML can support depends on the
  amount of memory and storage required during
  [data preparation](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-processing-instance-size "machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-processing-instance-size"),
  [model training](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size "machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-training-transform-instance-size"),
  and [inference](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-inference-endpoint-instance-size "machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-inference-endpoint-instance-size").
  - The maximum size of memory of a SageMaker AI data-processing instance is 768 GB.
    As a result, the data-processing stage fails if it needs more than 768 GB of memory.
  - The maximum size of memory of a SageMaker AI training instance is 732 GB.
    As a result, the training stage fails if it needs more than 732 GB of memory.

- The maximum size of an inference payload for a SageMaker AI endpoint is 6 MiB.
  As a result, inductive inference fails if the subgraph payload exceeds this size.
- Neptune ML is currently available only in Regions where Neptune
  and the other services it depends on (such as AWS Lambda, Amazon API Gateway and Amazon SageMaker AI) are
  all supported.

There are differences in China (Beijing) and China (Ningxia)
having to do with the default use of IAM authentication, as is [explained
here](https://docs.amazonaws.cn/en_us/aws/latest/userguide/api-gateway.html#feature-diff "https://docs.amazonaws.cn/en_us/aws/latest/userguide/api-gateway.html#feature-diff") along with other differences.

- The link prediction inference endpoints launched by Neptune ML currently
  can only predict possible links with nodes that were present in the graph during
  training.

For example, consider a graph with `User` and `Movie`
vertices and `Rated` edges. Using a corresponding Neptune ML
link-prediction recommendation model, you can add a new user to the graph and
have the model predict movies for them, but the model can only recommend movies
that were present during model training. Although the `User` node
embedding is calculated in real-time using its local subgraph and the GNN model,
and can therefore change with time as users rate movies, it's compared to the
static, pre-computed movie embeddings for the final recommendation.

- The KGE models supported by Neptune ML only work for link prediction tasks,
  and the representations are specific to vertices and edge types present in the graph
  during training. This means that all vertices and edge types referred to in an
  inference query must have been present in the graph during training.
  Predictions for new edge types or vertices cannot be made without retraining the
  model.

## SageMaker AI resource limitations

Depending on your activities and resource usage over time, you may encounter
error messages saying that [you've
exceeded your quota](../../../sagemaker/latest/dg/regions-quotas.md "../../../sagemaker/latest/dg/regions-quotas.md") ([ResourceLimitExceeded](https://repost.aws/knowledge-center/sagemaker-resource-limit-exceeded-error "https://repost.aws/knowledge-center/sagemaker-resource-limit-exceeded-error")).
and you need to scale up your SageMaker AI resources, follow the steps in the [Request
a service quota increase for SageMaker resources](../../../sagemaker/latest/dg/regions-quotas.md#service-limit-increase-request-procedure "../../../sagemaker/latest/dg/regions-quotas.md#service-limit-increase-request-procedure") procedure on this page to
request a quota increase from AWS Support.

SageMaker AI resource names correspond to Neptune ML stages as follows:

- The SageMaker AI `ProcessingJob` is used by Neptune
  data processing, model training, and model transform jobs.
- The SageMaker AI `HyperParameterTuningJob` is used by Neptune
  model training jobs.
- The SageMaker AI `TrainingJob` is used by Neptune
  model training jobs.
- The SageMaker AI `Endpoint` is used by Neptune
  inference endpoints.
