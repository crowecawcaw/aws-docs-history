

# Use secrets safely with AI Coding Agents
<a name="retrieving-secrets-ai-agents"></a>

When AI coding agents have shell or AWS API access, they can call `get-secret-value` and receive plaintext secrets in their context window. This creates multiple risks: secret values can leak into conversation history, logs, or downstream tool calls.

To prevent this, use the *secret safety* skill in the [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws). The skill teaches AI agents to use dynamic references resolved at runtime, so the agent orchestrates secret usage without ever seeing the plaintext value.

**Important**  
This is a best-effort defense, not a security boundary. It prevents the most common leakage path but cannot stop all evasion vectors. Combine with IAM least-privilege, CloudTrail monitoring, and VPC endpoint policies.

## How it works
<a name="retrieving-secrets-ai-agents-how-it-works"></a>

The secret safety skill provides two layers of protection:

1. **Skill guidance** – Teaches the agent to use `{{resolve:secretsmanager:...}}` dynamic references with `asm-exec`, a wrapper script that resolves references at runtime. The plaintext value exists only in the child process and never enters the agent's context window.

1. **Structural enforcement (hook)** – A `PreToolUse` hook automatically blocks any attempt to call `get-secret-value` or `batch-get-secret-value` via AWS CLI, SDK, MCP tools, or direct access to the AWS Workload Credentials Provider daemon. No manual configuration is required.

