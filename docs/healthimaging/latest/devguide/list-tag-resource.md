# Listing tags for a resource

Use the [`ListTagsForResource`](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") action to list tags for [data stores](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") and [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in AWS HealthImaging. The following code examples describe how to use the
`ListTagsForResource` action with the AWS Management Console, AWS CLI, and AWS SDKs. For
more information, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in
the _AWS General Reference Guide_.

###### To list tags for a resource

Choose a menu based on your access preference to AWS HealthImaging.

1. Open the HealthImaging console [Data stores page](https://console.aws.amazon.com/medical-imaging/home#/dataStores "https://console.aws.amazon.com/medical-imaging/home#/dataStores").
2. Choose a data store.

The **Data store details** page opens. 3. Choose the **Details** tab.

Under the **Tags** section, all data store tags are
listed.

CLI

**AWS CLI**

**Example 1: To list resource tags for a data store**

The following `list-tags-for-resource` code example lists tags for a data store.

```
`aws medical-imaging list-tags-for-resource \
 --resource-arn `"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"``

```

Output:

```
{
    "tags":{
        "Deployment":"Development"
    }
}
```

**Example 2: To list resource tags for an image set**

The following `list-tags-for-resource` code example lists tags for an image set.

```
`aws medical-imaging list-tags-for-resource \
 --resource-arn `"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"``

```

Output:

```
{
    "tags":{
        "Deployment":"Development"
    }
}
```

- For API details, see
  [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-tags-for-resource.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static ListTagsForResourceResponse listMedicalImagingResourceTags(MedicalImagingClient medicalImagingClient,
            String resourceArn) {
        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .build();

            return medicalImagingClient.listTagsForResource(listTagsForResourceRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }


```

- For API details, see
  [ListTagsForResource](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/ListTagsForResource.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/ListTagsForResource.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { ListTagsForResourceCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} resourceArn - The Amazon Resource Name (ARN) for the data store or image set.
 */
export const listTagsForResource = async (
  resourceArn = "arn:aws:medical-imaging:us-east-1:abc:datastore/def/imageset/ghi",
) => {
  const response = await medicalImagingClient.send(
    new ListTagsForResourceCommand({ resourceArn: resourceArn }),
  );
  console.log(response);
  // {
  //     '$metadata': {
  //         httpStatusCode: 200,
  //         requestId: '008fc6d3-abec-4870-a155-20fa3631e645',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  //     },
  //     tags: { Deployment: 'Development' }
  // }

  return response;
};


```

- For API details, see
  [ListTagsForResource](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/ListTagsForResourceCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/ListTagsForResourceCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples").

Python

**SDK for Python (Boto3)**

```
class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client


    def list_tags_for_resource(self, resource_arn):
        """
        List the tags for a resource.

        :param resource_arn: The ARN of the resource.
        :return: The list of tags.
        """
        try:
            tags = self.health_imaging_client.list_tags_for_resource(
                resourceArn=resource_arn
            )
        except ClientError as err:
            logger.error(
                "Couldn't list tags for resource. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return tags["tags"]



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [ListTagsForResource](../../../goto/boto3/medical-imaging-2023-07-19/ListTagsForResource.md "../../../goto/boto3/medical-imaging-2023-07-19/ListTagsForResource.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

SAP ABAP

**SDK for SAP ABAP**

```
    TRY.
        " iv_resource_arn = 'arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012'
        oo_result = lo_mig->listtagsforresource( iv_resourcearn = iv_resource_arn ).
        DATA(lt_tags) = oo_result->get_tags( ).
        DATA(lv_count) = lines( lt_tags ).
        MESSAGE |Found { lv_count } tags for resource.| TYPE 'I'.
      CATCH /aws1/cx_migaccessdeniedex.
        MESSAGE 'Access denied.' TYPE 'I'.
      CATCH /aws1/cx_miginternalserverex.
        MESSAGE 'Internal server error.' TYPE 'I'.
      CATCH /aws1/cx_migresourcenotfoundex.
        MESSAGE 'Resource not found.' TYPE 'I'.
      CATCH /aws1/cx_migthrottlingex.
        MESSAGE 'Request throttled.' TYPE 'I'.
      CATCH /aws1/cx_migvalidationex.
        MESSAGE 'Validation error.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [ListTagsForResource](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
