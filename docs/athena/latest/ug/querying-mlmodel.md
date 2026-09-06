

# Use Machine Learning (ML) with Amazon Athena
<a name="querying-mlmodel"></a>

Machine Learning (ML) with Amazon Athena lets you use Athena to write SQL statements that run Machine Learning (ML) inference using Amazon SageMaker AI. This feature simplifies access to ML models for data analysis, eliminating the need to use complex programming methods to run inference.

To use ML with Athena, you define an ML with Athena function with the `USING EXTERNAL FUNCTION` clause. The function points to the SageMaker AI model endpoint that you want to use and specifies the variable names and data types to pass to the model. Subsequent clauses in the query reference the function to pass values to the model. The model runs inference based on the values that the query passes and then returns inference results. For more information about SageMaker AI and how SageMaker AI endpoints work, see the [Amazon SageMaker AI Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/).

For an example that uses ML with Athena and SageMaker AI inference to detect an anomalous value in a result set, see the AWS Big Data Blog article [Detecting anomalous values by invoking the Amazon Athena machine learning inference function](https://aws.amazon.com/blogs/big-data/detecting-anomalous-values-by-invoking-the-amazon-athena-machine-learning-inference-function/).

## Considerations and limitations
<a name="considerations-and-limitations"></a>
+ **Available Regions** – The Athena ML feature is available in the AWS Regions where Athena engine version 2 or later are supported.
+ **SageMaker AI model endpoint must accept and return `text/csv`** – For more information about data formats, see [Common data formats for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html) in the *Amazon SageMaker AI Developer Guide*.
+ **Athena does not send CSV headers** – If your SageMaker AI endpoint is `text/csv`, your input handler should not assume that the first line of the input is a CSV header. Because Athena does not send CSV headers, the output returned to Athena will contain one less row than Athena expects and cause an error. 
+ **SageMaker AI endpoint scaling** – Make sure that the referenced SageMaker AI model endpoint is sufficiently scaled up for Athena calls to the endpoint. For more information, see [Automatically scale SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) in the *Amazon SageMaker AI Developer Guide* and [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html) in the *Amazon SageMaker AI API Reference*.
+ **IAM permissions** – To run a query that specifies an ML with Athena function, the IAM principal running the query must be allowed to perform the `sagemaker:InvokeEndpoint` action for the referenced SageMaker AI model endpoint. For more information, see [Allow access for ML with Athena](machine-learning-iam-access.md).
+ **ML with Athena functions cannot be used in `GROUP BY` clauses directly**

**Topics**
+ [Considerations and limitations](#considerations-and-limitations)
+ [Use ML with Athena syntax](ml-syntax.md)
+ [See customer use examples](ml-videos.md)