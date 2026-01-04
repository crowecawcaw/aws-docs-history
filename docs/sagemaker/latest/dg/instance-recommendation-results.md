# Get your inference

recommendation job results

Collect the results of your inference recommendation job programmatically with
AWS SDK for Python (Boto3), the AWS CLI, Studio Classic, or the SageMaker AI console.

AWS SDK for Python (Boto3)
Once an inference recommendation is complete, you can use
`DescribeInferenceRecommendationsJob` to get the job
details and recommendations. Provide the job name that you used when
you created the inference recommendation job.

```
job_name=`'<INSERT>'`
response = sagemaker_client.describe_inference_recommendations_job(
                    JobName=job_name)
```

Print the response object. The previous code sample stored the
response in a variable named `response`.

```
print(response['Status'])
```

This returns a JSON response similar to the following example.
Note that this example shows the recommended instance types for
real-time inference (for an example showing serverless inference
recommendations, see the example after this one).

```
{
    'JobName': `'job-name'`,
    'JobDescription': `'job-description'`,
    'JobType': 'Default',
    'JobArn': 'arn:aws:sagemaker:`region`:`account-id`:inference-recommendations-job/`resource-id`',
    'Status': 'COMPLETED',
    'CreationTime': datetime.datetime(2021, 10, 26, 20, 4, 57, 627000, tzinfo=tzlocal()),
    'LastModifiedTime': datetime.datetime(2021, 10, 26, 20, 25, 1, 997000, tzinfo=tzlocal()),
    'InputConfig': {
                'ModelPackageVersionArn': 'arn:aws:sagemaker:`region`:`account-id`:model-package/`resource-id`',
                'JobDurationInSeconds': 0
                },
    'InferenceRecommendations': [{
            'Metrics': {
                'CostPerHour': 0.20399999618530273,
                'CostPerInference': 5.246913588052848e-06,
                'MaximumInvocations': 648,
                'ModelLatency': 263596
                },
            'EndpointConfiguration': {
                'EndpointName': `'endpoint-name'`,
                'VariantName': `'variant-name'`,
                'InstanceType': 'ml.c5.xlarge',
                'InitialInstanceCount': 1
                },
            'ModelConfiguration': {
                'Compiled': False,
                'EnvironmentParameters': []
                }
         },
         {
            'Metrics': {
                'CostPerHour': 0.11500000208616257,
                'CostPerInference': 2.92620870823157e-06,
                'MaximumInvocations': 655,
                'ModelLatency': 826019
                },
            'EndpointConfiguration': {
                'EndpointName': `'endpoint-name'`,
                'VariantName': `'variant-name'`,
                'InstanceType': 'ml.c5d.large',
                'InitialInstanceCount': 1
                },
            'ModelConfiguration': {
                'Compiled': False,
                'EnvironmentParameters': []
                }
            },
            {
                'Metrics': {
                    'CostPerHour': 0.11500000208616257,
                    'CostPerInference': 3.3625731248321244e-06,
                    'MaximumInvocations': 570,
                    'ModelLatency': 1085446
                    },
                'EndpointConfiguration': {
                    'EndpointName': `'endpoint-name'`,
                    'VariantName': `'variant-name'`,
                    'InstanceType': 'ml.m5.large',
                    'InitialInstanceCount': 1
                    },
                'ModelConfiguration': {
                    'Compiled': False,
                    'EnvironmentParameters': []
                    }
            }],
    'ResponseMetadata': {
        'RequestId': `'request-id'`,
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': `'x-amzn-requestid'`,
            'content-type': `'content-type'`,
            'content-length': '1685',
            'date': 'Tue, 26 Oct 2021 20:31:10 GMT'
            },
        'RetryAttempts': 0
        }
}
```

The first few lines provide information about the inference
recommendation job itself. This includes the job name, role ARN, and
creation and deletion times.

The `InferenceRecommendations` dictionary contains a
list of Inference Recommender inference recommendations.

