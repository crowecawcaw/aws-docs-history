

# Actions, resources, and condition keys for AWS App Mesh Preview
<a name="list_appmesh-preview"></a>

AWS App Mesh Preview (service prefix: `appmesh-preview`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/app-mesh/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/app-mesh/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/app-mesh/latest/userguide/IAM_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appmesh-preview/appmesh-preview.json) for this service.

**Topics**
+ [Actions defined by AWS App Mesh Preview](#list_appmesh-preview-actions-as-permissions)
+ [Permission-only actions for AWS App Mesh Preview](#list_appmesh-preview-permission-only-actions)
+ [Resource types defined by AWS App Mesh Preview](#list_appmesh-preview-resources-for-iam-policies)
+ [Condition keys for AWS App Mesh Preview](#list_appmesh-preview-policy-keys)

## Actions defined by AWS App Mesh Preview
<a name="list_appmesh-preview-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateGatewayRoute.html)  **
  - **Description:** Grants permission to create a gateway route that is associated with a virtual gateway
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-preview-resource-gatewayRoute) / **Condition keys:**  
  - **Resource types (\*required):** [virtualService](#list_appmesh-preview-resource-virtualService) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateMesh.html)  **
  - **Description:** Grants permission to create a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateRoute.html)  **
  - **Description:** Grants permission to create a route that is associated with a virtual router
  - **Resource types (\*required):** [route\*](#list_appmesh-preview-resource-route) / **Condition keys:**  
  - **Resource types (\*required):** [virtualNode](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualGateway.html)  **
  - **Description:** Grants permission to create a virtual gateway within a service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-preview-resource-virtualGateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualNode.html)  **
  - **Description:** Grants permission to create a virtual node within a service mesh
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Resource types (\*required):** [virtualService](#list_appmesh-preview-resource-virtualService) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualRouter.html)  **
  - **Description:** Grants permission to create a virtual router within a service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-preview-resource-virtualRouter)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_CreateVirtualService.html)  **
  - **Description:** Grants permission to create a virtual service within a service mesh
  - **Resource types (\*required):** [virtualNode](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-preview-resource-virtualRouter) / **Condition keys:**  
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-preview-resource-virtualService) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteGatewayRoute.html)  **
  - **Description:** Grants permission to delete an existing gateway route
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-preview-resource-gatewayRoute)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteMesh.html)  **
  - **Description:** Grants permission to delete an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteRoute.html)  **
  - **Description:** Grants permission to delete an existing route
  - **Resource types (\*required):** [route\*](#list_appmesh-preview-resource-route)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualGateway.html)  **
  - **Description:** Grants permission to delete an existing virtual gateway
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-preview-resource-virtualGateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualNode.html)  **
  - **Description:** Grants permission to delete an existing virtual node
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-preview-resource-virtualNode)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualRouter.html)  **
  - **Description:** Grants permission to delete an existing virtual router
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-preview-resource-virtualRouter)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DeleteVirtualService.html)  **
  - **Description:** Grants permission to delete an existing virtual service
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-preview-resource-virtualService)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeGatewayRoute.html)  **
  - **Description:** Grants permission to describe an existing gateway route
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-preview-resource-gatewayRoute)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeMesh.html)  **
  - **Description:** Grants permission to describe an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeRoute.html)  **
  - **Description:** Grants permission to describe an existing route
  - **Resource types (\*required):** [route\*](#list_appmesh-preview-resource-route)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualGateway.html)  **
  - **Description:** Grants permission to describe an existing virtual gateway
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-preview-resource-virtualGateway)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualNode.html)  **
  - **Description:** Grants permission to describe an existing virtual node
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-preview-resource-virtualNode)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualRouter.html)  **
  - **Description:** Grants permission to describe an existing virtual router
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-preview-resource-virtualRouter)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DescribeVirtualService.html)  **
  - **Description:** Grants permission to describe an existing virtual service
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-preview-resource-virtualService)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListGatewayRoutes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListGatewayRoutes.html)  **
  - **Description:** Grants permission to list existing gateway routes in a service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-preview-resource-virtualGateway)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMeshes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListMeshes.html)  **
  - **Description:** Grants permission to list existing service meshes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRoutes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListRoutes.html)  **
  - **Description:** Grants permission to list existing routes in a service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-preview-resource-virtualRouter)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVirtualGateways](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualGateways.html)  **
  - **Description:** Grants permission to list existing virtual gateways in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVirtualNodes](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualNodes.html)  **
  - **Description:** Grants permission to list existing virtual nodes
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVirtualRouters](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualRouters.html)  **
  - **Description:** Grants permission to list existing virtual routers in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVirtualServices](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListVirtualServices.html)  **
  - **Description:** Grants permission to list existing virtual services in a service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** List

