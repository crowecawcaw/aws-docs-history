# Actions, resources, and condition keys for Amazon Location Service Places

Amazon Location Service Places (service prefix: `geo-places`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../location/latest/developerguide.md "../../../location/latest/developerguide.md").
- View a list of the [API operations available for
  this service](../../../location/latest/APIReference.md "../../../location/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../location/latest/developerguide/security-iam.md "../../../location/latest/developerguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-places/geo-places.json "https://servicereference.us-east-1.amazonaws.com/v1/geo-places/geo-places.json") for this service.

###### Topics

- [API operations defined by Amazon Location Service Places](#list_geo-places-operations "#list_geo-places-operations")
- [Actions defined by Amazon Location Service Places](#list_geo-places-actions-as-permissions "#list_geo-places-actions-as-permissions")
- [Resource types defined by Amazon Location Service Places](#list_geo-places-resources-for-iam-policies "#list_geo-places-resources-for-iam-policies")
- [Condition keys for Amazon Location Service Places](#list_geo-places-policy-keys "#list_geo-places-policy-keys")

## API operations defined by Amazon Location Service Places

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-places-actions-as-permissions "#list_geo-places-actions-as-permissions").

| Operation      | IAM action                                                                                                   | Condition key | Possible value(s) | Access level |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| Autocomplete   | [geo-places:Autocomplete](#list_geo-places-action-Autocomplete "#list_geo-places-action-Autocomplete")       |               |                   | Read         |
| Geocode        | [geo-places:Geocode](#list_geo-places-action-Geocode "#list_geo-places-action-Geocode")                      |               |                   | Read         |
| GetPlace       | [geo-places:GetPlace](#list_geo-places-action-GetPlace "#list_geo-places-action-GetPlace")                   |               |                   | Read         |
| ReverseGeocode | [geo-places:ReverseGeocode](#list_geo-places-action-ReverseGeocode "#list_geo-places-action-ReverseGeocode") |               |                   | Read         |
| SearchNearby   | [geo-places:SearchNearby](#list_geo-places-action-SearchNearby "#list_geo-places-action-SearchNearby")       |               |                   | Read         |
| SearchText     | [geo-places:SearchText](#list_geo-places-action-SearchText "#list_geo-places-action-SearchText")             |               |                   | Read         |
| Suggest        | [geo-places:Suggest](#list_geo-places-action-Suggest "#list_geo-places-action-Suggest")                      |               |                   | Read         |

## Actions defined by Amazon Location Service Places

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                         | Description                                                                                                                                               | Resource types (\*required)                                                           | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------- | ------------ |
| [Autocomplete](../../../location/latest/APIReference/API_geoplaces_Autocomplete.md "../../../location/latest/APIReference/API_geoplaces_Autocomplete.md")       | Grants permission to autocomplete text input with potential places and addresses as the user types                                                        | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [Geocode](../../../location/latest/APIReference/API_geoplaces_Geocode.md "../../../location/latest/APIReference/API_geoplaces_Geocode.md")                      | Grants permission to geocode a textual address or place into geographic coordinates                                                                       | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [GetPlace](../../../location/latest/APIReference/API_geoplaces_GetPlace.md "../../../location/latest/APIReference/API_geoplaces_GetPlace.md")                   | Grants permission to query a place by it's unqiue place ID                                                                                                | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [ReverseGeocode](../../../location/latest/APIReference/API_geoplaces_ReverseGeocode.md "../../../location/latest/APIReference/API_geoplaces_ReverseGeocode.md") | Grants permission to convert geographic coordinates into a human-readable address or place                                                                | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [SearchNearby](../../../location/latest/APIReference/API_geoplaces_SearchNearby.md "../../../location/latest/APIReference/API_geoplaces_SearchNearby.md")       | Grants permission to retrieve places near a position which match to a set of user defined restrictions such as category or food type offered by the place | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [SearchText](../../../location/latest/APIReference/API_geoplaces_SearchText.md "../../../location/latest/APIReference/API_geoplaces_SearchText.md")             | Grants permission to query for places using a single free-form text input                                                                                 | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |
| [Suggest](../../../location/latest/APIReference/API_geoplaces_Suggest.md "../../../location/latest/APIReference/API_geoplaces_Suggest.md")                      | Grants permission to suggest potential places based on the user's input                                                                                   | [provider\*](#list_geo-places-resource-provider "#list_geo-places-resource-provider") |                | Read         |

## Resource types defined by Amazon Location Service Places

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                      | ARN                                                     | Condition keys |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- |
| [provider](../../../location/latest/developerguide/Welcome.md "../../../location/latest/developerguide/Welcome.md") | arn:${Partition}:geo-places:${Region}::provider/default |                |

## Condition keys for Amazon Location Service Places

Amazon Location Service Places has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
