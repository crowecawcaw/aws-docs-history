# Creating a data store

Use the `CreateDatastore` action to create an AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") for importing DICOM P10 files. The following
menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For
more information, see [`CreateDatastore`](../APIReference/API_CreateDatastore.md "../APIReference/API_CreateDatastore.md") in the _AWS HealthImaging API
Reference_. When you create a data store, you can select the default transfer syntax
that AWS HealthImaging used to transcode and store lossless image frames. This configuration cannot be
changed after the data store is created.

###### High Throughput JPEG 2000 (HTJ2K)

HTJ2K (High Throughput JPEG 2000) is the default storage format for HealthImaging datastores.
It is an extension of the JPEG 2000 standard that offers significantly improved encoding
and decoding performance. When you create a datastore without specifying a
`—lossless-storage-format`, HealthImaging automatically uses HTJ2K. See the _AWS CLI and SDKs_
section below for creating a data store using HTJ2K.

###### JPEG 2000 Lossless

JPEG 2000 Lossless encoding allows creation of datastores that persist and
retrieve lossless image frames in JPEG 2000 format without transcoding, enabling lower
latency retrieval for applications that require JPEG 2000 Lossless (DICOM Transfer Syntax
UID 1.2.840.10008.1.2.4.90) see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md") for more details. See the _AWS CLI and SDKs_
section below for creating a data store using JPEG 2000 lossless format.

###### Important

- Do not name data stores with protected health information (PHI), personally identifiable information (PII), or other confidential or sensitive
  information.
- The AWS Console supports creation of data stores with default settings. Use the AWS CLI
  or AWS SDK to create a data store with an optional `—lossless-storage-format` specified.

###### To create a data store

Choose a menu based on your access preference to AWS HealthImaging.

