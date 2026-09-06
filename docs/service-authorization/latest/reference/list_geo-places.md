

# Actions, resources, and condition keys for Amazon Location Service Places
<a name="list_geo-places"></a>

Amazon Location Service Places (service prefix: `geo-places`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/location/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/location/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/geo-places/geo-places.json) for this service.

**Topics**
+ [API operations defined by Amazon Location Service Places](#list_geo-places-operations)
+ [Actions defined by Amazon Location Service Places](#list_geo-places-actions-as-permissions)
+ [Resource types defined by Amazon Location Service Places](#list_geo-places-resources-for-iam-policies)
+ [Condition keys for Amazon Location Service Places](#list_geo-places-policy-keys)

## API operations defined by Amazon Location Service Places
<a name="list_geo-places-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_geo-places-actions-as-permissions).




- **   Autocomplete  **
  - **IAM action:**  [geo-places:Autocomplete](#list_geo-places-action-Autocomplete) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Geocode  **
  - **IAM action:**  [geo-places:Geocode](#list_geo-places-action-Geocode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlace  **
  - **IAM action:**  [geo-places:GetPlace](#list_geo-places-action-GetPlace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ReverseGeocode  **
  - **IAM action:**  [geo-places:ReverseGeocode](#list_geo-places-action-ReverseGeocode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchNearby  **
  - **IAM action:**  [geo-places:SearchNearby](#list_geo-places-action-SearchNearby) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchText  **
  - **IAM action:**  [geo-places:SearchText](#list_geo-places-action-SearchText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Suggest  **
  - **IAM action:**  [geo-places:Suggest](#list_geo-places-action-Suggest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Location Service Places
<a name="list_geo-places-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html)  **
  - **Description:** Grants permission to autocomplete text input with potential places and addresses as the user types
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html)  **
  - **Description:** Grants permission to geocode a textual address or place into geographic coordinates
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html)  **
  - **Description:** Grants permission to query a place by it's unqiue place ID
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html)  **
  - **Description:** Grants permission to convert geographic coordinates into a human-readable address or place
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html)  **
  - **Description:** Grants permission to retrieve places near a position which match to a set of user defined restrictions such as category or food type offered by the place
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html)  **
  - **Description:** Grants permission to query for places using a single free-form text input
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read

- **   [Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html)  **
  - **Description:** Grants permission to suggest potential places based on the user's input
  - **Resource types (\*required):** [provider\*](#list_geo-places-resource-provider)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon Location Service Places
<a name="list_geo-places-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [provider](https://docs.aws.amazon.com/location/latest/developerguide/Welcome.html)  | arn:${Partition}:geo-places:${Region}::provider/default |   | 

## Condition keys for Amazon Location Service Places
<a name="list_geo-places-policy-keys"></a>

Amazon Location Service Places has no service-specific condition keys that can be used in the `Condition` element of policy statements.