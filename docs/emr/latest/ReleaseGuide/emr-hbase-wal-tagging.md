# Tagging WAL workspaces

You can add tags to a workspace when you create a new workspace and you can add,
remove, or list tags from an active workspace for a running cluster. You can't tag the
individual resources in the workspace, and you can't update existing tags; instead,
remove unwanted tags from the workspace and replace them.

You can tag workspaces from the EMRWAL CLI. For a list of EMRWAL CLI commands for
tagging workspaces, see [Amazon EMR WAL (EMRWAL) CLI reference](emrwalcli-ref.md "emrwalcli-ref.md").

The following example IAM policy illustrates a scenario that allows workspace CRUDL
operations only with the proper tagging key `resource_tag_allow_test_key` and
value `resource_tag_allow_test_value`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:ListBucket"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/resource_tag_allow_test_key": [
 "resource_tag_allow_test_value"
 ]
 }
 },
 "Sid": "AllowEMRWAL"
 }
 ]
}`

```

To verify that the tag is now required for workspace operations, use the [Amazon EMR WAL (EMRWAL) CLI reference](emrwalcli-ref.md "emrwalcli-ref.md") to call the [listTagsForResource](emrwalcli-ref.md#emrwalcli-ref-listtagsforresource "emrwalcli-ref.md#emrwalcli-ref-listtagsforresource")
command on `tagAllowResourceTag` for the workspace with the desired resource
tag. If you configured the condition correctly, the command will succeed.

```
emrwal listTagsForResource -r us-east-1 -arn arn:aws:emrwal:us-east-1:`arn`:workspace/tagAllowResourceTag
Tag(Key=resource_tag_allow_test_key, Value=resource_tag_allow_test_value)
```
