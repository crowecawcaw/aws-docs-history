# Stop a RAG evaluation job in

Amazon Bedrock

You can stop a Retrieval Augmented Generation (RAG) evaluation job that is currently processing so that you can
easily reconfigure your evaluation and chosen metrics, for example.

The following example shows you how to stop a knowledge base evaluation job using the
AWS CLI.

_AWS Command Line Interface_

```
aws bedrock stop-evaluation-job \
 --job-identifier "arn:aws:bedrock:<region>:<account-id>:evaluation-job/<job-id>"

```
