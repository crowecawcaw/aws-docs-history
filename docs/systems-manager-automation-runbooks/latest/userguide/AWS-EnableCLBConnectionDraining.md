# `AWS-EnableCLBConnectionDraining`

**Description**

The `AWS-EnableCLBConnectionDraining` runbook enables connection
draining on a Classic Load Balancer (CLB) to the specified timeout value. Connection drainings
enables the CLB to complete in-flight requests made to instances that are
deregistering or unhealthy with the specified timeout being the time it keeps
connections alive before reporting the instance as deregistered. For more
information about connection draining on CLBs, see [Configure connection draining for your
Classic Load Balancer](url-elb-cg.md "url-elb-cg.md") in the _User Guide for Classic Load Balancers_.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCLBConnectionDraining "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCLBConnectionDraining")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- LoadBalancerName

Type: String

Description: (Required) The name of the load balancer you want to enable
connection draining on.

- ConnectionTimeout

Type: Integer

Valid values: 1-3600

Default: 300

Description: (Required) The connection timeout value for the load
balancer. The timeout value can be set between 1 and 3600 seconds.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `elasticloadbalancing:DescribeLoadBalancerAttributes`
- `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

- ModifyLoadBalancerConnectionDraining (aws:executeAwsApi): Enables
  connection draining and sets the specified timeout value for the load
  balancer you specify.
- VerifyLoadBalancerConnectionDrainingEnabled
  (aws:assertAwsResourceProperty): Verifies that connection draining is
  enabled for the load balancer.
- VerifyLoadBalancerConnectionDrainingTimeout
  (aws:assertAwsResourceProperty): Verifies that the connection timeout value
  for the load balancer matches the value you specified.
