# Actions, resources, and condition keys for Amazon Location Service Routes

Amazon Location Service Routes (service prefix: `geo-routes`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../location/latest/developerguide.md "../../../location/latest/developerguide.md").
- View a list of the [API operations available for
  this service](../../../location/latest/APIReference.md "../../../location/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../location/latest/developerguide/security-iam.md "../../../location/latest/developerguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-routes/geo-routes.json "https://servicereference.us-east-1.amazonaws.com/v1/geo-routes/geo-routes.json") for this service.

###### Topics

- [API operations defined by Amazon Location Service Routes](#list_geo-routes-operations "#list_geo-routes-operations")
- [Actions defined by Amazon Location Service Routes](#list_geo-routes-actions-as-permissions "#list_geo-routes-actions-as-permissions")
- [Resource types defined by Amazon Location Service Routes](#list_geo-routes-resources-for-iam-policies "#list_geo-routes-resources-for-iam-policies")
- [Condition keys for Amazon Location Service Routes](#list_geo-routes-policy-keys "#list_geo-routes-policy-keys")

## API operations defined by Amazon Location Service Routes

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-routes-actions-as-permissions "#list_geo-routes-actions-as-permissions").

| Operation            | IAM action                                                                                                                     | Condition key | Possible value(s) | Access level |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| CalculateIsolines    | [geo-routes:CalculateIsolines](#list_geo-routes-action-CalculateIsolines "#list_geo-routes-action-CalculateIsolines")          |               |                   | Read         |
| CalculateRouteMatrix | [geo-routes:CalculateRouteMatrix](#list_geo-routes-action-CalculateRouteMatrix "#list_geo-routes-action-CalculateRouteMatrix") |               |                   | Read         |
| CalculateRoutes      | [geo-routes:CalculateRoutes](#list_geo-routes-action-CalculateRoutes "#list_geo-routes-action-CalculateRoutes")                |               |                   | Read         |
| OptimizeWaypoints    | [geo-routes:OptimizeWaypoints](#list_geo-routes-action-OptimizeWaypoints "#list_geo-routes-action-OptimizeWaypoints")          |               |                   | Read         |
| SnapToRoads          | [geo-routes:SnapToRoads](#list_geo-routes-action-SnapToRoads "#list_geo-routes-action-SnapToRoads")                            |               |                   | Read         |

## Actions defined by Amazon Location Service Routes

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                       | Description                                                                                                                                    | Resource types (\*required)                                                           | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------- | ------------ |
| [CalculateIsolines](../../../location/latest/APIReference/API_CalculateIsolines.md "../../../location/latest/APIReference/API_CalculateIsolines.md")          | Grants permission to determine destinations or service areas reachable within a specified time                                                 | [provider\*](#list_geo-routes-resource-provider "#list_geo-routes-resource-provider") |                | Read         |
| [CalculateRouteMatrix](../../../location/latest/APIReference/API_CalculateRouteMatrix.md "../../../location/latest/APIReference/API_CalculateRouteMatrix.md") | Grants permission to calculate routing matrice which providing travel time and distances between sets of origins and destinations              | [provider\*](#list_geo-routes-resource-provider "#list_geo-routes-resource-provider") |                | Read         |
| [CalculateRoutes](../../../location/latest/APIReference/API_CalculateRoutes.md "../../../location/latest/APIReference/API_CalculateRoutes.md")                | Grants permission to calculates routes between two or more locations                                                                           | [provider\*](#list_geo-routes-resource-provider "#list_geo-routes-resource-provider") |                | Read         |
| [OptimizeWaypoints](../../../location/latest/APIReference/API_OptimizeWaypoints.md "../../../location/latest/APIReference/API_OptimizeWaypoints.md")          | Grants permission to calculate the most efficient sequence for visiting multiple waypoints or locations along a route                          | [provider\*](#list_geo-routes-resource-provider "#list_geo-routes-resource-provider") |                | Read         |
| [SnapToRoads](../../../location/latest/APIReference/API_SnapToRoads.md "../../../location/latest/APIReference/API_SnapToRoads.md")                            | Grants permission to enhances the accuracy of geographic positioning by aligning GPS coordinates to the nearest road segments on a digital map | [provider\*](#list_geo-routes-resource-provider "#list_geo-routes-resource-provider") |                | Read         |

## Resource types defined by Amazon Location Service Routes

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                      | ARN                                                     | Condition keys |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- |
| [provider](../../../location/latest/developerguide/Welcome.md "../../../location/latest/developerguide/Welcome.md") | arn:${Partition}:geo-routes:${Region}::provider/default |                |

## Condition keys for Amazon Location Service Routes

Amazon Location Service Routes has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
