

# Instance selection for the Neptune ML stages
<a name="machine-learning-on-graphs-instance-selection"></a>

The different stages of Neptune ML processing use different SageMaker AI instances. Here, we discuss how to choose the right instance type for each stage. You can find information about SageMaker AI instance types and pricing at [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

## Selecting an instance for data processing
<a name="machine-learning-on-graphs-processing-instance-size"></a>

The SageMaker AI [data-processing](machine-learning-on-graphs-processing.md) step requires a [processing instance](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) that has enough memory and disk storage for the input, intermediate, and output data. The specific amount of memory and disk storage needed depends on the characteristics of the Neptune ML graph and its exported features.

By default, Neptune ML chooses the smallest `ml.r5` instance whose memory is ten times larger than the size of the exported graph data on disk.

## Selecting an instance for model training and model transform
<a name="machine-learning-on-graphs-training-transform-instance-size"></a>

Selecting the right instance type for [model training](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) or [model transform](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-batch.html) depends on the task type, the graph size, and your turn-around requirements. GPU instances provide the best performance. We generally recommend `p3` and `g4dn` serial instances. You can also use `p2` or `p4d` instances.

By default, Neptune ML chooses the smallest GPU instance with more memory than model training and model transform requires. You can find what that selection is in the `train_instance_recommendation.json` file, in the Amazon S3 data processing output location. Here is an example of the contents of a `train_instance_recommendation.json` file:

```
{ 
  "instance":     "{{(the recommended instance type for model training and transform)}}",
  "cpu_instance": "{{(the recommended instance type for base processing instance)}}", 
  "disk_size":    "{{(the estimated disk space required)}}",
  "mem_size":     "{{(the estimated memory required)}}"
}
```

## Selecting an instance for an inference endpoint
<a name="machine-learning-on-graphs-inference-endpoint-instance-size"></a>

Selecting the right instance type for an [inference endpoint](machine-learning-on-graphs-inference-endpoint.md) depends on the task type, the graph size and your budget. By default, Neptune ML chooses the smallest `ml.m5d` instance with more memory the inference endpoint requires.

**Note**  
If more than 384 GB of memory is needed, Neptune ML uses an `ml.r5d.24xlarge` instance.

You can see what instance type Neptune ML recommends in the `infer_instance_recommendation.json` file located in the Amazon S3 location you are using for model training. Here is an example of that file's contents:

```
{ 
  "instance" :   "{{(the recommended instance type for an inference endpoint)}}",
  "disk_size" :  "{{(the estimated disk space required)}}",
  "mem_size" :   "{{(the estimated memory required)}}"
}
```