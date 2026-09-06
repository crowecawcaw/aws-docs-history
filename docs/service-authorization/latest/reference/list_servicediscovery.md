

# Actions, resources, and condition keys for AWS Cloud Map
<a name="list_servicediscovery"></a>

AWS Cloud Map (service prefix: `servicediscovery`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloud-map/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloud-map/latest/dg/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/servicediscovery/servicediscovery.json) for this service.

**Topics**
+ [API operations defined by AWS Cloud Map](#list_servicediscovery-operations)
+ [Actions defined by AWS Cloud Map](#list_servicediscovery-actions-as-permissions)
+ [Permission-only actions for AWS Cloud Map](#list_servicediscovery-permission-only-actions)
+ [Resource types defined by AWS Cloud Map](#list_servicediscovery-resources-for-iam-policies)
+ [Condition keys for AWS Cloud Map](#list_servicediscovery-policy-keys)

## API operations defined by AWS Cloud Map
<a name="list_servicediscovery-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_servicediscovery-actions-as-permissions).




- **   CreateHttpNamespace  **
  - **IAM action:**  [servicediscovery:CreateHttpNamespace](#list_servicediscovery-action-CreateHttpNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicediscovery:TagResource](#list_servicediscovery-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePrivateDnsNamespace  **
  - **IAM action:**  [servicediscovery:CreatePrivateDnsNamespace](#list_servicediscovery-action-CreatePrivateDnsNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicediscovery:TagResource](#list_servicediscovery-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePublicDnsNamespace  **
  - **IAM action:**  [servicediscovery:CreatePublicDnsNamespace](#list_servicediscovery-action-CreatePublicDnsNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicediscovery:TagResource](#list_servicediscovery-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateService  **
  - **IAM action:**  [servicediscovery:CreateService](#list_servicediscovery-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [servicediscovery:TagResource](#list_servicediscovery-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteNamespace  **
  - **IAM action:**  [servicediscovery:DeleteNamespace](#list_servicediscovery-action-DeleteNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **IAM action:**  [servicediscovery:DeleteService](#list_servicediscovery-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceAttributes  **
  - **IAM action:**  [servicediscovery:DeleteServiceAttributes](#list_servicediscovery-action-DeleteServiceAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterInstance  **
  - **IAM action:**  [servicediscovery:DeregisterInstance](#list_servicediscovery-action-DeregisterInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DiscoverInstances  **
  - **IAM action:**  [servicediscovery:DiscoverInstances](#list_servicediscovery-action-DiscoverInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DiscoverInstancesRevision  **
  - **IAM action:**  [servicediscovery:DiscoverInstancesRevision](#list_servicediscovery-action-DiscoverInstancesRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstance  **
  - **IAM action:**  [servicediscovery:GetInstance](#list_servicediscovery-action-GetInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstancesHealthStatus  **
  - **IAM action:**  [servicediscovery:GetInstancesHealthStatus](#list_servicediscovery-action-GetInstancesHealthStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNamespace  **
  - **IAM action:**  [servicediscovery:GetNamespace](#list_servicediscovery-action-GetNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOperation  **
  - **IAM action:**  [servicediscovery:GetOperation](#list_servicediscovery-action-GetOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [servicediscovery:GetService](#list_servicediscovery-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceAttributes  **
  - **IAM action:**  [servicediscovery:GetServiceAttributes](#list_servicediscovery-action-GetServiceAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInstances  **
  - **IAM action:**  [servicediscovery:ListInstances](#list_servicediscovery-action-ListInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNamespaces  **
  - **IAM action:**  [servicediscovery:ListNamespaces](#list_servicediscovery-action-ListNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOperations  **
  - **IAM action:**  [servicediscovery:ListOperations](#list_servicediscovery-action-ListOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [servicediscovery:ListServices](#list_servicediscovery-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [servicediscovery:ListTagsForResource](#list_servicediscovery-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterInstance  **
  - **IAM action:**  [servicediscovery:RegisterInstance](#list_servicediscovery-action-RegisterInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [servicediscovery:TagResource](#list_servicediscovery-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [servicediscovery:UntagResource](#list_servicediscovery-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateHttpNamespace  **
  - **IAM action:**  [servicediscovery:UpdateHttpNamespace](#list_servicediscovery-action-UpdateHttpNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInstanceCustomHealthStatus  **
  - **IAM action:**  [servicediscovery:UpdateInstanceCustomHealthStatus](#list_servicediscovery-action-UpdateInstanceCustomHealthStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePrivateDnsNamespace  **
  - **IAM action:**  [servicediscovery:UpdatePrivateDnsNamespace](#list_servicediscovery-action-UpdatePrivateDnsNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePublicDnsNamespace  **
  - **IAM action:**  [servicediscovery:UpdatePublicDnsNamespace](#list_servicediscovery-action-UpdatePublicDnsNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateService  **
  - **IAM action:**  [servicediscovery:UpdateService](#list_servicediscovery-action-UpdateService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceAttributes  **
  - **IAM action:**  [servicediscovery:UpdateServiceAttributes](#list_servicediscovery-action-UpdateServiceAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Cloud Map
<a name="list_servicediscovery-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateHttpNamespace.html)  **
  - **Description:** Grants permission to create an HTTP namespace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html)  **
  - **Description:** Grants permission to create a private namespace based on DNS, which will be visible only inside a specified Amazon VPC
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePublicDnsNamespace.html)  **
  - **Description:** Grants permission to create a public namespace based on DNS, which will be visible on the internet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html)  **
  - **Description:** Grants permission to create a service
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)<br />[servicediscovery:NamespaceArn](#list_servicediscovery-servicediscovery_NamespaceArn)
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)<br />[servicediscovery:NamespaceArn](#list_servicediscovery-servicediscovery_NamespaceArn)
  - **Access level:** Write

- **   [DeleteNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteNamespace.html)  **
  - **Description:** Grants permission to delete a specified namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [DeleteServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteServiceAttributes.html)  **
  - **Description:** Grants permission to delete specified attributes from a service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [DeregisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeregisterInstance.html)  **
  - **Description:** Grants permission to delete the records and the health check, if any, that Amazon Route 53 created for the specified instance
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html)  **
  - **Description:** Grants permission to discover registered instances for a specified namespace and service
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:NamespaceName](#list_servicediscovery-servicediscovery_NamespaceName)<br />[servicediscovery:ServiceName](#list_servicediscovery-servicediscovery_ServiceName)
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:NamespaceName](#list_servicediscovery-servicediscovery_NamespaceName)<br />[servicediscovery:ServiceName](#list_servicediscovery-servicediscovery_ServiceName)
  - **Access level:** Read

- **   [DiscoverInstancesRevision](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstancesRevision.html)  **
  - **Description:** Grants permission to discover the revision of the instances for a specified namespace and service
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:NamespaceName](#list_servicediscovery-servicediscovery_NamespaceName)<br />[servicediscovery:ServiceName](#list_servicediscovery-servicediscovery_ServiceName)
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:NamespaceName](#list_servicediscovery-servicediscovery_NamespaceName)<br />[servicediscovery:ServiceName](#list_servicediscovery-servicediscovery_ServiceName)
  - **Access level:** Read

- **   [GetInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstance.html)  **
  - **Description:** Grants permission to get information about a specified instance
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)
  - **Access level:** Read

- **   [GetInstancesHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstancesHealthStatus.html)  **
  - **Description:** Grants permission to get the current health status (Healthy, Unhealthy, or Unknown) of one or more instances
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)
  - **Access level:** Read

- **   [GetNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetNamespace.html)  **
  - **Description:** Grants permission to get information about a namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html)  **
  - **Description:** Grants permission to get information about a specific operation
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_servicediscovery-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetService.html)  **
  - **Description:** Grants permission to get the settings for a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetServiceAttributes.html)  **
  - **Description:** Grants permission to get the attributes for a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html)  **
  - **Description:** Grants permission to get summary information about the instances that were registered with a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)
  - **Access level:** Read

- **   [ListNamespaces](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListNamespaces.html)  **
  - **Description:** Grants permission to get information about the namespaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html)  **
  - **Description:** Grants permission to list operations that match the criteria that you specify
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListServices.html)  **
  - **Description:** Grants permission to get settings for all the services that match specified filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tags for the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html)  **
  - **Description:** Grants permission to register an instance based on the settings in a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_servicediscovery-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_servicediscovery-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:TagKeys](#list_servicediscovery-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateHttpNamespace.html)  **
  - **Description:** Grants permission to update the settings for a HTTP namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInstanceCustomHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateInstanceCustomHealthStatus.html)  **
  - **Description:** Grants permission to update the current health status for an instance that has a custom health check
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceArn](#list_servicediscovery-servicediscovery_ServiceArn)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [UpdatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePrivateDnsNamespace.html)  **
  - **Description:** Grants permission to update the settings for a private DNS namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePublicDnsNamespace.html)  **
  - **Description:** Grants permission to update the settings for a public DNS namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateService.html)  **
  - **Description:** Grants permission to update the settings in a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write

- **   [UpdateServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html)  **
  - **Description:** Grants permission to update the attributes in a specified service
  - **Resource types (\*required):** [service\*](#list_servicediscovery-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)<br />[servicediscovery:ServiceCreatedByAccount](#list_servicediscovery-servicediscovery_ServiceCreatedByAccount)
  - **Access level:** Write



## Permission-only actions for AWS Cloud Map
<a name="list_servicediscovery-permission-only-actions"></a>

The following actions are defined by AWS Cloud Map but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)  **
  - **Description:** Grants permission to delete the RAM access control policy for a namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)  **
  - **Description:** Grants permission to read the RAM access control policy for a namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a namespace
  - **Resource types (\*required):** [namespace\*](#list_servicediscovery-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Cloud Map
<a name="list_servicediscovery-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/API_Namespace.html)  | arn:${Partition}:servicediscovery:${Region}:${Account}:namespace/${NamespaceId} | [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/cloud-map/latest/dg/API_Service.html)  | arn:${Partition}:servicediscovery:${Region}:${Account}:service/${ServiceId} | [aws:ResourceTag/${TagKey}](#list_servicediscovery-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Cloud Map
<a name="list_servicediscovery-policy-keys"></a>

AWS Cloud Map defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the tag keys that are passed in the request | ArrayOfString | 
|   [servicediscovery:NamespaceArn](https://docs.aws.amazon.com/cloud-map/latest/dg/access-control-overview.html#specifying-conditions)  | Filters access by specifying the Amazon Resource Name (ARN) for the related namespace | ARN | 
|   [servicediscovery:NamespaceName](https://docs.aws.amazon.com/cloud-map/latest/dg/access-control-overview.html#specifying-conditions)  | Filters access by specifying the name of the related namespace | String | 
|   [servicediscovery:ServiceArn](https://docs.aws.amazon.com/cloud-map/latest/dg/access-control-overview.html#specifying-conditions)  | Filters access by specifying the Amazon Resource Name (ARN) for the related service | ARN | 
|   [servicediscovery:ServiceCreatedByAccount](https://docs.aws.amazon.com/cloud-map/latest/dg/access-control-overview.html#specifying-conditions)  | Filters access by specifying the account id of the related service creator | String | 
|   [servicediscovery:ServiceName](https://docs.aws.amazon.com/cloud-map/latest/dg/access-control-overview.html#specifying-conditions)  | Filters access by specifying the name of the related service | String | 