

# Prerequisites
<a name="plan-prerequisites"></a>

AVX is a composition layer — it does not replicate the data or contact-center infrastructure it consumes. The four platform prerequisites below must be in place before you run the AVX deployment.

## Upstream platform foundations
<a name="plan-prereq-upstream-foundations"></a>


| Prerequisite | What it provides | Where to start | 
| --- | --- | --- | 
| Connected Mobility (CMS) deployed | Live vehicle state (DynamoDB \+ Redis Last-Known State), service history, trip records, IoT telemetry pipeline, recall integration, multi-tenant Cognito pools |  [Guidance for Connected Mobility on AWS](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws) — `make deploy-all` followed by `make bootstrap-demo`  | 
| Automotive Data Platform (ADP) vehicle knowledge base seeded | Vehicle Identity Graph (VIN decode), Parts Catalog, Service Network, Vehicle Lifecycle data products, and the Bedrock Knowledge Base (DTC guides, TSBs, recalls, owner manuals, service policy) used for grounded RAG answers |  [Guidance for Automotive Data Platform on AWS](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws) — `guidance-for-vehicle-knowledge-base` module: `make create-tables && make seed-all && make deploy && make upload-data && make sync-data`  | 
| Amazon Connect instance provisioned | Voice and chat contact flows, a chat queue per tenant, and for the P0 callback a callback flow, queue and claimed phone number | Create an Amazon Connect instance in your target region via the [Amazon Connect getting started guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-get-started.html). AVX wires to it via the Connect instance ARN supplied in your tenant configuration — no Connect-specific code changes required. | 
| Amazon Bedrock model access enabled | Claude Sonnet for the supervisor agent; Amazon Nova 2 Sonic for speech-to-speech voice; Amazon Titan Embeddings for KB ingestion (ADP-side) | Request model access in the [Amazon Bedrock console](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) for your deployment region. See the [Supported Region Posture](plan-region-posture.md) section for region requirements. | 

## Developer tooling
<a name="plan-prereq-tools"></a>

Install the following tools in your local environment before running any AVX deploy commands. All commands in the deployment guide assume these are on your `PATH`.


| Tool | Minimum version | Install | 
| --- | --- | --- | 
| AWS CLI | v2 |  [Install AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Configure credentials with access to your AVX deployment account. | 
| Node.js | 18\+ |  [nodejs.org](https://nodejs.org/) or use `nvm`. Required for AWS CDK. | 
| Python | 3.12\+ |  [python.org](https://www.python.org/downloads/) or system package manager. Use a virtual environment: `python3 -m venv .venv && source .venv/bin/activate`. | 
| AWS CDK CLI | 2.x |  `npm install -g aws-cdk` after Node.js is installed. | 
| Bedrock AgentCore CLI (`agentcore`) | Latest stable |  `pip install bedrock-agentcore-starter-toolkit` inside your activated virtual environment. The `agentcore` command is used to configure and deploy the agent runtime container. | 

**Note**  
The `bedrock-agentcore-starter-toolkit` package ships the `agentcore` CLI as a separate install — it is not included in the AVX `requirements.txt`. Install it after activating your virtual environment.