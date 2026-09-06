# VPC and AWS PrivateLink with AWS Agent Registry

You can use AWS PrivateLink to create a private connection between your VPC and AWS Agent Registry. You can access AWS Agent Registry as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don’t need public IP addresses to access AWS Agent Registry.

You establish this private connection by creating an _interface endpoint_ , which is powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for AWS Agent Registry.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for AWS Agent Registry

Before you set up an interface endpoint for AWS Agent Registry, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

AWS Agent Registry provides two AWS PrivateLink endpoints:

- **Control plane endpoint**: `com.amazonaws.region.agent-registry-control` — for registry and record management (create, update, delete operations, and so on).
- **Data plane endpoint**: `com.amazonaws.region.agent-registry` — for record discovery and the registry MCP endpoint (search, InvokeRegistryMcp, and so on).

For a list of AWS Regions in which AWS Agent Registry interface endpoints are available, see [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md"). Interface endpoints are available in every Region where AWS Agent Registry is available.

###### Important

The data plane APIs support both AWS Signature Version 4 (SigV4) headers for authentication and Bearer Token (OAuth) authentication, and your endpoint policy is evaluated for both. A bearer-token caller carries no IAM identity, so it matches only a statement whose `Principal` is \* — never a specific account, role, or user ARN. For bearer-token requests to succeed through the endpoint, an `Allow` statement with `Principal` set to \* must cover the action and resource; a statement naming a specific AWS identity does not admit them. To restrict bearer-token callers, use a `Deny` statement with `Principal` set to \* scoped by `Action` and `Resource` — you cannot single out an individual bearer caller by principal, because bearer callers are indistinguishable at the principal level. A registry is authorized by either SigV4 or JWT according to its `authorizerType`, never both, so each registry only needs the statement form matching its own authorization mode.

AWS Agent Registry supports AWS IAM global condition context keys, including `aws:SourceVpc` and `aws:SourceVpce`. By default, you have full access to AWS Agent Registry through the interface endpoint. To restrict that access, attach a custom endpoint policy to the interface endpoint or associate a security group with the endpoint network interfaces.

## Create an interface endpoint for AWS Agent Registry

You can create an interface endpoint for AWS Agent Registry using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS Agent Registry using the following service name format:

- For control plane operations (registry and record management): `com.amazonaws.region.agent-registry-control` (for example, `com.amazonaws.us-east-1.agent-registry-control`)
- For data plane operations (record discovery and the registry MCP endpoint): `com.amazonaws.region.agent-registry` (for example, `com.amazonaws.us-east-1.agent-registry`)

If you enable private DNS for the interface endpoint, you can make API requests to AWS Agent Registry using its default Regional DNS names:

- Control plane: `agent-registry-control.region.api.aws` (for example, `agent-registry-control.us-east-1.api.aws`)
- Data plane: `agent-registry.region.api.aws` (for example, `agent-registry.us-east-1.api.aws`)

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint. With the default endpoint policy, you have full access to AWS Agent Registry through the interface endpoint. To restrict that access, attach a custom endpoint policy.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and IAM roles).

  - For the AWS Agent Registry data plane endpoint, if a registry uses JWT authorization instead of AWS Signature Version 4 (SigV4), set `Principal` to \* for any statement that authorizes JWT callers. With SigV4-based authentication, you can define the `Principal` as a specific AWS identity.

- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

The following examples show endpoint policies for each AWS Agent Registry endpoint. Choose a tab to view the policy for the control plane, the data plane record-discovery operations, or the data plane MCP endpoint.

###### Example

Control plane (registry and record management)

1. The following endpoint policy allows a specific IAM principal to manage registries and their records through the control plane endpoint.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:root"
         },
         "Action": [
            "agent-registry:CreateRegistry",
            "agent-registry:GetRegistry",
            "agent-registry:UpdateRegistry",
            "agent-registry:DeleteRegistry",
            "agent-registry:ListRegistries",
            "agent-registry:CreateRegistryRecord",
            "agent-registry:GetRegistryRecord",
            "agent-registry:UpdateRegistryRecord",
            "agent-registry:DeleteRegistryRecord",
            "agent-registry:ListRegistryRecords",
            "agent-registry:SubmitRegistryRecordForApproval",
            "agent-registry:UpdateRegistryRecordStatus"
         ],
         "Resource": "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/*"
      }
   ]
}
```

The following endpoint policy allows a specific IAM principal read-only access to registry and record metadata through the control plane endpoint — useful for tooling that inventories registries without modifying them.

**Read-only access to registry metadata**

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:root"
         },
         "Action": [
            "agent-registry:GetRegistry",
            "agent-registry:ListRegistries",
            "agent-registry:GetRegistryRecord",
            "agent-registry:ListRegistryRecords"
         ],
         "Resource": "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/*"
      }
   ]
}
```

