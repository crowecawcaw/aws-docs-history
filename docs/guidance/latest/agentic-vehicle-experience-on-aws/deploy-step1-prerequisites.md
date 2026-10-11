

# Step 1: Deploy the prerequisites
<a name="deploy-step1-prerequisites"></a>

## CMS — Connected Mobility foundation
<a name="cms-connected-mobility-foundation"></a>

AVX requires CMS for live vehicle state (DynamoDB, Redis), KMS decrypt, and Cognito user pools. If CMS is not yet deployed in your target account and region, deploy it first:

```
# Run from the connected-mobility-guidance-on-aws project root
cd <cms-project-root>/deployment
make deploy-all          # deploys all CMS CDK stacks
make bootstrap-demo      # seeds demo vehicles, drivers, and tenant records
```

Capture the CMS stack outputs you will need for AVX configuration:

```
aws cloudformation describe-stacks \
  --stack-name cms-<stage>-storage \
  --region <region> \
  --query 'Stacks[0].Outputs' \
  --output table
```

Record the KMS key ARN, DynamoDB table prefix, Redis endpoint, VPC ID, and Redis security group ID. These populate the AVX `.env` file in Step 2.

## ADP — vehicle Knowledge Base and data products
<a name="adp-vehicle-knowledge-base-and-data-products"></a>

AVX uses ADP’s Bedrock Knowledge Base for RAG grounding (DTC guides, technical service bulletins, recalls, owner manuals, service policy) and the ADP Vehicle Knowledge Base data products for persona context. Seed the knowledge base from the ADP project:

```
# Run from the automotive-data-platform-on-aws guidance-for-vehicle-knowledge-base directory
cd <adp-project-root>/guidance-for-vehicle-knowledge-base
make create-tables       # provision DynamoDB tables for data products
make seed-all            # seed vehicle identity, parts, service network, and related data
make deploy              # deploy Bedrock Knowledge Base CDK stack
make upload-data         # upload knowledge documents to S3
make sync-data           # vectorize documents (starts the Bedrock KB ingestion job)
```

After `make sync-data` completes, note the Bedrock Knowledge Base ID from the ADP stack output:

```
aws cloudformation describe-stacks \
  --stack-name adp-<stage>-vehicle-knowledge-base \
  --region us-east-1 \
  --query 'Stacks[0].Outputs[?contains(OutputKey, `KnowledgeBase`)].OutputValue' \
  --output text
```

This Knowledge Base ID (`VSA_ADP_KB_ID`) is required for the AVX staging deploy pre-flight check. Without it, KB-grounded tools fall back to the embedded local corpora in `corpora/`.

**Note**  
ADP is technically optional. AVX falls back gracefully to embedded `corpora/` documents for triage and DTC guidance, and skips VIN decode, parts pricing, and service-center lookup tools. The full agentic experience described in this guidance requires ADP.