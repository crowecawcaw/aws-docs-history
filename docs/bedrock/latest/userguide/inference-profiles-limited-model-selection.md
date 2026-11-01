

# Inference profiles with limited model selection
<a name="inference-profiles-limited-model-selection"></a>

Amazon Bedrock offers a range of inference options, including in-Region inference, geographic cross-Region inference, and global cross-Region inference, to help customers meet different performance, cost, and compliance needs. For example, in-Region inference is designed primarily for customers with data residency requirements, and keeps inference processing within a specific Region. The following table lists the inference profiles that are designated as inference profiles with limited model selection. Compared with other inference profiles, they are expected to offer a narrower selection of models, new models or model versions might not be released for them, and quota increase requests might take longer to process.

Review the following considerations as you take dependencies on an inference profile with limited model selection.

## Current inference profiles with limited model selection
<a name="inference-profiles-limited-model-selection-current"></a>


| **Region name** | **Region code** | **Inference option** | 
| --- | --- | --- | 
| Canada (Central) | ca-central-1 | Canada cross-Region inference | 
| Canada West (Calgary) | ca-west-1 | Canada cross-Region inference | 
| Asia Pacific (Seoul) | ap-northeast-2 | In-Region inference | 
| Asia Pacific (Singapore) | ap-southeast-1 | In-Region inference | 
| Europe (London) | eu-west-2 | In-Region inference | 
| Europe (Zurich) | eu-central-2 | In-Region inference | 
| South America (São Paulo) | sa-east-1 | In-Region inference | 

The designation applies only to the inference options listed in this table. Other cross-Region inference profiles that you invoke from these Regions keep their standard model selection. These include global cross-Region inference and geographic cross-Region inference profiles that route requests outside these Regions.

## Considerations
<a name="inference-profiles-limited-model-selection-considerations"></a>

**Model availability expectations**
+ New models, and new versions of existing models, might not be released for inference profiles with limited model selection, or might be released much later than for other inference profiles.
+ When a model reaches end of life, a successor model might not be released for an inference profile with limited model selection.

**Model lifecycle**
+ Models offered through inference profiles with limited model selection continue to follow the standard Amazon Bedrock model lifecycle, including advance notice of Legacy and End-of-Life dates.
+ When a model reaches its End-of-Life date, it's no longer available through the inference profile. A replacement model might not be offered through the same inference profile for you to migrate to. Plan your workloads around published End-of-Life dates, including how you'll migrate to another inference profile if needed.

## Choosing an inference profile with limited model selection
<a name="inference-profiles-limited-model-selection-choosing"></a>

In-Region and geographic inference profiles are best suited for workloads whose compliance, regulatory, or contractual obligations require inference to be processed within a specific Region or geography. However, some of these inference profiles might be subject to the limitations described on this page.

If you use these inference profiles, we recommend that you do the following:
+ **Plan for model lifecycle events.** Treat each model's End-of-Life date as a planning milestone. Don't expect a successor model to become available through the same inference profile.
+ **Reassess your requirements periodically.** If your data residency requirements change, evaluate other inference profiles. For workloads that don't require inference to be processed within a specific Region or geography, global cross-Region inference and other geographic cross-Region inference profiles, such as US and EU cross-Region inference, route requests across a broader set of AWS Regions.
+ **Engage your AWS account team early.** Talk to your account team if your workload has long-term model or version requirements.

## Related resources
<a name="inference-profiles-limited-model-selection-resources"></a>
+ [Supported Regions and models for inference profiles](inference-profiles-support.md)
+ [Model lifecycle](model-lifecycle.md)
+ [Quotas for Amazon Bedrock](quotas.md)