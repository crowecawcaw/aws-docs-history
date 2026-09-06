

# Actions, resources, and condition keys for AWS Elastic Load Balancing
<a name="list_elb"></a>

AWS Elastic Load Balancing (service prefix: `elasticloadbalancing`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticloadbalancing/elasticloadbalancing.json) for this service.

**Topics**
+ [API operations defined by AWS Elastic Load Balancing](#list_elb-operations)
+ [Actions defined by AWS Elastic Load Balancing](#list_elb-actions-as-permissions)
+ [Resource types defined by AWS Elastic Load Balancing](#list_elb-resources-for-iam-policies)
+ [Condition keys for AWS Elastic Load Balancing](#list_elb-policy-keys)

## API operations defined by AWS Elastic Load Balancing
<a name="list_elb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_elb-actions-as-permissions).




- **   AddTags  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elb-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ApplySecurityGroupsToLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:ApplySecurityGroupsToLoadBalancer](#list_elb-action-ApplySecurityGroupsToLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachLoadBalancerToSubnets  **
  - **IAM action:**  [elasticloadbalancing:AttachLoadBalancerToSubnets](#list_elb-action-AttachLoadBalancerToSubnets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfigureHealthCheck  **
  - **IAM action:**  [elasticloadbalancing:ConfigureHealthCheck](#list_elb-action-ConfigureHealthCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAppCookieStickinessPolicy  **
  - **IAM action:**  [elasticloadbalancing:CreateAppCookieStickinessPolicy](#list_elb-action-CreateAppCookieStickinessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLBCookieStickinessPolicy  **
  - **IAM action:**  [elasticloadbalancing:CreateLBCookieStickinessPolicy](#list_elb-action-CreateLBCookieStickinessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elb-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateLoadBalancer](#list_elb-action-CreateLoadBalancer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateLoadBalancerListeners  **
  - **IAM action:**  [elasticloadbalancing:CreateLoadBalancerListeners](#list_elb-action-CreateLoadBalancerListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLoadBalancerPolicy  **
  - **IAM action:**  [elasticloadbalancing:CreateLoadBalancerPolicy](#list_elb-action-CreateLoadBalancerPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:DeleteLoadBalancer](#list_elb-action-DeleteLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoadBalancerListeners  **
  - **IAM action:**  [elasticloadbalancing:DeleteLoadBalancerListeners](#list_elb-action-DeleteLoadBalancerListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoadBalancerPolicy  **
  - **IAM action:**  [elasticloadbalancing:DeleteLoadBalancerPolicy](#list_elb-action-DeleteLoadBalancerPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterInstancesFromLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:DeregisterInstancesFromLoadBalancer](#list_elb-action-DeregisterInstancesFromLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountLimits  **
  - **IAM action:**  [elasticloadbalancing:DescribeAccountLimits](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeAccountLimits.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceHealth  **
  - **IAM action:**  [elasticloadbalancing:DescribeInstanceHealth](#list_elb-action-DescribeInstanceHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancerAttributes  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancerAttributes](#list_elb-action-DescribeLoadBalancerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancerPolicies  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancerPolicies](#list_elb-action-DescribeLoadBalancerPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancerPolicyTypes  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancerPolicyTypes](#list_elb-action-DescribeLoadBalancerPolicyTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancers  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancers](#list_elb-action-DescribeLoadBalancers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTags  **
  - **IAM action:**  [elasticloadbalancing:DescribeTags](#list_elb-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachLoadBalancerFromSubnets  **
  - **IAM action:**  [elasticloadbalancing:DetachLoadBalancerFromSubnets](#list_elb-action-DetachLoadBalancerFromSubnets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableAvailabilityZonesForLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:DisableAvailabilityZonesForLoadBalancer](#list_elb-action-DisableAvailabilityZonesForLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableAvailabilityZonesForLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:EnableAvailabilityZonesForLoadBalancer](#list_elb-action-EnableAvailabilityZonesForLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyLoadBalancerAttributes  **
  - **IAM action:**  [elasticloadbalancing:ModifyLoadBalancerAttributes](#list_elb-action-ModifyLoadBalancerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterInstancesWithLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:RegisterInstancesWithLoadBalancer](#list_elb-action-RegisterInstancesWithLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [elasticloadbalancing:RemoveTags](#list_elb-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   SetLoadBalancerListenerSSLCertificate  **
  - **IAM action:**  [elasticloadbalancing:SetLoadBalancerListenerSSLCertificate](#list_elb-action-SetLoadBalancerListenerSSLCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetLoadBalancerPoliciesForBackendServer  **
  - **IAM action:**  [elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer](#list_elb-action-SetLoadBalancerPoliciesForBackendServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetLoadBalancerPoliciesOfListener  **
  - **IAM action:**  [elasticloadbalancing:SetLoadBalancerPoliciesOfListener](#list_elb-action-SetLoadBalancerPoliciesOfListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elastic Load Balancing
<a name="list_elb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elb-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elb-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [ApplySecurityGroupsToLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ApplySecurityGroupsToLoadBalancer.html)  **
  - **Description:** Grants permission to associate one or more security groups with your load balancer in a virtual private cloud (VPC)
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityGroup](#list_elb-elasticloadbalancing_SecurityGroup)
  - **Access level:** Write

- **   [AttachLoadBalancerToSubnets](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AttachLoadBalancerToSubnets.html)  **
  - **Description:** Grants permission to add one or more subnets to the set of configured subnets for the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Subnet](#list_elb-elasticloadbalancing_Subnet)
  - **Access level:** Write

- **   [ConfigureHealthCheck](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConfigureHealthCheck.html)  **
  - **Description:** Grants permission to specify the health check settings to use when evaluating the health state of your back-end instances
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateAppCookieStickinessPolicy.html)  **
  - **Description:** Grants permission to generate a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLBCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLBCookieStickinessPolicy.html)  **
  - **Description:** Grants permission to generate a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancer.html)  **
  - **Description:** Grants permission to create a load balancer
  - **Resource types (\*required):** [loadbalancer](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elb-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elb-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Scheme](#list_elb-elasticloadbalancing_Scheme)<br />[elasticloadbalancing:SecurityGroup](#list_elb-elasticloadbalancing_SecurityGroup)<br />[elasticloadbalancing:Subnet](#list_elb-elasticloadbalancing_Subnet)
  - **Access level:** Write

- **   [CreateLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerListeners.html)  **
  - **Description:** Grants permission to create one or more listeners for the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ListenerProtocol](#list_elb-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerPolicy.html)  **
  - **Description:** Grants permission to create a policy with the specified attributes for the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elb-elasticloadbalancing_SecurityPolicy)
  - **Access level:** Write

- **   [DeleteLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancer.html)  **
  - **Description:** Grants permission to delete the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerListeners.html)  **
  - **Description:** Grants permission to delete the specified listeners from the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerPolicy.html)  **
  - **Description:** Grants permission to delete the specified policy from the specified load balancer. This policy must not be enabled for any listeners
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterInstancesFromLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeregisterInstancesFromLoadBalancer.html)  **
  - **Description:** Grants permission to deregister the specified instances from the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeInstanceHealth](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeInstanceHealth.html)  **
  - **Description:** Grants permission to describe the state of the specified instances with respect to the specified load balancer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerAttributes.html)  **
  - **Description:** Grants permission to describe the attributes for the specified load balancer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancerPolicies](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicies.html)  **
  - **Description:** Grants permission to describe the specified policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancerPolicyTypes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicyTypes.html)  **
  - **Description:** Grants permission to describe the specified load balancer policy types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html)  **
  - **Description:** Grants permission to describe the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe the tags associated with the specified load balancers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetachLoadBalancerFromSubnets](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DetachLoadBalancerFromSubnets.html)  **
  - **Description:** Grants permission to remove the specified subnets from the set of configured subnets for the load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DisableAvailabilityZonesForLoadBalancer.html)  **
  - **Description:** Grants permission to remove the specified Availability Zones from the set of Availability Zones for the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_EnableAvailabilityZonesForLoadBalancer.html)  **
  - **Description:** Grants permission to add the specified Availability Zones to the set of Availability Zones for the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html)  **
  - **Description:** Grants permission to modify the attributes of the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterInstancesWithLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RegisterInstancesWithLoadBalancer.html)  **
  - **Description:** Grants permission to add the specified instances to the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified load balancer
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elb-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [SetLoadBalancerListenerSSLCertificate](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerListenerSSLCertificate.html)  **
  - **Description:** Grants permission to set the certificate that terminates the specified listener's SSL connections
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetLoadBalancerPoliciesForBackendServer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesForBackendServer.html)  **
  - **Description:** Grants permission to replace the set of policies associated with the specified port on which the back-end server is listening with a new set of policies
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_SetLoadBalancerPoliciesOfListener.html)  **
  - **Description:** Grants permission to replace the current set of policies for the specified load balancer port with the specified set of policies
  - **Resource types (\*required):** [loadbalancer\*](#list_elb-resource-loadbalancer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elb-elasticloadbalancing_SecurityPolicy)
  - **Access level:** Write



## Resource types defined by AWS Elastic Load Balancing
<a name="list_elb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [loadbalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/${LoadBalancerName} | [aws:ResourceTag/${TagKey}](#list_elb-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elb-elasticloadbalancing_ResourceTag___TagKey_) | 

## Condition keys for AWS Elastic Load Balancing
<a name="list_elb-policy-keys"></a>

AWS Elastic Load Balancing defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:CreateAction](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/tagging-resources-during-creation.html)  | Filters access by the name of a resource-creating API action | String | 
|   [elasticloadbalancing:ListenerProtocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#listenerprotocol-condition)  | Filters access by the listener protocols that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:ResourceTag/](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the preface string for a tag key and value pair that are attached to a resource | String | 
|   [elasticloadbalancing:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the preface string for a tag key and value pair that are attached to a resource | String | 
|   [elasticloadbalancing:Scheme](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#scheme-condition)  | Filters access by the load balancer scheme that are allowed in the request | String | 
|   [elasticloadbalancing:SecurityGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#securitygroup-condition)  | Filters access by the security-group IDs that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:SecurityPolicy](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#securitypolicy-condition)  | Filters access by the SSL Security Policies that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:Subnet](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#subnet-condition)  | Filters access by the subnet IDs that are allowed in the request | ArrayOfString | 