

# Step 2: Configure AVX
<a name="deploy-step2-configure-cvx"></a>

Clone the AVX repository and create a Python virtual environment:

```
cd <cvx-project-root>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy the environment template and fill in values from the CMS and ADP stack outputs captured in Step 1:

```
cp .env.example .env
# Edit .env with your values; key variables:
#   CMS_STAGE           — CMS deployment stage (e.g., staging, prod)
#   CMS_KMS_KEY_ARN     — DynamoDB SSE decrypt key ARN from CMS stack output
#   REDIS_ENDPOINT      — Redis cluster endpoint from CMS MSK/ElastiCache output
#   VSA_STAGE           — AVX stack naming (e.g., staging, prod)
#   AWS_REGION          — primary deployment region
#   VSA_ADP_KB_ID       — Bedrock KB ID from ADP stack output (8-16 uppercase chars)
#   VSA_ADP_REGION      — ADP Athena/Glue region (default: us-east-1)
#   VSA_ADP_ACCOUNT_ID  — ADP account ID; omit to default to the AVX account
```

Copy the AgentCore runtime configuration template and fill in the execution role ARN and S3 bucket that CDK will create in Step 3:

```
cp .bedrock_agentcore.yaml.example .bedrock_agentcore.yaml
# Edit .bedrock_agentcore.yaml with:
#   execution_role — IAM role ARN for the AgentCore runtime (CDK output)
#   s3_path        — S3 bucket path for runtime artifacts (CDK output)
# Use relative paths for entrypoint and source_path to avoid machine-specific drift:
#   entrypoint: agents/supervisor/agentcore_app.py
#   source_path: .
```

Both files are gitignored. They must exist before any deploy command will succeed.