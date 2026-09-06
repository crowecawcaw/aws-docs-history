

# Connecting HealthOmics workflows to a VPC
<a name="workflows-vpc-networking"></a>

With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a private, virtual network that you've defined. You can give your HealthOmics workflows access to resources in your VPC by configuring your runs to use VPC networking mode. When VPC networking is enabled, your runs can access resources within your VPC and connect to external resources over the public internet if your VPC has internet access configured.

**Note**  
Every HealthOmics workflow run executes inside a VPC that is owned and managed by the HealthOmics service. These VPCs are maintained automatically and are not visible to customers. Configuring your run to access resources in your Amazon VPC has no effect on the HealthOmics-managed VPC.

## When to use VPC networking
<a name="vpc-when-to-use"></a>

Use VPC networking when your runs need to:
+ Access publicly available datasets over the internet (for example, NIH datasets, academic repositories)
+ Connect to third-party license servers or external APIs
+ Read or write data from Amazon S3 buckets in other AWS Regions
+ Access on-premises resources in your private network
+ Connect to AWS resources within your VPC

**Note**  
When you connect a run to a VPC, it can only access resources available within that VPC. To give your run access to the internet, you must also configure your VPC for internet access. For more information, see [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

**Topics**
+ [When to use VPC networking](#vpc-when-to-use)
+ [Networking modes](#vpc-networking-modes)
+ [Getting started](#vpc-getting-started)
+ [VPC requirements](#vpc-requirements)
+ [Service-linked role for VPC networking](vpc-service-linked-role.md)
+ [Connecting to a VPC in another account](workflows-vpc-cross-account.md)
+ [Configuration APIs](#vpc-configuration-apis)
+ [Running workflows with VPC networking](#vpc-running-workflows)
+ [Troubleshooting VPC networking](vpc-troubleshooting-guide.md)
+ [Best practices](#vpc-best-practices)
+ [VPC networking quotas](#vpc-quotas)

## Networking modes
<a name="vpc-networking-modes"></a>

HealthOmics Workflows supports two networking modes. By default, workflow runs operate in RESTRICTED mode. You can enable VPC networking on a per-run basis when you start the workflow run.

**RESTRICTED (default)**  
Runs can only access Amazon S3 and Amazon ECR resources within the same AWS Region. Runs cannot access other AWS services, resources across AWS Regions, or the public internet.

**VPC**  
Run traffic is routed through elastic network interfaces (ENIs) provisioned by HealthOmics in your VPC subnets. You control network routing, security groups, network ACLs, and internet access through NAT gateways. This mode enables access to:  
+ Public internet resources (requires NAT Gateway configuration)
+ AWS services in other Regions
+ Private resources in your VPC
+ Access on-premises resources in your private network

You specify the networking mode when you start a workflow run using the `networkingMode` parameter in the `StartRun` API.

## Getting started
<a name="vpc-getting-started"></a>

This section guides you through setting up VPC networking for HealthOmics Workflows for the first time.

### Prerequisites
<a name="vpc-networking-prerequisites"></a>

Before configuring VPC networking for HealthOmics Workflows, ensure that you have the following:
+ An existing VPC with appropriate subnets and security groups. The VPC must be in the same Region as your workflows.
+ At least one subnet in an Availability Zone where HealthOmics operates in your Region.
+ Appropriate IAM permissions to create and manage HealthOmics configurations.
+ Understanding of VPC networking concepts (subnets, security groups, route tables).
+ Sufficient ENI capacity in your AWS account. HealthOmics scales and manages ENIs in your VPC using the service-linked role. The number of ENIs required depends on your workload. Monitor your ENI usage in the Amazon EC2 console to ensure you have sufficient capacity.

**Important**  
Your VPC configuration must include at least one subnet in an Availability Zone where HealthOmics operates in your Region to support workflow task placement. When using VPC networking mode, you are responsible for determining whether it is safe and compliant to transfer or use data across AWS Regions.

### Step 1: Create or configure your VPC
<a name="vpc-step-create-vpc"></a>

Create a VPC with private subnets, security groups, and NAT gateways (if internet access is needed). For detailed step-by-step instructions, see [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

### Step 2: Configure security groups
<a name="vpc-step-security-groups"></a>

Create a security group that allows outbound traffic to the destinations your runs need to access. Configure security groups to allow only the minimum required outbound traffic following the principle of least privilege.

For example configurations and detailed guidance, see the security group section in [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

### Step 3: Verify route tables
<a name="vpc-step-route-tables"></a>

Ensure your private subnets have routes to a NAT Gateway for internet access. For example route table configurations, see the route table section in [Internet access for VPC-connected workflows](workflows-vpc-internet.md).

**Note**  
Connecting a run to a public subnet does not give it internet access or a public IP address. Always use private subnets with NAT Gateway routes for runs requiring internet connectivity.

### Step 4: Create a configuration resource
<a name="vpc-step-create-configuration"></a>

Create a HealthOmics Configuration resource that defines your VPC networking settings:

```
aws omics create-configuration \
  --name {{my-vpc-config}} \
  --description "VPC configuration for genomics workflows" \
  --run-configurations '{
    "vpcConfig": {
      "securityGroupIds": ["{{sg-0123456789abcdef0}}"],
      "subnetIds": [
        "{{subnet-0a1b2c3d4e5f6g7h8}}",
        "{{subnet-1a2b3c4d5e6f7g8h9}}"
      ]
    }
  }' \
  --region {{us-west-2}}
```

The configuration will transition from `CREATING` to `ACTIVE` status once network resources are provisioned. This takes up to 15 minutes.

### Step 5: Start a workflow run with VPC networking
<a name="vpc-step-start-run"></a>

Once your configuration is `ACTIVE`, start a workflow run with VPC networking enabled:

```
aws omics start-run \
  --workflow-id {{1234567}} \
  --role-arn arn:aws:iam::{{123456789012}}:role/{{OmicsWorkflowRole}} \
  --output-uri s3://{{my-bucket}}/outputs/ \
  --networking-mode VPC \
  --configuration-name {{my-vpc-config}} \
  --region {{us-west-2}}
```

### Step 6: Verify connectivity
<a name="vpc-step-verify"></a>

Monitor your workflow run to verify it can access the required external resources. Check the workflow logs in CloudWatch Logs for connection success or failure messages. For detailed guidance on testing connectivity, see [Testing VPC connectivity](workflows-vpc-internet.md#vpc-testing-connectivity).

## VPC requirements
<a name="vpc-requirements"></a>

Your VPC must meet the following requirements:

### Subnet requirements
<a name="vpc-subnet-requirements"></a>
+ **Minimum:** At least one subnet in an Availability Zone where HealthOmics operates
+ **Maximum:** 16 subnets per configuration
+ **Restriction:** Maximum of one subnet per Availability Zone
+ **Recommendation:** Use private subnets with NAT Gateway routes for runs requiring internet access. While you can specify a single subnet, we recommend using multiple subnets across different Availability Zones for better availability.

### Security group requirements
<a name="vpc-security-group-requirements"></a>
+ **Minimum:** 1 security group
+ **Maximum:** 5 security groups per configuration
+ **Requirement:** All security groups must belong to the same VPC as the subnets

Security groups control inbound and outbound traffic for your runs.

**Note**  
All subnets and security groups must belong to the same VPC.

### Network interface requirements
<a name="vpc-eni-requirements"></a>

HealthOmics provisions elastic network interfaces (ENIs) in your VPC to connect runs to your network. Ensure your AWS account has sufficient ENI capacity (default limit: 5,000 ENIs per Region).

ENIs created by HealthOmics are tagged with the following tags:

```
"TagSet": [
  {
    "Key": "Service",
    "Value": "HealthOmics"
  },
  {
    "Key": "eniType",
    "Value": "CUSTOMER"
  }
]
```

**Important**  
Do not modify or delete ENIs created by HealthOmics. Modifying these network interfaces can cause service delays or disruptions to your workflow runs.

## Configuration APIs
<a name="vpc-configuration-apis"></a>

HealthOmics provides APIs to create, manage, and delete VPC configurations. You can reuse configurations across multiple workflow runs.

**Topics**
+ [CreateConfiguration](#vpc-create-configuration)
+ [GetConfiguration](#vpc-get-configuration)
+ [ListConfigurations](#vpc-list-configurations)
+ [DeleteConfiguration](#vpc-delete-configuration)

### CreateConfiguration
<a name="vpc-create-configuration"></a>

Creates a new configuration resource with VPC networking settings. For a step-by-step example, see [Step 4: Create a configuration resource](#vpc-step-create-configuration).

**Request syntax:**

```
aws omics create-configuration \
  --name {{configuration-name}} \
  --description {{description}} \
  --run-configurations '{"vpcConfig":{"securityGroupIds":["{{security-group-id}}"],"subnetIds":["{{subnet-id}}"]}}' \
  --tags Key={{key}},Value={{value}} \
  --region {{region}}
```

**Parameters:**
+ **name** (required) — A unique name for the configuration (maximum 50 characters).
+ **description** (optional) — A description of the configuration.
+ **run-configurations** (optional) — VPC configuration settings:
  + `vpcConfig.securityGroupIds` — A list of 1–5 security group IDs.
  + `vpcConfig.subnetIds` — A list of 1–16 subnet IDs.
+ **tags** (optional) — Resource tags.

**Response:**

```
{
  "arn": "arn:aws:omics:{{region}}:{{account-id}}:configuration/{{configuration-name}}",
  "uuid": "{{configuration-uuid}}",
  "name": "{{configuration-name}}",
  "runConfigurations": {
    "vpcConfig": {
      "securityGroupIds": ["{{security-group-id}}"],
      "subnetIds": ["{{subnet-id}}"],
      "vpcId": "{{vpc-id}}"
    }
  },
  "status": "CREATING",
  "creationTime": "{{timestamp}}",
  "tags": {}
}
```

**Configuration status values:**
+ **CREATING** — The configuration is being created and network resources are being provisioned (up to 15 minutes).
+ **ACTIVE** — The configuration is ready to use.
+ **DELETING** — The configuration is being deleted.
+ **DELETED** — The configuration has been deleted.

### GetConfiguration
<a name="vpc-get-configuration"></a>

Retrieves details of a specific configuration.

**Request syntax:**

```
aws omics get-configuration \
  --name {{configuration-name}} \
  --region {{region}}
```

**Response:**

```
{
  "arn": "arn:aws:omics:{{region}}:{{account-id}}:configuration/{{configuration-name}}",
  "uuid": "{{configuration-uuid}}",
  "name": "{{configuration-name}}",
  "runConfigurations": {
    "vpcConfig": {
      "securityGroupIds": ["{{security-group-id}}"],
      "subnetIds": ["{{subnet-id}}"],
      "vpcId": "{{vpc-id}}"
    }
  },
  "status": "ACTIVE",
  "creationTime": "{{timestamp}}",
  "tags": {}
}
```

### ListConfigurations
<a name="vpc-list-configurations"></a>

Lists all configurations in your account.

**Request syntax:**

```
aws omics list-configurations \
  --region {{region}}
```

**Response:**

```
{
  "items": [
    {
      "arn": "arn:aws:omics:{{region}}:{{account-id}}:configuration/{{configuration-name}}",
      "name": "{{configuration-name}}",
      "description": "{{description}}",
      "status": "ACTIVE",
      "creationTime": "{{timestamp}}"
    }
  ]
}
```

### DeleteConfiguration
<a name="vpc-delete-configuration"></a>

Deletes a configuration. You cannot delete a configuration that is currently in use by active workflow runs.

**Request syntax:**

```
aws omics delete-configuration \
  --name {{configuration-name}} \
  --region {{region}}
```

**Note**  
The configuration status changes to DELETING while network resources are being cleaned up, and then to DELETED once the process is complete.

## Running workflows with VPC networking
<a name="vpc-running-workflows"></a>

### Starting a run with VPC networking
<a name="vpc-start-run"></a>

To use VPC networking in a workflow run, specify the `networking-mode` parameter and the `configuration-name`:

```
aws omics start-run \
  --workflow-id {{1234567}} \
  --role-arn arn:aws:iam::{{123456789012}}:role/{{OmicsWorkflowRole}} \
  --output-uri s3://{{my-bucket}}/outputs/ \
  --networking-mode VPC \
  --configuration-name {{my-vpc-config}} \
  --region {{us-west-2}}
```

**Parameters:**
+ **networking-mode** — Set to `VPC` to enable VPC networking. The default is `RESTRICTED`.
+ **configuration-name** (required) — The name of the configuration to use.

### Viewing run network configuration
<a name="vpc-get-run"></a>

Use `GetRun` to view the networking configuration for a run:

```
aws omics get-run \
  --id {{run-id}} \
  --region {{region}}
```

The response includes the networking mode, configuration details, and VPC configuration. The following example shows the VPC-related fields from the response:

```
{
  "arn": "arn:aws:omics:{{region}}:{{account-id}}:run/{{run-id}}",
  "id": "{{run-id}}",
  "status": "{{status}}",
  "workflowId": "{{workflow-id}}",
  "networkingMode": "VPC",
  "configuration": {
    "name": "{{configuration-name}}",
    "arn": "arn:aws:omics:{{region}}:{{account-id}}:configuration/{{configuration-name}}",
    "uuid": "{{configuration-uuid}}"
  },
  "vpcConfig": {
    "subnets": ["{{subnet-id-1}}", "{{subnet-id-2}}"],
    "securityGroupIds": ["{{security-group-id}}"],
    "vpcId": "{{vpc-id}}"
  }
}
```

### Configuration immutability
<a name="vpc-config-immutability"></a>

Configuration resources are immutable—after you create a configuration, you cannot change its settings. To use different networking settings, create a new configuration. You cannot delete a configuration while it is in use by active workflow runs—the `DeleteConfiguration` request is rejected until those runs reach a terminal state.

### Call caching considerations
<a name="vpc-call-caching"></a>

When using VPC networking with call caching, ensure your workflow engine is configured appropriately. For detailed guidance on call caching per engine, see [Engine-specific caching features](workflow-cache-per-engine.md).

**Important**  
When connecting to non-deterministic or dynamic resources (for example, third-party databases on the public internet), consider using the cache task opt-out feature in your workflows to avoid caching dynamic datasets that could impact run outputs.

## Best practices
<a name="vpc-best-practices"></a>

### Security
<a name="vpc-bp-security"></a>

1. **Use least-privilege security groups.** Allow only the minimum required outbound traffic. Use specific destination CIDR blocks instead of 0.0.0.0/0 when possible. Document the purpose of each security group rule.

1. **Separate configurations by environment.** Create separate configurations for development, staging, and production. Use different VPCs or subnets for each environment. Apply appropriate tags to configurations for organization.

1. **Implement network monitoring.** Enable VPC Flow Logs for security analysis. Set up CloudWatch alarms for unusual traffic patterns. Regularly review CloudTrail logs for configuration changes.

1. **Use VPC endpoints for AWS services.** Configure VPC endpoints for Amazon S3, Amazon ECR, and other AWS services. This reduces NAT Gateway costs, improves performance, and provides additional security by keeping traffic within the AWS network.

### Performance
<a name="vpc-bp-performance"></a>

1. **Plan for network scaling.** Network throughput starts at 10 Gbps and scales to 100 Gbps over time. For immediate high-throughput needs, plan ahead and request pre-warming. Monitor network metrics to understand your workflow requirements.

1. **Deploy NAT Gateways per Availability Zone.** Use one NAT Gateway per AZ for production workloads. This improves resiliency and throughput, and reduces cross-AZ data transfer costs.

1. **Reuse configurations.** Create configurations that can be shared across multiple workflows. This reduces configuration management overhead and ensures consistent network settings.

1. **Test configurations before production use.** Validate network connectivity with test workflows. Verify security group rules allow required traffic. Test failover scenarios with multi-AZ configurations.

### Cost optimization
<a name="vpc-bp-cost"></a>

1. **Use VPC endpoints instead of NAT Gateway.** For AWS service access, use VPC endpoints (no data processing charges). Amazon S3 Gateway endpoints have no additional costs. Interface endpoints have hourly charges but can be more cost-effective than NAT Gateway.

1. **Monitor data transfer costs.** Data transfer in has no charge. Data transfer out to internet incurs standard AWS data transfer rates. Cross-Region data transfer has higher rates. Use AWS Cost Explorer to track VPC-related costs.

1. **Right-size NAT Gateway deployment.** For development, use one NAT Gateway for all AZs. For production, use one NAT Gateway per AZ for resiliency. Monitor NAT Gateway utilization to avoid over-provisioning.

1. **Delete unused configurations.** Regularly review and delete configurations no longer in use. Use tags to identify configuration ownership and purpose.

### Operational
<a name="vpc-bp-operational"></a>

1. **Use descriptive configuration names.** Include environment, purpose, and team in the name (for example, `prod-genomics-vpc`, `dev-clinical-trials-vpc`).

1. **Tag all configurations.** Use consistent tagging strategy across all resources. Include tags for Environment, Owner, CostCenter, and Purpose.

1. **Document network requirements.** Document which external services each configuration accesses. Maintain a map of security group rules and their purposes. Share network architecture diagrams with your team.

## VPC networking quotas
<a name="vpc-quotas"></a>

The following table lists the quotas for VPC networking configurations:


| Resource | Default limit | Adjustable | 
| --- | --- | --- | 
| Maximum configurations per account | 10 | Yes | 
| Maximum security groups per configuration | 5 | No | 
| Maximum subnets per configuration | 16 | No | 
| Maximum subnets per Availability Zone | 1 | No | 
| CreateConfiguration API TPS | 1 | Yes | 
| Elastic network interfaces per Region (customer VPC) | 5,000 | Yes | 

To request a quota increase, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home), choose **AWS services**, search for **AWS HealthOmics**, select the quota you want to increase, and choose **Request quota increase**. Quota increase requests are typically processed within 1-2 business days.