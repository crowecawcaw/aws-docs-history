# Use IAM condition keys with AgentCore Runtime and built-in tools VPC settings

Use AgentCore-specific condition keys for VPC settings to
provide additional permission controls for your AgentCore Runtime and
built-in tools. For example, require that all runtimes in your organization are connected
to a VPC. Specify the subnets and security groups that AgentCore Runtime users can and
cannot use.

AgentCore supports the following condition keys in IAM
policies:

- **bedrock-agentcore:subnets** – Allow or deny one or more
  subnets.
- **bedrock-agentcore:securityGroups** – Allow or deny one or
  more security groups.
  The AgentCore Control Plane API operations
  `CreateAgentRuntime`, `UpdateAgentRuntime`,
  `CreateCodeInterpreter`, and `CreateBrowser` support these condition keys.
  For more information about using condition keys in IAM policies, see [IAM JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the IAM User Guide.

## Example policies with condition keys for VPC

settings

The following examples demonstrate how to use condition keys for VPC settings. Create a policy statement with the desired restrictions, then attach the policy statement to the
target user or role.

### Require that users deploy only VPC-connected

runtimes and tools

To require that all users deploy only VPC-connected AgentCore Runtime and built-in tools, deny runtime and tool create and update operations that don't include valid subnets and
security groups.

```
{
    "Sid": "EnforceVPCRuntime",
    "Action": [
        "bedrock-agentcore:CreateAgentRuntime",
        "bedrock-agentcore:UpdateAgentRuntime",
        "bedrock-agentcore:CreateCodeInterpreter",
        "bedrock-agentcore:CreateBrowser"
    ],
    "Effect": "Deny",
    "Resource": "*",
    "Condition": {
        "Null": {
            "bedrock-agentcore:subnets": "true",
            "bedrock-agentcore:securityGroups": "true"
        }
    }
}
```

### Enforce that users use only specific subnets

and security groups

To enforce that users use only specific approved subnets and security groups, use the `ForAnyValue` set operator with `StringNotEquals`. The condition returns true if any one of the context key values in the request does not match the context key values in the policy, denying requests that include any unapproved values. The following example enforces that users can only use
`subnet-0123456789abcdef0` and `subnet-0123456789abcdef1` for subnets, and `sg-0123456789abcdef0` and `sg-0123456789abcdef1` for security groups.

```
[
  {
    "Sid": "DenyIfNotSpecificSubnets",
    "Effect": "Deny",
    "Action": [
      "bedrock-agentcore:CreateAgentRuntime",
      "bedrock-agentcore:UpdateAgentRuntime",
      "bedrock-agentcore:CreateCodeInterpreter",
      "bedrock-agentcore:CreateBrowser"
    ],
    "Resource": "*",
    "Condition": {
      "ForAnyValue:StringNotEquals": {
        "bedrock-agentcore:subnets": ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]
      }
    }
  },
  {
    "Sid": "DenyIfNotSpecificSecurityGroups",
    "Effect": "Deny",
    "Action": [
      "bedrock-agentcore:CreateAgentRuntime",
      "bedrock-agentcore:UpdateAgentRuntime",
      "bedrock-agentcore:CreateCodeInterpreter",
      "bedrock-agentcore:CreateBrowser"
    ],
    "Resource": "*",
    "Condition": {
      "ForAnyValue:StringNotEquals": {
        "bedrock-agentcore:securityGroups": ["sg-0123456789abcdef0", "sg-0123456789abcdef1"]
      }
    }
  }
]
```

### Deny users access to specific subnets

or security groups

To deny users access to specific subnets and security groups, use the `ForAnyValue` set operator with `StringEquals`. The condition returns true if any one of the context key values in the request matches any one of the context key values in the policy. The following example denies users
access to `subnet-0123456789abcdef0` and `subnet-0123456789abcdef1` for subnets, and `sg-0123456789abcdef0` and `sg-0123456789abcdef1` for security groups.

```
[
  {
    "Sid": "EnforceOutOfSubnet",
    "Action": [
      "bedrock-agentcore:CreateAgentRuntime",
      "bedrock-agentcore:UpdateAgentRuntime",
      "bedrock-agentcore:CreateCodeInterpreter",
      "bedrock-agentcore:CreateBrowser"
    ],
    "Effect": "Deny",
    "Resource": "*",
    "Condition": {
      "ForAnyValue:StringEquals": {
        "bedrock-agentcore:subnets": ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]
      }
    }
  },
  {
    "Sid": "EnforceOutOfSecurityGroups",
    "Action": [
      "bedrock-agentcore:CreateAgentRuntime",
      "bedrock-agentcore:UpdateAgentRuntime",
      "bedrock-agentcore:CreateCodeInterpreter",
      "bedrock-agentcore:CreateBrowser"
    ],
    "Effect": "Deny",
    "Resource": "*",
    "Condition": {
      "ForAnyValue:StringEquals": {
        "bedrock-agentcore:securityGroups": ["sg-0123456789abcdef0", "sg-0123456789abcdef1"]
      }
    }
  }
]
```