1. Open the HealthImaging console [Create data store page](https://console.aws.amazon.com/medical-imaging/home#/dataStores/create "https://console.aws.amazon.com/medical-imaging/home#/dataStores/create").
2. Under **Details**, for **Data store name**, enter
   a name for your data store.
3. Under **Data encryption**, choose an AWS KMS key for encrypting your
   resources. For more information, see [Data protection in AWS HealthImaging](data-protection.md "data-protection.md").
4. Under **Tags - _optional_**, you can add tags to
   your data store when you create it. For more information, see [Tagging a resource](tag-resource.md "tag-resource.md").
5. Choose **Create data store**.

Bash

**AWS CLI with Bash script**

```
###############################################################################
# function errecho
#
# This function outputs everything sent to it to STDERR (standard error output).
###############################################################################
function errecho() {
  printf "%s\n" "$*" 1>&2
}

###############################################################################
# function imaging_create_datastore
#
# This function creates an AWS HealthImaging data store for importing DICOM P10 files.
#
# Parameters:
#       -n data_store_name - The name of the data store.
#
# Returns:
#       The datastore ID.
#    And:
#       0 - If successful.
#       1 - If it fails.
###############################################################################
function imaging_create_datastore() {
  local datastore_name response
  local option OPTARG # Required to use getopts command in a function.

  # bashsupport disable=BP5008
  function usage() {
    echo "function imaging_create_datastore"
    echo "Creates an AWS HealthImaging data store for importing DICOM P10 files."
    echo "  -n data_store_name - The name of the data store."
    echo ""
  }

  # Retrieve the calling parameters.
  while getopts "n:h" option; do
    case "${option}" in
      n) datastore_name="${OPTARG}" ;;
      h)
        usage
        return 0
        ;;
      \?)
        echo "Invalid parameter"
        usage
        return 1
        ;;
    esac
  done
  export OPTIND=1

  if [[ -z "$datastore_name" ]]; then
    errecho "ERROR: You must provide a data store name with the -n parameter."
    usage
    return 1
  fi

  response=$(aws medical-imaging create-datastore \
    --datastore-name "$datastore_name" \
    --output text \
    --query 'datastoreId')

  local error_code=${?}

  if [[ $error_code -ne 0 ]]; then
    aws_cli_error_log $error_code
    errecho "ERROR: AWS reports medical-imaging create-datastore operation failed.$response"
    return 1
  fi

  echo "$response"

  return 0
}


```

- For API details, see
  [CreateDatastore](../../../goto/aws-cli/medical-imaging-2023-07-19/CreateDatastore.md "../../../goto/aws-cli/medical-imaging-2023-07-19/CreateDatastore.md")
  in _AWS CLI Command Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples").

CLI

**AWS CLI**

**Example 1: To create a data store**

The following `create-datastore` code example creates a data store with the name `my-datastore`.
When you create a datastore without specifying a `--lossless-storage-format`, AWS HealthImaging defaults to HTJ2K (High Throughput JPEG 2000).

```
`aws medical-imaging create-datastore \
 --datastore-name `"my-datastore"``

```

Output:

```
{
    "datastoreId": "12345678901234567890123456789012",
    "datastoreStatus": "CREATING"
}
```

**Example 2: To create a data store with JPEG 2000 Lossless storage format**

A data store configured with JPEG 2000 Lossless storage format will transcode and persist lossless image frames in JPEG 2000 format. Image frames can then be retrieved in
JPEG 2000 Lossless without transcoding. The following `create-datastore` code example creates a data store configured for JPEG 2000 Lossless storage format with the name `my-datastore`.

```
`aws medical-imaging create-datastore \
 --datastore-name `"my-datastore"` \
 --lossless-storage-format `JPEG_2000_LOSSLESS``

```

Output:

```
{
    "datastoreId": "12345678901234567890123456789012",
    "datastoreStatus": "CREATING"
}
```

- For API details, see
  [CreateDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/create-datastore.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/create-datastore.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static String createMedicalImageDatastore(MedicalImagingClient medicalImagingClient,
            String datastoreName) {
        try {
            CreateDatastoreRequest datastoreRequest = CreateDatastoreRequest.builder()
                    .datastoreName(datastoreName)
                    .build();
            CreateDatastoreResponse response = medicalImagingClient.createDatastore(datastoreRequest);
            return response.datastoreId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return "";
    }


```

- For API details, see
  [CreateDatastore](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/CreateDatastore.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/CreateDatastore.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { CreateDatastoreCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} datastoreName - The name of the data store to create.
 */
export const createDatastore = async (datastoreName = "DATASTORE_NAME") => {
  const response = await medicalImagingClient.send(
    new CreateDatastoreCommand({ datastoreName: datastoreName }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //       httpStatusCode: 200,
  //       requestId: 'a71cd65f-2382-49bf-b682-f9209d8d399b',
  //       extendedRequestId: undefined,
  //       cfId: undefined,
  //       attempts: 1,
  //       totalRetryDelay: 0
  //    },
  //    datastoreId: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  //    datastoreStatus: 'CREATING'
  // }
  return response;
};


```

- For API details, see
  [CreateDatastore](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/CreateDatastoreCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/CreateDatastoreCommand.md")
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


    def create_datastore(self, name):
        """
        Create a data store.

        :param name: The name of the data store to create.
        :return: The data store ID.
        """
        try:
            data_store = self.health_imaging_client.create_datastore(datastoreName=name)
        except ClientError as err:
            logger.error(
                "Couldn't create data store %s. Here's why: %s: %s",
                name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return data_store["datastoreId"]



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [CreateDatastore](../../../goto/boto3/medical-imaging-2023-07-19/CreateDatastore.md "../../../goto/boto3/medical-imaging-2023-07-19/CreateDatastore.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

SAP ABAP

**SDK for SAP ABAP**

```
    TRY.
        " iv_datastore_name = 'my-datastore-name'
        oo_result = lo_mig->createdatastore( iv_datastorename = iv_datastore_name ).
        DATA(lv_datastore_id) = oo_result->get_datastoreid( ).
        MESSAGE 'Data store created.' TYPE 'I'.
      CATCH /aws1/cx_migaccessdeniedex.
        MESSAGE 'Access denied.' TYPE 'I'.
      CATCH /aws1/cx_migconflictexception.
        MESSAGE 'Conflict. Data store may already exist.' TYPE 'I'.
      CATCH /aws1/cx_miginternalserverex.
        MESSAGE 'Internal server error.' TYPE 'I'.
      CATCH /aws1/cx_migservicequotaexcdex.
        MESSAGE 'Service quota exceeded.' TYPE 'I'.
      CATCH /aws1/cx_migthrottlingex.
        MESSAGE 'Request throttled.' TYPE 'I'.
      CATCH /aws1/cx_migvalidationex.
        MESSAGE 'Validation error.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [CreateDatastore](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/mig#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
