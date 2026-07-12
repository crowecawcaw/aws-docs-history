# Actions, resources, and condition keys for Amazon Location Service Maps

Amazon Location Service Maps (service prefix: `geo-maps`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../location/latest/developerguide.md "../../../location/latest/developerguide.md").
- View a list of the [API operations available for
  this service](../../../location/latest/APIReference.md "../../../location/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../location/latest/developerguide/security-iam.md "../../../location/latest/developerguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-maps/geo-maps.json "https://servicereference.us-east-1.amazonaws.com/v1/geo-maps/geo-maps.json") for this service.

###### Topics

- [API operations defined by Amazon Location Service Maps](#list_geo-maps-operations "#list_geo-maps-operations")
- [Actions defined by Amazon Location Service Maps](#list_geo-maps-actions-as-permissions "#list_geo-maps-actions-as-permissions")
- [Resource types defined by Amazon Location Service Maps](#list_geo-maps-resources-for-iam-policies "#list_geo-maps-resources-for-iam-policies")
- [Condition keys for Amazon Location Service Maps](#list_geo-maps-policy-keys "#list_geo-maps-policy-keys")

## API operations defined by Amazon Location Service Maps

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-maps-actions-as-permissions "#list_geo-maps-actions-as-permissions").

| Operation    | IAM action                                                                                       | Condition key | Possible value(s) | Access level |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| GetStaticMap | [geo-maps:GetStaticMap](#list_geo-maps-action-GetStaticMap "#list_geo-maps-action-GetStaticMap") |               |                   | Read         |
| GetTile      | [geo-maps:GetTile](#list_geo-maps-action-GetTile "#list_geo-maps-action-GetTile")                |               |                   | Read         |

## Actions defined by Amazon Location Service Maps

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                               | Description                                  | Resource types (\*required)                                                       | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------- | -------------- | ------------ |
| [GetStaticMap](../../../location/latest/APIReference/API_geomaps_GetStaticMap.md "../../../location/latest/APIReference/API_geomaps_GetStaticMap.md") | Grants permission to retrieve the static map | [provider\*](#list_geo-maps-resource-provider "#list_geo-maps-resource-provider") |                | Read         |
| [GetTile](../../../location/latest/APIReference/API_geomaps_GetTile.md "../../../location/latest/APIReference/API_geomaps_GetTile.md")                | Grants permission to retrieve the map tile   | [provider\*](#list_geo-maps-resource-provider "#list_geo-maps-resource-provider") |                | Read         |

## Resource types defined by Amazon Location Service Maps

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                      | ARN                                                   | Condition keys |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- |
| [provider](../../../location/latest/developerguide/Welcome.md "../../../location/latest/developerguide/Welcome.md") | arn:${Partition}:geo-maps:${Region}::provider/default |                |

## Condition keys for Amazon Location Service Maps

Amazon Location Service Maps has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
