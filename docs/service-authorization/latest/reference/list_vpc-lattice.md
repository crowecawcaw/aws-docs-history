

# Actions, resources, and condition keys for Amazon VPC Lattice
<a name="list_vpc-lattice"></a>

Amazon VPC Lattice (service prefix: `vpc-lattice`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/vpc-lattice/vpc-lattice.json) for this service.

**Topics**
+ [API operations defined by Amazon VPC Lattice](#list_vpc-lattice-operations)
+ [Actions defined by Amazon VPC Lattice](#list_vpc-lattice-actions-as-permissions)
+ [Permission-only actions for Amazon VPC Lattice](#list_vpc-lattice-permission-only-actions)
+ [Resource types defined by Amazon VPC Lattice](#list_vpc-lattice-resources-for-iam-policies)
+ [Condition keys for Amazon VPC Lattice](#list_vpc-lattice-policy-keys)

## API operations defined by Amazon VPC Lattice
<a name="list_vpc-lattice-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_vpc-lattice-actions-as-permissions).




- **   BatchUpdateRule  **
  - **IAM action:**  [vpc-lattice:UpdateRule](#list_vpc-lattice-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessLogSubscription  **
  - **IAM action:**  [vpc-lattice:CreateAccessLogSubscription](#list_vpc-lattice-action-CreateAccessLogSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateListener  **
  - **IAM action:**  [vpc-lattice:CreateListener](#list_vpc-lattice-action-CreateListener)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceConfiguration  **
  - **IAM action:**  [vpc-lattice:CreateResourceConfiguration](#list_vpc-lattice-action-CreateResourceConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceGateway  **
  - **IAM action:**  [vpc-lattice:CreateResourceGateway](#list_vpc-lattice-action-CreateResourceGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRule  **
  - **IAM action:**  [vpc-lattice:CreateRule](#list_vpc-lattice-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateService  **
  - **IAM action:**  [vpc-lattice:CreateService](#list_vpc-lattice-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceNetwork  **
  - **IAM action:**  [vpc-lattice:CreateServiceNetwork](#list_vpc-lattice-action-CreateServiceNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceNetworkResourceAssociation  **
  - **IAM action:**  [vpc-lattice:AssociateViaAWSService](#list_vpc-lattice-action-AssociateViaAWSService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [vpc-lattice:AssociateViaAWSService-EventsAndStates](#list_vpc-lattice-action-AssociateViaAWSService-EventsAndStates)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [vpc-lattice:CreateServiceNetworkResourceAssociation](#list_vpc-lattice-action-CreateServiceNetworkResourceAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceNetworkServiceAssociation  **
  - **IAM action:**  [vpc-lattice:CreateServiceNetworkServiceAssociation](#list_vpc-lattice-action-CreateServiceNetworkServiceAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceNetworkVpcAssociation  **
  - **IAM action:**  [vpc-lattice:CreateServiceNetworkVpcAssociation](#list_vpc-lattice-action-CreateServiceNetworkVpcAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTargetGroup  **
  - **IAM action:**  [vpc-lattice:CreateTargetGroup](#list_vpc-lattice-action-CreateTargetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccessLogSubscription  **
  - **IAM action:**  [vpc-lattice:DeleteAccessLogSubscription](#list_vpc-lattice-action-DeleteAccessLogSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAuthPolicy  **
  - **IAM action:**  [vpc-lattice:DeleteAuthPolicy](#list_vpc-lattice-action-DeleteAuthPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteDomainVerification  **
  - **IAM action:**  [vpc-lattice:DeleteDomainVerification](#list_vpc-lattice-action-DeleteDomainVerification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteListener  **
  - **IAM action:**  [vpc-lattice:DeleteListener](#list_vpc-lattice-action-DeleteListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceConfiguration  **
  - **IAM action:**  [vpc-lattice:DeleteResourceConfiguration](#list_vpc-lattice-action-DeleteResourceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceEndpointAssociation  **
  - **IAM action:**  [vpc-lattice:DeleteResourceEndpointAssociation](#list_vpc-lattice-action-DeleteResourceEndpointAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceGateway  **
  - **IAM action:**  [vpc-lattice:DeleteResourceGateway](#list_vpc-lattice-action-DeleteResourceGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [vpc-lattice:DeleteResourcePolicy](#list_vpc-lattice-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [vpc-lattice:DeleteRule](#list_vpc-lattice-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **IAM action:**  [vpc-lattice:DeleteService](#list_vpc-lattice-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceNetwork  **
  - **IAM action:**  [vpc-lattice:DeleteServiceNetwork](#list_vpc-lattice-action-DeleteServiceNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceNetworkResourceAssociation  **
  - **IAM action:**  [vpc-lattice:DeleteServiceNetworkResourceAssociation](#list_vpc-lattice-action-DeleteServiceNetworkResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceNetworkServiceAssociation  **
  - **IAM action:**  [vpc-lattice:DeleteServiceNetworkServiceAssociation](#list_vpc-lattice-action-DeleteServiceNetworkServiceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceNetworkVpcAssociation  **
  - **IAM action:**  [vpc-lattice:DeleteServiceNetworkVpcAssociation](#list_vpc-lattice-action-DeleteServiceNetworkVpcAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTargetGroup  **
  - **IAM action:**  [vpc-lattice:DeleteTargetGroup](#list_vpc-lattice-action-DeleteTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTargets  **
  - **IAM action:**  [vpc-lattice:DeregisterTargets](#list_vpc-lattice-action-DeregisterTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessLogSubscription  **
  - **IAM action:**  [vpc-lattice:GetAccessLogSubscription](#list_vpc-lattice-action-GetAccessLogSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthPolicy  **
  - **IAM action:**  [vpc-lattice:GetAuthPolicy](#list_vpc-lattice-action-GetAuthPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainVerification  **
  - **IAM action:**  [vpc-lattice:GetDomainVerification](#list_vpc-lattice-action-GetDomainVerification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetListener  **
  - **IAM action:**  [vpc-lattice:GetListener](#list_vpc-lattice-action-GetListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceConfiguration  **
  - **IAM action:**  [vpc-lattice:GetResourceConfiguration](#list_vpc-lattice-action-GetResourceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceGateway  **
  - **IAM action:**  [vpc-lattice:GetResourceGateway](#list_vpc-lattice-action-GetResourceGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [vpc-lattice:GetResourcePolicy](#list_vpc-lattice-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRule  **
  - **IAM action:**  [vpc-lattice:GetRule](#list_vpc-lattice-action-GetRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [vpc-lattice:GetService](#list_vpc-lattice-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceNetwork  **
  - **IAM action:**  [vpc-lattice:GetServiceNetwork](#list_vpc-lattice-action-GetServiceNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceNetworkResourceAssociation  **
  - **IAM action:**  [vpc-lattice:GetServiceNetworkResourceAssociation](#list_vpc-lattice-action-GetServiceNetworkResourceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceNetworkServiceAssociation  **
  - **IAM action:**  [vpc-lattice:GetServiceNetworkServiceAssociation](#list_vpc-lattice-action-GetServiceNetworkServiceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceNetworkVpcAssociation  **
  - **IAM action:**  [vpc-lattice:GetServiceNetworkVpcAssociation](#list_vpc-lattice-action-GetServiceNetworkVpcAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTargetGroup  **
  - **IAM action:**  [vpc-lattice:GetTargetGroup](#list_vpc-lattice-action-GetTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessLogSubscriptions  **
  - **IAM action:**  [vpc-lattice:ListAccessLogSubscriptions](#list_vpc-lattice-action-ListAccessLogSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainVerifications  **
  - **IAM action:**  [vpc-lattice:ListDomainVerifications](#list_vpc-lattice-action-ListDomainVerifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListListeners  **
  - **IAM action:**  [vpc-lattice:ListListeners](#list_vpc-lattice-action-ListListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceConfigurations  **
  - **IAM action:**  [vpc-lattice:ListResourceConfigurations](#list_vpc-lattice-action-ListResourceConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceEndpointAssociations  **
  - **IAM action:**  [vpc-lattice:ListResourceEndpointAssociations](#list_vpc-lattice-action-ListResourceEndpointAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceGateways  **
  - **IAM action:**  [vpc-lattice:ListResourceGateways](#list_vpc-lattice-action-ListResourceGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRules  **
  - **IAM action:**  [vpc-lattice:ListRules](#list_vpc-lattice-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceNetworkResourceAssociations  **
  - **IAM action:**  [vpc-lattice:ListServiceNetworkResourceAssociations](#list_vpc-lattice-action-ListServiceNetworkResourceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceNetworkServiceAssociations  **
  - **IAM action:**  [vpc-lattice:ListServiceNetworkServiceAssociations](#list_vpc-lattice-action-ListServiceNetworkServiceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceNetworkVpcAssociations  **
  - **IAM action:**  [vpc-lattice:ListServiceNetworkVpcAssociations](#list_vpc-lattice-action-ListServiceNetworkVpcAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceNetworkVpcEndpointAssociations  **
  - **IAM action:**  [vpc-lattice:ListServiceNetworkVpcEndpointAssociations](#list_vpc-lattice-action-ListServiceNetworkVpcEndpointAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceNetworks  **
  - **IAM action:**  [vpc-lattice:ListServiceNetworks](#list_vpc-lattice-action-ListServiceNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [vpc-lattice:ListServices](#list_vpc-lattice-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [vpc-lattice:ListTagsForResource](#list_vpc-lattice-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTargetGroups  **
  - **IAM action:**  [vpc-lattice:ListTargetGroups](#list_vpc-lattice-action-ListTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTargets  **
  - **IAM action:**  [vpc-lattice:ListTargets](#list_vpc-lattice-action-ListTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAuthPolicy  **
  - **IAM action:**  [vpc-lattice:PutAuthPolicy](#list_vpc-lattice-action-PutAuthPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutResourcePolicy  **
  - **IAM action:**  [vpc-lattice:PutResourcePolicy](#list_vpc-lattice-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterTargets  **
  - **IAM action:**  [vpc-lattice:RegisterTargets](#list_vpc-lattice-action-RegisterTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDomainVerification  **
  - **IAM action:**  [vpc-lattice:StartDomainVerification](#list_vpc-lattice-action-StartDomainVerification)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [vpc-lattice:TagResource](#list_vpc-lattice-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [vpc-lattice:UntagResource](#list_vpc-lattice-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessLogSubscription  **
  - **IAM action:**  [vpc-lattice:UpdateAccessLogSubscription](#list_vpc-lattice-action-UpdateAccessLogSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateListener  **
  - **IAM action:**  [vpc-lattice:UpdateListener](#list_vpc-lattice-action-UpdateListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceConfiguration  **
  - **IAM action:**  [vpc-lattice:UpdateResourceConfiguration](#list_vpc-lattice-action-UpdateResourceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceGateway  **
  - **IAM action:**  [vpc-lattice:UpdateResourceGateway](#list_vpc-lattice-action-UpdateResourceGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRule  **
  - **IAM action:**  [vpc-lattice:UpdateRule](#list_vpc-lattice-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateService  **
  - **IAM action:**  [vpc-lattice:UpdateService](#list_vpc-lattice-action-UpdateService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceNetwork  **
  - **IAM action:**  [vpc-lattice:UpdateServiceNetwork](#list_vpc-lattice-action-UpdateServiceNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceNetworkVpcAssociation  **
  - **IAM action:**  [vpc-lattice:UpdateServiceNetworkVpcAssociation](#list_vpc-lattice-action-UpdateServiceNetworkVpcAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTargetGroup  **
  - **IAM action:**  [vpc-lattice:UpdateTargetGroup](#list_vpc-lattice-action-UpdateTargetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon VPC Lattice
<a name="list_vpc-lattice-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateAccessLogSubscription.html)  **
  - **Description:** Grants permission to create an access log subscription
  - **Resource types (\*required):** [AccessLogSubscription\*](#list_vpc-lattice-resource-AccessLogSubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [CreateListener](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateListener.html)  **
  - **Description:** Grants permission to create a listener
  - **Resource types (\*required):** [Listener\*](#list_vpc-lattice-resource-Listener)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [CreateResourceConfiguration](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateResourceConfiguration.html)  **
  - **Description:** Grants permission to create a resource configuration
  - **Resource types (\*required):** [DomainVerification](#list_vpc-lattice-resource-DomainVerification) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [ResourceGateway](#list_vpc-lattice-resource-ResourceGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [CreateResourceGateway](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateResourceGateway.html)  **
  - **Description:** Grants permission to create a resource gateway
  - **Resource types (\*required):** [ResourceGateway\*](#list_vpc-lattice-resource-ResourceGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [CreateRule](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateRule.html)  **
  - **Description:** Grants permission to create a rule
  - **Resource types (\*required):** [Rule\*](#list_vpc-lattice-resource-Rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateService.html)  **
  - **Description:** Grants permission to create a service
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-resource-Service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [CreateServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetwork.html)  **
  - **Description:** Grants permission to create a service network
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [CreateServiceNetworkResourceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkResourceAssociation.html)  **
  - **Description:** Grants permission to create an association between a service network and a resource
  - **Resource types (\*required):** [ResourceConfiguration\*](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkResourceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkResourceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Write

- **   [CreateServiceNetworkServiceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkServiceAssociation.html)  **
  - **Description:** Grants permission to create a service network and service association
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkServiceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkServiceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Write

- **   [CreateServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateServiceNetworkVpcAssociation.html)  **
  - **Description:** Grants permission to create a service network and VPC association
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation\*](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [CreateTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_CreateTargetGroup.html)  **
  - **Description:** Grants permission to create a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [DeleteAccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteAccessLogSubscription.html)  **
  - **Description:** Grants permission to delete an access log subscription
  - **Resource types (\*required):** [AccessLogSubscription\*](#list_vpc-lattice-resource-AccessLogSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAuthPolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteAuthPolicy.html)  **
  - **Description:** Grants permission to delete an auth policy
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Permissions management, Write

- **   [DeleteDomainVerification](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteDomainVerification.html)  **
  - **Description:** Grants permission to delete a domain verification
  - **Resource types (\*required):** [DomainVerification\*](#list_vpc-lattice-resource-DomainVerification)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Access level:** Write

- **   [DeleteListener](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteListener.html)  **
  - **Description:** Grants permission to delete a listener
  - **Resource types (\*required):** [Listener\*](#list_vpc-lattice-resource-Listener)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [DeleteResourceConfiguration](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourceConfiguration.html)  **
  - **Description:** Grants permission to delete a resource configuration
  - **Resource types (\*required):** [ResourceConfiguration\*](#list_vpc-lattice-resource-ResourceConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteResourceEndpointAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourceEndpointAssociation.html)  **
  - **Description:** Grants permission to delete a resource endpoint association
  - **Resource types (\*required):** [ResourceEndpointAssociation\*](#list_vpc-lattice-resource-ResourceEndpointAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:VpcEndpointId](#list_vpc-lattice-vpc-lattice_VpcEndpointId)
  - **Access level:** Write

- **   [DeleteResourceGateway](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourceGateway.html)  **
  - **Description:** Grants permission to delete a resource gateway
  - **Resource types (\*required):** [ResourceGateway\*](#list_vpc-lattice-resource-ResourceGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete a rule
  - **Resource types (\*required):** [Rule\*](#list_vpc-lattice-resource-Rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a service
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-resource-Service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [DeleteServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteServiceNetwork.html)  **
  - **Description:** Grants permission to delete a service network
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [DeleteServiceNetworkResourceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteServiceNetworkResourceAssociation.html)  **
  - **Description:** Grants permission to delete the association between a service network and resource
  - **Resource types (\*required):** [ServiceNetworkResourceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkResourceAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Write

- **   [DeleteServiceNetworkServiceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteServiceNetworkServiceAssociation.html)  **
  - **Description:** Grants permission to delete a service network service association
  - **Resource types (\*required):** [ServiceNetworkServiceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkServiceAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Write

- **   [DeleteServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteServiceNetworkVpcAssociation.html)  **
  - **Description:** Grants permission to delete a service network and VPC association
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation\*](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [DeleteTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteTargetGroup.html)  **
  - **Description:** Grants permission to delete a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [DeregisterTargets](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeregisterTargets.html)  **
  - **Description:** Grants permission to deregister targets from a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [GetAccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetAccessLogSubscription.html)  **
  - **Description:** Grants permission to get information about an access log subscription
  - **Resource types (\*required):** [AccessLogSubscription\*](#list_vpc-lattice-resource-AccessLogSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Read

- **   [GetAuthPolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetAuthPolicy.html)  **
  - **Description:** Grants permission to get information about an auth policy
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Read

- **   [GetDomainVerification](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetDomainVerification.html)  **
  - **Description:** Grants permission to get information about a domain verification
  - **Resource types (\*required):** [DomainVerification\*](#list_vpc-lattice-resource-DomainVerification)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Access level:** Read

- **   [GetListener](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetListener.html)  **
  - **Description:** Grants permission to get information about a listener
  - **Resource types (\*required):** [Listener\*](#list_vpc-lattice-resource-Listener)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Read

- **   [GetResourceConfiguration](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourceConfiguration.html)  **
  - **Description:** Grants permission to get information about a resource configuration
  - **Resource types (\*required):** [ResourceConfiguration\*](#list_vpc-lattice-resource-ResourceConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Read

- **   [GetResourceGateway](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourceGateway.html)  **
  - **Description:** Grants permission to get information about a resource gateway
  - **Resource types (\*required):** [ResourceGateway\*](#list_vpc-lattice-resource-ResourceGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get information about a resource policy
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Read

- **   [GetRule](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetRule.html)  **
  - **Description:** Grants permission to get information about a rule
  - **Resource types (\*required):** [Rule\*](#list_vpc-lattice-resource-Rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to get information about a service
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-resource-Service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Read

- **   [GetServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetwork.html)  **
  - **Description:** Grants permission to get information about a service network
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Read

- **   [GetServiceNetworkResourceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkResourceAssociation.html)  **
  - **Description:** Grants permission to get information about an association between a service network and resource configuration
  - **Resource types (\*required):** [ServiceNetworkResourceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkResourceAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Read

- **   [GetServiceNetworkServiceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkServiceAssociation.html)  **
  - **Description:** Grants permission to get information about a service network and service association
  - **Resource types (\*required):** [ServiceNetworkServiceAssociation\*](#list_vpc-lattice-resource-ServiceNetworkServiceAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** Read

- **   [GetServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetServiceNetworkVpcAssociation.html)  **
  - **Description:** Grants permission to get information about a service network and VPC association
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation\*](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Read

- **   [GetTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetTargetGroup.html)  **
  - **Description:** Grants permission to get information about a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Read

- **   [ListAccessLogSubscriptions](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListAccessLogSubscriptions.html)  **
  - **Description:** Grants permission to list some or all access log subscriptions about a service network or a service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainVerifications](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListDomainVerifications.html)  **
  - **Description:** Grants permission to list some or all domain verifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListListeners](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListListeners.html)  **
  - **Description:** Grants permission to list some or all listeners
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceConfigurations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceConfigurations.html)  **
  - **Description:** Grants permission to list some or all resource configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceEndpointAssociations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceEndpointAssociations.html)  **
  - **Description:** Grants permission to list some or all associations between a resource configuration and VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:** [vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:VpcEndpointId](#list_vpc-lattice-vpc-lattice_VpcEndpointId)
  - **Access level:** List

- **   [ListResourceGateways](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListResourceGateways.html)  **
  - **Description:** Grants permission to list some or all resource gateways
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRules](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListRules.html)  **
  - **Description:** Grants permission to list some or all rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceNetworkResourceAssociations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkResourceAssociations.html)  **
  - **Description:** Grants permission to list some or all associations between a service network and resource configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceNetworkServiceAssociations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkServiceAssociations.html)  **
  - **Description:** Grants permission to list some or all service network and service associations
  - **Resource types (\*required):** 
  - **Condition keys:** [vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Access level:** List

- **   [ListServiceNetworkVpcAssociations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkVpcAssociations.html)  **
  - **Description:** Grants permission to list some or all service network and VPC associations
  - **Resource types (\*required):** 
  - **Condition keys:** [vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** List

- **   [ListServiceNetworkVpcEndpointAssociations](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworkVpcEndpointAssociations.html)  **
  - **Description:** Grants permission to list some or all associations between a service network and VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceNetworks](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServiceNetworks.html)  **
  - **Description:** Grants permission to list the service networks owned by a caller account or shared with the caller account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list the services owned by a caller account or shared with the caller account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a vpc-lattice resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTargetGroups](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListTargetGroups.html)  **
  - **Description:** Grants permission to list some or all target groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTargets](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListTargets.html)  **
  - **Description:** Grants permission to list some or all targets in a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** List

- **   [PutAuthPolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_PutAuthPolicy.html)  **
  - **Description:** Grants permission to create or update the auth policy for a service network or a service
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create a resource policy for a resource configuration, service, or service network
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [RegisterTargets](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_RegisterTargets.html)  **
  - **Description:** Grants permission to register targets to a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [StartDomainVerification](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_StartDomainVerification.html)  **
  - **Description:** Grants permission to start a domain verification
  - **Resource types (\*required):** [DomainVerification\*](#list_vpc-lattice-resource-DomainVerification)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a vpc-lattice resource
  - **Resource types (\*required):** [AccessLogSubscription](#list_vpc-lattice-resource-AccessLogSubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)
  - **Resource types (\*required):** [DomainVerification](#list_vpc-lattice-resource-DomainVerification) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Resource types (\*required):** [Listener](#list_vpc-lattice-resource-Listener) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)
  - **Resource types (\*required):** [ResourceEndpointAssociation](#list_vpc-lattice-resource-ResourceEndpointAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:VpcEndpointId](#list_vpc-lattice-vpc-lattice_VpcEndpointId)
  - **Resource types (\*required):** [ResourceGateway](#list_vpc-lattice-resource-ResourceGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Resource types (\*required):** [Rule](#list_vpc-lattice-resource-Rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)
  - **Resource types (\*required):** [ServiceNetworkResourceAssociation](#list_vpc-lattice-resource-ServiceNetworkResourceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkServiceAssociation](#list_vpc-lattice-resource-ServiceNetworkServiceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Resource types (\*required):** [TargetGroup](#list_vpc-lattice-resource-TargetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:CreateAction](#list_vpc-lattice-vpc-lattice_CreateAction)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a vpc-lattice resource
  - **Resource types (\*required):** [AccessLogSubscription](#list_vpc-lattice-resource-AccessLogSubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [DomainVerification](#list_vpc-lattice-resource-DomainVerification) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName)
  - **Resource types (\*required):** [Listener](#list_vpc-lattice-resource-Listener) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Resource types (\*required):** [ResourceConfiguration](#list_vpc-lattice-resource-ResourceConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Resource types (\*required):** [ResourceEndpointAssociation](#list_vpc-lattice-resource-ResourceEndpointAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:VpcEndpointId](#list_vpc-lattice-vpc-lattice_VpcEndpointId)
  - **Resource types (\*required):** [ResourceGateway](#list_vpc-lattice-resource-ResourceGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Resource types (\*required):** [Rule](#list_vpc-lattice-resource-Rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Resource types (\*required):** [Service](#list_vpc-lattice-resource-Service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetwork](#list_vpc-lattice-resource-ServiceNetwork) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Resource types (\*required):** [ServiceNetworkResourceAssociation](#list_vpc-lattice-resource-ServiceNetworkResourceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkServiceAssociation](#list_vpc-lattice-resource-ServiceNetworkServiceAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Resource types (\*required):** [TargetGroup](#list_vpc-lattice-resource-TargetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Tagging, Write

- **   [UpdateAccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateAccessLogSubscription.html)  **
  - **Description:** Grants permission to update an access log subscription
  - **Resource types (\*required):** [AccessLogSubscription\*](#list_vpc-lattice-resource-AccessLogSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateListener](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateListener.html)  **
  - **Description:** Grants permission to update a listener
  - **Resource types (\*required):** [Listener\*](#list_vpc-lattice-resource-Listener)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [UpdateResourceConfiguration](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateResourceConfiguration.html)  **
  - **Description:** Grants permission to update a resource configuration
  - **Resource types (\*required):** [ResourceConfiguration\*](#list_vpc-lattice-resource-ResourceConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateResourceGateway](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateResourceGateway.html)  **
  - **Description:** Grants permission to update a resource gateway
  - **Resource types (\*required):** [ResourceGateway\*](#list_vpc-lattice-resource-ResourceGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [UpdateRule](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateRule.html)  **
  - **Description:** Grants permission to update a rule
  - **Resource types (\*required):** [Rule\*](#list_vpc-lattice-resource-Rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns)
  - **Access level:** Write

- **   [UpdateService](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateService.html)  **
  - **Description:** Grants permission to update a service
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-resource-Service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [UpdateServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateServiceNetwork.html)  **
  - **Description:** Grants permission to update a service network
  - **Resource types (\*required):** [ServiceNetwork\*](#list_vpc-lattice-resource-ServiceNetwork)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType)
  - **Access level:** Write

- **   [UpdateServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateServiceNetworkVpcAssociation.html)  **
  - **Description:** Grants permission to update a service network and VPC association
  - **Resource types (\*required):** [ServiceNetworkVpcAssociation\*](#list_vpc-lattice-resource-ServiceNetworkVpcAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write

- **   [UpdateTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_UpdateTargetGroup.html)  **
  - **Description:** Grants permission to update a target group
  - **Resource types (\*required):** [TargetGroup\*](#list_vpc-lattice-resource-TargetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId)
  - **Access level:** Write



## Permission-only actions for Amazon VPC Lattice
<a name="list_vpc-lattice-permission-only-actions"></a>

The following actions are defined by Amazon VPC Lattice but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssociateViaAWSService](service-network-associations.html#service-network-resource-configuration)  | Grants permission to associate a resource configuration through any AWS service managed networks |  |   | Permissions management, Write | 
|   [AssociateViaAWSService-EventsAndStates](service-network-associations.html#service-network-resource-configuration)  | Grants permission to associate a resource configuration through Amazon EventBridge and AWS Step Functions service networks |  |   | Permissions management, Write | 
|   [CreateServiceNetworkVpcEndpointAssociation](service-network-associations.html#service-network-vpc-endpoint)  | Grants permission to create an association between a service network and VPC endpoint |  |   | Permissions management, Write | 

## Resource types defined by Amazon VPC Lattice
<a name="list_vpc-lattice-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AccessLogSubscription](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:accesslogsubscription/${AccessLogSubscriptionId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys) | 
|  [DomainVerification](https://docs.aws.amazon.com/vpc-lattice/latest/ug/domain-verification.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:domainverification/${DomainVerificationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:DomainName](#list_vpc-lattice-vpc-lattice_DomainName) | 
|  [Listener](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:service/${ServiceId}/listener/${ListenerId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:Protocol](#list_vpc-lattice-vpc-lattice_Protocol)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns) | 
|  [ResourceConfiguration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configurations.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:resourceconfiguration/${ResourceConfigurationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys) | 
|  [ResourceEndpointAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-endpoint-associations.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:resourceendpointassociation/${ResourceEndpointAssociationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:VpcEndpointId](#list_vpc-lattice-vpc-lattice_VpcEndpointId) | 
|  [ResourceGateway](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateways.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:resourcegateway/${ResourceGatewayId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId) | 
|  [Rule](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:service/${ServiceId}/listener/${ListenerId}/rule/${RuleId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:TargetGroupArns](#list_vpc-lattice-vpc-lattice_TargetGroupArns) | 
|  [Service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:service/${ServiceId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType) | 
|  [ServiceNetwork](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:servicenetwork/${ServiceNetworkId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:AuthType](#list_vpc-lattice-vpc-lattice_AuthType) | 
|  [ServiceNetworkResourceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-resource-configuration)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:servicenetworkresourceassociation/${ServiceNetworkResourceAssociationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ResourceConfigurationArn](#list_vpc-lattice-vpc-lattice_ResourceConfigurationArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn) | 
|  [ServiceNetworkServiceAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:servicenetworkserviceassociation/${ServiceNetworkServiceAssociationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:ServiceArn](#list_vpc-lattice-vpc-lattice_ServiceArn)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn) | 
|  [ServiceNetworkVpcAssociation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:servicenetworkvpcassociation/${ServiceNetworkVpcAssociationId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:PrivateDnsPreference](#list_vpc-lattice-vpc-lattice_PrivateDnsPreference)<br />[vpc-lattice:PrivateDnsSpecifiedDomains](#list_vpc-lattice-vpc-lattice_PrivateDnsSpecifiedDomains)<br />[vpc-lattice:SecurityGroupIds](#list_vpc-lattice-vpc-lattice_SecurityGroupIds)<br />[vpc-lattice:ServiceNetworkArn](#list_vpc-lattice-vpc-lattice_ServiceNetworkArn)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId) | 
|  [TargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:targetgroup/${TargetGroupId} | [aws:RequestTag/${TagKey}](#list_vpc-lattice-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_vpc-lattice-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_vpc-lattice-aws_TagKeys)<br />[vpc-lattice:VpcId](#list_vpc-lattice-vpc-lattice_VpcId) | 

## Condition keys for Amazon VPC Lattice
<a name="list_vpc-lattice-policy-keys"></a>

Amazon VPC Lattice defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [vpc-lattice:AuthType](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the auth type specified in the request | String | 
|   [vpc-lattice:CreateAction](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the name of a resource-creating API action and only available during tagging resources on creation | String | 
|   [vpc-lattice:DomainName](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the domain name | String | 
|   [vpc-lattice:PrivateDnsPreference](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the private dns preference | String | 
|   [vpc-lattice:PrivateDnsSpecifiedDomains](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the private dns domains | ArrayOfString | 
|   [vpc-lattice:Protocol](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the protocol specified in the request | String | 
|   [vpc-lattice:ResourceConfigurationArn](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ARN of a resource configuration | ARN | 
|   [vpc-lattice:SecurityGroupIds](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the IDs of security groups | ArrayOfString | 
|   [vpc-lattice:ServiceArn](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ARN of a service | ARN | 
|   [vpc-lattice:ServiceNetworkArn](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ARN of a service network | ARN | 
|   [vpc-lattice:TargetGroupArns](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ARNs of target groups | ArrayOfARN | 
|   [vpc-lattice:VpcEndpointId](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ID of a VPC endpoint | String | 
|   [vpc-lattice:VpcId](https://docs.aws.amazon.com/vpc-lattice/latest/ug/)  | Filters access by the ID of a virtual private cloud (VPC) | String | 