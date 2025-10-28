# Tagging collections (AWS CLI)

To tag a collection using the AWS CLI, send a [TagResource](../ServerlessAPIReference/API_TagResource.md "../ServerlessAPIReference/API_TagResource.md") request:

```
aws opensearchserverless tag-resource
  --resource-arn arn:aws:aoss:`us-east-1`:`123456789012`:collection/`my-collection`
  --tags Key=`service`,Value=`aoss` Key=`source`,Value=`logs`
```

View the existing tags for a collection with the [ListTagsForResource](../ServerlessAPIReference/API_ListTagsForResource.md "../ServerlessAPIReference/API_ListTagsForResource.md") command:

```
aws opensearchserverless list-tags-for-resource
  --resource-arn arn:aws:aoss:`us-east-1`:`123456789012`:collection/`my-collection`
```

Remove tags from a collection using the [UntagResource](../ServerlessAPIReference/API_UntagResource.md "../ServerlessAPIReference/API_UntagResource.md") command:

```
aws opensearchserverless untag-resource
  --resource-arn arn:aws:aoss:`us-east-1`:`123456789012`:collection/`my-collection`
  --tag-keys `service`
```
