

# Cross-Region processing for the Apache Spark agents

The Apache Spark agents use cross-Region inference to process natural language requests and generate responses. With cross-Region inference, the agents automatically route your inference request to optimize performance, maximizing available compute resources and model availability, and providing the best customer experience. The type of cross-Region inference used depends on the Region where you run the Apache Spark agents. In most Regions, the agents select the optimal Region within your geography to process your inference requests. However, in some Regions an inference request made by the agents is securely routed to all available compute resources across all global commercial AWS Regions.

## Cross-Region inference
<a name="cross-region-inference-overview"></a>

The Apache Spark agents are powered by Amazon Bedrock and use cross-Region inference to distribute traffic across different AWS Regions to enhance large language model (LLM) inference performance and reliability.

Although cross-Region inference doesn't change where your Spark application or your analysis experience is hosted, or where your data is stored, your input prompts and output results might be transmitted to different Regions for inference processing. All data is transmitted encrypted across Amazon's secure network.

There is no additional cost for using cross-Region inference.

## Supported Regions for cross-Region inference
<a name="supported-regions-cross-region"></a>

**Regions using geographic cross-Region inference**

For most Regions, cross-Region inference requests are kept within AWS Regions that are part of the same geography where you run the Apache Spark agents. For example, a request made from an agent in the US East (N. Virginia) Region is routed only to AWS Regions within the United States geography. The following table shows the geography that processes your inference requests for each Region where you run the Apache Spark agents.


| Supported geography | Regions where you run the Apache Spark agents | 
| --- | --- | 
| United States | US East (N. Virginia) (us-east-1), US West (Oregon) (us-west-2), US East (Ohio) (us-east-2), US West (N. California) (us-west-1) | 
| Europe | Europe (Frankfurt) (eu-central-1), Europe (Ireland) (eu-west-1), Europe (Paris) (eu-west-3), Europe (Stockholm) (eu-north-1), Europe (London) (eu-west-2), Europe (Zurich) (eu-central-2), Europe (Milan) (eu-south-1), Europe (Spain) (eu-south-2) | 
| Asia Pacific | Asia Pacific (Tokyo) (ap-northeast-1), Asia Pacific (Seoul) (ap-northeast-2), Asia Pacific (Mumbai) (ap-south-1), Asia Pacific (Osaka) (ap-northeast-3), Asia Pacific (Hyderabad) (ap-south-2), Asia Pacific (Hong Kong) (ap-east-1), Asia Pacific (Taipei) (ap-east-2), Asia Pacific (Melbourne) (ap-southeast-4), Asia Pacific (Jakarta) (ap-southeast-3), Asia Pacific (Malaysia) (ap-southeast-5), Asia Pacific (New Zealand) (ap-southeast-6), Asia Pacific (Thailand) (ap-southeast-7) | 

### Regions using global cross-Region inference
<a name="global-cross-region-inference"></a>

**Important**  
The following AWS Regions use global cross-Region inference. When you use the Apache Spark agents in these Regions, your requests might be transmitted globally to other AWS Regions for inference processing to optimize performance and availability:  
South America (São Paulo) (sa-east-1)
Asia Pacific (Singapore) (ap-southeast-1)
Asia Pacific (Sydney) (ap-southeast-2)
Canada (Central) (ca-central-1)
Canada West (Calgary) (ca-west-1)
Mexico (Central) (mx-central-1)
Africa (Cape Town) (af-south-1)
Israel (Tel Aviv) (il-central-1)