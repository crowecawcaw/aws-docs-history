# Add tags to an existing stream processor

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a
user-defined key and value.

To add one or more tags to an existing stream processor, use the `TagResource` operation.
Specify the stream processor's Amazon Resource Name (ARN) (`ResourceArn`) and the tags (`Tags`) that you want to add. The following example shows how to add two tags.

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'

```

###### Note

If you do not know the stream processor's Amazon Resource Name, you can use the `DescribeStreamProcessor` operation.
