# Deleting a data store

Use the `DeleteDatastore` action to delete an AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). The following menus provide a procedure
for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more information, see
[`DeleteDatastore`](../APIReference/API_DeleteDatastore.md "../APIReference/API_DeleteDatastore.md") in the _AWS HealthImaging API
Reference_.

###### Note

Before a data store can be deleted, you must first delete all [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") within it. For more information, see
[Deleting an image set](delete-image-set.md "delete-image-set.md").

###### To delete a data store

Choose a menu based on your access preference to AWS HealthImaging.

1. Open the HealthImaging console [Data stores page](https://console.aws.amazon.com/medical-imaging/home#/dataStores "https://console.aws.amazon.com/medical-imaging/home#/dataStores").
2. Choose a data store.
3. Choose **Delete**.

The **Delete data store** page opens. 4. To confirm data store deletion, enter the data store name in the text
input field. 5. Choose **Delete data store**.

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
# function imaging_delete_datastore
#
# This function deletes an AWS HealthImaging data store.
#
# Parameters:
#       -i datastore_id - The ID of the data store.
#
# Returns:
#       0 - If successful.
#       1 - If it fails.
###############################################################################
function imaging_delete_datastore() {
  local datastore_id response
  local option OPTARG # Required to use getopts command in a function.

  # bashsupport disable=BP5008
  function usage() {
    echo "function imaging_delete_datastore"
    echo "Deletes an AWS HealthImaging data store."
    echo "  -i datastore_id - The ID of the data store."
    echo ""
  }

  # Retrieve the calling parameters.
  while getopts "i:h" option; do
    case "${option}" in
      i) datastore_id="${OPTARG}" ;;
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

  if [[ -z "$datastore_id" ]]; then
    errecho "ERROR: You must provide a data store ID with the -i parameter."
    usage
    return 1
  fi

  response=$(aws medical-imaging delete-datastore \
    --datastore-id "$datastore_id")

  local error_code=${?}

  if [[ $error_code -ne 0 ]]; then
    aws_cli_error_log $error_code
    errecho "ERROR: AWS reports medical-imaging delete-datastore operation failed.$response"
    return 1
  fi

  return 0
}


```

- For API details, see
  [DeleteDatastore](../../../goto/aws-cli/medical-imaging-2023-07-19/DeleteDatastore.md "../../../goto/aws-cli/medical-imaging-2023-07-19/DeleteDatastore.md")
  in _AWS CLI Command Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/medical-imaging#code-examples").

CLI

**AWS CLI**

**To delete a data store**

The following `delete-datastore` code example deletes a data store.

```
`aws medical-imaging delete-datastore \
 --datastore-id `"12345678901234567890123456789012"``

```

Output:

```
{
    "datastoreId": "12345678901234567890123456789012",
    "datastoreStatus": "DELETING"
}
```

- For API details, see
  [DeleteDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-datastore.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-datastore.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static void deleteMedicalImagingDatastore(MedicalImagingClient medicalImagingClient,
            String datastoreID) {
        try {
            DeleteDatastoreRequest datastoreRequest = DeleteDatastoreRequest.builder()
                    .datastoreId(datastoreID)
                    .build();
            medicalImagingClient.deleteDatastore(datastoreRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [DeleteDatastore](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteDatastore.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteDatastore.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { DeleteDatastoreCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} datastoreId - The ID of the data store to delete.
 */
export const deleteDatastore = async (datastoreId = "DATASTORE_ID") => {
  const response = await medicalImagingClient.send(
    new DeleteDatastoreCommand({ datastoreId }),
  );
  console.log(response);
  // {
  //   '$metadata': {
  //           httpStatusCode: 200,
  //           requestId: 'f5beb409-678d-48c9-9173-9a001ee1ebb1',
  //           extendedRequestId: undefined,
  //           cfId: undefined,
  //           attempts: 1,
  //           totalRetryDelay: 0
  //        },
  //     datastoreId: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  //     datastoreStatus: 'DELETING'
  // }

  return response;
};


```

- For API details, see
  [DeleteDatastore](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/DeleteDatastoreCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/DeleteDatastoreCommand.md")
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


    def delete_datastore(self, datastore_id):
        """
        Delete a data store.

        :param datastore_id: The ID of the data store.
        """
        try:
            self.health_imaging_client.delete_datastore(datastoreId=datastore_id)
        except ClientError as err:
            logger.error(
                "Couldn't delete data store %s. Here's why: %s: %s",
                datastore_id,
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
  [DeleteDatastore](../../../goto/boto3/medical-imaging-2023-07-19/DeleteDatastore.md "../../../goto/boto3/medical-imaging-2023-07-19/DeleteDatastore.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.
