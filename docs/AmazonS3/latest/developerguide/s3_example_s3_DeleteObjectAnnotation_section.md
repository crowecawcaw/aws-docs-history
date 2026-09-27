

# Use `DeleteObjectAnnotation` with an AWS SDK
<a name="s3_example_s3_DeleteObjectAnnotation_section"></a>

The following code example shows how to use `DeleteObjectAnnotation`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Manage object annotations](s3_example_s3_Scenario_ObjectAnnotations_section.md) 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/object_annotations#code-examples). 

```
    def delete_object_annotation(
        self,
        bucket_name: str,
        object_key: str,
        annotation_name: str,
    ) -> None:
        """
        Permanently deletes a specific annotation from an S3 object.

        :param bucket_name: The name of the bucket containing the object.
        :param object_key: The key of the object.
        :param annotation_name: The name of the annotation to delete.
        :raises ClientError: If the annotation does not exist
                             (NoSuchAnnotation) or another error occurs.
        """
        try:
            self.s3_client.delete_object_annotation(
                Bucket=bucket_name,
                Key=object_key,
                AnnotationName=annotation_name,
            )
            logger.info(
                "Deleted annotation '%s' from object '%s' in bucket '%s'.",
                annotation_name,
                object_key,
                bucket_name,
            )
        except ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchAnnotation":
                logger.error(
                    "Annotation '%s' has already been deleted or does not exist "
                    "on object '%s' in bucket '%s'.",
                    annotation_name,
                    object_key,
                    bucket_name,
                )
            raise
```
+  For API details, see [DeleteObjectAnnotation](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/DeleteObjectAnnotation) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.