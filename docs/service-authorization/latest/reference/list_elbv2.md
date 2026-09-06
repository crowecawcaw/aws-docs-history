

# Actions, resources, and condition keys for AWS Elastic Load Balancing V2
<a name="list_elbv2"></a>

AWS Elastic Load Balancing V2 (service prefix: `elasticloadbalancing`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticloadbalancing/elasticloadbalancing.json) for this service.

**Topics**
+ [API operations defined by AWS Elastic Load Balancing V2](#list_elbv2-operations)
+ [Actions defined by AWS Elastic Load Balancing V2](#list_elbv2-actions-as-permissions)
+ [Permission-only actions for AWS Elastic Load Balancing V2](#list_elbv2-permission-only-actions)
+ [Resource types defined by AWS Elastic Load Balancing V2](#list_elbv2-resources-for-iam-policies)
+ [Condition keys for AWS Elastic Load Balancing V2](#list_elbv2-policy-keys)

## API operations defined by AWS Elastic Load Balancing V2
<a name="list_elbv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_elbv2-actions-as-permissions).




- **   AddListenerCertificates  **
  - **IAM action:**  [elasticloadbalancing:AddListenerCertificates](#list_elbv2-action-AddListenerCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTags  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AddTrustStoreRevocations  **
  - **IAM action:**  [elasticloadbalancing:AddTrustStoreRevocations](#list_elbv2-action-AddTrustStoreRevocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateListener  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateListener](#list_elbv2-action-CreateListener)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateLoadBalancer](#list_elbv2-action-CreateLoadBalancer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateRule  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateRule](#list_elbv2-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTargetGroup  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateTargetGroup](#list_elbv2-action-CreateTargetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTrustStore  **
  - **IAM action:**  [elasticloadbalancing:AddTags](#list_elbv2-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticloadbalancing:CreateTrustStore](#list_elbv2-action-CreateTrustStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteListener  **
  - **IAM action:**  [elasticloadbalancing:DeleteListener](#list_elbv2-action-DeleteListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoadBalancer  **
  - **IAM action:**  [elasticloadbalancing:DeleteLoadBalancer](#list_elbv2-action-DeleteLoadBalancer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [elasticloadbalancing:DeleteRule](#list_elbv2-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSharedTrustStoreAssociation  **
  - **IAM action:**  [elasticloadbalancing:DeleteSharedTrustStoreAssociation](#list_elbv2-action-DeleteSharedTrustStoreAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTargetGroup  **
  - **IAM action:**  [elasticloadbalancing:DeleteTargetGroup](#list_elbv2-action-DeleteTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrustStore  **
  - **IAM action:**  [elasticloadbalancing:DeleteTrustStore](#list_elbv2-action-DeleteTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTargets  **
  - **IAM action:**  [elasticloadbalancing:DeregisterTargets](#list_elbv2-action-DeregisterTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountLimits  **
  - **IAM action:**  [elasticloadbalancing:DescribeAccountLimits](#list_elbv2-action-DescribeAccountLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCapacityReservation  **
  - **IAM action:**  [elasticloadbalancing:DescribeCapacityReservation](#list_elbv2-action-DescribeCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeListenerAttributes  **
  - **IAM action:**  [elasticloadbalancing:DescribeListenerAttributes](#list_elbv2-action-DescribeListenerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeListenerCertificates  **
  - **IAM action:**  [elasticloadbalancing:DescribeListenerCertificates](#list_elbv2-action-DescribeListenerCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeListeners  **
  - **IAM action:**  [elasticloadbalancing:DescribeListeners](#list_elbv2-action-DescribeListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancerAttributes  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancerAttributes](#list_elbv2-action-DescribeLoadBalancerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoadBalancers  **
  - **IAM action:**  [elasticloadbalancing:DescribeLoadBalancers](#list_elbv2-action-DescribeLoadBalancers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeRules  **
  - **IAM action:**  [elasticloadbalancing:DescribeRules](#list_elbv2-action-DescribeRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSSLPolicies  **
  - **IAM action:**  [elasticloadbalancing:DescribeSSLPolicies](#list_elbv2-action-DescribeSSLPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTags  **
  - **IAM action:**  [elasticloadbalancing:DescribeTags](#list_elbv2-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTargetGroupAttributes  **
  - **IAM action:**  [elasticloadbalancing:DescribeTargetGroupAttributes](#list_elbv2-action-DescribeTargetGroupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTargetGroups  **
  - **IAM action:**  [elasticloadbalancing:DescribeTargetGroups](#list_elbv2-action-DescribeTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTargetHealth  **
  - **IAM action:**  [elasticloadbalancing:DescribeTargetHealth](#list_elbv2-action-DescribeTargetHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustStoreAssociations  **
  - **IAM action:**  [elasticloadbalancing:DescribeTrustStoreAssociations](#list_elbv2-action-DescribeTrustStoreAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustStoreRevocations  **
  - **IAM action:**  [elasticloadbalancing:DescribeTrustStoreRevocations](#list_elbv2-action-DescribeTrustStoreRevocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrustStores  **
  - **IAM action:**  [elasticloadbalancing:DescribeTrustStores](#list_elbv2-action-DescribeTrustStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [elasticloadbalancing:GetResourcePolicy](#list_elbv2-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrustStoreCaCertificatesBundle  **
  - **IAM action:**  [elasticloadbalancing:GetTrustStoreCaCertificatesBundle](#list_elbv2-action-GetTrustStoreCaCertificatesBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrustStoreRevocationContent  **
  - **IAM action:**  [elasticloadbalancing:GetTrustStoreRevocationContent](#list_elbv2-action-GetTrustStoreRevocationContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyCapacityReservation  **
  - **IAM action:**  [elasticloadbalancing:ModifyCapacityReservation](#list_elbv2-action-ModifyCapacityReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyIpPools  **
  - **IAM action:**  [elasticloadbalancing:ModifyIpPools](#list_elbv2-action-ModifyIpPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyListener  **
  - **IAM action:**  [elasticloadbalancing:ModifyListener](#list_elbv2-action-ModifyListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyListenerAttributes  **
  - **IAM action:**  [elasticloadbalancing:ModifyListenerAttributes](#list_elbv2-action-ModifyListenerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyLoadBalancerAttributes  **
  - **IAM action:**  [elasticloadbalancing:ModifyLoadBalancerAttributes](#list_elbv2-action-ModifyLoadBalancerAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyRule  **
  - **IAM action:**  [elasticloadbalancing:ModifyRule](#list_elbv2-action-ModifyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyTargetGroup  **
  - **IAM action:**  [elasticloadbalancing:ModifyTargetGroup](#list_elbv2-action-ModifyTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyTargetGroupAttributes  **
  - **IAM action:**  [elasticloadbalancing:ModifyTargetGroupAttributes](#list_elbv2-action-ModifyTargetGroupAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyTrustStore  **
  - **IAM action:**  [elasticloadbalancing:ModifyTrustStore](#list_elbv2-action-ModifyTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterTargets  **
  - **IAM action:**  [elasticloadbalancing:RegisterTargets](#list_elbv2-action-RegisterTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveListenerCertificates  **
  - **IAM action:**  [elasticloadbalancing:RemoveListenerCertificates](#list_elbv2-action-RemoveListenerCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [elasticloadbalancing:RemoveTags](#list_elbv2-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RemoveTrustStoreRevocations  **
  - **IAM action:**  [elasticloadbalancing:RemoveTrustStoreRevocations](#list_elbv2-action-RemoveTrustStoreRevocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetIpAddressType  **
  - **IAM action:**  [elasticloadbalancing:SetIpAddressType](#list_elbv2-action-SetIpAddressType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetRulePriorities  **
  - **IAM action:**  [elasticloadbalancing:SetRulePriorities](#list_elbv2-action-SetRulePriorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetSecurityGroups  **
  - **IAM action:**  [elasticloadbalancing:SetSecurityGroups](#list_elbv2-action-SetSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetSubnets  **
  - **IAM action:**  [elasticloadbalancing:SetSubnets](#list_elbv2-action-SetSubnets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elastic Load Balancing V2
<a name="list_elbv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddListenerCertificates.html)  **
  - **Description:** Grants permission to add the specified certificates to the specified secure listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags
  - **Resource types (\*required):** [listener-rule/app](#list_elbv2-resource-listener-rule_app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener-rule/net](#list_elbv2-resource-listener-rule_net) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/app](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/gwy](#list_elbv2-resource-listener_gwy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [targetgroup](#list_elbv2-resource-targetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [truststore](#list_elbv2-resource-truststore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:CreateAction](#list_elbv2-elasticloadbalancing_CreateAction)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [AddTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTrustStoreRevocations.html)  **
  - **Description:** Grants permission to add revocations to a trust store
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html)  **
  - **Description:** Grants permission to create a listener for the specified Application Load Balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Access level:** Write

- **   [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateLoadBalancer.html)  **
  - **Description:** Grants permission to create a load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Scheme](#list_elbv2-elasticloadbalancing_Scheme)<br />[elasticloadbalancing:SecurityGroup](#list_elbv2-elasticloadbalancing_SecurityGroup)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Scheme](#list_elbv2-elasticloadbalancing_Scheme)<br />[elasticloadbalancing:SecurityGroup](#list_elbv2-elasticloadbalancing_SecurityGroup)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Scheme](#list_elbv2-elasticloadbalancing_Scheme)<br />[elasticloadbalancing:SecurityGroup](#list_elbv2-elasticloadbalancing_SecurityGroup)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Access level:** Write

- **   [CreateRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateRule.html)  **
  - **Description:** Grants permission to create a rule for the specified listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTargetGroup.html)  **
  - **Description:** Grants permission to create a target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTrustStore.html)  **
  - **Description:** Grants permission to create a trust store
  - **Resource types (\*required):** [truststore](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteListener.html)  **
  - **Description:** Grants permission to delete the specified listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/gwy\*](#list_elbv2-resource-listener_gwy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteLoadBalancer.html)  **
  - **Description:** Grants permission to delete the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete the specified rule
  - **Resource types (\*required):** [listener-rule/app\*](#list_elbv2-resource-listener-rule_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener-rule/net\*](#list_elbv2-resource-listener-rule_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSharedTrustStoreAssociation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteSharedTrustStoreAssociation.html)  **
  - **Description:** Grants permission to delete the specified shared trust store association
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteTargetGroup.html)  **
  - **Description:** Grants permission to delete the specified target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteTrustStore.html)  **
  - **Description:** Grants permission to delete the specified trust store
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterTargets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeregisterTargets.html)  **
  - **Description:** Grants permission to deregister the specified targets from the specified target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountLimits](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeAccountLimits.html)  **
  - **Description:** Grants permission to describe the Elastic Load Balancing resource limits for the AWS account 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCapacityReservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeCapacityReservation.html)  **
  - **Description:** Grants permission to describe the capacity reservation for a load balancer 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeListenerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListenerAttributes.html)  **
  - **Description:** Grants permission to describe the attributes for the specified listener
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListenerCertificates.html)  **
  - **Description:** Grants permission to describe the certificates for the specified secure listener 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeListeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListeners.html)  **
  - **Description:** Grants permission to describe the specified listeners or the listeners for the specified Application Load Balancer 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancerAttributes.html)  **
  - **Description:** Grants permission to describe the attributes for the specified load balancer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html)  **
  - **Description:** Grants permission to describe the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRules](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeRules.html)  **
  - **Description:** Grants permission to describe the specified rules or the rules for the specified listener 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSSLPolicies](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeSSLPolicies.html)  **
  - **Description:** Grants permission to describe the specified policies or all policies used for SSL negotiation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe the tags associated with the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTargetGroupAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroupAttributes.html)  **
  - **Description:** Grants permission to describe the attributes for the specified target group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html)  **
  - **Description:** Grants permission to describe the specified target groups or all of your target groups 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTargetHealth](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetHealth.html)  **
  - **Description:** Grants permission to describe the health of the specified targets or all of your targets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTrustStoreAssociations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreAssociations.html)  **
  - **Description:** Grants permission to describe the associations with a trust store
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreRevocations.html)  **
  - **Description:** Grants permission to describe the specified trust stores revocations or all of your revocations related to a trust store
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTrustStores](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStores.html)  **
  - **Description:** Grants permission to describe the specified trust stores or all of your trust stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve the resource policy associated with the resource
  - **Resource types (\*required):** [truststore](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrustStoreCaCertificatesBundle](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetTrustStoreCaCertificatesBundle.html)  **
  - **Description:** Grants permission to retrieve a trust store CA certificates bundle
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrustStoreRevocationContent](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetTrustStoreRevocationContent.html)  **
  - **Description:** Grants permission to retrieve a trust store revocation content
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyCapacityReservation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyCapacityReservation.html)  **
  - **Description:** Grants permission to modify the capacity reservation for a load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyIpPools](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyIpPools.html)  **
  - **Description:** Grants permission to modify the ip pools for a load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListener.html)  **
  - **Description:** Grants permission to modify the specified properties of the specified listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Resource types (\*required):** [listener/gwy\*](#list_elbv2-resource-listener_gwy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ListenerProtocol](#list_elbv2-elasticloadbalancing_ListenerProtocol)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityPolicy](#list_elbv2-elasticloadbalancing_SecurityPolicy)
  - **Access level:** Write

- **   [ModifyListenerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListenerAttributes.html)  **
  - **Description:** Grants permission to modify the attributes of the specified listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/gwy\*](#list_elbv2-resource-listener_gwy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyLoadBalancerAttributes.html)  **
  - **Description:** Grants permission to modify the attributes of the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyRule](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyRule.html)  **
  - **Description:** Grants permission to modify the specified rule
  - **Resource types (\*required):** [listener-rule/app\*](#list_elbv2-resource-listener-rule_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener-rule/net\*](#list_elbv2-resource-listener-rule_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyTargetGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroup.html)  **
  - **Description:** Grants permission to modify the health checks used when evaluating the health state of the targets in the specified target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyTargetGroupAttributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroupAttributes.html)  **
  - **Description:** Grants permission to modify the specified attributes of the specified target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyTrustStore](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTrustStore.html)  **
  - **Description:** Grants permission to modify the specified trust store
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterTargets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RegisterTargets.html)  **
  - **Description:** Grants permission to register the specified targets with the specified target group
  - **Resource types (\*required):** [targetgroup\*](#list_elbv2-resource-targetgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveListenerCertificates.html)  **
  - **Description:** Grants permission to remove the specified certificates of the specified secure listener
  - **Resource types (\*required):** [listener/app\*](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net\*](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified load balancer
  - **Resource types (\*required):** [listener-rule/app](#list_elbv2-resource-listener-rule_app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener-rule/net](#list_elbv2-resource-listener-rule_net) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/app](#list_elbv2-resource-listener_app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/gwy](#list_elbv2-resource-listener_gwy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener/net](#list_elbv2-resource-listener_net) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [targetgroup](#list_elbv2-resource-targetgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [truststore](#list_elbv2-resource-truststore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elbv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elbv2-aws_TagKeys)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [RemoveTrustStoreRevocations](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTrustStoreRevocations.html)  **
  - **Description:** Grants permission to remove revocations from a trust store
  - **Resource types (\*required):** [truststore\*](#list_elbv2-resource-truststore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetIpAddressType](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetIpAddressType.html)  **
  - **Description:** Grants permission to set the type of IP addresses used by the subnets of the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetRulePriorities](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetRulePriorities.html)  **
  - **Description:** Grants permission to set the priorities of the specified rules
  - **Resource types (\*required):** [listener-rule/app\*](#list_elbv2-resource-listener-rule_app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [listener-rule/net\*](#list_elbv2-resource-listener-rule_net) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetSecurityGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSecurityGroups.html)  **
  - **Description:** Grants permission to associate the specified security groups with the specified load balancer 
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityGroup](#list_elbv2-elasticloadbalancing_SecurityGroup)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:SecurityGroup](#list_elbv2-elasticloadbalancing_SecurityGroup)
  - **Access level:** Write

- **   [SetSubnets](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSubnets.html)  **
  - **Description:** Grants permission to enable the Availability Zone for the specified subnets for the specified load balancer 
  - **Resource types (\*required):** [loadbalancer/app/](#list_elbv2-resource-loadbalancer_app_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Resource types (\*required):** [loadbalancer/gwy/](#list_elbv2-resource-loadbalancer_gwy_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Resource types (\*required):** [loadbalancer/net/](#list_elbv2-resource-loadbalancer_net_) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)<br />[elasticloadbalancing:Subnet](#list_elbv2-elasticloadbalancing_Subnet)
  - **Access level:** Write



## Permission-only actions for AWS Elastic Load Balancing V2
<a name="list_elbv2-permission-only-actions"></a>

The following actions are defined by AWS Elastic Load Balancing V2 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AllowVendedLogDeliveryForResource.html)  **
  - **Description:** Grants permission to configure vended log delivery for load balancers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [CreateWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  **
  - **Description:** Grants permission to associate WAF WebACL to the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_elbv2-resource-loadbalancer_app_)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  **
  - **Description:** Grants permission to disassociate WAF WebACL from the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_elbv2-resource-loadbalancer_app_)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeWebACLAssociation](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  **
  - **Description:** Grants permission to describe all load balancers associated to a WAF WebACL in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetLoadBalancerWebACL](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  **
  - **Description:** Grants permission to retrieve the WAF WebACL associated to the specified load balancer
  - **Resource types (\*required):** [loadbalancer/app/\*](#list_elbv2-resource-loadbalancer_app_)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SetWebAcl](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html#security_iam_action-AssociateWebACL)  **
  - **Description:** Grants permission to give WebAcl permission to WAF
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Elastic Load Balancing V2
<a name="list_elbv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [listener-rule/app](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener-rule/app/${LoadBalancerName}/${LoadBalancerId}/${ListenerId}/${ListenerRuleId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [listener-rule/net](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener-rule/net/${LoadBalancerName}/${LoadBalancerId}/${ListenerId}/${ListenerRuleId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [listener/app](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener/app/${LoadBalancerName}/${LoadBalancerId}/${ListenerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [listener/gwy](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener/gwy/${LoadBalancerName}/${LoadBalancerId}/${ListenerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [listener/net](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:listener/net/${LoadBalancerName}/${LoadBalancerId}/${ListenerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [loadbalancer/app/](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html#application-load-balancer-overview)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/app/${LoadBalancerName}/${LoadBalancerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [loadbalancer/gwy/](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/gwy/${LoadBalancerName}/${LoadBalancerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [loadbalancer/net/](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#network-load-balancer-overview)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/net/${LoadBalancerName}/${LoadBalancerId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [targetgroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:targetgroup/${TargetGroupName}/${TargetGroupId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [truststore](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/trust-store.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:truststore/${TrustStoreName}/${TrustStoreId} | [aws:ResourceTag/${TagKey}](#list_elbv2-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_elbv2-elasticloadbalancing_ResourceTag___TagKey_) | 

## Condition keys for AWS Elastic Load Balancing V2
<a name="list_elbv2-policy-keys"></a>

AWS Elastic Load Balancing V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:CreateAction](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/tagging-resources-during-creation.html)  | Filters access by the name of a resource-creating API action | String | 
|   [elasticloadbalancing:ListenerProtocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#listenerprotocol-condition)  | Filters access by the listener protocol that is allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the preface string for a tag key and value pair that are attached to a resource | String | 
|   [elasticloadbalancing:Scheme](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#scheme-condition)  | Filters access by the load balancer scheme that is allowed in the request | String | 
|   [elasticloadbalancing:SecurityGroup](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#securitygroup-condition)  | Filters access by the security-group IDs that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:SecurityPolicy](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#securitypolicy-condition)  | Filters access by the SSL Security Policies that are allowed in the request | ArrayOfString | 
|   [elasticloadbalancing:Subnet](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security_iam_service-with-iam.html#subnet-condition)  | Filters access by the subnet IDs that are allowed in the request | ArrayOfString | 