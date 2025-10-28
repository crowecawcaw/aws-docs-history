# Code examples for HealthImaging using AWS SDKs

The following code examples show how to use HealthImaging with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using HealthImaging.

C++

**SDK for C++**

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS medical-imaging)

# Set this project's name.
project("hello_health-imaging")

# Set the C++ standard to use to build this target.
# At least C++ 11 is required for the AWS SDK for C++.
set(CMAKE_CXX_STANDARD 11)

# Use the MSVC variable to determine if this is a Windows build.
set(WINDOWS_BUILD ${MSVC})

if (WINDOWS_BUILD) # Set the location where CMake can find the installed libraries for the AWS SDK.
    string(REPLACE ";" "/aws-cpp-sdk-all;" SYSTEM_MODULE_PATH "${CMAKE_SYSTEM_PREFIX_PATH}/aws-cpp-sdk-all")
    list(APPEND CMAKE_PREFIX_PATH ${SYSTEM_MODULE_PATH})
endif ()

# Find the AWS SDK for C++ package.
find_package(AWSSDK REQUIRED COMPONENTS ${SERVICE_COMPONENTS})

if (WINDOWS_BUILD AND AWSSDK_INSTALL_AS_SHARED_LIBS)
    # Copy relevant AWS SDK for C++ libraries into the current binary directory for running and debugging.

    # set(BIN_SUB_DIR "/Debug") # If you are building from the command line, you may need to uncomment this
    # and set the proper subdirectory to the executable location.

    AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif ()

add_executable(${PROJECT_NAME}
        hello_health_imaging.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_health_imaging.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/medical-imaging/MedicalImagingClient.h>
#include <aws/medical-imaging/model/ListDatastoresRequest.h>

#include <iostream>

/*
 *  A "Hello HealthImaging" starter application which initializes an AWS HealthImaging (HealthImaging) client
 *  and lists the HealthImaging data stores in the current account.
 *
 *  main function
 *
 *  Usage: 'hello_health-imaging'
 *
 */
#include <aws/core/auth/AWSCredentialsProviderChain.h>
#include <aws/core/platform/Environment.h>

int main(int argc, char **argv) {
    (void) argc;
    (void) argv;
    Aws::SDKOptions options;
    //   Optional: change the log level for debugging.
    //   options.loggingOptions.logLevel = Aws::Utils::Logging::LogLevel::Debug;

    Aws::InitAPI(options); // Should only be called once.
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::MedicalImaging::MedicalImagingClient medicalImagingClient(clientConfig);
        Aws::MedicalImaging::Model::ListDatastoresRequest listDatastoresRequest;

        Aws::Vector<Aws::MedicalImaging::Model::DatastoreSummary> allDataStoreSummaries;
        Aws::String nextToken; // Used for paginated results.
        do {
            if (!nextToken.empty()) {
                listDatastoresRequest.SetNextToken(nextToken);
            }
            Aws::MedicalImaging::Model::ListDatastoresOutcome listDatastoresOutcome =
                    medicalImagingClient.ListDatastores(listDatastoresRequest);
            if (listDatastoresOutcome.IsSuccess()) {
                const Aws::Vector<Aws::MedicalImaging::Model::DatastoreSummary> &dataStoreSummaries =
                        listDatastoresOutcome.GetResult().GetDatastoreSummaries();
                allDataStoreSummaries.insert(allDataStoreSummaries.cend(),
                                             dataStoreSummaries.cbegin(),
                                             dataStoreSummaries.cend());
                nextToken = listDatastoresOutcome.GetResult().GetNextToken();
            }
            else {
                std::cerr << "ListDatastores error: "
                          << listDatastoresOutcome.GetError().GetMessage() << std::endl;
                break;
            }
        } while (!nextToken.empty());

        std::cout << allDataStoreSummaries.size() << " HealthImaging data "
                  << ((allDataStoreSummaries.size() == 1) ?
                      "store was retrieved." : "stores were retrieved.") << std::endl;

        for (auto const &dataStoreSummary: allDataStoreSummaries) {
            std::cout << "  Datastore: " << dataStoreSummary.GetDatastoreName()
                      << std::endl;
            std::cout << "  Datastore ID: " << dataStoreSummary.GetDatastoreId()
                      << std::endl;
        }
    }

    Aws::ShutdownAPI(options); // Should only be called once.
    return 0;
}


```

- For API details, see
  [ListDatastores](../../../goto/SdkForCpp/medical-imaging-2023-07-19/ListDatastores.md "../../../goto/SdkForCpp/medical-imaging-2023-07-19/ListDatastores.md")
  in _AWS SDK for C++ API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/hello_health_imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/hello_health_imaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import {
  ListDatastoresCommand,
  MedicalImagingClient,
} from "@aws-sdk/client-medical-imaging";

// When no region or credentials are provided, the SDK will use the
// region and credentials from the local AWS config.
const client = new MedicalImagingClient({});

export const helloMedicalImaging = async () => {
  const command = new ListDatastoresCommand({});

  const { datastoreSummaries } = await client.send(command);
  console.log("Datastores: ");
  console.log(datastoreSummaries.map((item) => item.datastoreName).join("\n"));
  return datastoreSummaries;
};


```

