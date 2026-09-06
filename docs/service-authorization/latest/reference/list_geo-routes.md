

# Actions, resources, and condition keys for Amazon Location Service Routes
<a name="list_geo-routes"></a>

Amazon Location Service Routes (service prefix: `geo-routes`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/location/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/location/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-routes/geo-routes.json) for this service.

**Topics**
+ [API operations defined by Amazon Location Service Routes](#list_geo-routes-operations)
+ [Actions defined by Amazon Location Service Routes](#list_geo-routes-actions-as-permissions)
+ [Resource types defined by Amazon Location Service Routes](#list_geo-routes-resources-for-iam-policies)
+ [Condition keys for Amazon Location Service Routes](#list_geo-routes-policy-keys)

## API operations defined by Amazon Location Service Routes
<a name="list_geo-routes-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-routes-actions-as-permissions).




- **   CalculateIsolines  **
  - **IAM action:**  [geo-routes:CalculateIsolines](#list_geo-routes-action-CalculateIsolines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CalculateRouteMatrix  **
  - **IAM action:**  [geo-routes:CalculateRouteMatrix](#list_geo-routes-action-CalculateRouteMatrix) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CalculateRoutes  **
  - **IAM action:**  [geo-routes:CalculateRoutes](#list_geo-routes-action-CalculateRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   OptimizeWaypoints  **
  - **IAM action:**  [geo-routes:OptimizeWaypoints](#list_geo-routes-action-OptimizeWaypoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SnapToRoads  **
  - **IAM action:**  [geo-routes:SnapToRoads](#list_geo-routes-action-SnapToRoads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Location Service Routes
<a name="list_geo-routes-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CalculateIsolines](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html)  **
  - **Description:** Grants permission to determine destinations or service areas reachable within a specified time
  - **Resource types (\*required):** [provider\*](#list_geo-routes-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html)  **
  - **Description:** Grants permission to calculate routing matrice which providing travel time and distances between sets of origins and destinations
  - **Resource types (\*required):** [provider\*](#list_geo-routes-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html)  **
  - **Description:** Grants permission to calculates routes between two or more locations
  - **Resource types (\*required):** [provider\*](#list_geo-routes-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html)  **
  - **Description:** Grants permission to calculate the most efficient sequence for visiting multiple waypoints or locations along a route
  - **Resource types (\*required):** [provider\*](#list_geo-routes-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html)  **
  - **Description:** Grants permission to enhances the accuracy of geographic positioning by aligning GPS coordinates to the nearest road segments on a digital map
  - **Resource types (\*required):** [provider\*](#list_geo-routes-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon Location Service Routes
<a name="list_geo-routes-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [provider](https://docs.aws.amazon.com/location/latest/developerguide/Welcome.html)  | arn:${Partition}:geo-routes:${Region}::provider/default |   | 

## Condition keys for Amazon Location Service Routes
<a name="list_geo-routes-policy-keys"></a>

Amazon Location Service Routes has no service-specific condition keys that can be used in the `Condition` element of policy statements.