- **   [StreamAggregatedResources](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html)  **
  - **Description:** Grants permission to receive streamed resources for an App Mesh endpoint (VirtualNode/VirtualGateway)
  - **Resource types (\*required):** [virtualGateway](#list_appmesh-preview-resource-virtualGateway) / **Condition keys:**  
  - **Resource types (\*required):** [virtualNode](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Access level:** Read

- **   [UpdateGatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateGatewayRoute.html)  **
  - **Description:** Grants permission to update an existing gateway route for a specified service mesh and virtual gateway
  - **Resource types (\*required):** [gatewayRoute\*](#list_appmesh-preview-resource-gatewayRoute) / **Condition keys:**  
  - **Resource types (\*required):** [virtualService](#list_appmesh-preview-resource-virtualService) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMesh](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateMesh.html)  **
  - **Description:** Grants permission to update an existing service mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRoute](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateRoute.html)  **
  - **Description:** Grants permission to update an existing route for a specified service mesh and virtual router
  - **Resource types (\*required):** [route\*](#list_appmesh-preview-resource-route) / **Condition keys:**  
  - **Resource types (\*required):** [virtualNode](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVirtualGateway](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualGateway.html)  **
  - **Description:** Grants permission to update an existing virtual gateway in a specified service mesh
  - **Resource types (\*required):** [virtualGateway\*](#list_appmesh-preview-resource-virtualGateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVirtualNode](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualNode.html)  **
  - **Description:** Grants permission to update an existing virtual node in a specified service mesh
  - **Resource types (\*required):** [virtualNode\*](#list_appmesh-preview-resource-virtualNode)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVirtualRouter](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualRouter.html)  **
  - **Description:** Grants permission to update an existing virtual router in a specified service mesh
  - **Resource types (\*required):** [virtualRouter\*](#list_appmesh-preview-resource-virtualRouter)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVirtualService](https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_UpdateVirtualService.html)  **
  - **Description:** Grants permission to update an existing virtual service in a specified service mesh
  - **Resource types (\*required):** [virtualNode](#list_appmesh-preview-resource-virtualNode) / **Condition keys:**  
  - **Resource types (\*required):** [virtualRouter](#list_appmesh-preview-resource-virtualRouter) / **Condition keys:**  
  - **Resource types (\*required):** [virtualService\*](#list_appmesh-preview-resource-virtualService) / **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS App Mesh Preview
<a name="list_appmesh-preview-permission-only-actions"></a>

The following actions are defined by AWS App Mesh Preview but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to delete the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to read the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutMeshPolicy](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a mesh
  - **Resource types (\*required):** [mesh\*](#list_appmesh-preview-resource-mesh)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS App Mesh Preview
<a name="list_appmesh-preview-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [gatewayRoute](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualGateway/${VirtualGatewayName}/gatewayRoute/${GatewayRouteName} |   | 
|  [mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName} |   | 
|  [route](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualRouter/${VirtualRouterName}/route/${RouteName} |   | 
|  [virtualGateway](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualGateway/${VirtualGatewayName} |   | 
|  [virtualNode](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualNode/${VirtualNodeName} |   | 
|  [virtualRouter](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualRouter/${VirtualRouterName} |   | 
|  [virtualService](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)  | arn:${Partition}:appmesh-preview:${Region}:${Account}:mesh/${MeshName}/virtualService/${VirtualServiceName} |   | 

## Condition keys for AWS App Mesh Preview
<a name="list_appmesh-preview-policy-keys"></a>

AWS App Mesh Preview has no service-specific condition keys that can be used in the `Condition` element of policy statements.