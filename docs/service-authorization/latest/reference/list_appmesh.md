

# Actions, resources, and condition keys for AWS App Mesh
<a name="list_appmesh"></a>

AWS App Mesh (service prefix: `appmesh`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/app-mesh/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/app-mesh/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/app-mesh/latest/userguide/IAM_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appmesh/appmesh.json) for this service.

**Topics**
+ [API operations defined by AWS App Mesh](#list_appmesh-operations)
+ [Actions defined by AWS App Mesh](#list_appmesh-actions-as-permissions)
+ [Permission-only actions for AWS App Mesh](#list_appmesh-permission-only-actions)
+ [Resource types defined by AWS App Mesh](#list_appmesh-resources-for-iam-policies)
+ [Condition keys for AWS App Mesh](#list_appmesh-policy-keys)

## API operations defined by AWS App Mesh
<a name="list_appmesh-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appmesh-actions-as-permissions).




- **   CreateGatewayRoute  **
  - **IAM action:**  [appmesh:CreateGatewayRoute](#list_appmesh-action-CreateGatewayRoute)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMesh  **
  - **IAM action:**  [appmesh:CreateMesh](#list_appmesh-action-CreateMesh)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRoute  **
  - **IAM action:**  [appmesh:CreateRoute](#list_appmesh-action-CreateRoute)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVirtualGateway  **
  - **IAM action:**  [appmesh:CreateVirtualGateway](#list_appmesh-action-CreateVirtualGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVirtualNode  **
  - **IAM action:**  [appmesh:CreateVirtualNode](#list_appmesh-action-CreateVirtualNode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appmesh.amazonaws.com / **Access level:** Write

- **   CreateVirtualRouter  **
  - **IAM action:**  [appmesh:CreateVirtualRouter](#list_appmesh-action-CreateVirtualRouter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVirtualService  **
  - **IAM action:**  [appmesh:CreateVirtualService](#list_appmesh-action-CreateVirtualService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGatewayRoute  **
  - **IAM action:**  [appmesh:DeleteGatewayRoute](#list_appmesh-action-DeleteGatewayRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMesh  **
  - **IAM action:**  [appmesh:DeleteMesh](#list_appmesh-action-DeleteMesh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoute  **
  - **IAM action:**  [appmesh:DeleteRoute](#list_appmesh-action-DeleteRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualGateway  **
  - **IAM action:**  [appmesh:DeleteVirtualGateway](#list_appmesh-action-DeleteVirtualGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualNode  **
  - **IAM action:**  [appmesh:DeleteVirtualNode](#list_appmesh-action-DeleteVirtualNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualRouter  **
  - **IAM action:**  [appmesh:DeleteVirtualRouter](#list_appmesh-action-DeleteVirtualRouter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualService  **
  - **IAM action:**  [appmesh:DeleteVirtualService](#list_appmesh-action-DeleteVirtualService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeGatewayRoute  **
  - **IAM action:**  [appmesh:DescribeGatewayRoute](#list_appmesh-action-DescribeGatewayRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMesh  **
  - **IAM action:**  [appmesh:DescribeMesh](#list_appmesh-action-DescribeMesh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRoute  **
  - **IAM action:**  [appmesh:DescribeRoute](#list_appmesh-action-DescribeRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualGateway  **
  - **IAM action:**  [appmesh:DescribeVirtualGateway](#list_appmesh-action-DescribeVirtualGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualNode  **
  - **IAM action:**  [appmesh:DescribeVirtualNode](#list_appmesh-action-DescribeVirtualNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualRouter  **
  - **IAM action:**  [appmesh:DescribeVirtualRouter](#list_appmesh-action-DescribeVirtualRouter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualService  **
  - **IAM action:**  [appmesh:DescribeVirtualService](#list_appmesh-action-DescribeVirtualService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListGatewayRoutes  **
  - **IAM action:**  [appmesh:ListGatewayRoutes](#list_appmesh-action-ListGatewayRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMeshes  **
  - **IAM action:**  [appmesh:ListMeshes](#list_appmesh-action-ListMeshes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoutes  **
  - **IAM action:**  [appmesh:ListRoutes](#list_appmesh-action-ListRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [appmesh:ListTagsForResource](#list_appmesh-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualGateways  **
  - **IAM action:**  [appmesh:ListVirtualGateways](#list_appmesh-action-ListVirtualGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualNodes  **
  - **IAM action:**  [appmesh:ListVirtualNodes](#list_appmesh-action-ListVirtualNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualRouters  **
  - **IAM action:**  [appmesh:ListVirtualRouters](#list_appmesh-action-ListVirtualRouters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualServices  **
  - **IAM action:**  [appmesh:ListVirtualServices](#list_appmesh-action-ListVirtualServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [appmesh:TagResource](#list_appmesh-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [appmesh:UntagResource](#list_appmesh-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateGatewayRoute  **
  - **IAM action:**  [appmesh:UpdateGatewayRoute](#list_appmesh-action-UpdateGatewayRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMesh  **
  - **IAM action:**  [appmesh:UpdateMesh](#list_appmesh-action-UpdateMesh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoute  **
  - **IAM action:**  [appmesh:UpdateRoute](#list_appmesh-action-UpdateRoute) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVirtualGateway  **
  - **IAM action:**  [appmesh:UpdateVirtualGateway](#list_appmesh-action-UpdateVirtualGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVirtualNode  **
  - **IAM action:**  [appmesh:UpdateVirtualNode](#list_appmesh-action-UpdateVirtualNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVirtualRouter  **
  - **IAM action:**  [appmesh:UpdateVirtualRouter](#list_appmesh-action-UpdateVirtualRouter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVirtualService  **
  - **IAM action:**  [appmesh:UpdateVirtualService](#list_appmesh-action-UpdateVirtualService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS App Mesh
<a name="list_appmesh-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateGatewayRoute.html)  **
  - **Description:** Grants permission to create a gateway route that is associated with a virtual gateway
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-resource-gatewayRoute) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateMesh.html)  **
  - **Description:** Grants permission to create a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateRoute.html)  **
  - **Description:** Grants permission to create a route that is associated with a virtual router
  - **Resource types (\*required):** [route\*](#list_appmesh-resource-route) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualGateway.html)  **
  - **Description:** Grants permission to create a virtual gateway within a service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-resource-virtualGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualNode.html)  **
  - **Description:** Grants permission to create a virtual node within a service mesh
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualRouter.html)  **
  - **Description:** Grants permission to create a virtual router within a service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-resource-virtualRouter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualService.html)  **
  - **Description:** Grants permission to create a virtual service within a service mesh
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-resource-virtualRouter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteGatewayRoute.html)  **
  - **Description:** Grants permission to delete an existing gateway route
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-resource-gatewayRoute)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteMesh.html)  **
  - **Description:** Grants permission to delete an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteRoute.html)  **
  - **Description:** Grants permission to delete an existing route
  - **Resource types (\*required):** [route\*](#list_appmesh-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualGateway.html)  **
  - **Description:** Grants permission to delete an existing virtual gateway
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-resource-virtualGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualNode.html)  **
  - **Description:** Grants permission to delete an existing virtual node
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-resource-virtualNode)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualRouter.html)  **
  - **Description:** Grants permission to delete an existing virtual router
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-resource-virtualRouter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualService.html)  **
  - **Description:** Grants permission to delete an existing virtual service
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-resource-virtualService)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeGatewayRoute.html)  **
  - **Description:** Grants permission to describe an existing gateway route
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-resource-gatewayRoute)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeMesh.html)  **
  - **Description:** Grants permission to describe an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeRoute.html)  **
  - **Description:** Grants permission to describe an existing route
  - **Resource types (\*required):** [route\*](#list_appmesh-resource-route)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualGateway.html)  **
  - **Description:** Grants permission to describe an existing virtual gateway
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-resource-virtualGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualNode.html)  **
  - **Description:** Grants permission to describe an existing virtual node
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-resource-virtualNode)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualRouter.html)  **
  - **Description:** Grants permission to describe an existing virtual router
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-resource-virtualRouter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualService.html)  **
  - **Description:** Grants permission to describe an existing virtual service
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-resource-virtualService)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListGatewayRoutes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListGatewayRoutes.html)  **
  - **Description:** Grants permission to list existing gateway routes in a service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-resource-virtualGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMeshes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListMeshes.html)  **
  - **Description:** Grants permission to list existing service meshes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRoutes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListRoutes.html)  **
  - **Description:** Grants permission to list existing routes in a service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-resource-virtualRouter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an App Mesh resource
  - **Resource types (\*required):** [gatewayRoute](#list_appmesh-resource-gatewayRoute) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mesh](#list_appmesh-resource-mesh) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [route](#list_appmesh-resource-route) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualGateway](#list_appmesh-resource-virtualGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-resource-virtualRouter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualGateways](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualGateways.html)  **
  - **Description:** Grants permission to list existing virtual gateways in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualNodes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualNodes.html)  **
  - **Description:** Grants permission to list existing virtual nodes
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualRouters](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualRouters.html)  **
  - **Description:** Grants permission to list existing virtual routers in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualServices](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualServices.html)  **
  - **Description:** Grants permission to list existing virtual services in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StreamAggregatedResources](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html)  **
  - **Description:** Grants permission to receive streamed resources for an App Mesh endpoint (VirtualNode/VirtualGateway)
  - **Resource types (\*required):** [virtualGateway](#list_appmesh-resource-virtualGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with a specified resourceArn
  - **Resource types (\*required):** [gatewayRoute](#list_appmesh-resource-gatewayRoute) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [mesh](#list_appmesh-resource-mesh) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [route](#list_appmesh-resource-route) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualGateway](#list_appmesh-resource-virtualGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-resource-virtualRouter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appmesh-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to delete a tag from a resource
  - **Resource types (\*required):** [gatewayRoute](#list_appmesh-resource-gatewayRoute) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [mesh](#list_appmesh-resource-mesh) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [route](#list_appmesh-resource-route) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualGateway](#list_appmesh-resource-virtualGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-resource-virtualRouter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appmesh-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateGatewayRoute.html)  **
  - **Description:** Grants permission to update an existing gateway route for a specified service mesh and virtual gateway
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-resource-gatewayRoute) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualService](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateMesh.html)  **
  - **Description:** Grants permission to update an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateRoute.html)  **
  - **Description:** Grants permission to update an existing route for a specified service mesh and virtual router
  - **Resource types (\*required):** [route\*](#list_appmesh-resource-route) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualGateway.html)  **
  - **Description:** Grants permission to update an existing virtual gateway in a specified service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-resource-virtualGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualNode.html)  **
  - **Description:** Grants permission to update an existing virtual node in a specified service mesh
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-resource-virtualNode)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualRouter.html)  **
  - **Description:** Grants permission to update an existing virtual router in a specified service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-resource-virtualRouter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualService.html)  **
  - **Description:** Grants permission to update an existing virtual service in a specified service mesh
  - **Resource types (\*required):** [virtualNode](#list_appmesh-resource-virtualNode) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-resource-virtualRouter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-resource-virtualService) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS App Mesh
<a name="list_appmesh-permission-only-actions"></a>

The following actions are defined by AWS App Mesh but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to delete the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to read the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-resource-mesh)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS App Mesh
<a name="list_appmesh-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [gatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualGateway/${VirtualGatewayName}/gatewayRoute/${GatewayRouteName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [route](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualRouter/${VirtualRouterName}/route/${RouteName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [virtualGateway](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualGateway/${VirtualGatewayName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [virtualNode](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualNode/${VirtualNodeName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [virtualRouter](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualRouter/${VirtualRouterName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 
|  [virtualService](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)  | arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}/virtualService/${VirtualServiceName} | [aws:ResourceTag/${TagKey}](#list_appmesh-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS App Mesh
<a name="list_appmesh-policy-keys"></a>

AWS App Mesh defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions by the presence of tag keys in the request | ArrayOfString | 