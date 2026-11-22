

# Tagging Amazon Textract Insights resources

To help you manage your Amazon Textract Insights resources, you can assign metadata to them as tags. A tag is a label that you assign to an AWS resource. Each tag consists of a key and a value. You can tag projects, blueprints, and jobs.

Tags help you do the following:
+ **Identify and organize your resources.** Categorize projects, blueprints, and jobs by purpose, owner, environment, or application. Many AWS services support tagging, so you can apply the same tag across services to show that resources belong together.
+ **Control access to your resources.** Use tags in IAM policies to allow or deny actions on Amazon Textract Insights resources based on their tags (attribute-based access control, or ABAC).

For tagging best practices, see the AWS tagging best-practices guidance.

Before you begin, install and configure the AWS CLI or an AWS SDK. See [Prerequisites and setup](insights-prerequisites.md).

## Taggable resources
<a name="insights-tagging-taggable"></a>

You can tag the following Amazon Textract Insights resources.


**Taggable Amazon Textract Insights resources**  

| **Resource** | **ARN format** | **Tag at creation** | **Tag after creation** | 
| --- | --- | --- | --- | 
| Blueprint | `arn:aws:textract:<region>:<account-id>:blueprint/<blueprint-id>` | `CreateBlueprint` | `TagResource` | 
| Project | `arn:aws:textract:<region>:<account-id>:project/<project-id>` | `CreateProject` | `TagResource` | 
| Job | `arn:aws:textract:<region>:<account-id>:job/<job-id>` | `StartDocumentInsights` | `TagResource` | 

Note the following:
+ Tags apply to a blueprint as a whole. You can't tag an individual blueprint version, and `CreateBlueprintVersion` doesn't accept tags.
+ You can't tag public blueprints, such as `arn:aws:textract:us-east-1:aws:blueprint/public-w2-form`, because AWS owns them.
+ A job doesn't inherit tags from its project or blueprints. To tag a job, pass `--tags` when you start it, or call `TagResource` on the job ARN afterward.
+ `UpdateProject` and `UpdateBlueprint` don't change tags. Use `TagResource` and `UntagResource`.
+ `GetProject`, `GetBlueprint`, and `GetDocumentInsights` don't return tags. Use `ListTagsForResource`.
+ You can tag only resources in your own account and in the AWS Region you call.
+ If you delete a resource, any tags associated with the resource are also deleted.

## Tag a resource when you create it
<a name="insights-tagging-create"></a>

Pass `--tags` as a map of key-value pairs.

**Project**

```bash
aws textract create-project \
  --region us-east-1 \
  --project-name "invoice-processing" \
  --extraction-configuration '{"BoundingBox": {"State": "DISABLED"}, "Granularity": {"Types": ["PAGE"]}, "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}}' \
  --custom-configuration '{"Blueprints": [{"BlueprintArn": "arn:aws:textract:us-east-1:aws:blueprint/public-invoice"}]}' \
  --tags '{"Team": "finance", "Environment": "production"}'
```

**Blueprint**

```bash
aws textract create-blueprint \
  --region us-east-1 \
  --blueprint-name "my-invoice-blueprint" \
  --schema file://invoice-schema.json \
  --tags '{"Team": "finance", "Environment": "production"}'
```

**Job**

```bash
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --tags '{"Team": "finance", "Workflow": "accounts-payable"}'
```

Tagging a resource when you create it requires the `textract:TagResource` permission in addition to the create permission. See [Required permissions](#insights-tagging-permissions).

## Manage tags on an existing resource
<a name="insights-tagging-manage"></a>

Use `TagResource`, `ListTagsForResource`, and `UntagResource` with the resource ARN.

**Add or update tags**

If a tag key already exists on the resource, `TagResource` replaces its value.

```bash
aws textract tag-resource \
  --region us-east-1 \
  --resource-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --tags '{"Owner": "doc-platform-team"}'
```

**List tags**

```bash
aws textract list-tags-for-resource \
  --region us-east-1 \
  --resource-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"
```

```json
{
  "Tags": {
    "Team": "finance",
    "Environment": "production",
    "Owner": "doc-platform-team"
  }
}
```

**Remove tags**

Specify the keys of the tags to remove.

```bash
aws textract untag-resource \
  --region us-east-1 \
  --resource-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --tag-keys Owner Environment
```

**Python (boto3)**

```python
import boto3

textract = boto3.client("textract", region_name="us-east-1")
project_arn = "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh"

# Add or update tags
textract.tag_resource(ResourceARN=project_arn, Tags={"Team": "finance", "Environment": "production"})

# List tags
print(textract.list_tags_for_resource(ResourceARN=project_arn)["Tags"])

# Remove tags
textract.untag_resource(ResourceARN=project_arn, TagKeys=["Environment"])
```

**Note**  
When you view these operations in AWS CloudTrail, you can identify the resource being tagged by checking the request parameters in the event details.

## Control access with tags
<a name="insights-tagging-access"></a>

You can use the following condition keys in IAM policies for Amazon Textract Insights resources.


**Tag condition keys for Amazon Textract Insights**  

| **Condition key** | **Use it to** | 
| --- | --- | 
| `aws:ResourceTag/<key>` | Allow or deny actions based on the tags already on a project, blueprint, or job. | 
| `aws:RequestTag/<key>` | Require or restrict specific tag values in a request that creates or tags a resource. | 
| `aws:TagKeys` | Control which tag keys a request can include. | 

For examples of tag-based policies, see the IAM User Guide.

## Required permissions
<a name="insights-tagging-permissions"></a>

Tagging operations require the following permissions.


**Permissions for tagging operations**  

| **Action** | **Required for** | 
| --- | --- | 
| `textract:TagResource` | Calling `TagResource`. Also required when you pass `Tags` to `CreateProject`, `CreateBlueprint`, or `StartDocumentInsights`. Not required when you create a resource without tags. | 
| `textract:UntagResource` | Calling `UntagResource`. | 
| `textract:ListTagsForResource` | Calling `ListTagsForResource`. | 

Add these actions to the policy in [Data protection and encryption](insights-data-protection.md) if your workflow uses tags.

## Tag restrictions
<a name="insights-tagging-restrictions"></a>

Amazon Textract Insights tags have the following restrictions.


**Tag restrictions**  

| **Restriction** | **Value** | 
| --- | --- | 
| Maximum user tags per resource | 50 | 
| Tag key length | 1–128 characters | 
| Tag value length | 0–256 characters | 
| Allowed characters | Unicode letters, numbers, and spaces, plus `_ . : / = + - @` | 
| Reserved prefix | Tag keys can't begin with `aws:`. You can't add, change, or remove tags with this prefix. | 

Tag keys and values are case sensitive.

## Next steps
<a name="insights-tagging-next-steps"></a>

To set up IAM for your workflow, see [Data protection and encryption](insights-data-protection.md) and [Prerequisites and setup](insights-prerequisites.md).

For request parameters and errors, see the Amazon Textract Insights API Reference