- For API details, see
  [ListDatastores](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/ListDatastoresCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/ListDatastoresCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples").

Python

**SDK for Python (Boto3)**

```
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def hello_medical_imaging(medical_imaging_client):
    """
    Use the AWS SDK for Python (Boto3) to create an AWS HealthImaging
    client and list the data stores in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param medical_imaging_client: A Boto3 AWS HealthImaging Client object.
    """
    print("Hello, Amazon Health Imaging! Let's list some of your data stores:\n")
    try:
        paginator = medical_imaging_client.get_paginator("list_datastores")
        page_iterator = paginator.paginate()
        datastore_summaries = []
        for page in page_iterator:
            datastore_summaries.extend(page["datastoreSummaries"])
        print("\tData Stores:")
        for ds in datastore_summaries:
            print(f"\t\tDatastore: {ds['datastoreName']} ID {ds['datastoreId']}")
    except ClientError as err:
        logger.error(
            "Couldn't list data stores. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise


if __name__ == "__main__":
    hello_medical_imaging(boto3.client("medical-imaging"))


```

- For API details, see
  [ListDatastores](../../../goto/boto3/medical-imaging-2023-07-19/ListDatastores.md "../../../goto/boto3/medical-imaging-2023-07-19/ListDatastores.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging/imaging_set_and_frames_workflow#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging/imaging_set_and_frames_workflow#code-examples").

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello HealthImaging](example_medical-imaging_Hello_section.md "example_medical-imaging_Hello_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CopyImageSet](example_medical-imaging_CopyImageSet_section.md "example_medical-imaging_CopyImageSet_section.md")
    - [CreateDatastore](example_medical-imaging_CreateDatastore_section.md "example_medical-imaging_CreateDatastore_section.md")
    - [DeleteDatastore](example_medical-imaging_DeleteDatastore_section.md "example_medical-imaging_DeleteDatastore_section.md")
    - [DeleteImageSet](example_medical-imaging_DeleteImageSet_section.md "example_medical-imaging_DeleteImageSet_section.md")
    - [GetDICOMImportJob](example_medical-imaging_GetDICOMImportJob_section.md "example_medical-imaging_GetDICOMImportJob_section.md")
    - [GetDatastore](example_medical-imaging_GetDatastore_section.md "example_medical-imaging_GetDatastore_section.md")
    - [GetImageFrame](example_medical-imaging_GetImageFrame_section.md "example_medical-imaging_GetImageFrame_section.md")
    - [GetImageSet](example_medical-imaging_GetImageSet_section.md "example_medical-imaging_GetImageSet_section.md")
    - [GetImageSetMetadata](example_medical-imaging_GetImageSetMetadata_section.md "example_medical-imaging_GetImageSetMetadata_section.md")
    - [ListDICOMImportJobs](example_medical-imaging_ListDICOMImportJobs_section.md "example_medical-imaging_ListDICOMImportJobs_section.md")
    - [ListDatastores](example_medical-imaging_ListDatastores_section.md "example_medical-imaging_ListDatastores_section.md")
    - [ListImageSetVersions](example_medical-imaging_ListImageSetVersions_section.md "example_medical-imaging_ListImageSetVersions_section.md")
    - [ListTagsForResource](example_medical-imaging_ListTagsForResource_section.md "example_medical-imaging_ListTagsForResource_section.md")
    - [SearchImageSets](example_medical-imaging_SearchImageSets_section.md "example_medical-imaging_SearchImageSets_section.md")
    - [StartDICOMImportJob](example_medical-imaging_StartDICOMImportJob_section.md "example_medical-imaging_StartDICOMImportJob_section.md")
    - [TagResource](example_medical-imaging_TagResource_section.md "example_medical-imaging_TagResource_section.md")
    - [UntagResource](example_medical-imaging_UntagResource_section.md "example_medical-imaging_UntagResource_section.md")
    - [UpdateImageSetMetadata](example_medical-imaging_UpdateImageSetMetadata_section.md "example_medical-imaging_UpdateImageSetMetadata_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Get started with image sets and image frames](example_medical-imaging_Scenario_ImageSetsAndFrames_section.md "example_medical-imaging_Scenario_ImageSetsAndFrames_section.md")
  - [Tagging a data store](example_medical-imaging_Scenario_TaggingDataStores_section.md "example_medical-imaging_Scenario_TaggingDataStores_section.md")
  - [Tagging an image set](example_medical-imaging_Scenario_TaggingImageSets_section.md "example_medical-imaging_Scenario_TaggingImageSets_section.md")
