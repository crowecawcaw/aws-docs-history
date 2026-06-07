# Security and access controls

The harness gives you the same security primitives as the rest of AgentCore, wired in by configuration.

- **Isolated execution.** Every session runs in its own Firecracker microVM in [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md"). No shared state, no shared filesystem.
- **IAM execution role.** The harness assumes an IAM role you own, configurable to include Bedrock, ECR, CloudWatch, and the AgentCore primitives it touches. See sample [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") below.
- **IAM permissions model.** Harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") resource. For example, calling `InvokeHarness` requires both `bedrock-agentcore:InvokeHarness` and `bedrock-agentcore:InvokeAgentRuntime` permissions on the harness ARN. The same pattern applies to control plane operations: `UpdateHarness` requires `bedrock-agentcore:UpdateAgentRuntime`, `DeleteHarness` requires `bedrock-agentcore:DeleteAgentRuntime`, and so on. See [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") for the full list.
- **Inbound OAuth Support.** JWT configured Harness resources require callers to present a valid JWT issued by a configured identity provider before they can invoke the harness. [AgentCore Identity](identity.md "identity.md") threads the end-user identity through the agent, so downstream tools can call APIs with scoped user credentials instead of a shared service account.
- **VPC.** Connect harness sessions to your VPC for private access to internal resources.
- **Policies on Gateway.** When tools are served through [AgentCore Gateway](gateway.md "gateway.md"), Cedar-based [policies](policy.md "policy.md") can be configured to gate every call: who can call which tool, under which conditions, with which arguments.
  Harness follows the AgentCore [shared responsibility model](runtime-security-best-practices.md#security-bp-shared-responsibility "runtime-security-best-practices.md#security-bp-shared-responsibility")

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

###### Important

The harness pulls its application container from Amazon ECR Public at the start of each session. When running in VPC mode, your VPC must allow outbound access to `public.ecr.aws`. Amazon ECR Public does not support VPC endpoints, so your VPC must have a NAT gateway with a route to an internet gateway. If this connectivity is not available, sessions will fail to start due to image pull timeouts.

For additional network configuration guidance, see [Configure AgentCore Runtime and built-in tools VPC configuration](agentcore-vpc.md "agentcore-vpc.md"). For inbound API connectivity via PrivateLink, see [VPC interface endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

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

Harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") resource. The following table lists the required actions for each API:

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
        "arn:aws:bedrock:<region>:<accountId>:*"
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
      "Resource": "arn:aws:logs:<region>:<accountId>:log-group:/aws/bedrock-agentcore/runtimes/*"
    },
    {
      "Sid": "CloudWatchLogsDescribeGroups",
      "Effect": "Allow",
      "Action": [
        "logs:DescribeLogGroups"
      ],
      "Resource": "arn:aws:logs:<region>:<accountId>:log-group:*"
    },
    {
      "Sid": "CloudWatchLogsStream",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:<region>:<accountId>:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
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
      "Resource": [
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default/workload-identity/harness_<agentName>-*"
      ]
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
      "Resource": "arn:aws:bedrock-agentcore:<region>:aws:browser/*"
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
      "Resource": "arn:aws:bedrock-agentcore:<region>:aws:code-interpreter/*"
    }
  ]
}
```

The AgentCore CLI creates a role with these permissions automatically when you scaffold a harness project. The policy above is for cases where you create the role yourself.

###### Note

The `BedrockModelInvocation` sample statement above allows invocation of all foundation models across all regions and all Bedrock resources in your account. To scope this down, replace the resource ARNs with specific [inference profiles](../../../bedrock/latest/userguide/inference-profiles.md "../../../bedrock/latest/userguide/inference-profiles.md"), which let you route requests across models and regions with a single ARN. For example: `arn:aws:bedrock:<destination_regions>:<accountId>:inference-profile/<profileId>` paired with all allowed regions `arn:aws:bedrock:<region>:<accountId>:foundation-model/<modelId>`.

For production workloads, scope `Resource` values down to the specific ARNs your harness needs rather than using `"*"`.

### Additional permissions for optional features

Below are sample policies you can append to your execution role based on the features your harness uses. Follow the principle of least privilege - grant your harness agent only the specific tools and credentials it needs for inference. See [Placeholder reference](#harness-optional-placeholders "#harness-optional-placeholders") for placeholder definitions.

#### Private ECR access (custom container images)

Add this policy when your harness uses a private ECR image for a custom container.

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
      "Resource": "arn:aws:ecr:<ecrRegion>:<ecrAccountId>:repository/<ecrRepoName>"
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

Add this policy when your harness uses a customer-owned memory instance.

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
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:memory/<memoryId>"
    }
  ]
}
```

#### AgentCore Browser (custom)

