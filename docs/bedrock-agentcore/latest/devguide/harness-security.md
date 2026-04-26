# Security and access controls

The harness gives you the same security primitives as the rest of AgentCore, wired in by configuration.

- **Isolated execution.** Every session runs in its own Firecracker microVM in [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md"). No shared state, no shared filesystem.
- **IAM execution role.** The harness assumes an IAM role you own. Least-privilege access to Bedrock, ECR, CloudWatch, and the AgentCore primitives it touches. See [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") below.
- **IAM permissions model.** harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") resource. For example, calling `InvokeHarness` requires both `bedrock-agentcore:InvokeHarness` and `bedrock-agentcore:InvokeAgentRuntime` permissions on the harness ARN. The same pattern applies to control plane operations: `UpdateHarness` requires `bedrock-agentcore:UpdateAgentRuntime`, `DeleteHarness` requires `bedrock-agentcore:DeleteAgentRuntime`, and so on. See [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") for the full list.
- **Inbound OAuth.** Require callers to present a valid JWT issued by a configured identity provider before they can invoke the harness. [AgentCore Identity](identity.md "identity.md") threads the end-user identity through the agent, so downstream tools can call APIs with scoped user credentials instead of a shared service account.
- **VPC.** Connect harness sessions to your VPC for private access to internal resources.
- **Policies on Gateway.** When tools are served through [AgentCore Gateway](gateway.md "gateway.md"), Cedar-based [policies](policy.md "policy.md") gate every call: who can call which tool, under which conditions, with which arguments.

###### Note

**SigV4 and per-user identity.** When callers authenticate with SigV4 (AWS IAM), the harness does not propagate per-user identity into downstream tool calls. This means per-user credential scoping features in [AgentCore Identity](identity.md "identity.md") Token Vault - such as user-scoped OAuth token storage and on-behalf-of token exchange - are only available when callers authenticate with a Bearer JWT via the OAuth inbound path. If your use case requires per-user credential scoping for downstream tools, configure inbound OAuth on the harness. SigV4 support for per-user identity is planned for a future release.

## Network configuration

By default, harness sessions run on the public network. To access private resources (databases, internal APIs, private subnets), deploy the harness in your VPC.

###### Example

AgentCore CLI

```
agentcore add harness --name internal-agent \
  --network-mode VPC \
  --subnets subnet-0abc1234def56789a \
  --security-groups sg-0abc1234def56789a
agentcore deploy
```

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "VpcHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --environment '{"agentCoreRuntimeEnvironment": {"networkConfiguration": {"networkMode": "VPC", "vpcConfig": {"securityGroupIds": ["sg-0abc1234def56789a"], "subnetIds": ["subnet-0abc1234def56789a"]}}}}'
```

Learn more: [AgentCore VPC](agentcore-vpc.md "agentcore-vpc.md") · [VPC interface endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md")

## Inbound OAuth

Require callers to present a valid JWT issued by a configured identity provider before they can invoke the harness. [AgentCore Identity](identity.md "identity.md") threads the end-user identity through the agent, so downstream tools can call APIs with scoped user credentials instead of a shared service account.

###### Example

AgentCore CLI

```
agentcore add harness --name MyNewHarness \
  --authorizer-type CUSTOM_JWT \
  --discovery-url {DISCOVERY_URL} \
  --allowed-clients {CLIENT_ID}
agentcore deploy
```

Invoke with a bearer token:

```
agentcore invoke --harness MyNewHarness --bearer-token "{token}" "Hello"
```

See [inbound JWT authorizer](inbound-jwt-authorizer.md "inbound-jwt-authorizer.md") for the full OAuth setup flow.

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "OAuthHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --authorizer-configuration '{"oidcAuthorizerConfiguration": {"discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/<POOL_ID>/.well-known/openid-configuration"}}'
```

Invoke with a Bearer token instead of SigV4 credentials:

```
curl -X POST "https://bedrock-agentcore.us-west-2.amazonaws.com/harnesses/invoke?harnessArn=${HARNESS_ARN}" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ID_TOKEN}" \
  -H "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: $(uuidgen)" \
  -d '{"messages": [{"role": "user", "content": [{"text": "Hi"}]}]}'
```

Learn more: [AgentCore Identity](identity.md "identity.md") · [inbound JWT authorizer](inbound-jwt-authorizer.md "inbound-jwt-authorizer.md") · [outbound credentials](identity-outbound-credential-provider.md "identity-outbound-credential-provider.md")

## Gateway policies

When tools are served through [AgentCore Gateway](gateway.md "gateway.md"), Cedar-based [policies](policy.md "policy.md") gate every call: who can call which tool, under which conditions, with which arguments.

Learn more: [AgentCore Policy](policy.md "policy.md") · [common patterns](policy-common-patterns.md "policy-common-patterns.md")

## Execution role policy

The harness assumes an IAM execution role you provide. The role’s trust policy must allow the AgentCore service principal to assume it:

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "bedrock-agentcore.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
```

### Required IAM permissions for callers

harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") resource. The following table lists the required actions for each API:

| API                         | Required IAM actions                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------- |
| `InvokeHarness`             | `bedrock-agentcore:InvokeHarness`, `bedrock-agentcore:InvokeAgentRuntime`             |
| `InvokeAgentRuntimeCommand` | `bedrock-agentcore:InvokeAgentRuntimeCommand`, `bedrock-agentcore:InvokeAgentRuntime` |
| `CreateHarness`             | `bedrock-agentcore:CreateHarness`, `bedrock-agentcore:CreateAgentRuntime`             |
| `UpdateHarness`             | `bedrock-agentcore:UpdateHarness`, `bedrock-agentcore:UpdateAgentRuntime`             |
| `DeleteHarness`             | `bedrock-agentcore:DeleteHarness`, `bedrock-agentcore:DeleteAgentRuntime`             |
| `GetHarness`                | `bedrock-agentcore:GetHarness`                                                        |
| `ListHarnesses`             | `bedrock-agentcore:ListHarnesses`                                                     |

All actions are scoped to the harness ARN (e.g., `arn:aws:bedrock-agentcore:{region}:{account}:harness/{id}`).

### Sample execution role policy

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockModelInvocation",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/*",
        "arn:aws:bedrock:{{region}}:{{accountId}}:*"
      ]
    },
    {
      "Sid": "EcrPublicTokenAccess",
      "Effect": "Allow",
      "Action": [
        "ecr-public:GetAuthorizationToken"
      ],
      "Resource": "*"
    },
    {
      "Sid": "StsForEcrPublicPull",
      "Effect": "Allow",
      "Action": [
        "sts:GetServiceBearerToken"
      ],
      "Resource": "*"
    },
    {
      "Sid": "XRayTracingAccess",
      "Effect": "Allow",
      "Action": [
        "xray:PutTraceSegments",
        "xray:PutTelemetryRecords",
        "xray:GetSamplingRules",
        "xray:GetSamplingTargets"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogsGroup",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:{{region}}:{{accountId}}:log-group:/aws/bedrock-agentcore/runtimes/*"
    },
    {
      "Sid": "CloudWatchLogsDescribeGroups",
      "Effect": "Allow",
      "Action": [
        "logs:DescribeLogGroups"
      ],
      "Resource": "arn:aws:logs:{{region}}:{{accountId}}:log-group:*"
    },
    {
      "Sid": "CloudWatchLogsStream",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:{{region}}:{{accountId}}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
    },
    {
      "Sid": "CloudWatchMetricsPublish",
      "Effect": "Allow",
      "Resource": "*",
      "Action": "cloudwatch:PutMetricData",
      "Condition": {
        "StringEquals": {
          "cloudwatch:namespace": "bedrock-agentcore"
        }
      }
    },
    {
      "Sid": "AgentCoreWorkloadIdentity",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetWorkloadAccessToken",
        "bedrock-agentcore:GetWorkloadAccessTokenForJWT"
      ],
      "Resource": ["*"]
    },
    {
      "Sid": "AgentCoreBrowserDefault",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:StartBrowserSession",
        "bedrock-agentcore:StopBrowserSession",
        "bedrock-agentcore:GetBrowserSession",
        "bedrock-agentcore:ListBrowserSessions",
        "bedrock-agentcore:UpdateBrowserStream",
        "bedrock-agentcore:ConnectBrowserAutomationStream",
        "bedrock-agentcore:ConnectBrowserLiveViewStream"
      ],
      "Resource": "arn:aws:bedrock-agentcore:{{region}}:aws:browser/*"
    },
    {
      "Sid": "AgentCoreCodeInterpreterDefault",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:StartCodeInterpreterSession",
        "bedrock-agentcore:StopCodeInterpreterSession",
        "bedrock-agentcore:GetCodeInterpreterSession",
        "bedrock-agentcore:ListCodeInterpreterSessions",
        "bedrock-agentcore:InvokeCodeInterpreter"
      ],
      "Resource": "arn:aws:bedrock-agentcore:{{region}}:aws:code-interpreter/*"
    }
  ]
}
```

The AgentCore CLI creates a role with these permissions automatically when you scaffold a harness project. The policy above is for cases where you create the role yourself.

For production workloads, scope `Resource` values down to the specific ARNs your harness needs rather than using `"*"`.

### Additional permissions for optional features

Add the following policies to the execution role based on the features your harness uses.

#### Private ECR access (custom container images)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ECRImageAccess",
      "Effect": "Allow",
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "arn:aws:ecr:*:*:repository/*"
    },
    {
      "Sid": "ECRTokenAccess",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
```

#### AgentCore Memory

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreMemory",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:CreateEvent",
        "bedrock-agentcore:DeleteEvent",
        "bedrock-agentcore:GetEvent",
        "bedrock-agentcore:ListEvents",
        "bedrock-agentcore:RetrieveMemoryRecords"
      ],
      "Resource": "arn:aws:bedrock-agentcore:*:*:memory/*"
    }
  ]
}
```

#### AgentCore Gateway

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreGateway",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:InvokeGateway",
      "Resource": "arn:aws:bedrock-agentcore:*:*:gateway/*"
    }
  ]
}
```

#### API key credential provider (OpenAI, Gemini)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreApiKeyTokenVault",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceApiKey",
      "Resource": [
        "arn:aws:bedrock-agentcore:*:*:token-vault/default",
        "arn:aws:bedrock-agentcore:*:*:token-vault/default/apikeycredentialprovider/*"
      ]
    },
    {
      "Sid": "AgentCoreApiKeySecret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:*:*:secret:bedrock-agentcore-identity!default/apikey/*"
    }
  ]
}
```

#### OAuth2 credential provider (OAuth-protected Gateway)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreOAuth2TokenVault",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceOauth2Token",
      "Resource": [
        "arn:aws:bedrock-agentcore:*:*:token-vault/default",
        "arn:aws:bedrock-agentcore:*:*:token-vault/default/oauth2credentialprovider/*",
        "arn:aws:bedrock-agentcore:*:*:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:*:*:workload-identity-directory/default/workload-identity/*"
      ]
    },
    {
      "Sid": "AgentCoreOAuth2Secret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:*:*:secret:bedrock-agentcore-identity!default/oauth2/*"
    }
  ]
}
```

#### Related topics

- [Connect to tools](harness-tools.md "harness-tools.md") - tool types and allowedTools patterns
- [Environment and Skills](harness-environment.md "harness-environment.md") - custom environments and ECR permissions
- [Control cost with limits](harness-operations.md#harness-limits "harness-operations.md#harness-limits") - execution limits to control cost
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
