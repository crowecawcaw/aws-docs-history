

# Investigative agent processing location
<a name="agent-processing-location"></a>

 The investigative agent runs in the Region where you create your case. Amazon Bedrock then sends model requests based on that Region's *inference profile*. An inference profile determines where your data can be processed. There are two types: 
+ **Geographic**: Processing stays within a specific geography, such as the US or the EU. Your data doesn't leave that geography.
+ **Global**: Processing can happen in any commercial AWS Region.

 Regardless of profile type, results are always stored in your case Region, and Amazon Bedrock doesn't keep the metadata used during processing. 

## Supported Regions and where your data is processed
<a name="agent-processing-location-supported"></a>

 Cases created in the following Regions have full investigative agent support. Find your case Region in the first column to see where your data can be processed. 


**Investigative agent processing locations by case Region**  

| Case Region | Inference profile | Where processing can occur | 
| --- | --- | --- | 
| US East (N. Virginia) | US | `us-east-1`, `us-east-2`, `us-west-2` | 
| US East (Ohio) | US | `us-east-1`, `us-east-2`, `us-west-2` | 
| US West (Oregon) | US | `us-east-1`, `us-east-2`, `us-west-2` | 
| Europe (Ireland) | EU | `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-3` | 
| Europe (London) | EU | `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-3` | 
| Europe (Paris) | EU | `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-3` | 
| Europe (Frankfurt) | EU | `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-3` | 
| Europe (Stockholm) | EU | `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-3` | 
| Asia Pacific (Tokyo) | Japan | `ap-northeast-1`, `ap-northeast-3` | 
| Asia Pacific (Sydney) | Australia | `ap-southeast-2` | 
| Canada (Central) | Global | Any commercial AWS Region | 
| South America (São Paulo) | Global | Any commercial AWS Region | 
| Asia Pacific (Seoul) | Global | Any commercial AWS Region | 
| Asia Pacific (Singapore) | Global | Any commercial AWS Region | 
| Asia Pacific (Mumbai) | Global | Any commercial AWS Region | 

**Important**  
 If you create cases in a Region that uses the Global inference profile, case metadata can be processed in any commercial AWS Region. Organizations with strict data residency requirements must evaluate whether this cross-Region processing is compatible with their compliance obligations. Results are always stored in your case Region. 

## Regions where the investigative agent isn't available
<a name="agent-processing-location-unsupported"></a>

 AWS Security Incident Response is available in the following Regions, but the investigative agent isn't available in them. Cases created in these Regions don't receive automated investigation. 
+ Africa (Cape Town): `af-south-1`
+ Asia Pacific (Hong Kong): `ap-east-1`
+ Asia Pacific (Hyderabad): `ap-south-2`
+ Asia Pacific (Jakarta): `ap-southeast-3`
+ Asia Pacific (Melbourne): `ap-southeast-4`
+ Europe (Milan): `eu-south-1`
+ Europe (Spain): `eu-south-2`
+ Europe (Zurich): `eu-central-2`
+ Middle East (Bahrain): `me-south-1`
+ Middle East (UAE): `me-central-1`

## How the investigative agent investigates resources in multiple Regions
<a name="agent-processing-location-cross-region"></a>

 A case can include impacted resources in more than one Region. The agent retrieves metadata from each Region separately. What it can access depends on the type of Region: 
+ **Standard Regions**: The agent can retrieve metadata, such as AWS CloudTrail events and Amazon Elastic Compute Cloud (Amazon EC2) details, from any standard Region. This is true even if the Region differs from your case Region.
+ **Opt-in Regions**: The agent can't retrieve metadata from opt-in Regions. Resources in an opt-in Region aren't included in the investigation.
+ **Global services**: Data from AWS Identity and Access Management (IAM) and AWS Cost Explorer is always available, regardless of Region.