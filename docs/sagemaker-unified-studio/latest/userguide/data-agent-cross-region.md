# Cross-region processing in the SageMaker Data Agent

for Notebook

## Cross-region inference

The SageMaker Data Agent for Notebooks uses geographic cross-region inference to process
natural language requests and generate code responses. With geographic cross-region
inference, the agent will automatically route your inference request to optimize
performance, maximizing available compute resources and model availability, and providing
the best customer experience. The type of geographic cross-region inference used depends on
your Amazon SageMaker Unified Studio domain's Region. Most Regions use geographic cross-region inference, which
keeps requests within the same geography. However, some Regions use global cross-region
inference, which may route requests to any AWS Region globally.

### Cross-Region Inference

The SageMaker Data Agent is powered by Amazon Bedrock and uses cross-region inference
to distribute traffic across different AWS Regions to enhance large language model (LLM)
inference performance and reliability. With cross-region inference, you get:

- Increased throughput and resilience during high demand periods
- Improved performance

Although cross-region inference does not change where your notebook data or generated
code is stored, your natural language prompts, code context, and AWS Glue Data Catalog
metadata may be transmitted to different Regions for inference processing. All data is
encrypted in transit across Amazon's secure network.

There is no additional cost for using cross-region inference.

## Supported regions for cross-region

inference

**Regions Using Geographic cross-region inference**

For most Regions, cross-region inference requests are kept within the AWS Regions that
are part of the same geography where your Amazon SageMaker Unified Studio domain resides.
For example, a request made from a notebook in the US East (N. Virginia) Region is routed
only to AWS Regions within the United States geography. The following table describes what
Regions your requests may be routed to depending on the geography where the request
originated:

| Supported geography | Inference regions                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| United States       | US East (N. Virginia) (us-east-1), US West (Oregon) (us-west-2), US East<br>(Ohio) (us-east-2)                                  |
| Europe              | Europe (Frankfurt) (eu-central-1), Europe (Ireland) (eu-west-1), Europe<br>(Paris) (eu-west-3), Europe (Stockholm) (eu-north-1) |

## Regions Using Global Cross-Region

Inference

###### Important

The following AWS Regions use global cross-region inference. An inference request
made by the SageMaker Data Agent when your Amazon SageMaker Unified Studio domain's Region
is listed below will be securely routed to all available compute resources across all
global commercial AWS Regions, to optimize performance and availability:

- Asia Pacific (Mumbai) (ap-south-1)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Asia Pacific (Seoul) (ap-northeast-2)
- Asia Pacific (Singapore) (ap-southeast-1)
- Asia Pacific (Sydney) (ap-southeast-2)
- South America (São Paulo) (sa-east-1)
- Canada (Central) (ca-central-1)