To limit control plane access to a single registry and its records, use two resource ARNs targeting a specific `REGISTRY_ID` — one for the registry itself (`registry/REGISTRY_ID`) and one for its records (`registry/REGISTRY_ID/record/*`). `CreateRegistry` and `ListRegistries` operate at the account level and can’t be scoped to a specific registry ARN, so drop them from the action list — grant them separately with a wildcard resource if the caller needs them.

**Scope access to a single registry**

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:root"
         },
         "Action": [
            "agent-registry:GetRegistry",
            "agent-registry:UpdateRegistry",
            "agent-registry:DeleteRegistry",
            "agent-registry:CreateRegistryRecord",
            "agent-registry:GetRegistryRecord",
            "agent-registry:UpdateRegistryRecord",
            "agent-registry:DeleteRegistryRecord",
            "agent-registry:ListRegistryRecords",
            "agent-registry:SubmitRegistryRecordForApproval",
            "agent-registry:UpdateRegistryRecordStatus"
         ],
         "Resource": [
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/REGISTRY_ID",
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/REGISTRY_ID/record/*"
         ]
      }
   ]
}
```

Data plane (record discovery)

1. The following endpoint policy allows a specific IAM principal to search and browse approved records in one registry through the data plane endpoint.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:root"
         },
         "Action": [
            "agent-registry:SearchDiscoverableRegistryRecords",
            "agent-registry:ListDiscoverableRegistryRecords",
            "agent-registry:GetDiscoverableRegistryRecord"
         ],
         "Resource": [
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/REGISTRY_ID",
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/REGISTRY_ID/record/*"
         ]
      }
   ]
}
```

The following policy allows a specific IAM principal to search a SigV4-authorized registry, and any authenticated JWT caller to search a JWT-authorized registry, through the same endpoint.

**Mixed SigV4 and JWT authorization**

```
{
   "Statement": [
      {
         "Sid": "AllowIamSearchOnSigV4Registry",
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:root"
         },
         "Action": [
            "agent-registry:SearchDiscoverableRegistryRecords",
            "agent-registry:ListDiscoverableRegistryRecords",
            "agent-registry:GetDiscoverableRegistryRecord"
         ],
         "Resource": [
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/SIGV4_REGISTRY_ID",
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/SIGV4_REGISTRY_ID/record/*"
         ]
      },
      {
         "Sid": "AllowJwtSearchOnJwtRegistry",
         "Effect": "Allow",
         "Principal": "*",
         "Action": [
            "agent-registry:SearchDiscoverableRegistryRecords",
            "agent-registry:ListDiscoverableRegistryRecords",
            "agent-registry:GetDiscoverableRegistryRecord"
         ],
         "Resource": [
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/JWT_REGISTRY_ID",
            "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/JWT_REGISTRY_ID/record/*"
         ]
      }
   ]
}
```

Data plane (registry MCP endpoint)

1. The following endpoint policy allows any authenticated caller to invoke the registry MCP endpoint on a JWT-authorized registry. Because the MCP endpoint on a JWT-authorized registry is authenticated by bearer token rather than SigV4, set `Principal` to \*.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": "*",
         "Action": [
            "agent-registry:InvokeRegistryMcp",
            "agent-registry:SearchDiscoverableRegistryRecords"
         ],
         "Resource": "arn:aws:agent-registry:us-east-1:ACCOUNT_ID:registry/REGISTRY_ID"
      }
   ]
}
```

`InvokeRegistryMcp` is not exposed as an SDK client method — it is the IAM action that authorizes traffic sent to the registry’s MCP protocol path over the data plane endpoint. Invoking the registry MCP endpoint requires both `agent-registry:InvokeRegistryMcp` and the discovery-search action. In the `agent-registry` namespace the search action is `agent-registry:SearchDiscoverableRegistryRecords`; in the legacy `bedrock-agentcore` namespace it is `bedrock-agentcore:SearchRegistryRecords`.