The `EndpointConfiguration` nested dictionary contains
the instance type (`InstanceType`) recommendation along
with the endpoint and variant name (a deployed AWS machine
learning model) that was used during the recommendation job. You can
use the endpoint and variant name for monitoring in Amazon CloudWatch Events. See
[Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") for more
information.

The `Metrics` nested dictionary contains information
about the estimated cost per hour (`CostPerHour`) for
your real-time endpoint in US dollars, the estimated cost per
inference (`CostPerInference`) in US dollars for your
real-time endpoint, the expected maximum number of
`InvokeEndpoint` requests per minute sent to the
endpoint (`MaxInvocations`), and the model latency
(`ModelLatency`), which is the interval of time (in
microseconds) that your model took to respond to SageMaker AI. The model
latency includes the local communication times taken to send the
request and to fetch the response from the container of a model and
the time taken to complete the inference in the container.

The following example shows the
`InferenceRecommendations` part of the response for
an inference recommendations job configured to return serverless
inference recommendations:

```
"InferenceRecommendations": [
      {
         "EndpointConfiguration": {
            "EndpointName": "`value`",
            "InitialInstanceCount": `value`,
            "InstanceType": "`value`",
            "VariantName": "`value`",
            "ServerlessConfig": {
                "MaxConcurrency": `value`,
                "MemorySizeInMb": `value`
            }
         },
         "InvocationEndTime": `value`,
         "InvocationStartTime": `value`,
         "Metrics": {
            "CostPerHour": `value`,
            "CostPerInference": `value`,
            "CpuUtilization": `value`,
            "MaxInvocations": `value`,
            "MemoryUtilization": `value`,
            "ModelLatency": `value`,
            "ModelSetupTime": `value`
         },
         "ModelConfiguration": {
            "Compiled": "False",
            "EnvironmentParameters": [],
            "InferenceSpecificationName": "`value`"
         },
         "RecommendationId": "`value`"
      }
   ]
```

You can interpret the recommendations for serverless inference
similarly to the results for real-time inference, with the exception
of the `ServerlessConfig`, which tells you the metrics
returned for a serverless endpoint with the given
`MemorySizeInMB` and when `MaxConcurrency =
 1`. To increase the throughput possible on the endpoint,
increase the value of `MaxConcurrency` linearly. For
example, if the inference recommendation shows
`MaxInvocations` as `1000`, then
increasing `MaxConcurrency` to `2` would
support 2000 `MaxInvocations`. Note that this is true
only up to a certain point, which can vary based on your model and
code. Serverless recommendations also measure the metric
`ModelSetupTime`, which measures (in microseconds)
the time it takes to launch computer resources on a serverless
endpoint. For more information about setting up serverless
endpoints, see the [Serverless Inference
documentation](serverless-endpoints.md "serverless-endpoints.md").

AWS CLI
Once an inference recommendation is complete, you can use
`describe-inference-recommendations-job` to get the
job details and recommended instance types. Provide the job name
that you used when you created the inference recommendation
job.

```
aws sagemaker describe-inference-recommendations-job\
    --job-name `<job-name>`\
    --region `<aws-region>`

```

The JSON response similar should resemble the following example.
Note that this example shows the recommended instance types for
real-time inference (for an example showing serverless inference
recommendations, see the example after this one).

```
{
    'JobName': `'job-name'`,
    'JobDescription': `'job-description'`,
    'JobType': 'Default',
    'JobArn': 'arn:aws:sagemaker:`region`:`account-id`:inference-recommendations-job/`resource-id`',
    'Status': 'COMPLETED',
    'CreationTime': datetime.datetime(2021, 10, 26, 20, 4, 57, 627000, tzinfo=tzlocal()),
    'LastModifiedTime': datetime.datetime(2021, 10, 26, 20, 25, 1, 997000, tzinfo=tzlocal()),
    'InputConfig': {
                'ModelPackageVersionArn': 'arn:aws:sagemaker:`region`:`account-id`:model-package/`resource-id`',
                'JobDurationInSeconds': 0
                },
    'InferenceRecommendations': [{
            'Metrics': {
                'CostPerHour': 0.20399999618530273,
                'CostPerInference': 5.246913588052848e-06,
                'MaximumInvocations': 648,
                'ModelLatency': 263596
                },
            'EndpointConfiguration': {
                'EndpointName': `'endpoint-name'`,
                'VariantName': `'variant-name'`,
                'InstanceType': 'ml.c5.xlarge',
                'InitialInstanceCount': 1
                },
            'ModelConfiguration': {
                'Compiled': False,
                'EnvironmentParameters': []
                }
         },
         {
            'Metrics': {
                'CostPerHour': 0.11500000208616257,
                'CostPerInference': 2.92620870823157e-06,
                'MaximumInvocations': 655,
                'ModelLatency': 826019
                },
            'EndpointConfiguration': {
                'EndpointName': `'endpoint-name'`,
                'VariantName': `'variant-name'`,
                'InstanceType': 'ml.c5d.large',
                'InitialInstanceCount': 1
                },
            'ModelConfiguration': {
                'Compiled': False,
                'EnvironmentParameters': []
                }
            },
            {
                'Metrics': {
                    'CostPerHour': 0.11500000208616257,
                    'CostPerInference': 3.3625731248321244e-06,
                    'MaximumInvocations': 570,
                    'ModelLatency': 1085446
                    },
                'EndpointConfiguration': {
                    'EndpointName': `'endpoint-name'`,
                    'VariantName': `'variant-name'`,
                    'InstanceType': 'ml.m5.large',
                    'InitialInstanceCount': 1
                    },
                'ModelConfiguration': {
                    'Compiled': False,
                    'EnvironmentParameters': []
                    }
            }],
    'ResponseMetadata': {
        'RequestId': `'request-id'`,
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': `'x-amzn-requestid'`,
            'content-type': `'content-type'`,
            'content-length': '1685',
            'date': 'Tue, 26 Oct 2021 20:31:10 GMT'
            },
        'RetryAttempts': 0
        }
}
```

The first few lines provide information about the inference
recommendation job itself. This includes the job name, role ARN,
creation, and deletion time.

The `InferenceRecommendations` dictionary contains a
list of Inference Recommender inference recommendations.

The `EndpointConfiguration` nested dictionary contains
the instance type (`InstanceType`) recommendation along
with the endpoint and variant name (a deployed AWS machine
learning model) used during the recommendation job. You can use the
endpoint and variant name for monitoring in Amazon CloudWatch Events. See [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") for more
information.

The `Metrics` nested dictionary contains information
about the estimated cost per hour (`CostPerHour`) for
your real-time endpoint in US dollars, the estimated cost per
inference (`CostPerInference`) in US dollars for your
real-time endpoint, the expected maximum number of
`InvokeEndpoint` requests per minute sent to the
endpoint (`MaxInvocations`), and the model latency
(`ModelLatency`), which is the interval of time (in
milliseconds) that your model took to respond to SageMaker AI. The model
latency includes the local communication times taken to send the
request and to fetch the response from the container of a model and
the time taken to complete the inference in the container.

The following example shows the
`InferenceRecommendations` part of the response for
an inference recommendations job configured to return serverless
inference recommendations:

```
"InferenceRecommendations": [
      {
         "EndpointConfiguration": {
            "EndpointName": "`value`",
            "InitialInstanceCount": `value`,
            "InstanceType": "`value`",
            "VariantName": "`value`",
            "ServerlessConfig": {
                "MaxConcurrency": `value`,
                "MemorySizeInMb": `value`
            }
         },
         "InvocationEndTime": `value`,
         "InvocationStartTime": `value`,
         "Metrics": {
            "CostPerHour": `value`,
            "CostPerInference": `value`,
            "CpuUtilization": `value`,
            "MaxInvocations": `value`,
            "MemoryUtilization": `value`,
            "ModelLatency": `value`,
            "ModelSetupTime": `value`
         },
         "ModelConfiguration": {
            "Compiled": "False",
            "EnvironmentParameters": [],
            "InferenceSpecificationName": "`value`"
         },
         "RecommendationId": "`value`"
      }
   ]
```

You can interpret the recommendations for serverless inference
similarly to the results for real-time inference, with the exception
of the `ServerlessConfig`, which tells you the metrics
returned for a serverless endpoint with the given
`MemorySizeInMB` and when `MaxConcurrency =
 1`. To increase the throughput possible on the endpoint,
increase the value of `MaxConcurrency` linearly. For
example, if the inference recommendation shows
`MaxInvocations` as `1000`, then
increasing `MaxConcurrency` to `2` would
support 2000 `MaxInvocations`. Note that this is true
only up to a certain point, which can vary based on your model and
code. Serverless recommendations also measure the metric
`ModelSetupTime`, which measures (in microseconds)
the time it takes to launch computer resources on a serverless
endpoint. For more information about setting up serverless
endpoints, see the [Serverless Inference
documentation](serverless-endpoints.md "serverless-endpoints.md").

Amazon SageMaker Studio Classic
The inference recommendations populate in a new
**Inference recommendations** tab within
Studio Classic. It can take up to 45 minutes for the results to show up.
This tab contains **Results** and
**Details** column headings.

The **Details** column provides information about
the inference recommendation job, such as the name of the inference
recommendation, when the job was created (**Creation
time**), and more. It also provides
**Settings** information, such as the maximum
number of invocations that occurred per minute and information about
the Amazon Resource Names used.

The **Results** column provides a **Deployment goals** and **SageMaker AI
recommendations** window in which you can adjust the
order that the results are displayed based on deployment importance.
There are three dropdown menus that you can use to provide the level
of importance of the **Cost**,
**Latency**, and
**Throughput** for your use case. For each goal
(cost, latency, and throughput), you can set the level of
importance: **Lowest Importance**, **Low
Importance**, **Moderate importance**,
**High importance**, or **Highest
importance**.

Based on your selections of importance for each goal, Inference Recommender
displays its top recommendation in the **SageMaker
recommendation** field on the right of the panel, along
with the estimated cost per hour and inference request. It also
provides information about the expected model latency, maximum
number of invocations, and the number of instances. For serverless
recommendations, you can see the ideal values for the maximum
concurrency and endpoint memory size.

In addition to the top recommendation displayed, you can also see
the same information displayed for all instances that Inference Recommender tested
in the **All runs** section.

SageMaker AI console
You can view your instance recommendation jobs in the SageMaker AI console
by doing the following:

1. Go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose
   **Inference**, and then choose
   **Inference recommender**.
3. On the **Inference recommender jobs**
   page, choose the name of your inference recommendation
   job.

On the details page for your job, you can view the
**Inference recommendations**, which are the
instance types SageMaker AI recommends for your model, as shown in the
following screenshot.

![Screenshot of the inference recommendations list on the job details page in the SageMaker AI console.](/images/sagemaker/latest/dg/images/inf-rec-instant-recs.png)

In this section, you can compare the instance types by various
factors such as **Model latency**, **Cost
per hour**, **Cost per inference**,
and **Invocations per minute**.

On this page, you can also view the configurations you specified
for your job. In the **Monitor** section, you can
view the Amazon CloudWatch metrics that were logged for each instance type.
To learn more about interpreting these metrics, see [Interpret results](inference-recommender-interpret-results.md "inference-recommender-interpret-results.md").

For more information about interpreting the results of your recommendation
job, see [Recommendation
results](inference-recommender-interpret-results.md "inference-recommender-interpret-results.md").
