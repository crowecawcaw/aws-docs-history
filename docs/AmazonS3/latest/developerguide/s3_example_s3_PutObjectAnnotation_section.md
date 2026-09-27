

# Use `PutObjectAnnotation` with an AWS SDK
<a name="s3_example_s3_PutObjectAnnotation_section"></a>

The following code example shows how to use `PutObjectAnnotation`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Manage object annotations](s3_example_s3_Scenario_ObjectAnnotations_section.md) 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/object_annotations#code-examples). 

```
    def put_object_annotation(
        self,
        bucket_name: str,
        object_key: str,
        annotation_name: str,
        annotation_payload: str,
    ) -> dict:
        """
        Attaches a named annotation payload to an S3 object.

        :param bucket_name: The name of the bucket containing the object.
        :param object_key: The key of the object to annotate.
        :param annotation_name: The name of the annotation (1-512 bytes).
        :param annotation_payload: The annotation content (1 byte to 1 MiB).
        :return: A dict containing the PutObjectAnnotation response with ETag.
        :raises ClientError: If the annotation name is invalid
                             (InvalidAnnotationName) or another error occurs.
        """
        try:
            response = self.s3_client.put_object_annotation(
                Bucket=bucket_name,
                Key=object_key,
                AnnotationName=annotation_name,
                AnnotationPayload=annotation_payload.encode("utf-8"),
            )
            logger.info(
                "Put annotation '%s' on object '%s' in bucket '%s'. ETag: %s",
                annotation_name,
                object_key,
                bucket_name,
                response.get("ETag", "N/A"),
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidAnnotationName":
                logger.error(
                    "Annotation name '%s' is invalid. Names must be 1-512 bytes, "
                    "UTF-8 encoded, and cannot start with 'aws' or 's3'.",
                    annotation_name,
                )
            raise
```
+  For API details, see [PutObjectAnnotation](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutObjectAnnotation) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.