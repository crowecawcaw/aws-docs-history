

# Investigative agent processing
<a name="investigative-agent-processing"></a>

 The AWS Security Incident Response investigative agent uses Amazon Bedrock to analyze the metadata from your cases and findings. The agent helps you: 
+ Identify patterns
+ Generate insights
+ Decide on response actions

## How the investigative agent retains, stores, and processes your data
<a name="investigative-agent-data-handling"></a>
+ **The investigative agent doesn't keep your data.** The agent uses your metadata only while it analyzes your case. Amazon Bedrock doesn't store it afterward.
+ **Your results stay in your case Region.** All results are stored in the Region where you created the case.
+ **Processing location depends on your case Region.** For most Regions, processing stays within a geography, such as the EU. For others, processing can happen in any commercial AWS Region. For details, see [Investigative agent processing location](agent-processing-location.md).