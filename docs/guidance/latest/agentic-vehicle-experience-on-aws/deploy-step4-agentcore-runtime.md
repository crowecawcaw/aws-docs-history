

# Step 4: Deploy the AgentCore runtime
<a name="deploy-step4-agentcore-runtime"></a>

The `agentcore` CLI is provided by the `bedrock-agentcore-starter-toolkit` package, already installed via `pip install -r requirements.txt` in Step 2. Verify it is available:

```
agentcore --version
```

## Initial configure (first time only)
<a name="initial-configure-first-time-only"></a>

If `.bedrock_agentcore.yaml` does not yet exist, or after running `agentcore destroy`, configure the runtime before deploying:

```
# Text-mode (HTTP InvokeAgentRuntime — used by the web UI /assistant/chat route)
agentcore configure \
  --entrypoint agents/supervisor/agentcore_app.py \
  --name vsa_supervisor_text_<stage> \
  --execution-role arn:aws:iam::<account>:role/<agentcore-execution-role-name> \
  --region <region> \
  --deployment-type direct_code_deploy \
  --runtime PYTHON_3_12 \
  --protocol HTTP \
  --disable-otel \
  --non-interactive

# Bidirectional voice (Nova 2 Sonic — used by iOS companion and Connect voice channel)
agentcore configure \
  --entrypoint agents/supervisor/bidi_app.py \
  --name vsa_supervisor_bidi_<stage> \
  --execution-role arn:aws:iam::<account>:role/<agentcore-execution-role-name> \
  --region <region> \
  --deployment-type direct_code_deploy \
  --runtime PYTHON_3_12 \
  --protocol BIDIRECTIONAL_HTTP \
  --disable-otel \
  --non-interactive
```

After `agentcore configure`, edit `.bedrock_agentcore.yaml` to use relative paths for `entrypoint` and `source_path` — machine-absolute paths cause runtime artifact errors on redeploy from a different working directory:

```
# Verify relative paths in .bedrock_agentcore.yaml:
#   entrypoint: agents/supervisor/agentcore_app.py   (not /Users/.../agents/...)
#   source_path: .                                    (not /Users/...)
```

## Subsequent deploys
<a name="subsequent-deploys"></a>

Once `.bedrock_agentcore.yaml` exists, `make deploy-staging` (or `make deploy`) handles everything. For agent-code-only changes (no CDK change), deploy the runtime directly without re-running CDK:

```
# Deploy only the voice runtime
agentcore deploy -a vsa_supervisor_bidi_<stage> --auto-update-on-conflict \
  --env CMS_STAGE=<stage> \
  --env VSA_STAGE=<stage> \
  --env AWS_REGION=<region> \
  --env VSA_ADP_KB_ID=<adp-kb-id> \
  --env VSA_ADP_REGION=<adp-region> \
  --env VSA_FOUNDATION_MEMORY_ID=<memory-id> \
  --env VSA_KB_SOURCE_CATEGORY_FILTER=true

# Deploy only the text runtime
agentcore deploy -a vsa_supervisor_text_<stage> --auto-update-on-conflict \
  --env CMS_STAGE=<stage> \
  --env VSA_STAGE=<stage> \
  --env AWS_REGION=<region> \
  --env VSA_ADP_KB_ID=<adp-kb-id> \
  --env VSA_ADP_REGION=<adp-region> \
  --env VSA_FOUNDATION_MEMORY_ID=<memory-id> \
  --env VSA_KB_SOURCE_CATEGORY_FILTER=true
```

 `agentcore deploy` packages the source tree, uploads it to S3, builds a container via AWS CodeBuild, and updates the runtime. The process takes approximately three to five minutes on first deploy and slightly less on subsequent deploys when the dependency layer is cached.

## Verify the runtime is ready
<a name="verify-the-runtime-is-ready"></a>

```
aws bedrock-agentcore-control get-agent-runtime \
  --agent-runtime-id <runtime-id> \
  --region <region> \
  --query 'status' \
  --output text
```

The response should be `READY`. A status of `FAILED` indicates a container build or entrypoint error; inspect CodeBuild logs for root cause.