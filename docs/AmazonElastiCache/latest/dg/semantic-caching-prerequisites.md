# Prerequisites

To implement semantic caching with ElastiCache for Valkey, you need:

1. An AWS account with access to Amazon Bedrock, including Amazon Bedrock AgentCore
   Runtime, Amazon Titan Text Embeddings v2 model, and an LLM such as Amazon Nova Premier enabled
   in the US East (N. Virginia) Region.
2. The AWS Command Line Interface (AWS CLI) configured with Python 3.11 or later.
3. An Amazon Elastic Compute Cloud instance inside your Amazon VPC with the following packages installed:

```
pip install numpy pandas valkey bedrock-agentcore \
            langchain-aws 'langgraph-checkpoint-aws[valkey]'
```

4. An ElastiCache for Valkey cluster running version 8.2 or later, which supports vector
   search. For instructions on creating a cluster, see
   [Creating a cluster for Valkey or Redis OSS](Clusters.Create.md "Clusters.Create.md").
