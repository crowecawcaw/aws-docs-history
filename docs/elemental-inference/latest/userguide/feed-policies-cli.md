

# Managing policies using the CLI
<a name="feed-policies-cli"></a>

You can use the Elemental Inference API to attach, retrieve, and delete feed policies.

## Attaching a policy (PutFeedPolicy)
<a name="feed-policies-cli-put"></a>

Use `PutFeedPolicy` to attach or replace a resource-based policy on a feed. If a policy already exists on the feed, this operation replaces it.

```
aws elemental-inference put-feed-policy \
  --id <{{feed-id}}> \
  --policy '{"Version":"2012-10-17","Statement":[{"Sid":"AllowMediaTailorGetMetadata","Effect":"Allow","Principal":{"Service":"mediatailor.amazonaws.com"},"Action":"elemental-inference:GetMetadata","Resource":"arn:aws:elemental-inference:<{{region}}>:<{{account-id}}>:feed/<{{feed-id}}>","Condition":{"StringEquals":{"aws:SourceAccount":"<{{account-id}}>"},"ArnLike":{"aws:SourceArn":"arn:aws:mediatailor:<{{region}}>:<{{account-id}}>:playbackConfiguration/*"}}}]}'
```

## Retrieving a policy (GetFeedPolicy)
<a name="feed-policies-cli-get"></a>

Use `GetFeedPolicy` to retrieve the resource-based policy attached to a feed.

```
aws elemental-inference get-feed-policy \
  --id <{{feed-id}}>
```

The response contains the JSON policy document:

```
{
    "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"AllowMediaTailorGetMetadata\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"mediatailor.amazonaws.com\"},\"Action\":\"elemental-inference:GetMetadata\",\"Resource\":\"arn:aws:elemental-inference:us-west-2:111122223333:feed/abc123\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:mediatailor:us-west-2:111122223333:playbackConfiguration/*\"}}}]}"
}
```

## Deleting a policy (DeleteFeedPolicy)
<a name="feed-policies-cli-delete"></a>

Use `DeleteFeedPolicy` to remove the resource-based policy from a feed. After you delete the policy, accounts and services that the policy previously authorized can no longer access the feed.

```
aws elemental-inference delete-feed-policy \
  --id <{{feed-id}}>
```