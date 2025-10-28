# Getting image set pixel data

An [image frame](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") is the pixel data that exists
within an image set to make up a 2D medical image. Use the `GetImageFrame` action
to retrieve an HTJ2K-encoded image frame for a given [image
set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in HealthImaging. The following menus provide code examples for the AWS CLI and AWS
SDKs. For more information, see [`GetImageFrame`](../APIReference/API_GetImageFrame.md "../APIReference/API_GetImageFrame.md") in the _AWS HealthImaging API
Reference_.

###### Note

Keep the following points in mind when using the `GetImageFrame`
action:

- During [import](importing-imaging-data.md "importing-imaging-data.md"), HealthImaging retains
  encoding for some transfer syntaxes, but transcodes others to HTJ2K lossless by
  default. Therefore, image frames must be decoded prior to viewing in an image
  viewer. For more information, see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md") and [HTJ2K decoding libraries](reference-htj2k.md "reference-htj2k.md").
- For instances stored in HealthImaging with one or more image frames encoded
  in the MPEG family of Transfer Syntaxes (which includes MPEG2, MPEG-4 AVC/H.264
  and HEVC/H.265) the `GetImageFrame` action will return a video object
  in the [stored transfer syntax](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md").
- The `GetImageFrame` action returns the image frame in the stored
  transfer syntax of the instance by default. For more information, see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md").
- You can also use `GetDICOMInstanceFrames`, HealthImaging's representation
  of a DICOMweb service, to retrieve DICOM instance frames (`multipart`
  request) for DICOMweb-compatible viewers and applications. For more information,
  see [Getting DICOM instance frames from
  HealthImaging](dicomweb-retrieve-instance-frames.md "dicomweb-retrieve-instance-frames.md").

###### To get image set pixel data

Choose a menu based on your access preference to AWS HealthImaging.

###### Note

Image frames must be accessed and decoded programmatically, as an image viewer
is not available in the AWS Management Console.

For more information about decoding and viewing image frames, see [HTJ2K decoding libraries](reference-htj2k.md "reference-htj2k.md").

C++

**SDK for C++**

```
//! Routine which downloads an AWS HealthImaging image frame.
/*!
  \param dataStoreID: The HealthImaging data store ID.
  \param imageSetID: The image set ID.
  \param frameID: The image frame ID.
  \param jphFile: File to store the downloaded frame.
  \param clientConfig: Aws client configuration.
  \return bool: Function succeeded.
*/
bool AwsDoc::Medical_Imaging::getImageFrame(const Aws::String &dataStoreID,
                                            const Aws::String &imageSetID,
                                            const Aws::String &frameID,
                                            const Aws::String &jphFile,
                                            const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::MedicalImaging::MedicalImagingClient client(clientConfig);

    Aws::MedicalImaging::Model::GetImageFrameRequest request;
    request.SetDatastoreId(dataStoreID);
    request.SetImageSetId(imageSetID);

    Aws::MedicalImaging::Model::ImageFrameInformation imageFrameInformation;
    imageFrameInformation.SetImageFrameId(frameID);
    request.SetImageFrameInformation(imageFrameInformation);

    Aws::MedicalImaging::Model::GetImageFrameOutcome outcome = client.GetImageFrame(
            request);

    if (outcome.IsSuccess()) {
        std::cout << "Successfully retrieved image frame." << std::endl;
        auto &buffer = outcome.GetResult().GetImageFrameBlob();

        std::ofstream outfile(jphFile, std::ios::binary);
        outfile << buffer.rdbuf();
    }
    else {
        std::cout << "Error retrieving image frame." << outcome.GetError().GetMessage()
                  << std::endl;

    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [GetImageFrame](../../../goto/SdkForCpp/medical-imaging-2023-07-19/GetImageFrame.md "../../../goto/SdkForCpp/medical-imaging-2023-07-19/GetImageFrame.md")
  in _AWS SDK for C++ API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples").

CLI

**AWS CLI**

**To get image set pixel data**

The following `get-image-frame` code example gets an image frame.

```
`aws medical-imaging get-image-frame \
 --datastore-id `"12345678901234567890123456789012"` \
 --image-set-id `"98765412345612345678907890789012"` \
 --image-frame-information `imageFrameId=3abf5d5d7ae72f80a0ec81b2c0de3ef4` \
 `imageframe.jph``

```

Note:
This code example does not include output because the GetImageFrame action returns a stream of pixel data to the imageframe.jph file. For information about decoding and viewing image frames, see HTJ2K decoding libraries.

- For API details, see
  [GetImageFrame](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-frame.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-frame.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
        public static void getMedicalImageSetFrame(MedicalImagingClient medicalImagingClient,
                        String destinationPath,
                        String datastoreId,
                        String imagesetId,
                        String imageFrameId) {

                try {
                        GetImageFrameRequest getImageSetMetadataRequest = GetImageFrameRequest.builder()
                                        .datastoreId(datastoreId)
                                        .imageSetId(imagesetId)
                                        .imageFrameInformation(ImageFrameInformation.builder()
                                                        .imageFrameId(imageFrameId)
                                                        .build())
                                        .build();
                        medicalImagingClient.getImageFrame(getImageSetMetadataRequest,
                                        FileSystems.getDefault().getPath(destinationPath));

                        System.out.println("Image frame downloaded to " + destinationPath);
                } catch (MedicalImagingException e) {
                        System.err.println(e.awsErrorDetails().errorMessage());
                        System.exit(1);
                }
        }


```

- For API details, see
  [GetImageFrame](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageFrame.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageFrame.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { GetImageFrameCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} imageFrameFileName - The name of the file for the HTJ2K-encoded image frame.
 * @param {string} datastoreID - The data store's ID.
 * @param {string} imageSetID - The image set's ID.
 * @param {string} imageFrameID - The image frame's ID.
 */
export const getImageFrame = async (
  imageFrameFileName = "image.jph",
  datastoreID = "DATASTORE_ID",
  imageSetID = "IMAGE_SET_ID",
  imageFrameID = "IMAGE_FRAME_ID",
) => {
  const response = await medicalImagingClient.send(
    new GetImageFrameCommand({
      datastoreId: datastoreID,
      imageSetId: imageSetID,
      imageFrameInformation: { imageFrameId: imageFrameID },
    }),
  );
  const buffer = await response.imageFrameBlob.transformToByteArray();
  writeFileSync(imageFrameFileName, buffer);

  console.log(response);
  // {
  //     '$metadata': {
  //         httpStatusCode: 200,
  //         requestId: 'e4ab42a5-25a3-4377-873f-374ecf4380e1',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  //     },
  //     contentType: 'application/octet-stream',
  //     imageFrameBlob: <ref *1> IncomingMessage {}
  // }
  return response;
};


```

- For API details, see
  [GetImageFrame](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/GetImageFrameCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/GetImageFrameCommand.md")
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


    def get_pixel_data(
        self, file_path_to_write, datastore_id, image_set_id, image_frame_id
    ):
        """
        Get an image frame's pixel data.

        :param file_path_to_write: The path to write the image frame's HTJ2K encoded pixel data.
        :param datastore_id: The ID of the data store.
        :param image_set_id: The ID of the image set.
        :param image_frame_id: The ID of the image frame.
        """
        try:
            image_frame = self.health_imaging_client.get_image_frame(
                datastoreId=datastore_id,
                imageSetId=image_set_id,
                imageFrameInformation={"imageFrameId": image_frame_id},
            )
            with open(file_path_to_write, "wb") as f:
                for chunk in image_frame["imageFrameBlob"].iter_chunks():
                    if chunk:
                        f.write(chunk)
        except ClientError as err:
            logger.error(
                "Couldn't get image frame. Here's why: %s: %s",
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

- For API details, see
  [GetImageFrame](../../../goto/boto3/medical-imaging-2023-07-19/GetImageFrame.md "../../../goto/boto3/medical-imaging-2023-07-19/GetImageFrame.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
