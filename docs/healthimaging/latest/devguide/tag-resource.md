

# Tagging a resource
<a name="tag-resource"></a>

Use the [`TagResource`](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_TagResource.html) action to tag [data stores](getting-started-concepts.md#concept-data-store) and [image sets](getting-started-concepts.md#concept-image-set) in AWS HealthImaging. The following code examples describe how to use the `TagResource` action with the AWS Management Console, AWS CLI, and AWS SDKs. For more information, see [ Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *AWS General Reference Guide*.

**To tag a resource**  
Choose a menu based on your access preference to AWS HealthImaging.

## AWS Console
<a name="code-example-console-tag-resource"></a>

1. Open the HealthImaging console [Data stores page](https://console.aws.amazon.com/medical-imaging/home#/dataStores).

1. Choose a data store.

   The **Data store details** page opens.

1. Choose the **Details** tab.

1. Under the **Tags** section, choose **Manage tags**.

   The **Manage tags** page opens.

1. Choose **Add new tag**.

1. Enter a **Key** and **Value** (optional).

1. Choose **Save changes**.

## AWS CLI and SDKs
<a name="code-example-cli-sdk-tag-resource"></a>

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To tag a data store**  
The following `tag-resource` code examples tags a data store.  

```
aws medical-imaging tag-resource \
  --resource-arn {{"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"}} \
  --tags '{{{"Deployment":"Development"}}}'
```
This command produces no output.  
**Example 2: To tag an image set**  
The following `tag-resource` code examples tags an image set.  

```
aws medical-imaging tag-resource \
    --resource-arn {{"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"}} \
    --tags '{{{"Deployment":"Development"}}}'
```
This command produces no output.  
  
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/tag-resource.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  

```
    public static void tagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Map<String, String> tags) {
        try {
            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tags(tags)
                    .build();

            medicalImagingClient.tagResource(tagResourceRequest);

            System.out.println("Tags have been added to the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/TagResource) in *AWS SDK for Java 2.x API Reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples). 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  

```
import { TagResourceCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} resourceArn - The Amazon Resource Name (ARN) for the data store or image set.
 * @param {Record<string,string>} tags - The tags to add to the resource as JSON.
 *                     - For example: {"Deployment" : "Development"}
 */
export const tagResource = async (
  resourceArn = "arn:aws:medical-imaging:us-east-1:xxxxxx:datastore/xxxxx/imageset/xxx",
  tags = {},
) => {
  const response = await medicalImagingClient.send(
    new TagResourceCommand({ resourceArn: resourceArn, tags: tags }),
  );
  console.log(response);
  // {
  //     '$metadata': {
  //        httpStatusCode: 204,
  //         requestId: '8a6de9a3-ec8e-47ef-8643-473518b19d45',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  //    }
  // }

  return response;
};
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/TagResourceCommand) in *AWS SDK for JavaScript API Reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples). 

------
#### [ Python ]

**SDK for Python (Boto3)**  

```
class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client


    def tag_resource(self, resource_arn, tags):
        """
        Tag a resource.

        :param resource_arn: The ARN of the resource.
        :param tags: The tags to apply.
        """
        try:
            self.health_imaging_client.tag_resource(resourceArn=resource_arn, tags=tags)
        except ClientError as err:
            logger.error(
                "Couldn't tag resource. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
The following code instantiates the MedicalImagingWrapper object.   

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/TagResource) in *AWS SDK for Python (Boto3) API Reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples). 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  

```
    TRY.
        " iv_resource_arn = 'arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012'
        lo_mig->tagresource(
          iv_resourcearn = iv_resource_arn
          it_tags = it_tags ).
        MESSAGE 'Resource tagged successfully.' TYPE 'I'.
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
+  For API details, see [TagResource](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples). 

------

**Example availability**  
Can't find what you need? Request a code example using the **Provide feedback** link on the right sidebar of this page.