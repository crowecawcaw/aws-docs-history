# Security and access controls

The harness gives you the same security primitives as the rest of AgentCore, wired in by configuration.

- **Isolated execution.** Every session runs in its own Firecracker microVM in [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md"). No shared state, no shared filesystem.
- **IAM execution role.** The harness assumes an IAM role you own, configurable to include Bedrock, ECR, CloudWatch, and the AgentCore primitives it touches. See sample [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") below.
- **IAM permissions model.** Harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") resource. For example, calling `InvokeHarness` requires both `bedrock-agentcore:InvokeHarness` and `bedrock-agentcore:InvokeAgentRuntime` permissions on the harness ARN. The same pattern applies to control plane operations: `UpdateHarness` requires `bedrock-agentcore:UpdateAgentRuntime`, `DeleteHarness` requires `bedrock-agentcore:DeleteAgentRuntime`, and so on. See [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy") for the full list.
- **Inbound OAuth Support.** JWT configured Harness resources require callers to present a valid JWT issued by a configured identity provider before they can invoke the harness. [AgentCore Identity](identity.md "identity.md") threads the end-user identity through the agent, so downstream tools can call APIs with scoped user credentials instead of a shared service account.
- **VPC.** Connect harness sessions to your VPC for private access to internal resources.
- **Policies on Gateway.** When tools are served through [AgentCore Gateway](gateway.md "gateway.md"), Cedar-based [policies](policy.md "policy.md") can be configured to gate every call: who can call which tool, under which conditions, with which arguments.

###### Note

**SigV4 and per-user identity.** When callers authenticate with SigV4 (AWS IAM), the harness does not propagate per-user identity into downstream tool calls. This means per-user credential scoping features in [AgentCore Identity](identity.md "identity.md") Token Vault - such as user-scoped OAuth token storage and on-behalf-of token exchange - are only available when callers authenticate with a Bearer JWT via the OAuth inbound path. If your use case requires per-user credential scoping for downstream tools, configure inbound OAuth on the harness. SigV4 support for per-user identity is planned for a future release.

## Shared responsibility model

The harness is built on AgentCore Runtime and the security boundary is the same: IAM or JWT authentication combined with microVM isolation. Any principal that passes that gate reaches the tools and capabilities configured on the harness, which makes caller authorization and input validation a customer responsibility.

###### AWS responsibilities:

- Secure infrastructure and microVM isolation at the hardware level
- OS kernel patching
- Language runtime patching for direct code deployments
- Managed harness runtime code, including validation of the request structure `InvokeHarness` accepts
- Network infrastructure security
- Service availability and resilience

###### Your responsibilities:

- Agent code security and dependency management
- IAM access controls and resource policies
- Security of commands executed in runtime sessions
- Session-to-user mapping enforcement
- Input validation and prompt injection prevention - including validating all `InvokeHarness` input (see [Trust boundary and input validation](#harness-trust-boundary "#harness-trust-boundary"))
- Model configuration validation - such as `additionalParams`, `apiBase`, and `modelId` fields (see [Model configuration parameters](#harness-model-params-security "#harness-model-params-security"))
- Skill and instruction sources - ensuring that S3 buckets, Git repositories, and URLs used for skills contain trusted content (see [Skills and instructions](#harness-skills-security "#harness-skills-security"))
- Container image updates (for container deployments) - rebuild with the latest secure base image regularly
- Network configuration (security groups, VPC endpoints, route tables)

For the full AgentCore Runtime shared responsibility model, see [Security best practices for AgentCore Runtime](runtime-security-best-practices.md#security-bp-shared-responsibility "runtime-security-best-practices.md#security-bp-shared-responsibility").

### Trust boundary and input validation

Any principal that passes the IAM or JWT authentication and authorization gate has access to the full microVM session, including the tools and capabilities configured on the harness. The harness validates the structure of the request it accepts, but it does not inspect the meaning of prompts, screen content, or enforce behavioral constraints on the agent.

If you expose the harness to end users you do not fully trust (employees, external consumers, or third-party integrations), validate and sanitize messages in your application layer before passing them to `InvokeHarness`. This includes stripping content-block types or model configuration fields you do not want dispatched. This is the same pattern as any service that accepts payloads from authorized callers, such as Lambda, Amazon API Gateway, and Amazon SQS.

Tools run only as a result of model reasoning. The harness does not accept a [toolUse](../APIReference/API_HarnessToolUseBlock.md "../APIReference/API_HarnessToolUseBlock.md") block in the final message of an `InvokeHarness` request, so a caller cannot name a tool and have it dispatched directly.

The following example shows a request that the harness is configured to reject. The final message contains a `toolUse` block naming the built-in `shell` tool:

```
response = client.invoke_harness(
    harnessArn=HARNESS_ARN,
    runtimeSessionId=SESSION_ID,
    messages=[{
      "role": "assistant",
      "content": [
        {
          "toolUse": {
            "toolUseId": TOOL_USE_ID,
            "name": "shell",
            "input": {
              "command": "pwd",
            }
          }
        }
      ]
    }],
)
```

The harness does not evaluate which tool the block names, so this applies to built-in server-side tools and to inline functions supplied on the call.

Returning a tool result is still supported. The harness accepts a [toolResult](../APIReference/API_HarnessToolResultBlock.md "../APIReference/API_HarnessToolResultBlock.md") block in the final message, and the model resumes reasoning over that result. This is how [inline function tools](harness-tools.md "harness-tools.md") work: the assistant `toolUse` message is followed by the `toolResult` in the same request, so the `toolUse` block is not in the final message.

### Model configuration parameters

The `model` field in `InvokeHarness` accepts `additionalParams` for Bedrock, OpenAI, and LiteLLM configurations. These parameters are passed through to the underlying model provider unchanged. The harness does not validate, filter, or restrict these parameters.

Callers who can set `additionalParams` can:

- **Redirect requests to arbitrary endpoints** - LiteLLM’s `aws_bedrock_runtime_endpoint` parameter overrides the Bedrock endpoint URL. A caller can route the signed request - including the SigV4 signature and session credentials - to an endpoint that is specified in the trust model configuration.
- **Override HTTP headers** - OpenAI’s `extra_headers` parameter injects or overrides HTTP headers on the outbound request to the model provider, including the `Authorization` header.
- **Attempt IAM role assumption** - LiteLLM’s `aws_role_name` parameter instructs the runtime to assume a different IAM role before calling the model provider. The attempt succeeds or fails based on the execution role’s `sts:AssumeRole` permissions.
- **Change the target model or region** - The `modelId` and `apiBase` fields can redirect inference to a different model, region, or provider entirely.

If your application exposes `InvokeHarness` capabilities to callers you do not fully trust, consider implementing input validation in your application layer. Examples include:

- Stripping or allowlisting the `model` field before forwarding requests
- Validating or removing `additionalParams`, `apiBase`, and `modelId`
- Denying `sts:AssumeRole` on the execution role if role switching is not required
- Scoping the harness network access using VPC security groups

### Skills and instructions

Skills are bundles of markdown and scripts that the harness fetches from Amazon S3 or Git at invocation time and injects into the agent’s context. The harness treats all skill content as trusted input. It does not validate, sanitize, or inspect the content or source of skills before providing them to the agent.

You are responsible for:

- Ensuring that skill sources (S3 buckets, Git repositories, URLs) are trusted and access-controlled
- Reviewing skill content - including markdown instructions and any embedded scripts - before configuring them on the harness
- Controlling which principals can override the `skills` field per invocation, since callers can point the harness at arbitrary S3 or Git sources

Skills can be overridden per `InvokeHarness` call. If your application forwards caller-supplied input to `InvokeHarness`, a caller can supply their own skill sources containing arbitrary instructions or scripts. Examples of mitigations include:

- Stripping or ignoring the `skills` field from caller-supplied requests
- Allowlisting permitted S3 prefixes or Git repositories

### Observability and trace correlation

The harness automatically propagates correlation identifiers to downstream AgentCore primitives (Gateway, Memory, Code Interpreter, Browser) to enable unified trace views in CloudWatch. These identifiers are used for observability only - they are never used for authorization or data access decisions.

## Network configuration

By default, harness sessions run on the public network. To access private resources (databases, internal APIs, private subnets), deploy the harness in your VPC.

###### Example

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "VpcHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --environment '{"agentCoreRuntimeEnvironment": {"networkConfiguration": {"networkMode": "VPC", "vpcConfig": {"securityGroupIds": ["sg-0abc1234def56789a"], "subnetIds": ["subnet-0abc1234def56789a"]}}}}'
```

AgentCore CLI

```
agentcore add harness --name internal-agent \
  --network-mode VPC \
  --subnets subnet-0abc1234def56789a \
  --security-groups sg-0abc1234def56789a
agentcore deploy
```

###### Important

In VPC mode, the harness pulls its managed application container from a private Amazon ECR repository in the harness Region at the start of each session. Your VPC does not need a NAT gateway or internet access for this pull. Instead, create interface VPC endpoints for `com.amazonaws.<region>.ecr.dkr` and `com.amazonaws.<region>.ecr.api`, and a gateway VPC endpoint for `com.amazonaws.<region>.s3`, so the image and its layers resolve inside your VPC. If your agent calls Amazon Bedrock for inference, also create an interface endpoint for `com.amazonaws.<region>.bedrock-runtime`. Without the required endpoints, sessions fail to start due to image pull timeouts. The execution role must allow pulling from the private repository. See the [execution role policy](#harness-execution-role-policy "#harness-execution-role-policy").

For additional network configuration guidance, see [Configure AgentCore Runtime and built-in tools VPC configuration](agentcore-vpc.md "agentcore-vpc.md"). For inbound API connectivity via PrivateLink, see [VPC interface endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

## Inbound OAuth

Require callers to present a valid JWT issued by a configured identity provider before they can invoke the harness. [AgentCore Identity](identity.md "identity.md") threads the end-user identity through the agent, so downstream tools can call APIs with scoped user credentials instead of a shared service account.

###### Example

AWS CLI/boto3

```
aws bedrock-agentcore-control create-harness \
  --harness-name "OAuthHarness" \
  --execution-role-arn "arn:aws:iam::123456789012:role/MyHarnessRole" \
  --authorizer-configuration '{"customJWTAuthorizer": {"discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/<POOL_ID>/.well-known/openid-configuration", "allowedClients": ["<CLIENT_ID>"]}}'
```

Invoke with a Bearer token instead of SigV4 credentials:

```
curl -X POST "https://bedrock-agentcore.us-west-2.amazonaws.com/harnesses/invoke?harnessArn=${HARNESS_ARN}" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ID_TOKEN}" \
  -H "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: $(uuidgen)" \
  -d '{"messages": [{"role": "user", "content": [{"text": "Hi"}]}]}'
```

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

When your identity provider’s OIDC discovery endpoint is reachable only over PrivateLink, add private-endpoint flags to the CUSTOM\_JWT authorizer. Use a service-managed VPC endpoint:

```
agentcore add harness --name MyNewHarness \
  --authorizer-type CUSTOM_JWT \
  --discovery-url {DISCOVERY_URL} \
  --allowed-clients {CLIENT_ID} \
  --private-endpoint-vpc-id vpc-0abc1234def56789a \
  --private-endpoint-subnets subnet-0abc1234def56789a,subnet-0def5678abc12349b \
  --private-endpoint-ip-type IPV4 \
  --private-endpoint-security-groups sg-0abc1234def56789a
agentcore deploy
```

Or point at an existing VPC Lattice resource configuration instead of a managed VPC endpoint:

```
agentcore add harness --name MyNewHarness \
  --authorizer-type CUSTOM_JWT \
  --discovery-url {DISCOVERY_URL} \
  --allowed-clients {CLIENT_ID} \
  --private-endpoint-lattice-arn rcfg-0abc1234def56789a
agentcore deploy
```

###### Note

The private-endpoint flags are valid only with `--authorizer-type CUSTOM_JWT`. `--private-endpoint-vpc-id` and `--private-endpoint-lattice-arn` are mutually exclusive — choose one. With `--private-endpoint-vpc-id`, both `--private-endpoint-subnets` and `--private-endpoint-ip-type` (`IPV4` or `IPV6`) are required.

See [inbound JWT authorizer](inbound-jwt-authorizer.md "inbound-jwt-authorizer.md") for the full OAuth setup flow.

Interactive
Run `agentcore` in a project directory, select **add** , choose **Harness** , and advance to **Advanced settings** . Enable **Authentication** (and **Network** for VPC access) with **Space** , then press **Enter** .

1. Choose the authorizer type: **AWS IAM** (default) or **Custom JWT** for OIDC bearer-token auth.

![Select the harness authorizer type](images/tui/harness-security-02-auth-type.png) 2. For **Custom JWT** , enter the OIDC discovery URL.

![Configure Custom JWT: discovery URL](images/tui/harness-security-03-jwt.png) 3. Select which token constraints to validate - allowed audiences, allowed clients, allowed scopes, or custom claims.

![Select JWT constraints to configure](images/tui/harness-security-04-jwt-constraints.png) 4. Choose how the harness reaches the IdP discovery endpoint: **None** (publicly reachable), a **VPC Lattice resource** , or a **Managed VPC endpoint** (PrivateLink).

![PrivateLink options for the IdP discovery endpoint](images/tui/harness-security-05-privatelink.png) 5. For **Network** , choose VPC mode and provide the subnet IDs and security group IDs.

![Enter VPC subnet IDs](images/tui/harness-security-06-network-subnets.png)

Confirm the wizard, then run `agentcore deploy` to apply.

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

Harness APIs require permissions on both the harness resource and the underlying [AgentCore Runtime](runtime-how-it-works.md "runtime-how-it-works.md") and optional [AgentCore Memory](memory.md "memory.md") resources. The following table lists the required actions for each API:

| API                         | Required IAM actions                                                                                        |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `InvokeHarness`             | `bedrock-agentcore:InvokeHarness`, `bedrock-agentcore:InvokeAgentRuntime`                                   |
| `InvokeAgentRuntimeCommand` | `bedrock-agentcore:InvokeAgentRuntimeCommand`, `bedrock-agentcore:InvokeAgentRuntime`                       |
| `CreateHarness`             | `bedrock-agentcore:CreateHarness`, `bedrock-agentcore:CreateAgentRuntime`, `bedrock-agentcore:CreateMemory` |
| `UpdateHarness`             | `bedrock-agentcore:UpdateHarness`, `bedrock-agentcore:UpdateAgentRuntime`, `bedrock-agentcore:UpdateMemory` |
| `DeleteHarness`             | `bedrock-agentcore:DeleteHarness`, `bedrock-agentcore:DeleteAgentRuntime`, `bedrock-agentcore:DeleteMemory` |
| `GetHarness`                | `bedrock-agentcore:GetHarness`                                                                              |
| `ListHarnesses`             | `bedrock-agentcore:ListHarnesses`                                                                           |
| `CreateHarnessEndpoint`     | `bedrock-agentcore:CreateHarnessEndpoint`, `bedrock-agentcore:CreateAgentRuntimeEndpoint`                   |
| `UpdateHarnessEndpoint`     | `bedrock-agentcore:UpdateHarnessEndpoint`, `bedrock-agentcore:UpdateAgentRuntimeEndpoint`                   |
| `DeleteHarnessEndpoint`     | `bedrock-agentcore:DeleteHarnessEndpoint`, `bedrock-agentcore:DeleteAgentRuntimeEndpoint`                   |
| `GetHarnessEndpoint`        | `bedrock-agentcore:GetHarnessEndpoint`                                                                      |
| `ListHarnessEndpoints`      | `bedrock-agentcore:ListHarnessEndpoints`                                                                    |
| `ListHarnessVersions`       | `bedrock-agentcore:ListHarnessVersions`                                                                     |

Most actions use the harness ARN as the resource scope: `arn:aws:bedrock-agentcore:<region>:<accountId>:harness/<id>`. Endpoint actions also use the harness endpoint ARN: `arn:aws:bedrock-agentcore:<region>:<accountId>:harness/<id>/harness-endpoint/<endpointName>`.

The `GetHarnessEndpoint`, `UpdateHarnessEndpoint`, and `DeleteHarnessEndpoint` actions require both the harness ARN and the endpoint ARN. `CreateHarnessEndpoint` requires only the harness ARN. The endpoint doesn’t exist yet, so no endpoint ARN is needed. When you invoke a custom endpoint, `InvokeHarness` and `InvokeAgentRuntimeCommand` require both the harness ARN and the endpoint ARN.

### Sample execution role policy

The following sample covers a harness on the public network, which pulls its managed container image from Amazon ECR Public. A harness in VPC mode pulls the managed image from a private Amazon ECR repository in the harness Region, so its execution role also needs private ECR pull permissions. Add the statements in [VPC mode: managed image pull from private ECR](#harness-vpc-managed-ecr "#harness-vpc-managed-ecr") to the execution role for a VPC-mode harness.

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
      "Sid": "CloudWatchLogsPutResourcePolicy",
      "Effect": "Allow",
      "Action": [
        "logs:PutResourcePolicy"
      ],
      "Resource": "*"
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
    },
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
      "Resource": "arn:aws:bedrock-agentcore:<region>:<accountId>:memory/harness_<agentNameAbbrv>_*"
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

#### VPC mode: managed image pull from private ECR

Add this policy when your harness runs in VPC mode. In VPC mode, the harness pulls its managed application container from a private Amazon ECR repository in the harness Region (named `harness-<region>`). This pull uses private ECR instead of Amazon ECR Public, so the execution role needs private ECR pull permissions. This policy is separate from the [custom container image permissions](#harness-custom-container-ecr "#harness-custom-container-ecr")—it applies to the AWS managed image even when you do not supply your own container.

The repository is owned by an AWS service account, so the account in the repository ARN is wildcarded. The pull permissions are scoped to the harness Region.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EcrManagedImagePull",
      "Effect": "Allow",
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "arn:aws:ecr:<region>:*:repository/harness-*"
    },
    {
      "Sid": "EcrManagedImageToken",
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
```

Make sure the required VPC endpoints exist in your VPC (see [Network configuration](#harness-network-config "#harness-network-config")): interface endpoints for `com.amazonaws.<region>.ecr.dkr` and `com.amazonaws.<region>.ecr.api`, and a gateway endpoint for `com.amazonaws.<region>.s3`.

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

| Placeholder                 | Description                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| `<region>`                  | The AWS Region where your resource is deployed.                                                  |
| `<accountId>`               | Your AWS account ID.                                                                             |
| `<agentName>`               | The name of your harness agent.                                                                  |
| `<agentNameAbbrv>`          | The abbreviated form of your harness agent name used in default AgentCore Memory resource names. |
| `<memoryId>`                | The ID of your AgentCore memory resource.                                                        |
| `<browserCustomId>`         | The ID of your custom browser resource.                                                          |
| `<codeInterpreterCustomId>` | The ID of your custom code interpreter resource.                                                 |
| `<gatewayId>`               | The ID of your AgentCore Gateway resource.                                                       |
| `<apiKeyName>`              | The name of your API key credential provider.                                                    |
| `<skillBucket>`             | The name of the S3 bucket that holds your skill files.                                           |
| `<oauthProviderName>`       | The name of your OAuth2 credential provider.                                                     |
| `<ecrRegion>`               | The region where your ECR repository is hosted.                                                  |
| `<ecrAccountId>`            | The AWS account ID that owns the ECR repository.                                                 |
| `<ecrRepoName>`             | The name of your ECR repository.                                                                 |

###### Note

The trailing `-*` on Secrets Manager resources accounts for the random suffix that Secrets Manager appends to secret ARNs.

#### Related topics

- [Tools](harness-tools.md "harness-tools.md") - tool types and allowedTools patterns
- [Environment and filesystem](harness-environment.md "harness-environment.md") - custom environments and ECR permissions
- [Control cost with limits](harness-operations.md#harness-limits "harness-operations.md#harness-limits") - execution limits to control cost
- [API Documentation](harness-get-started.md#api-documentation "harness-get-started.md#api-documentation")
