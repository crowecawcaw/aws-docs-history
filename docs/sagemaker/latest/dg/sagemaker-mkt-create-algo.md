# Create an Algorithm Resource

You can create an algorithm resource to use with training jobs in Amazon SageMaker AI, and you can
publish it on AWS Marketplace. The following sections explain how to do that using the AWS Management Console and
the SageMaker API.

To create an algorithm resource, you specify the following information:

- The Docker containers that contains the training and, optionally,
  inference code.
- The configuration of the input data that your algorithm expects for
  training.
- The hyperparameters that your algorithm supports.
- Metrics that your algorithm sends to Amazon CloudWatch during training jobs.
- The instance types that your algorithm supports for training and
  inference, and whether it supports distributed training across multiple
  instances.
- Validation profiles, which are training jobs that SageMaker AI uses to test your
  algorithm's training code and batch transform jobs that SageMaker AI runs to test
  your algorithm's inference code.

To ensure that buyers and sellers can be confident that products work in
SageMaker AI, we require that you validate your algorithms before listing them on
AWS Marketplace. You can list products in the AWS Marketplace only if validation succeeds. To
validate your algorithms, SageMaker AI uses your validation profile and sample data
to run the following validations tasks:

    1. Create a training job in your account to verify that your training
     image works with SageMaker AI.
    2. If you included inference code in your algorithm, create a model
     in your account using the algorithm's inference image and the model
     artifacts produced by the training job.
    3. If you included inference code in your algorithm, create a
     transform job in your account using the model to verify that your
     inference image works with SageMaker AI.

When you list your product on AWS Marketplace, the inputs and outputs of this
validation process persist as part of your product and are made available to
your buyers. This helps buyers understand and evaluate the product before
they buy it. For example, buyers can inspect the input data that you used,
the outputs generated, and the logs and metrics emitted by your code. The
more comprehensive your validation specification, the easier it is for
customers to evaluate your product.

###### Note

In your validation profile, provide only data that you want to expose
publicly.

Validation can take up to a few hours. To see the status of the jobs in
your account, in the SageMaker AI console, see the **Training
jobs** and **Transform jobs** pages. If
validation fails, you can access the scan and validation reports from the
SageMaker AI console. If any issues are found, you will have to create the algorithm
again.

###### Note

To publish your algorithm on AWS Marketplace, at least one validation profile is
required.
You can create an algorithm by using either the SageMaker AI console or the SageMaker AI
API.

###### Topics

