# Update resources in a private hub

You can update resources in your private hub to make changes to their metadata. The resources
that you can update include model references to Amazon SageMaker JumpStart models, custom models, and notebooks.

When updating model or notebook resources, you can update the content description,
display name, keywords, and support status. When updating model references to JumpStart
models, you can only update the field specifying the minimum model version that you'd like to use.

Follow the section specific to the resource that you want to update.

##

Update model or notebook resources

To update a model or a notebook resource, use the [UpdateHubContent](../APIReference/API_UpdateHubContent.md "../APIReference/API_UpdateHubContent.md") API.

The valid metadata fields that you can update with this API are the following:

- `HubContentDescription` – The description of the resource.
- `HubContentDisplayName` – The display name of the resource.
- `HubContentMarkdown` – The description of the resource,
  in Markdown formatting.
- `HubContentSearchKeywords` – The searchable
  keywords of the resource.
- `SupportStatus` – The current status of the resource.

In your request, include a change for one or more of the preceding fields. If you attempt to
update any other fields, such as the hub content type, you receive an error.

AWS SDK for Python (Boto3)
The following example shows how you can use the AWS SDK for Python (Boto3) to submit an
[UpdateHubContent](../APIReference/API_UpdateHubContent.md "../APIReference/API_UpdateHubContent.md") request.

###### Note

The `HubContentVersion` you specify in the request means
that the specific version's metadata is updated. To find all of the available versions
of your hub content, you can use the [ListHubContentVersions](../APIReference/API_ListHubContentVersions.md "../APIReference/API_ListHubContentVersions.md") API.

```
import boto3
sagemaker_client = boto3.Session(region_name=<AWS-region>).client("sagemaker")

sagemaker_client.update_hub_contents(
    HubName=`<hub-name>`,
    HubContentName=`<resource-content-name>`,
    HubContentType=`<"Model"|"Notebook">`,
    HubContentVersion='1.0.0', # specify the correct version that you want to update
    HubContentDescription=`<updated-description-string>`
)
```

AWS CLI
The following example shows how you can use the AWS CLI to submit an
[update-hub-content](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content.html") request.

```
aws sagemaker update-hub-content \
--hub-name `<hub-name>` \
--hub-content-name `<resource-content-name>` \
--hub-content-type `<"Model"|"Notebook">` \
--hub-content-version "1.0.0" \
--hub-content-description `<updated-description-string>`
```

## Update model references

To update a model reference to a JumpStart model, use the [UpdateHubContentReference](../APIReference/API_UpdateHubContentReference.md "../APIReference/API_UpdateHubContentReference.md") API.

You can only update the `MinVersion` field for model references.

AWS SDK for Python (Boto3)
The following example shows how you can use the AWS SDK for Python (Boto3) to submit
an [UpdateHubContentReference](../APIReference/API_UpdateHubContentReference.md "../APIReference/API_UpdateHubContentReference.md") request.

```
import boto3
sagemaker_client = boto3.Session(region_name=<AWS-region>).client("sagemaker")

update_response = sagemaker_client.update_hub_content_reference(
    HubName=`<hub-name>`,
    HubContentName=`<model-reference-content-name>`,
    HubContentType='ModelReference',
    MinVersion='1.0.0'
)
```

AWS CLI
The following example shows how you can use the AWS CLI to submit an
[update-hub-content-reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content-reference.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content-reference.html") request.

```
aws sagemaker update-hub-content-reference \
 --hub-name `<hub-name>` \
 --hub-content-name `<model-reference-content-name>` \
 --hub-content-type "ModelReference" \
 --min-version "1.0.0"
```
