

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Manage network tags with the
<a name="manage-network-tags-cli"></a>

Use the following commands to manage tags. Replace the example network ARN and tag values with your own.

To add or update tags, use the `tag-resource` command:

```
aws wickr tag-resource \
    --arn arn:aws:wickr:us-east-1:123456789012:network/12345678 \
    --tags '{"Environment":"production","Owner":"security"}'
```

To remove tags, use the `untag-resource` command:

```
aws wickr untag-resource \
    --arn arn:aws:wickr:us-east-1:123456789012:network/12345678 \
    --tag-keys Environment Owner
```

To list tags, use the `list-tags-for-resource` command:

```
aws wickr list-tags-for-resource \
    --arn arn:aws:wickr:us-east-1:123456789012:network/12345678
```

You can add tags when you create a network by specifying the `--tags` option with the `create-network` command:

```
aws wickr create-network \
    --network-name example-network \
    --access-level STANDARD \
    --tags '{"Environment":"production","Owner":"security"}'
```