# Getting image set properties

Use the `GetImageSet` action to return properties for a given [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in HealthImaging. The following menus provide a
procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more
information, see [`GetImageSet`](../APIReference/API_GetImageSet.md "../APIReference/API_GetImageSet.md") in the _AWS HealthImaging API
Reference_.

###### Note

By default, AWS HealthImaging returns properties for the latest version of an image set. To
view properties for an older version of an image set, provide the `versionId`
with your request.

Use `GetDICOMInstance`, HealthImaging's representation of a DICOMweb service, to
return a DICOM instance binary (`.dcm` file). For more information, see [Getting a DICOM instance from HealthImaging](dicomweb-retrieve-instance.md "dicomweb-retrieve-instance.md").

###### To get image set properties

Choose a menu based on your access preference to AWS HealthImaging.

1. Open the HealthImaging console [Data stores page](https://console.aws.amazon.com/medical-imaging/home#/dataStores "https://console.aws.amazon.com/medical-imaging/home#/dataStores").
2. Choose a data store.

The **Data store details** page opens and the
**Image sets** tab is selected by default. 3. Choose an image set.

The **Image set details** page opens and displays image
set properties.

CLI

**AWS CLI**

**To get image set properties**

The following `get-image-set` code example gets the properties for an image set.

```
`aws medical-imaging get-image-set \
 --datastore-id `12345678901234567890123456789012` \
 --image-set-id `18f88ac7870584f58d56256646b4d92b` \
 --version-id `1``

```

Output:

```
{
    "versionId": "1",
    "imageSetWorkflowStatus": "COPIED",
    "updatedAt": 1680027253.471,
    "imageSetId": "18f88ac7870584f58d56256646b4d92b",
    "imageSetState": "ACTIVE",
    "createdAt": 1679592510.753,
    "datastoreId": "12345678901234567890123456789012"
}
```

- For API details, see
  [GetImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static GetImageSetResponse getMedicalImageSet(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String imagesetId,
            String versionId) {
        try {
            GetImageSetRequest.Builder getImageSetRequestBuilder = GetImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId);

            if (versionId != null) {
                getImageSetRequestBuilder = getImageSetRequestBuilder.versionId(versionId);
            }

            return medicalImagingClient.getImageSet(getImageSetRequestBuilder.build());
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }


```

- For API details, see
  [GetImageSet](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSet.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSet.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { GetImageSetCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} datastoreId - The ID of the data store.
 * @param {string} imageSetId - The ID of the image set.
 * @param {string} imageSetVersion - The optional version of the image set.
 *
 */
export const getImageSet = async (
  datastoreId = "xxxxxxxxxxxxxxx",
  imageSetId = "xxxxxxxxxxxxxxx",
  imageSetVersion = "",
) => {
  const params = { datastoreId: datastoreId, imageSetId: imageSetId };
  if (imageSetVersion !== "") {
    params.imageSetVersion = imageSetVersion;
  }
  const response = await medicalImagingClient.send(
    new GetImageSetCommand(params),
  );
  console.log(response);
  // {
  //     '$metadata': {
  //     httpStatusCode: 200,
  //         requestId: '0615c161-410d-4d06-9d8c-6e1241bb0a5a',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  // },
  //     createdAt: 2023-09-22T14:49:26.427Z,
  //     datastoreId: 'xxxxxxxxxxxxxxx',
  //     imageSetArn: 'arn:aws:medical-imaging:us-east-1:xxxxxxxxxx:datastore/xxxxxxxxxxxxxxxxxxxx/imageset/xxxxxxxxxxxxxxxxxxxx',
  //     imageSetId: 'xxxxxxxxxxxxxxx',
  //     imageSetState: 'ACTIVE',
  //     imageSetWorkflowStatus: 'CREATED',
  //     updatedAt: 2023-09-22T14:49:26.427Z,
  //     versionId: '1'
  // }

  return response;
};



```

- For API details, see
  [GetImageSet](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/GetImageSetCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/GetImageSetCommand.md")
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


    def get_image_set(self, datastore_id, image_set_id, version_id=None):
        """
        Get the properties of an image set.

        :param datastore_id: The ID of the data store.
        :param image_set_id: The ID of the image set.
        :param version_id: The optional version of the image set.
        :return: The image set properties.
        """
        try:
            if version_id:
                image_set = self.health_imaging_client.get_image_set(
                    imageSetId=image_set_id,
                    datastoreId=datastore_id,
                    versionId=version_id,
                )
            else:
                image_set = self.health_imaging_client.get_image_set(
                    imageSetId=image_set_id, datastoreId=datastore_id
                )
        except ClientError as err:
            logger.error(
                "Couldn't get image set. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return image_set



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [GetImageSet](../../../goto/boto3/medical-imaging-2023-07-19/GetImageSet.md "../../../goto/boto3/medical-imaging-2023-07-19/GetImageSet.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
