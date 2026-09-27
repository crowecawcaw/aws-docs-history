

# Use `ListObjectAnnotations` with an AWS SDK
<a name="s3_example_s3_ListObjectAnnotations_section"></a>

The following code example shows how to use `ListObjectAnnotations`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Manage object annotations](s3_example_s3_Scenario_ObjectAnnotations_section.md) 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/s3/scenarios/object_annotations#code-examples). 

```
    def list_object_annotations(
        self,
        bucket_name: str,
        object_key: str,
        annotation_prefix: Optional[str] = None,
    ) -> list:
        """
        Lists annotations attached to an S3 object. Uses a paginator to
        handle results that span multiple pages.

        :param bucket_name: The name of the bucket containing the object.
        :param object_key: The key of the object.
        :param annotation_prefix: Optional prefix to filter annotation names.
        :return: A list of annotation entry dicts, each containing
                 AnnotationName, Size, ETag, and LastModified.
        :raises ClientError: If the object does not exist (NoSuchKey) or
                             another error occurs.
        """
        try:
            annotations = list()
            paginator = self.s3_client.get_paginator("list_object_annotations")
            params = dict(Bucket=bucket_name, Key=object_key)
            if annotation_prefix is not None:
                params["AnnotationPrefix"] = annotation_prefix
            for page in paginator.paginate(**params):
                page_annotations = page.get("Annotations", list())
                for annotation in page_annotations:
                    annotations.append(
                        dict(
                            AnnotationName=annotation.get("AnnotationName", ""),
                            Size=annotation.get("Size", 0),
                            ETag=annotation.get("ETag", ""),
                            LastModified=annotation.get("LastModified", None),
                        )
                    )
            logger.info(
                "Listed %d annotation(s) on object '%s' in bucket '%s'%s.",
                len(annotations),
                object_key,
                bucket_name,
                f" with prefix '{annotation_prefix}'" if annotation_prefix else "",
            )
            return annotations
        except ClientError as err:
            if err.response["Error"]["Code"] == "NoSuchKey":
                logger.error(
                    "Object '%s' does not exist in bucket '%s'.",
                    object_key,
                    bucket_name,
                )
            raise
```
+  For API details, see [ListObjectAnnotations](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/ListObjectAnnotations) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.