## Prerequisites
<a name="retrieving-secrets-ai-agents-prerequisites"></a>
+ An AI coding agent that supports plugins, such as [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or [OpenAI Codex](https://openai.com/index/codex/).
+ The [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) `aws-core` plugin installed.
+ One of the following secret resolution backends:
  + **AWS Workload Credentials Provider** running on `localhost:2773`. See [Using the AWS Workload Credentials Provider](workload-credentials-provider.md).
  + **AWS credentials** that can sign requests to the AWS MCP endpoint.
+ IAM permissions: `secretsmanager:GetSecretValue` on the secrets you want to resolve.

## Install the plugin
<a name="retrieving-secrets-ai-agents-install"></a>

Install the `aws-core` plugin for your agent platform. The secret safety skill and hook activate automatically.

For Claude Code:

```
claude plugin add ./plugins/aws-core
```

For OpenAI Codex:

```
codex plugin add ./plugins/aws-core
```

For other supported platforms, see the [Agent Toolkit for AWS README](https://github.com/aws/agent-toolkit-for-aws).

## The `{{resolve:...}}` syntax
<a name="retrieving-secrets-ai-agents-syntax"></a>

When the agent needs to pass a secret to a command, it uses a dynamic reference instead of calling `get-secret-value`:

```
{{resolve:secretsmanager:<secret-id>:<field-type>:<json-key>:<version-stage>}}
```


| Component | Required | Default | Description | 
| --- | --- | --- | --- | 
| secret-id | Yes | – | Secret name or full ARN | 
| field-type | No | SecretString | Must be SecretString | 
| json-key | No | (full value) | Key to extract from JSON secret value | 
| version-stage | No | AWSCURRENT | Version stage label | 

## Use `asm-exec` to run commands with secrets
<a name="retrieving-secrets-ai-agents-asm-exec"></a>

`asm-exec` is a wrapper script that resolves `{{resolve:...}}` references in command arguments, then runs the target command. The secret value exists only in the child process.

```
asm-exec -- <command> [arguments with {{resolve:...}} references]
```

`asm-exec` resolves references through the first available backend:

1. **AWS Workload Credentials Provider** on `localhost:2773` – locally cached.

1. **AWS MCP endpoint** – SigV4-signed request using available AWS credentials.

**Example Connect to a PostgreSQL database**  

```
asm-exec -- psql \
  "host=mydb.example.com \
  user={{resolve:secretsmanager:prod/db-creds:SecretString:username}} \
  password={{resolve:secretsmanager:prod/db-creds:SecretString:password}}" \
  -c "SELECT * FROM users LIMIT 10"
```

**Example Make an API call with a bearer token**  

```
asm-exec -- curl -H "Authorization: Bearer {{resolve:secretsmanager:prod/api-token}}" \
  https://api.example.com/data
```

**Example Connect to MySQL with multiple secrets**  

```
asm-exec -- mysql \
  -h {{resolve:secretsmanager:prod/mysql:SecretString:host}} \
  -u {{resolve:secretsmanager:prod/mysql:SecretString:username}} \
  -p{{resolve:secretsmanager:prod/mysql:SecretString:password}} \
  -e "SHOW TABLES"
```

**Example Pass a secret as an environment variable to a Docker container**  

```
asm-exec -- docker run \
  -e "DB_PASSWORD={{resolve:secretsmanager:prod/db:SecretString:password}}" \
  myapp:latest
```

## Cross-region secrets
<a name="retrieving-secrets-ai-agents-cross-region"></a>

For secrets stored in a different region than your default region, either use the full ARN (which includes the region) or set the `AWS_REGION` environment variable.

```
# Using full ARN (region is extracted automatically)
asm-exec -- curl -H "X-Api-Key: {{resolve:secretsmanager:arn:aws:secretsmanager:eu-west-1:123456789012:secret:prod/key-a1b2c3}}" \
  https://eu.api.example.com/data

# Using AWS_REGION
export AWS_REGION=eu-west-1
asm-exec -- curl -H "X-Api-Key: {{resolve:secretsmanager:prod/key}}" \
  https://eu.api.example.com/data
```

## Security considerations
<a name="retrieving-secrets-ai-agents-security"></a>
+ **Subprocess isolation** – The target command runs via `subprocess.run`. Secret values exist only in the `asm-exec` process memory and the child process arguments.

## How the hook blocks direct secret access
<a name="retrieving-secrets-ai-agents-hook"></a>

When the `aws-core` plugin is enabled, a `PreToolUse` hook intercepts tool calls before execution. It blocks:
+ `aws secretsmanager get-secret-value` and `batch-get-secret-value` via CLI
+ `get_secret_value` and `batch_get_secret_value` via SDK calls in scripts
+ Direct access to the AWS Workload Credentials Provider daemon path (`localhost:2773/secretsmanager/get`)
+ `GetSecretValue` operations via MCP tools or structured AWS API calls

When a call is blocked, the agent receives a deny message that directs it to use `{{resolve:...}}` references with `asm-exec` instead.

## Troubleshooting
<a name="retrieving-secrets-ai-agents-troubleshooting"></a>

### "Secret not found" errors
<a name="retrieving-secrets-ai-agents-ts-not-found"></a>

Verify the secret exists and your IAM role has `secretsmanager:GetSecretValue` permission. Secret names are case-sensitive.

### AWS Workload Credentials Provider connection refused
<a name="retrieving-secrets-ai-agents-ts-connection-refused"></a>

The AWS Workload Credentials Provider may not be running. This is non-fatal – `asm-exec` falls through to the SigV4-signed MCP endpoint. Ensure AWS credentials are available so that backend can authenticate.

### "Failed to resolve" errors
<a name="retrieving-secrets-ai-agents-ts-failed-resolve"></a>

Both backends were unreachable. Check that either the AWS Workload Credentials Provider is running or AWS credentials are valid (`aws sts get-caller-identity`), that the secret's region is correct, and that your identity has `secretsmanager:GetSecretValue` on the secret.

### Resolution produces empty string
<a name="retrieving-secrets-ai-agents-ts-empty-string"></a>

The JSON key may not exist in the secret value. Verify the secret structure in the AWS console or ask the secret owner to confirm available keys.

### Hook does not block a call
<a name="retrieving-secrets-ai-agents-ts-hook-not-blocking"></a>

Hooks load at agent session start. If you installed the plugin mid-session, restart the agent session for the hook to activate.