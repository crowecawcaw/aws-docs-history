# Using Amazon Comprehend endpoints

You create an endpoint to run real-time analysis using a custom model. An endpoint includes managed resources
that makes your custom model available for real-time inference.

Amazon Comprehend assigns throughput to an endpoint using _Inference units_ (IU). An IU represents data
throughput of 100 characters per second. You can provision the endpoint with up to 10 inference units. You can scale
the endpoint throughput either up or down by updating the endpoint.

If your input documents include semi-structured documents or image files, the throughput of 100 characters per
second is for the characters extracted from the input file. The number of IUs that you provision for an endpoint
depends on character density of the input documents.

The [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") and [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md") API
responses include the character count for each page of input. You can use this information to estimate the number of
inference units to provision to achieve the desired throughput.

After you have completed your real-time analysis, delete the endpoint because the charge for it continues as
long as it's active. You can create another endpoint when you are ready to run further real-time analysis.

For more information on endpoint cost, see [Amazon Comprehend
Pricing](https://aws.amazon.com/comprehend/pricing/ "https://aws.amazon.com/comprehend/pricing/").

After you create an endpoint, you can monitor it with Amazon CloudWatch, update it to change its inference units, or
delete it when no longer needed. For more information, see [Monitoring Amazon Comprehend endpoints](manage-endpoints-monitor.md "manage-endpoints-monitor.md").
