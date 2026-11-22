

# How Infrastructure Performance works with IAM

The following sections describe how Infrastructure Performance works with IAM.

**Topics**
+ [Infrastructure Performance identity-based policies](#CloudWatch-InfrastructurePerformance-IAM-Identity-Based)
+ [Infrastructure Performance IAM roles](#CloudWatch-InfrastructurePerformance-IAM-Roles)

## Infrastructure Performance identity-based policies
<a name="CloudWatch-InfrastructurePerformance-IAM-Identity-Based"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources and the conditions under which actions are allowed or denied. Infrastructure Performance supports specific actions and resources.

### Actions
<a name="CloudWatch-InfrastructurePerformance-IAM-Actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. Infrastructure Performance shares its API namespace with Amazon EC2. Policy actions use the prefix: `ec2:`

Example: `ec2:GetAwsNetworkPerformanceData`

To specify multiple actions in a single statement, separate them with commas:

```json
"Action": ["ec2:action1", "ec2:action2"]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action. This grants all Amazon EC2 Describe actions, not only Infrastructure Performance actions.

```json
"Action": "ec2:Describe*"
```

The following are the supported Infrastructure Performance actions:
+ `ec2:DescribeAwsNetworkPerformanceMetricSubscriptions`
+ `ec2:DisableAwsNetworkPerformanceMetricSubscription`
+ `ec2:EnableAwsNetworkPerformanceMetricSubscription`
+ `ec2:GetAwsNetworkPerformanceData`

### Resources
<a name="CloudWatch-InfrastructurePerformance-IAM-Resources"></a>

Infrastructure Performance doesn't support resource-level permissions. You must use the following wildcard resource:

```json
"Resource": "*"
```

### Condition keys
<a name="CloudWatch-InfrastructurePerformance-IAM-Condition-Keys"></a>

Infrastructure Performance doesn't provide any service-specific condition keys but supports some global condition keys. All Amazon EC2 actions support the `aws:RequestedRegion` and `ec2:Region` condition keys.

The Condition element is optional.

## Infrastructure Performance IAM roles
<a name="CloudWatch-InfrastructurePerformance-IAM-Roles"></a>

An IAM role is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Infrastructure Performance
<a name="CloudWatch-InfrastructurePerformance-IAM-Temp-Credentials"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or assume a cross-account role. Infrastructure Performance supports using temporary credentials.

### Service-linked roles
<a name="CloudWatch-InfrastructurePerformance-IAM-Service-Linked-Roles"></a>

Infrastructure Performance doesn't use a service-linked role. Performance monitors use the Network Flow Monitor service-linked role. For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md).

### Service roles
<a name="CloudWatch-InfrastructurePerformance-IAM-Service-Roles"></a>

Infrastructure Performance has no service roles.