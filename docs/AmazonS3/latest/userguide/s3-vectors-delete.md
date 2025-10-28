# Deleting vectors from a vector index

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can delete specific vectors from a vector index by specifying their vector keys. This operation is useful for removing outdated or incorrect data while
preserving the rest of your vector data.

To delete vectors, use the following example commands. Replace the `user input placeholders` with your own information.

```
aws s3vectors delete-vectors \
 --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
 --index-name "`idx`" \
 --keys '["`vec2`","`vec3`"]'
```
