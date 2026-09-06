

# Cross-region processing
<a name="cross-region-processing"></a>

 Amazon Connect Decisions is powered by Amazon Bedrock and uses cross-region inference (CRIS) to distribute traffic across different AWS Regions to enhance large language model (LLM) inference performance and reliability. With cross-region inference, you get: 
+ Increased throughput and resilience during high demand periods
+ Improved performance
+ Access to newly launched Amazon Connect Decisions capabilities and features that rely on the most powerful LLMs hosted on Amazon Bedrock

 Cross-region inferencing works differently based on the AWS Region in which your Amazon Connect Decisions instance is created in. 

 For all instances created in the US geographical region, Amazon Connect Decisions will use Global CRIS. This means that inference requests will be routed to supported commercial AWS Regions worldwide, optimizing available resources and enabling higher model throughput. Refer to [Amazon Bedrock user guide to learn more about Global CRIS](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html). 

 For all instances created in the EU geographical region, Amazon Connect Decisions will use Geographic CRIS. This means that inference requests are kept within the AWS Regions that are part of the geography where the data originally resides. Refer to [Amazon Bedrock user guide to learn more about Geographic CRIS](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html). 

 For example, a request made from an Amazon Connect Decisions instance created in the US East (N. Virginia) (us-east-1) region can be routed to any AWS Region globally such as Asia Pacific (Sydney) (ap-southeast-2). However, for a request made from an Amazon Connect Decisions instance created in the Europe (Ireland) (eu-west-1) region is routed to an AWS Regions within the EU such as Europe (Frankfurt) (eu-central-1). For more information, see [Supported regions for Amazon Connect Decisions](security-supported-regions.html). 

 Although cross-region inferencing doesn't change where your data is stored, your requests and output results may move outside of the Region where the data originally resides. All data is encrypted while transmitted across Amazon's secure network. There's no additional cost for using cross-region inference. For information on where data is stored when you use Amazon Connect Decisions, see [Data protection in Amazon Connect Decisions](security-data-protection.html). 