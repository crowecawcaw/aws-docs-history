

# Updating a HealthLake data store
<a name="managing-data-stores-update"></a>

Use `UpdateFHIRDatastore` to update the configuration of an existing AWS HealthLake data store. You can update the data store name, the natural language processing (NLP) configuration, the analytics configuration, the default FHIR validation profiles, and the identity provider configuration. The encryption configuration that you chose when you created the data store can't be changed.

**Note**  
Updating the identity provider configuration replaces it in full—include every field you want to keep. Any field you omit is cleared.

The following menu provides examples for the AWS CLI and AWS SDKs. For more information, see [`UpdateFHIRDatastore`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateFHIRDatastore.html) in the *AWS HealthLake API Reference*.

**Important**  
NLP and analytics changes are applied through an asynchronous workflow: the data store status changes to `UPDATING` and returns to `ACTIVE` when the update completes, or shows `UPDATE_FAILED` if it doesn't. Data store name, FHIR validation profile, and identity provider changes take effect immediately and don't change the status. Only one update can be in progress for a data store at a time; a second update submitted while one is running returns `ConflictException`. Use `DescribeFHIRDatastore` to track the status of an update.

**To update a HealthLake data store**  
Choose a menu based on your access preference to AWS HealthLake.

## AWS CLI and SDKs
<a name="managing-data-stores-update-cli-sdk"></a>

------
#### [ AWS CLI ]

**Example 1: Rename a data store**

```
aws healthlake update-fhir-datastore \
  --datastore-id "{{datastore-id}}" \
  --datastore-name "RenamedFhirDatastore"
```

**Example 2: Enable NLP**

```
aws healthlake update-fhir-datastore \
  --datastore-id "{{datastore-id}}" \
  --nlp-configuration '{ "Status": "ENABLED" }'
```

**Example 3: Pause analytics**

```
aws healthlake update-fhir-datastore \
  --datastore-id "{{datastore-id}}" \
  --analytics-configuration '{ "Status": "PAUSED" }'
```

**Example 4: Update default FHIR validation profiles**

```
aws healthlake update-fhir-datastore \
  --datastore-id "{{datastore-id}}" \
  --profile-configuration '{ "DefaultProfiles": ["us-core-3.1.1", "carin-bb-2.0.0"] }'
```

The response returns the full `DatastoreProperties` — the same shape returned by `DescribeFHIRDatastore`.

```
{
    "DatastoreProperties": {
        "DatastoreId": "{{datastore-id}}",
        "DatastoreArn": "arn:aws:healthlake:us-east-1:{{account-id}}:datastore/{{datastore-id}}",
        "DatastoreName": "RenamedFhirDatastore",
        "DatastoreStatus": "UPDATING",
        "DatastoreTypeVersion": "R4",
        "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/{{datastore-id}}/r4/",
        "NlpConfiguration": { "Status": "ENABLING" },
        "AnalyticsConfiguration": { "Status": "PAUSING" },
        "ProfileConfiguration": { "DefaultProfiles": [ "us-core-3.1.1", "carin-bb-2.0.0" ] },
        "IdentityProviderConfiguration": {
            "AuthorizationStrategy": "SMART_ON_FHIR_V1",
            "FineGrainedAuthorizationEnabled": true
        }
    }
}
```

For API details, see [update-fhir-datastore](https://docs.aws.amazon.com/cli/latest/reference/healthlake/update-fhir-datastore.html) in the *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**

```
def update_fhir_datastore(
    self,
    datastore_id: str,
    **kwargs,
) -> dict[str, any]:
    """
    Updates the configuration of an existing HealthLake data store.

    Pass any of DatastoreName, NlpConfiguration, AnalyticsConfiguration,
    ProfileConfiguration, or IdentityProviderConfiguration as keyword
    arguments. Omitted fields are left unchanged.

    :param datastore_id: The ID of the data store to update.
    :return: The response, including the full DatastoreProperties.
    """
    try:
        return self.health_lake_client.update_fhir_datastore(
            DatastoreId=datastore_id, **kwargs
        )
    except ClientError as err:
        logger.exception(
            "Couldn't update data store %s. Here's why: %s",
            datastore_id,
            err.response["Error"]["Message"],
        )
        raise
```

For API details, see [UpdateFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/UpdateFHIRDatastore) in the *AWS SDK for Python (Boto3) API Reference*.

------

**Example availability**  
Can't find what you need? Request a code example using the **Provide feedback** link on the right sidebar of this page.