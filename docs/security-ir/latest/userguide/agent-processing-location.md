

# Investigative agent processing location
<a name="agent-processing-location"></a>

 The Security Incident Response investigative agent processes metadata in Amazon Bedrock's global region, regardless of which Region your case or findings data originates from. This processing is transient—the agent analyzes the metadata to generate insights and recommendations but does not store the metadata persistently in the Amazon Bedrock infrastructure. 

 When the agent completes its analysis, the generated insights and recommendations are stored with your case investigation data in the Region where the case was created. The metadata used for processing is not retained in Amazon Bedrock global Region after the analysis completes. 