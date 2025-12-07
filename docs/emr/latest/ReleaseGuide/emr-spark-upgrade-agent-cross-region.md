# Cross-region processing for the Apache Spark Upgrade Agent

The Apache Spark Upgrade Agent uses cross-region inference to process natural language requests and generate responses. With cross-region inference, the agent will automatically route your inference request to optimize performance, maximizing available compute resources and model availability, and providing the best customer experience. The type of cross-region inference used depends on the region where you run the Apache Spark Upgrade Agent. In most Regions the agent will select the optimal region within your geography to process your inference requests. However, in some Regions an inference request made by the Agent will be securely routed to all available compute resources across all global commercial AWS Regions.

## Cross-Region Inference

The Apache Spark Upgrade agent is powered by and uses cross-region inference to distribute traffic across different AWS Regions to enhance large language model (LLM) inference performance and reliability.

Although cross-region inference does not change where your Spark application or your upgrade experience is hosted or your data is stored, your input prompts and output results may be transmitted to different Regions for inference processing. All data will be transmitted encrypted across Amazon's secure network.

There is no additional cost for using cross-region inference.

## Supported regions for cross-region inference

### Regions Using Geographic cross-region inference

For most Regions, cross-region inference requests are kept within AWS Regions that are part of the same geography where you run the Apache Spark Upgrade Agent. For example, a request made from the agent in the US East (N. Virginia) Region is routed only to AWS Regions within the United States geography. The following table describes what Regions your requests may be routed to depending on the geography where the request originated:

|     | Supported geography | Inference regions                                                                                                                                         |
| --- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | United States       | US East (N. Virginia) (us-east-1), US West (Oregon) (us-west-2), US East (Ohio) (us-east-2), US West (N. California) (us-west-2)                          |
| 2   | Europe              | Europe (Frankfurt) (eu-central-1), Europe (Ireland) (eu-west-1), Europe (Paris) (eu-west-3), Europe (Stockholm) (eu-north-1), Europe (London) (eu-west-2) |
| 3   | Asia Pacific        | Asia Pacific (Tokyo) (ap-northeast-1), Asia Pacific (Seoul) (ap-northeast-2), Asia Pacific (Mumbai) (ap-south-1)                                          |

### Regions Using Global Cross-Region Inference

###### Important

The following AWS Regions use global cross-region inference. When you use the Apache Spark Upgrade Agent in these Regions, your requests may be transmitted globally to other AWS Regions for inference processing to optimize performance and availability:

- South America (Sao Paulo) (sa-east-1)
- Asia Pacific (Singapore) (ap-southeast-1)
- Asia Pacific (Sydney) (ap-southeast-2)
- Canada (Central) (ca-central-1)
