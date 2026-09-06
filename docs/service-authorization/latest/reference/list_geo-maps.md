

# Actions, resources, and condition keys for Amazon Location Service Maps
<a name="list_geo-maps"></a>

Amazon Location Service Maps (service prefix: `geo-maps`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/location/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/location/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-maps/geo-maps.json) for this service.

**Topics**
+ [API operations defined by Amazon Location Service Maps](#list_geo-maps-operations)
+ [Actions defined by Amazon Location Service Maps](#list_geo-maps-actions-as-permissions)
+ [Resource types defined by Amazon Location Service Maps](#list_geo-maps-resources-for-iam-policies)
+ [Condition keys for Amazon Location Service Maps](#list_geo-maps-policy-keys)

## API operations defined by Amazon Location Service Maps
<a name="list_geo-maps-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-maps-actions-as-permissions).




- **   GetStaticMap  **
  - **IAM action:**  [geo-maps:GetStaticMap](#list_geo-maps-action-GetStaticMap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTile  **
  - **IAM action:**  [geo-maps:GetTile](#list_geo-maps-action-GetTile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Location Service Maps
<a name="list_geo-maps-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetStaticMap](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html)  **
  - **Description:** Grants permission to retrieve the static map
  - **Resource types (\*required):** [provider\*](#list_geo-maps-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTile](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html)  **
  - **Description:** Grants permission to retrieve the map tile
  - **Resource types (\*required):** [provider\*](#list_geo-maps-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon Location Service Maps
<a name="list_geo-maps-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [provider](https://docs.aws.amazon.com/location/latest/developerguide/Welcome.html)  | arn:${Partition}:geo-maps:${Region}::provider/default |   | 

## Condition keys for Amazon Location Service Maps
<a name="list_geo-maps-policy-keys"></a>

Amazon Location Service Maps has no service-specific condition keys that can be used in the `Condition` element of policy statements.