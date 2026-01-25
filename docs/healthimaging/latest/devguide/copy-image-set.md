# Copying an image set

Use the `CopyImageSet` action to copy an [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in HealthImaging. You use this asynchronous process to copy the contents of an
image set into a new or existing image set. You can copy into a _new_
image set to split an image set, as well as to create a separate copy. You can also copy
into an _existing_ image set to merge two image sets together. For more
information, see [`CopyImageSet`](../APIReference/API_CopyImageSet.md "../APIReference/API_CopyImageSet.md") in the _AWS HealthImaging API
Reference_.

###### Note

Keep the following points in mind when using the `CopyImageSet`
action:

- The `CopyImageSet` action will create a new image set, or a new
  version of the `destinationImageSet`. For more information, see [Listing image set versions](list-image-set-versions.md "list-image-set-versions.md").
- Copy is an asynchronous process. Therefore, the state ([`imageSetState`](../APIReference/API_CopySourceImageSetProperties.md#healthimaging-Type-CopySourceImageSetProperties-imageSetState "../APIReference/API_CopySourceImageSetProperties.md#healthimaging-Type-CopySourceImageSetProperties-imageSetState")) and status ([`imageSetWorkflowStatus`](../APIReference/API_CopySourceImageSetProperties.md#healthimaging-Type-CopySourceImageSetProperties-imageSetWorkflowStatus "../APIReference/API_CopySourceImageSetProperties.md#healthimaging-Type-CopySourceImageSetProperties-imageSetWorkflowStatus")) response elements are
  available to let you know what operation is happening on a locked image set.
  Other write operations cannot be performed on a locked image set.
- `CopyImageSet` requires SOP Instance UIDs be unique within an image
  set.
- You can copy subsets of SOP Instances using [`copiableAttributes`](../APIReference/API_MetadataCopies.md#healthimaging-Type-MetadataCopies-copiableAttributes "../APIReference/API_MetadataCopies.md#healthimaging-Type-MetadataCopies-copiableAttributes"). This allows you to pick one or
  more SOP Instances from the `sourceImageSet` to copy to the
  `destinationImageSet`.
- If the `CopyImageSet` action is not successful, call
  `GetImageSet` and review the [`message`](../APIReference/API_GetImageSet.md#healthimaging-GetImageSet-response-message "../APIReference/API_GetImageSet.md#healthimaging-GetImageSet-response-message") property. For more information, see [Getting image set properties](get-image-set-properties.md "get-image-set-properties.md").
- Real-world DICOM imports can result in multiple image sets per DICOM Series.
  The `CopyImageSet` action requires `sourceImageSet` and
  `destinationImageSet` to have consistent metadata, unless the
  optional [`force`](../APIReference/API_CopyImageSet.md#API_CopyImageSet_RequestParameters "../APIReference/API_CopyImageSet.md#API_CopyImageSet_RequestParameters") parameter is supplied.
- Set the [`force`](../APIReference/API_CopyImageSet.md#API_CopyImageSet_RequestParameters "../APIReference/API_CopyImageSet.md#API_CopyImageSet_RequestParameters") parameter to force the operation, even if there
  are inconsistent metadata elements between the `sourceImageSet` and
  `destinationImageSet`. In these cases, the Patient, Study, and
  Series metadata remains unchanged in the
  `destinationImageSet`.

###### To copy an image set

Choose a tab based on your access preference to AWS HealthImaging.

CLI

**AWS CLI**

**Example 1: To copy an image set without a destination.**

The following `copy-image-set` example makes a duplicate copy of an image set without a destination.

```
`aws medical-imaging copy-image-set \
 --datastore-id `12345678901234567890123456789012` \
 --source-image-set-id `ea92b0d8838c72a3f25d00d13616f87e` \
 --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1" } }`'`

```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042357.432,
        "imageSetId": "b9a06fef182a5f992842f77f8e0868e5",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042357.432,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

**Example 2: To copy an image set with a destination.**

The following `copy-image-set` example makes a duplicate copy of an image set with a destination.

```
`aws medical-imaging copy-image-set \
 --datastore-id `12345678901234567890123456789012` \
 --source-image-set-id `ea92b0d8838c72a3f25d00d13616f87e` \
 --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1" }, "destinationImageSet": { "imageSetId": "b9a06fef182a5f992842f77f8e0868e5", "latestVersionId": "1"} }`'`

```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042505.135,
        "imageSetId": "b9a06fef182a5f992842f77f8e0868e5",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042505.135,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

**Example 3: To copy a subset of instances from a source image set to a destination image set.**

The following `copy-image-set` example copies one DICOM instance from the source image set to the destination image set.
The force parameter is provided to override inconsistencies in the Patient, Study, and Series level attributes.

```
`aws medical-imaging copy-image-set \
 --datastore-id `12345678901234567890123456789012` \
 --source-image-set-id `ea92b0d8838c72a3f25d00d13616f87e` \
 --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1","DICOMCopies": {"copiableAttributes": "{\"SchemaVersion\":\"1.1\",\"Study\":{\"Series\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3666.0\":{\"Instances\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3669.0\":{}}}}}}"}},"destinationImageSet": {"imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7","latestVersionId": "1"}}`' \
 --force`

```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042505.135,
        "imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042505.135,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

- For API details, see
  [CopyImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```

    /**
     * Copy an AWS HealthImaging image set.
     *
     * @param medicalImagingClient  - The AWS HealthImaging client object.
     * @param datastoreId           - The datastore ID.
     * @param imageSetId            - The image set ID.
     * @param latestVersionId       - The version ID.
     * @param destinationImageSetId - The optional destination image set ID, ignored if null.
     * @param destinationVersionId  - The optional destination version ID, ignored if null.
     * @param force                 - The force flag.
     * @param subsets               - The optional subsets to copy, ignored if null.
     * @return                      - The image set ID of the copy.
     * @throws MedicalImagingException - Base exception for all service exceptions thrown by AWS HealthImaging.
     */
    public static String copyMedicalImageSet(MedicalImagingClient medicalImagingClient,
                                             String datastoreId,
                                             String imageSetId,
                                             String latestVersionId,
                                             String destinationImageSetId,
                                             String destinationVersionId,
                                             boolean force,
                                             Vector<String> subsets) {

        try {
            CopySourceImageSetInformation.Builder copySourceImageSetInformation = CopySourceImageSetInformation.builder()
                    .latestVersionId(latestVersionId);

            // Optionally copy a subset of image instances.
            if (subsets != null) {
                String subsetInstanceToCopy = getCopiableAttributesJSON(imageSetId, subsets);
                copySourceImageSetInformation.dicomCopies(MetadataCopies.builder()
                        .copiableAttributes(subsetInstanceToCopy)
                        .build());
            }

            CopyImageSetInformation.Builder copyImageSetBuilder = CopyImageSetInformation.builder()
                    .sourceImageSet(copySourceImageSetInformation.build());

            // Optionally designate a destination image set.
            if (destinationImageSetId != null) {
                copyImageSetBuilder = copyImageSetBuilder.destinationImageSet(CopyDestinationImageSet.builder()
                        .imageSetId(destinationImageSetId)
                        .latestVersionId(destinationVersionId)
                        .build());
            }

            CopyImageSetRequest copyImageSetRequest = CopyImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .sourceImageSetId(imageSetId)
                    .copyImageSetInformation(copyImageSetBuilder.build())
                    .force(force)
                    .build();

            CopyImageSetResponse response = medicalImagingClient.copyImageSet(copyImageSetRequest);

            return response.destinationImageSetProperties().imageSetId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            throw e;
        }
    }


```

Utility function to create copiable attributes.

```

    /**
     * Create a JSON string of copiable image instances.
     *
     * @param imageSetId - The image set ID.
     * @param subsets    - The subsets to copy.
     * @return A JSON string of copiable image instances.
     */
    private static String getCopiableAttributesJSON(String imageSetId, Vector<String> subsets) {
        StringBuilder subsetInstanceToCopy = new StringBuilder(
                """
                        {
                          "SchemaVersion": 1.1,
                          "Study": {
                            "Series": {
                                "
                                 """
        );

        subsetInstanceToCopy.append(imageSetId);

        subsetInstanceToCopy.append(
                """
                                ": {
                                "Instances": {
                        """
        );

        for (String subset : subsets) {
            subsetInstanceToCopy.append('"' + subset + "\": {},");
        }
        subsetInstanceToCopy.deleteCharAt(subsetInstanceToCopy.length() - 1);
        subsetInstanceToCopy.append("""
                         }
                       }
                    }
                  }
                }
                """);
        return subsetInstanceToCopy.toString();
    }


```

- For API details, see
  [CopyImageSet](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/CopyImageSet.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/CopyImageSet.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

Utility function to copy an image set.

```
import { CopyImageSetCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} datastoreId - The ID of the data store.
 * @param {string} imageSetId - The source image set ID.
 * @param {string} sourceVersionId - The source version ID.
 * @param {string} destinationImageSetId - The optional ID of the destination image set.
 * @param {string} destinationVersionId - The optional version ID of the destination image set.
 * @param {boolean} force - Force the copy action.
 * @param {[string]} copySubsets - A subset of instance IDs to copy.
 */
export const copyImageSet = async (
  datastoreId = "xxxxxxxxxxx",
  imageSetId = "xxxxxxxxxxxx",
  sourceVersionId = "1",
  destinationImageSetId = "",
  destinationVersionId = "",
  force = false,
  copySubsets = [],
) => {
  try {
    const params = {
      datastoreId: datastoreId,
      sourceImageSetId: imageSetId,
      copyImageSetInformation: {
        sourceImageSet: { latestVersionId: sourceVersionId },
      },
      force: force,
    };
    if (destinationImageSetId !== "" && destinationVersionId !== "") {
      params.copyImageSetInformation.destinationImageSet = {
        imageSetId: destinationImageSetId,
        latestVersionId: destinationVersionId,
      };
    }

    if (copySubsets.length > 0) {
      let copySubsetsJson;
      copySubsetsJson = {
        SchemaVersion: 1.1,
        Study: {
          Series: {
            imageSetId: {
              Instances: {},
            },
          },
        },
      };

      for (let i = 0; i < copySubsets.length; i++) {
        copySubsetsJson.Study.Series.imageSetId.Instances[copySubsets[i]] = {};
      }

      params.copyImageSetInformation.dicomCopies = copySubsetsJson;
    }

    const response = await medicalImagingClient.send(
      new CopyImageSetCommand(params),
    );
    console.log(response);
    // {
    //     '$metadata': {
    //         httpStatusCode: 200,
    //         requestId: 'd9b219ce-cc48-4a44-a5b2-c5c3068f1ee8',
    //         extendedRequestId: undefined,
    //         cfId: undefined,
    //         attempts: 1,
    //         totalRetryDelay: 0
    //      },
    //       datastoreId: 'xxxxxxxxxxxxxx',
    //       destinationImageSetProperties: {
    //             createdAt: 2023-09-27T19:46:21.824Z,
    //             imageSetArn: 'arn:aws:medical-imaging:us-east-1:xxxxxxxxxxx:datastore/xxxxxxxxxxxxx/imageset/xxxxxxxxxxxxxxxxxxx',
    //             imageSetId: 'xxxxxxxxxxxxxxx',
    //             imageSetState: 'LOCKED',
    //             imageSetWorkflowStatus: 'COPYING',
    //             latestVersionId: '1',
    //             updatedAt: 2023-09-27T19:46:21.824Z
    //       },
    //       sourceImageSetProperties: {
    //             createdAt: 2023-09-22T14:49:26.427Z,
    //             imageSetArn: 'arn:aws:medical-imaging:us-east-1:xxxxxxxxxxx:datastore/xxxxxxxxxxxxx/imageset/xxxxxxxxxxxxxxxx',
    //             imageSetId: 'xxxxxxxxxxxxxxxx',
    //             imageSetState: 'LOCKED',
    //             imageSetWorkflowStatus: 'COPYING_WITH_READ_ONLY_ACCESS',
    //             latestVersionId: '4',
    //             updatedAt: 2023-09-27T19:46:21.824Z
    //      }
    // }
    return response;
  } catch (err) {
    console.error(err);
  }
};


```

Copy an image set without a destination.

```

  await copyImageSet(
    "12345678901234567890123456789012",
    "12345678901234567890123456789012",
    "1",
  );


```

Copy an image set with a destination.

```

  await copyImageSet(
    "12345678901234567890123456789012",
    "12345678901234567890123456789012",
    "1",
    "12345678901234567890123456789012",
    "1",
    false,
  );



```

Copy a subset of an image set with a destination and force the copy.

```

  await copyImageSet(
    "12345678901234567890123456789012",
    "12345678901234567890123456789012",
    "1",
    "12345678901234567890123456789012",
    "1",
    true,
    ["12345678901234567890123456789012", "11223344556677889900112233445566"],
  );



```

- For API details, see
  [CopyImageSet](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/CopyImageSetCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/CopyImageSetCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples").

Python

**SDK for Python (Boto3)**

Utility function to copy an image set.

```
class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client


    def copy_image_set(
        self,
        datastore_id,
        image_set_id,
        version_id,
        destination_image_set_id=None,
        destination_version_id=None,
        force=False,
        subsets=[],
    ):
        """
        Copy an image set.

        :param datastore_id: The ID of the data store.
        :param image_set_id: The ID of the image set.
        :param version_id: The ID of the image set version.
        :param destination_image_set_id: The ID of the optional destination image set.
        :param destination_version_id: The ID of the optional destination image set version.
        :param force: Force the copy.
        :param subsets: The optional subsets to copy. For example: ["12345678901234567890123456789012"].
        :return: The copied image set ID.
        """
        try:
            copy_image_set_information = {
                "sourceImageSet": {"latestVersionId": version_id}
            }
            if destination_image_set_id and destination_version_id:
                copy_image_set_information["destinationImageSet"] = {
                    "imageSetId": destination_image_set_id,
                    "latestVersionId": destination_version_id,
                }
            if len(subsets) > 0:
                copySubsetsJson = {
                    "SchemaVersion": "1.1",
                    "Study": {"Series": {"imageSetId": {"Instances": {}}}},
                }

                for subset in subsets:
                    copySubsetsJson["Study"]["Series"]["imageSetId"]["Instances"][
                        subset
                    ] = {}

                copy_image_set_information["sourceImageSet"]["DICOMCopies"] = {
                    "copiableAttributes": json.dumps(copySubsetsJson)
                }
            copy_results = self.health_imaging_client.copy_image_set(
                datastoreId=datastore_id,
                sourceImageSetId=image_set_id,
                copyImageSetInformation=copy_image_set_information,
                force=force,
            )
        except ClientError as err:
            logger.error(
                "Couldn't copy image set. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return copy_results["destinationImageSetProperties"]["imageSetId"]



```

Copy an image set without a destination.

```
            copy_image_set_information = {
                "sourceImageSet": {"latestVersionId": version_id}
            }

            copy_results = self.health_imaging_client.copy_image_set(
                datastoreId=datastore_id,
                sourceImageSetId=image_set_id,
                copyImageSetInformation=copy_image_set_information,
                force=force,
            )


```

Copy an image set with a destination.

```
            copy_image_set_information = {
                "sourceImageSet": {"latestVersionId": version_id}
            }

            if destination_image_set_id and destination_version_id:
                copy_image_set_information["destinationImageSet"] = {
                    "imageSetId": destination_image_set_id,
                    "latestVersionId": destination_version_id,
                }

            copy_results = self.health_imaging_client.copy_image_set(
                datastoreId=datastore_id,
                sourceImageSetId=image_set_id,
                copyImageSetInformation=copy_image_set_information,
                force=force,
            )


```

Copy a subset of an image set.

```
            copy_image_set_information = {
                "sourceImageSet": {"latestVersionId": version_id}
            }

            if len(subsets) > 0:
                copySubsetsJson = {
                    "SchemaVersion": "1.1",
                    "Study": {"Series": {"imageSetId": {"Instances": {}}}},
                }

                for subset in subsets:
                    copySubsetsJson["Study"]["Series"]["imageSetId"]["Instances"][
                        subset
                    ] = {}

                copy_image_set_information["sourceImageSet"]["DICOMCopies"] = {
                    "copiableAttributes": json.dumps(copySubsetsJson)
                }

            copy_results = self.health_imaging_client.copy_image_set(
                datastoreId=datastore_id,
                sourceImageSetId=image_set_id,
                copyImageSetInformation=copy_image_set_information,
                force=force,
            )


```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [CopyImageSet](../../../goto/boto3/medical-imaging-2023-07-19/CopyImageSet.md "../../../goto/boto3/medical-imaging-2023-07-19/CopyImageSet.md")
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
        " iv_source_image_set_id = '1234567890123456789012345678901234567890'
        " iv_source_version_id = '1'
        " iv_destination_image_set_id = '1234567890123456789012345678901234567890' (optional)
        " iv_destination_version_id = '1' (optional)
        " iv_force = abap_false
        DATA(lo_source_info) = NEW /aws1/cl_migcpsrcimagesetinf00(
          iv_latestversionid = iv_source_version_id ).
        DATA(lo_copy_info) = NEW /aws1/cl_migcpimagesetinfmtion(
          io_sourceimageset = lo_source_info ).
        IF iv_destination_image_set_id IS NOT INITIAL AND
           iv_destination_version_id IS NOT INITIAL.
          DATA(lo_dest_info) = NEW /aws1/cl_migcopydstimageset(
            iv_imagesetid = iv_destination_image_set_id
            iv_latestversionid = iv_destination_version_id ).
          lo_copy_info = NEW /aws1/cl_migcpimagesetinfmtion(
            io_sourceimageset = lo_source_info
            io_destinationimageset = lo_dest_info ).
        ENDIF.
        oo_result = lo_mig->copyimageset(
          iv_datastoreid = iv_datastore_id
          iv_sourceimagesetid = iv_source_image_set_id
          io_copyimagesetinformation = lo_copy_info
          iv_force = iv_force ).
        DATA(lo_dest_props) = oo_result->get_dstimagesetproperties( ).
        DATA(lv_new_id) = lo_dest_props->get_imagesetid( ).
        MESSAGE |Image set copied with new ID: { lv_new_id }.| TYPE 'I'.
      CATCH /aws1/cx_migaccessdeniedex.
        MESSAGE 'Access denied.' TYPE 'I'.
      CATCH /aws1/cx_migconflictexception.
        MESSAGE 'Conflict error.' TYPE 'I'.
      CATCH /aws1/cx_miginternalserverex.
        MESSAGE 'Internal server error.' TYPE 'I'.
      CATCH /aws1/cx_migresourcenotfoundex.
        MESSAGE 'Image set not found.' TYPE 'I'.
      CATCH /aws1/cx_migservicequotaexcdex.
        MESSAGE 'Service quota exceeded.' TYPE 'I'.
      CATCH /aws1/cx_migthrottlingex.
        MESSAGE 'Request throttled.' TYPE 'I'.
      CATCH /aws1/cx_migvalidationex.
        MESSAGE 'Validation error.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [CopyImageSet](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
