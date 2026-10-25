

# Delete a configuration bundle
<a name="configuration-bundles-delete"></a>

Delete a configuration bundle and all of its versions. Deletion is asynchronous — the API returns immediately with a `DELETING` status, and the service removes the bundle and its version history in the background.

You cannot delete a bundle that is referenced by an active A/B test. Stop the A/B test first.

## Code samples
<a name="delete-bundle-examples"></a>

**Example**  
If you added the bundle with `agentcore add config-bundle`, remove it from the project and deploy. The deployment deletes the bundle and all of its versions:  

```
agentcore remove config-bundle --name myAgentConfig
agentcore deploy
```
To delete a configuration bundle that your project does not manage, such as one that you created with `agentcore eval config-bundle create`, use its ID:  

```
agentcore eval config-bundle delete --id <configuration-bundle-id>
```

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client.delete_configuration_bundle(
    bundleId="myAgentConfig-a1b2c3d4e5"
)

print(f"Bundle ID: {response['bundleId']}")
print(f"Status: {response['status']}")  # DELETING
```

## Request parameters
<a name="delete-bundle-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `bundleId`  | String | Yes | The ID of the configuration bundle to delete. Passed as a path parameter. | 

## Response
<a name="delete-bundle-response"></a>

The API returns HTTP 202 (Accepted), indicating the deletion has been queued.


| Field | Type | Description | 
| --- | --- | --- | 
|  `bundleId`  | String | ID of the bundle being deleted. | 
|  `status`  | String | Status of the bundle. Returns `DELETING`. | 

## Deletion behavior
<a name="delete-bundle-behavior"></a>
+ The operation is **idempotent** — calling delete on an already-deleting bundle returns the same response without error.
+ All versions across all branches are deleted along with the bundle.
+ Once deletion completes, the bundle ID and name become available for reuse.
+ If the bundle is referenced by an active A/B test, the delete fails with a `ConflictException`. Stop the A/B test first.

## Errors
<a name="delete-bundle-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ValidationException`  | 400 | Invalid request parameters. | 
|  `ResourceNotFoundException`  | 404 | The specified `bundleId` does not exist. | 
|  `ConflictException`  | 409 | The bundle is in use by another resource (for example, an active A/B test) and cannot be deleted. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. Verify IAM policies include `bedrock-agentcore:DeleteConfigurationBundle`. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. Retry with exponential backoff. | 
|  `InternalServerException`  | 500 | Service-side error. Retry the request. | 