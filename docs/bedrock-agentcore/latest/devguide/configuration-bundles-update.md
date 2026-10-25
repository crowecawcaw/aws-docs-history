

# Update a configuration bundle
<a name="configuration-bundles-update"></a>

Update a configuration bundle to create a new immutable version with changed configuration. Each update produces a new version ID; existing versions are never modified. Versions form a chain via `parentVersionIds`, similar to git commits.

## Code samples
<a name="update-bundle-examples"></a>

**Example**  
If you added the bundle with `agentcore add config-bundle`, change its `components` in `agentcore/agentcore.json` and deploy. The deployment creates a new immutable version:  

```
agentcore deploy
```
To update a configuration bundle that your project does not manage, such as one that you created with `agentcore eval config-bundle create`, provide the complete replacement component map. The command creates a new immutable version on `mainline` by default:  

```
agentcore eval config-bundle update \
  --id <configuration-bundle-id> \
  --components file://components.json \
  --commit-message "Switch to Claude Sonnet 4"
```
To list the versions of either kind of bundle, run the following command. For a bundle in your project, the bundle ID is the last segment of its `arn` in `agentcore status --json`:  

```
agentcore eval config-bundle version list --id <configuration-bundle-id>
```
Update changing the model ID:  

```
import boto3
import uuid

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

RUNTIME_ARN = "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/MyAgent-abc123"

# The parent must be the latest version on the branch you update
latest = client.get_configuration_bundle(bundleId="myAgentConfig-a1b2c3d4e5", branchName="mainline")

response = client.update_configuration_bundle(
    bundleId="myAgentConfig-a1b2c3d4e5",
    components={
        RUNTIME_ARN: {
            "configuration": {
                "system_prompt": "You are a helpful customer support assistant.",
                "model_id": "us.anthropic.claude-sonnet-4-20250514-v1:0",
                "temperature": 0.7,
            }
        }
    },
    parentVersionIds=[latest["versionId"]],
    commitMessage="Switch to Claude Sonnet 4",
    clientToken=str(uuid.uuid4()),
)

print(f"New version ID: {response['versionId']}")
```
Update with a recommended system prompt from a recommendation result:  

```
import time
import boto3
import uuid

cp_client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")
dp_client = boto3.client("bedrock-agentcore", region_name="us-west-2")

RUNTIME_ARN = "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/MyAgent-abc123"

# Wait for the recommendation to complete
while True:
    recommendation = dp_client.get_recommendation(recommendationId="myRec-A1B2C3D4E5")
    if recommendation["status"] == "COMPLETED":
        break
    if recommendation["status"] == "FAILED":
        raise RuntimeError("Recommendation failed")
    time.sleep(30)

result = recommendation["recommendationResult"]["systemPromptRecommendationResult"]
recommended_prompt = result["recommendedSystemPrompt"]

# The parent must be the latest version on the branch you update
latest = cp_client.get_configuration_bundle(bundleId="myAgentConfig-a1b2c3d4e5", branchName="mainline")

# Update the bundle with the recommended prompt
response = cp_client.update_configuration_bundle(
    bundleId="myAgentConfig-a1b2c3d4e5",
    components={
        RUNTIME_ARN: {
            "configuration": {
                "system_prompt": recommended_prompt,
                "model_id": "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
                "temperature": 0.7,
            }
        }
    },
    parentVersionIds=[latest["versionId"]],
    commitMessage="Apply recommended system prompt",
    createdBy={"name": "optimization-job", "arn": recommendation["recommendationArn"]},
    clientToken=str(uuid.uuid4()),
)

print(f"New version ID: {response['versionId']}")
```

## Request parameters
<a name="update-bundle-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `bundleId`  | String | Yes | The ID of the configuration bundle to update. Passed as a path parameter. | 
|  `bundleName`  | String | No | Updated name for the bundle. | 
|  `description`  | String | No | Updated description. Maximum 500 characters. | 
|  `components`  | Map | No | Updated component configurations. Creates a new version with these components. | 
|  `parentVersionIds`  | List of strings | Yes | Parent version IDs for lineage tracking. Regular commits have one parent, the latest version on the branch. Merge commits have two parents: the latest version on the target branch, then the latest version on the source branch. If the branch already exists, the first parent must be the latest version on that branch. | 
|  `branchName`  | String | No | Branch name for this version. If not specified, inherits the parent’s branch or defaults to `mainline`. | 
|  `commitMessage`  | String | No | Commit message describing the changes. Maximum 500 characters. | 
|  `createdBy`  | Object | No | Source that created this version. Contains `name` (required) and `arn` (optional). Use this to track whether a version was created by a user, recommendation job, or other automation. | 
|  `clientToken`  | String | No | Idempotency token. | 

## Response
<a name="update-bundle-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `bundleArn`  | String | ARN of the configuration bundle. | 
|  `bundleId`  | String | ID of the configuration bundle. | 
|  `versionId`  | String | UUID of the new version created by this update. | 
|  `updatedAt`  | Timestamp | When the update was applied. | 

## Branching and merges
<a name="update-bundle-branching"></a>

Configuration bundles support git-like branching:
+  **Linear commits.** Pass the latest version on the branch as the single parent. The new version extends the branch lineage. The AgentCore CLI looks up the latest version on the branch and passes it as the parent for you.
+  **New branch.** Specify a `branchName` that does not yet exist and a `parentVersionIds` pointing to the version you want to branch from.
+  **Merge commits.** Pass two `parentVersionIds`: the first is the latest version on the target branch, the second is the latest on the source branch. This creates a merge commit on the target branch.

## Errors
<a name="update-bundle-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ValidationException`  | 400 | Invalid request parameters. Check field constraints. | 
|  `ResourceNotFoundException`  | 404 | The specified `bundleId` does not exist. | 
|  `ConflictException`  | 409 | Version conflict. The specified parent version is not the latest on the branch. Fetch the latest version and retry. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. Verify IAM policies include `bedrock-agentcore:UpdateConfigurationBundle`. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. Retry with exponential backoff. | 
|  `InternalServerException`  | 500 | Service-side error. Retry the request. | 