- [Create an Algorithm Resource
  (Console)](#sagemaker-mkt-create-algo-console "#sagemaker-mkt-create-algo-console")
- [Create an Algorithm Resource
  (API)](#sagemaker-mkt-create-algo-api "#sagemaker-mkt-create-algo-api")

## Create an Algorithm Resource

(Console)

###### To create an algorithm resource (console)

1.  Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  From the left menu, choose **Training**.
3.  From the dropdown menu, choose **Algorithms**, then choose **Create
    algorithm**.
4.  On the **Training specifications** page, provide the
    following information:
    1. For **Algorithm name**, type a name for your
       algorithm. The algorithm name must be unique in your account and
       in the AWS region. The name must have 1 to 64 characters.
       Valid characters are a-z, A-Z, 0-9, and - (hyphen).
    2. Type a description for your algorithm. This description
       appears in the SageMaker AI console and in the AWS Marketplace.
    3. For **Training image, type the path in Amazon ECR where
       your training container is stored.**
    4. For **Support distributed training**, Choose
       **Yes** if your algorithm supports training
       on multiple instances. Otherwise, choose
       **No**.
    5. For **Support instance types for training**,
       choose the instance types that your algorithm supports.
    6. For **Channel specification**, specify up to
       8 channels of input data for your algorithm. For example, you
       might specify 3 input channels named `train`,
       `validation`, and `test`. For each
       channel, specify the following information:
       1. For **Channel name**, type a name for
          the channel. The name must have 1 to 64 characters.
          Valid characters are a-z, A-Z, 0-9, and -
          (hyphen).
       2. To require the channel for your algorithm, choose
          **Channel required**.
       3. Type a description for the channel.
       4. For **Supported input modes**, choose
          **Pipe mode** if your algorithm
          supports streaming the input data, and **File
          mode** if your algorithm supports
          downloading the input data as a file. You can choose
          both.
       5. For **Supported content types**, type
          the MIME type that your algorithm expects for input
          data.
       6. For **Supported compression type**,
          choose **Gzip** if your algorithm
          supports Gzip compression. Otherwise, choose
          **None**.
       7. Choose **Add channel** to add another
          data input channel, or choose **Next**
          if you are done adding channels.

5.  On the **Tuning specifications** page, provide the
    following information:
    1. For **Hyperparameter specification**, specify
       the hyperparameters that your algorithm supports by editing the
       JSON object. For each hyperparameter that your algorithm
       supports, construct a JSON block similar to the
       following:

    ```
    {
    "DefaultValue": "5",
    "Description": "The first hyperparameter",
    "IsRequired": true,
    "IsTunable": false,
    "Name": "intRange",
    "Range": {
    "IntegerParameterRangeSpecification": {
    "MaxValue": "10",
    "MinValue": "1"
    },
    "Type": "Integer"
    }
    ```

    In the JSON, supply the following:

        1. For `DefaultValue`, specify a default value
         for the hyperparameter, if there is one.
        2. For `Description`, specify a description
         for the hyperparameter.
        3. For `IsRequired`, specify whether the
         hyperparameter is required.
        4. For `IsTunable`, specify `true`
         if this hyperparameter can be tuned when a user runs a
         hyperparameter tuning job that uses this algorithm. For
         information, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").
        5. For `Name`, specify a name for the
         hyperparameter.
        6. For `Range`, specify one of the
         following:




        	* `IntegerParameterRangeSpecification`
        	 - the values of the hyperparameter are integers.
        	 Specify minimum and maximum values for the
        	 hyperparameter.
        	*
        	* `ContinuousParameterRangeSpecification`
        	 - the values of the hyperparameter are
        	 floating-point values. Specify minimum and maximum
        	 values for the hyperparameter.
        	* `CategoricalParameterRangeSpecification`
        	 - the values of the hyperparameter are categorical
        	 values. Specify a list of all of the possible
        	 values.
        7. For `Type`, specify `Integer`,
         `Continuous`, or
         `Categorical`. The value must correspond to
         the type of `Range` that you
         specified.

    2. For **Metric definitions**, specify any
       training metrics that you want your algorithm to emit. SageMaker AI uses
       the regular expression that you specify to find the metrics by
       parsing the logs from your training container during training.
       Users can view these metrics when they run training jobs with
       your algorithm, and they can monitor and plot the metrics in
       Amazon CloudWatch. For information, see [Amazon CloudWatch Metrics for Monitoring and Analyzing Training Jobs](training-metrics.md "training-metrics.md"). For each metric, provide
       the following information:
       1. For **Metric name**, type a name for
          the metric.
       2. For `Regex`, type the regular expression
          that SageMaker AI uses to parse training logs so that it can
          find the metric value.
       3. For **Objective metric support**
          choose **Yes** if this metric can be
          used as the objective metric for a hyperparameter tuning
          job. For information, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").
       4. Choose **Add metric** to add another
          metric, or choose **Next** if you are
          done adding metrics.

6.  On the **Inference specifications** page, provide the
    following information if your algorithm supports inference:
    1. For **Location of inference image**, type the path in
       Amazon ECR where your inference container is stored.
    2. For **Container DNS host name**, type the
       name of a DNS host for your image.
    3. For **Supported instance types for real-time
       inference**, choose the instance types that your
       algorithm supports for models deployed as hosted endpoints in
       SageMaker AI. For information, see [Deploy models for inference](deploy-model.md "deploy-model.md").
    4. For **Supported instance types for batch transform
       jobs**, choose the instance types that your
       algorithm supports for batch transform jobs. For information,
       see [Batch transform for inference with Amazon SageMaker AI](batch-transform.md "batch-transform.md").
    5. For **Supported content types**, type the
       type of input data that your algorithm expects for inference
       requests.
    6. For **Supported response MIME types**, type
       the MIME types that your algorithm supports for inference
       responses.
    7. Choose **Next**.

7.  On the **Validation specifications** page, provide
    the following information:
    1. For **Publish this algorithm on AWS Marketplace**,
       choose **Yes** to publish the algorithm on
       AWS Marketplace.
    2. For **Validate this resource**, choose
       **Yes** if you want SageMaker AI to run training jobs and/or
       batch transform jobs that you specify to test the training and/or inference
       code of your algorithm.

    ###### Note

    To publish your algorithm on AWS Marketplace, your algorithm must be
    validated. 3. For **IAM role**, choose an IAM role that
    has the required permissions to run training jobs and batch
    transform jobs in SageMaker AI, or choose **Create a new
    role** to allow SageMaker AI to create a role that has the
    `AmazonSageMakerFullAccess` managed policy
    attached. For information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md"). 4. For **Validation profile**, specify the
    following:

        * A name for the validation profile.
        * A **Training job definition**. This
         is a JSON block that describes a training job. This is
         in the same format as the [`TrainingJobDefinition`](../APIReference/API_TrainingJobDefinition.md "../APIReference/API_TrainingJobDefinition.md") input
         parameter of the [`CreateAlgorithm`](../APIReference/API_CreateAlgorithm.md "../APIReference/API_CreateAlgorithm.md") API.
        * A **Transform job definition**. This
         is a JSON block that describes a batch transform job.
         This is in the same format as the [`TransformJobDefinition`](../APIReference/API_TransformJobDefinition.md "../APIReference/API_TransformJobDefinition.md") input
         parameter of the [`CreateAlgorithm`](../APIReference/API_CreateAlgorithm.md "../APIReference/API_CreateAlgorithm.md") API.

    5. Choose **Create algorithm**.

## Create an Algorithm Resource

(API)

To create an algorithm resource by using the SageMaker API, call the [`CreateAlgorithm`](../APIReference/API_CreateAlgorithm.md "../APIReference/API_CreateAlgorithm.md") API.
