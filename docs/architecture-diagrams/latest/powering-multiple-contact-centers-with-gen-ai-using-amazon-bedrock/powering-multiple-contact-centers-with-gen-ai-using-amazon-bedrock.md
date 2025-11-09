# Powering Multiple Contact Centers with GenAI Using Amazon Bedrock

Publication date: **October 4, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

Many contact center operators have a hybrid setup of using multiple vendors,
where each contact center has its own artificial intelligence and machine learning
(AI/ML) support. This architecture is designed to consolidate this support to a
single AI/ML stack for multiple contact center instances, powering multiple contact
centers by a single large language model (LLM) using Amazon Bedrock, thus
reducing cost and improving efficiency.

## Powering Multiple Contact Centers with GenAI Using Amazon Bedrock Diagram

![Reference architecture diagram showing how to consolidate support to a single AI/ML stack for multiple contact center instances, powering multiple contact centers by a single large language model.](images/powering-multiple-contact-centers-with-gen-ai-using-amazon-bedrock.png)

1. Call ingestion from a Genesys cloud contact center is achieved using an
   AudioHook websocket; call processing is handled using
   **Amazon Transcribe**.
2. **Amazon Connect** is an end-to-end
   cloud based contact center solution with built-in AI/ML capabilities.
   Call processing is done by using **Amazon Connect**
   Contact Lens.
3. Any other contact center based on session recording protocol (SIPREC)
   ingestion can be done by using **Amazon Chime**
   Voice Connector, with call processing by **Amazon Transcribe**.
4. **Amazon Kinesis Data Streams** streams all call transcripts
   simultaneously from all contact center instances.
5. **AWS Lambda** is used to initiate
   **Amazon Comprehend** sentiment analysis, which
   determines agent and caller sentiment. **Lambda**
   also initiates agent assist and transcript summarization.
6. Agent assist is based on **Amazon Lex** and
   **Amazon Kendra**. **Amazon Lex**
   is the conversational interface and uses **Lambda**
   to activate **Amazon Kendra** to provide intelligent search.
7. The event call processor **Lambda** function invokes
   the transcript summarization **Lambda** function when
   the call ends to generate a summary of the call from full transcript.
8. The LLM hosted in **Amazon Bedrock** leverages
   retrieval-augmented generation (RAG) with **Amazon Kendra**
   to securely ingest enterprise data into LLMs and fine tune it.
9. The post call summary **Lambda** hook that the
   LCA call event/transcript processor will invoke after the call summary is
   processed. This updates the call summary to a CRM system like Salesforce.
10. The web application establishes a secure GraphQL connection to the
    **AWS AppSync** API and subscribes to
    receive real-time events, such as new calls and call status changes
    for the calls list page, and new or updated transcription segments
    and computed analytics for the call details page.
11. **Amazon CloudFront** hosts a custom dashboard
    application for agents.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/powering-multiple-contact-centers-with-gen-ai-using-amazon-bedrock.md "samples/powering-multiple-contact-centers-with-gen-ai-using-amazon-bedrock.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [AWS Contact Center Intelligence (CCI) Solutions](https://aws.amazon.com/machine-learning/ml-use-cases/contact-center-intelligence/ "https://aws.amazon.com/machine-learning/ml-use-cases/contact-center-intelligence/")
- [Live call analytics and agent assist for your contact center with Amazon language AI services](https://aws.amazon.com/blogs/machine-learning/live-call-analytics-and-agent-assist-for-your-contact-center-with-amazon-language-ai-services/ "https://aws.amazon.com/blogs/machine-learning/live-call-analytics-and-agent-assist-for-your-contact-center-with-amazon-language-ai-services/")
- [Amazon Transcribe Live Call Analytics (LCA) Sample Solution (GitHub repo)](https://github.com/aws-samples/amazon-transcribe-live-call-analytics "https://github.com/aws-samples/amazon-transcribe-live-call-analytics")
- [Salesforce Integration](https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/plugins/salesforce-integration "https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/plugins/salesforce-integration")
- [Agent Assist with Amazon Connect](https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-connect-integration-stack "https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-connect-integration-stack")
- [Agent Assist with Genesys Cloud CX](https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-genesys-audiohook-stack "https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-genesys-audiohook-stack")
- [Agent Assist using Chime SDK](https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-chimevc-stack "https://github.com/aws-samples/amazon-transcribe-live-call-analytics/tree/develop/lca-chimevc-stack")

## Contributors

Contributors to this reference architecture diagram include:

- Ninad Joshi, AI/ML Partner Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | October 4, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