Add this policy when your harness uses a customer-owned custom browser resource.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreBrowserCustom",
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
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:browser-custom/<browserCustomId>"
    }
  ]
}
```

#### AgentCore Code Interpreter (custom)

Add this policy when your harness uses a customer-owned custom code interpreter.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreCodeInterpreterCustom",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:StartCodeInterpreterSession",
        "bedrock-agentcore:StopCodeInterpreterSession",
        "bedrock-agentcore:GetCodeInterpreterSession",
        "bedrock-agentcore:ListCodeInterpreterSessions",
        "bedrock-agentcore:InvokeCodeInterpreter"
      ],
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:code-interpreter-custom/<codeInterpreterCustomId>"
    }
  ]
}
```

#### AgentCore Gateway

Add this policy when your harness uses a gateway configured with SigV4 inbound authentication.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreGatewayAccess",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:InvokeGateway",
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:gateway/<gatewayId>"
    }
  ]
}
```

#### Skill sources in Amazon S3 and Git

Add this policy when your harness fetches a skill from an Amazon S3 source. The execution role lists and downloads the skill objects under the bucket prefix.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreSkillS3Access",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::<skillBucket>",
        "arn:aws:s3:::<skillBucket>/*"
      ]
    }
  ]
}
```

To fetch a skill from a private Git repository, the harness reads a personal access token from an API key credential provider. Grant the **API key credential provider** policy shown below for the credential provider that holds the token.

#### API key credential provider (OpenAI, Gemini, LiteLLM, or MCP header ARN references)

Add this policy when your harness uses an API key credential provider for model providers such as OpenAI, Gemini, or LiteLLM.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreApiKeyTokenVaultDefault",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceApiKey",
      "Resource": [
        "arn:aws:bedrock-agentcore:<region>:<accountId>:token-vault/default",
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default/workload-identity/harness_<agentName>-*"
      ]
    },
    {
      "Sid": "AgentCoreApiKeyTokenVaultPerKey",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceApiKey",
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:token-vault/default/apikeycredentialprovider/<apiKeyName>"
    },
    {
      "Sid": "AgentCoreApiKeySecret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:<region>:<accountId>:secret:bedrock-agentcore-identity!default/apikey/<apiKeyName>-*"
    }
  ]
}
```

#### OAuth2 credential provider (OAuth-protected Gateway)

Add this policy when your harness uses an OAuth2 credential provider for OAuth-protected gateway tools.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AgentCoreOAuth2TokenVaultDefault",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceOauth2Token",
      "Resource": [
        "arn:aws:bedrock-agentcore:<region>:<accountId>:token-vault/default",
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default",
        "arn:aws:bedrock-agentcore:<region>:<accountId>:workload-identity-directory/default/workload-identity/harness_<agentName>-*"
      ]
    },
    {
      "Sid": "AgentCoreOAuth2TokenVaultPerProvider",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceOauth2Token",
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:token-vault/default/oauth2credentialprovider/<oauthProviderName>"
    },
    {
      "Sid": "AgentCoreOAuth2Secret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:<region>:<accountId>:secret:bedrock-agentcore-identity!default/oauth2/<oauthProviderName>-*"
    }
  ]
}
```

#### Placeholder reference

Replace the following placeholders in the policies above with values specific to your environment:

| Placeholder                 | Description                                            |
| --------------------------- | ------------------------------------------------------ |
| `<region>`                  | The AWS Region where your resource is deployed.        |
| `<accountId>`               | Your AWS account ID.                                   |
| `<agentName>`               | The name of your harness agent.                        |
| `<memoryId>`                | The ID of your AgentCore memory resource.              |
| `<browserCustomId>`         | The ID of your custom browser resource.                |
| `<codeInterpreterCustomId>` | The ID of your custom code interpreter resource.       |
| `<gatewayId>`               | The ID of your AgentCore Gateway resource.             |
| `<apiKeyName>`              | The name of your API key credential provider.          |
| `<skillBucket>`             | The name of the S3 bucket that holds your skill files. |
| `<oauthProviderName>`       | The name of your OAuth2 credential provider.           |
| `<ecrRegion>`               | The region where your ECR repository is hosted.        |
| `<ecrAccountId>`            | The AWS account ID that owns the ECR repository.       |
| `<ecrRepoName>`             | The name of your ECR repository.                       |

###### Note

The trailing `-*` on Secrets Manager resources accounts for the random suffix that Secrets Manager appends to secret ARNs.

#### Related topics

- [Connect to tools](harness-tools.md "harness-tools.md") - tool types and allowedTools patterns
- [Environment and Skills](harness-environment.md "harness-environment.md") - custom environments and ECR permissions
- [Control cost with limits](harness-operations.md#harness-limits "harness-operations.md#harness-limits") - execution limits to control cost
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
