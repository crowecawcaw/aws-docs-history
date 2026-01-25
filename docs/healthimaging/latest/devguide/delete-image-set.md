# Deleting an image set

Use the `DeleteImageSet` action to delete an [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in HealthImaging. The following menus provide a procedure for the AWS Management Console and code
examples for the AWS CLI and AWS SDKs. For more information, see [`DeleteImageSet`](../APIReference/API_DeleteImageSet.md "../APIReference/API_DeleteImageSet.md") in the _AWS HealthImaging API
Reference_.

###### To delete an image set

Choose a menu based on your access preference to AWS HealthImaging.

1. Open the HealthImaging console [Data stores page](https://console.aws.amazon.com/medical-imaging/home#/dataStores "https://console.aws.amazon.com/medical-imaging/home#/dataStores").
2. Choose a data store.

The **Data store details** page opens and the **Image
sets** tab is selected by default. 3. Choose an image set and choose **Delete**.

The **Delete image set** modal opens. 4. Provide the ID of the image set and choose **Delete image
set**.

C++

**SDK for C++**

```
//! Routine which deletes an AWS HealthImaging image set.
/*!
  \param dataStoreID: The HealthImaging data store ID.
  \param imageSetID: The image set ID.
  \param clientConfig: Aws client configuration.
  \return bool: Function succeeded.
  */
bool AwsDoc::Medical_Imaging::deleteImageSet(
        const Aws::String &dataStoreID, const Aws::String &imageSetID,
        const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::MedicalImaging::MedicalImagingClient client(clientConfig);
    Aws::MedicalImaging::Model::DeleteImageSetRequest request;
    request.SetDatastoreId(dataStoreID);
    request.SetImageSetId(imageSetID);
    Aws::MedicalImaging::Model::DeleteImageSetOutcome outcome = client.DeleteImageSet(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully deleted image set " << imageSetID
                  << " from data store " << dataStoreID << std::endl;
    }
    else {
        std::cerr << "Error deleting image set " << imageSetID << " from data store "
                  << dataStoreID << ": " <<
                  outcome.GetError().GetMessage() << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [DeleteImageSet](../../../goto/SdkForCpp/medical-imaging-2023-07-19/DeleteImageSet.md "../../../goto/SdkForCpp/medical-imaging-2023-07-19/DeleteImageSet.md")
  in _AWS SDK for C++ API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples").

CLI

**AWS CLI**

**To delete an image set**

The following `delete-image-set` code example deletes an image set.

```
`aws medical-imaging delete-image-set \
 --datastore-id `12345678901234567890123456789012` \
 --image-set-id `ea92b0d8838c72a3f25d00d13616f87e``

```

Output:

```
{
    "imageSetWorkflowStatus": "DELETING",
    "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
    "imageSetState": "LOCKED",
    "datastoreId": "12345678901234567890123456789012"
}
```

- For API details, see
  [DeleteImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-image-set.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-image-set.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static void deleteMedicalImageSet(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String imagesetId) {
        try {
            DeleteImageSetRequest deleteImageSetRequest = DeleteImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId)
                    .build();

            medicalImagingClient.deleteImageSet(deleteImageSetRequest);

            System.out.println("The image set was deleted.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [DeleteImageSet](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteImageSet.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteImageSet.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { DeleteImageSetCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} datastoreId - The data store ID.
 * @param {string} imageSetId - The image set ID.
 */
export const deleteImageSet = async (
  datastoreId = "xxxxxxxxxxxxxxxx",
  imageSetId = "xxxxxxxxxxxxxxxx",
) => {
  const response = await medicalImagingClient.send(
    new DeleteImageSetCommand({
      datastoreId: datastoreId,
      imageSetId: imageSetId,
    }),
  );
  console.log(response);
  // {
  //    '$metadata': {
  //         httpStatusCode: 200,
  //         requestId: '6267bbd2-eaa5-4a50-8ee8-8fddf535cf73',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  //     },
  //     datastoreId: 'xxxxxxxxxxxxxxxx',
  //     imageSetId: 'xxxxxxxxxxxxxxx',
  //     imageSetState: 'LOCKED',
  //     imageSetWorkflowStatus: 'DELETING'
  // }
  return response;
};


```

- For API details, see
  [DeleteImageSet](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/DeleteImageSetCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/DeleteImageSetCommand.md")
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


    def delete_image_set(self, datastore_id, image_set_id):
        """
        Delete an image set.

        :param datastore_id: The ID of the data store.
        :param image_set_id: The ID of the image set.
        :return: The delete results.
        """
        try:
            delete_results = self.health_imaging_client.delete_image_set(
                imageSetId=image_set_id, datastoreId=datastore_id
            )
        except ClientError as err:
            logger.error(
                "Couldn't delete image set. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return delete_results



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [DeleteImageSet](../../../goto/boto3/medical-imaging-2023-07-19/DeleteImageSet.md "../../../goto/boto3/medical-imaging-2023-07-19/DeleteImageSet.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

SAP ABAP

**SDK for SAP ABAP**

```
    TRY.
        " iv_datastore_id = '1234567890123456789012345678901234567890'
        " iv_image_set_id = '1234567890123456789012345678901234567890'
        oo_result = lo_mig->deleteimageset(
          iv_datastoreid = iv_datastore_id
          iv_imagesetid = iv_image_set_id ).
        MESSAGE 'Image set deleted.' TYPE 'I'.
      CATCH /aws1/cx_migaccessdeniedex.
        MESSAGE 'Access denied.' TYPE 'I'.
      CATCH /aws1/cx_migconflictexception.
        MESSAGE 'Conflict error.' TYPE 'I'.
      CATCH /aws1/cx_miginternalserverex.
        MESSAGE 'Internal server error.' TYPE 'I'.
      CATCH /aws1/cx_migresourcenotfoundex.
        MESSAGE 'Image set not found.' TYPE 'I'.
      CATCH /aws1/cx_migthrottlingex.
        MESSAGE 'Request throttled.' TYPE 'I'.
      CATCH /aws1/cx_migvalidationex.
        MESSAGE 'Validation error.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [DeleteImageSet](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
