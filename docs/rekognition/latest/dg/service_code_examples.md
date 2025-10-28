# Code examples for Amazon Rekognition using AWS SDKs

The following code examples show how to use Amazon Rekognition with an AWS software development kit (SDK).
The code examples in this chapter are intended to supplement the code examples found throughout the rest of this guide.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code example shows how to get started using Amazon Rekognition.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/rekognition/hello_rekognition#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/rekognition/hello_rekognition#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS rekognition)

# Set this project's name.
project("hello_rekognition")

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
                                    # and set the proper subdirectory to the executables' location.

     AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif ()

add_executable(${PROJECT_NAME}
        hello_rekognition.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_rekognition.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/rekognition/RekognitionClient.h>
#include <aws/rekognition/model/ListCollectionsRequest.h>
#include <iostream>

/*
 *  A "Hello Rekognition" starter application which initializes an Amazon Rekognition client and
 *  lists the Amazon Rekognition collections in the current account and region.
 *
 *  main function
 *
 *  Usage: 'hello_rekognition'
 *
 */

int main(int argc, char **argv) {
    Aws::SDKOptions options;
    //  Optional: change the log level for debugging.
    //  options.loggingOptions.logLevel = Aws::Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::Rekognition::RekognitionClient rekognitionClient(clientConfig);
        Aws::Rekognition::Model::ListCollectionsRequest request;
        Aws::Rekognition::Model::ListCollectionsOutcome outcome =
                rekognitionClient.ListCollections(request);

        if (outcome.IsSuccess()) {
            const Aws::Vector<Aws::String>& collectionsIds = outcome.GetResult().GetCollectionIds();
            if (!collectionsIds.empty()) {
                std::cout << "collectionsIds: " << std::endl;
                for (auto &collectionId : collectionsIds) {
                    std::cout << "- " << collectionId << std::endl;
                }
            } else {
                std::cout << "No collections found" << std::endl;
            }
        } else {
            std::cerr << "Error with ListCollections: " << outcome.GetError()
                      << std::endl;
        }
    }


    Aws::ShutdownAPI(options); // Should only be called once.
    return 0;
}


```

- For API details, see
  [ListCollections](../../../goto/SdkForCpp/rekognition-2016-06-27/ListCollections.md "../../../goto/SdkForCpp/rekognition-2016-06-27/ListCollections.md")
  in _AWS SDK for C++ API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon Rekognition](example_rekognition_Hello_section.md "example_rekognition_Hello_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CompareFaces](example_rekognition_CompareFaces_section.md "example_rekognition_CompareFaces_section.md")
    - [CreateCollection](example_rekognition_CreateCollection_section.md "example_rekognition_CreateCollection_section.md")
    - [DeleteCollection](example_rekognition_DeleteCollection_section.md "example_rekognition_DeleteCollection_section.md")
    - [DeleteFaces](example_rekognition_DeleteFaces_section.md "example_rekognition_DeleteFaces_section.md")
    - [DescribeCollection](example_rekognition_DescribeCollection_section.md "example_rekognition_DescribeCollection_section.md")
    - [DetectFaces](example_rekognition_DetectFaces_section.md "example_rekognition_DetectFaces_section.md")
    - [DetectLabels](example_rekognition_DetectLabels_section.md "example_rekognition_DetectLabels_section.md")
    - [DetectModerationLabels](example_rekognition_DetectModerationLabels_section.md "example_rekognition_DetectModerationLabels_section.md")
    - [DetectText](example_rekognition_DetectText_section.md "example_rekognition_DetectText_section.md")
    - [DisassociateFaces](example_rekognition_DisassociateFaces_section.md "example_rekognition_DisassociateFaces_section.md")
    - [GetCelebrityInfo](example_rekognition_GetCelebrityInfo_section.md "example_rekognition_GetCelebrityInfo_section.md")
    - [IndexFaces](example_rekognition_IndexFaces_section.md "example_rekognition_IndexFaces_section.md")
    - [ListCollections](example_rekognition_ListCollections_section.md "example_rekognition_ListCollections_section.md")
    - [ListFaces](example_rekognition_ListFaces_section.md "example_rekognition_ListFaces_section.md")
    - [RecognizeCelebrities](example_rekognition_RecognizeCelebrities_section.md "example_rekognition_RecognizeCelebrities_section.md")
    - [SearchFaces](example_rekognition_SearchFaces_section.md "example_rekognition_SearchFaces_section.md")
    - [SearchFacesByImage](example_rekognition_SearchFacesByImage_section.md "example_rekognition_SearchFacesByImage_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Build a collection and find faces in it](example_rekognition_Usage_FindFacesInCollection_section.md "example_rekognition_Usage_FindFacesInCollection_section.md")
  - [Create a serverless application to manage photos](example_cross_PAM_section.md "example_cross_PAM_section.md")
  - [Detect PPE in images](example_cross_RekognitionPhotoAnalyzerPPE_section.md "example_cross_RekognitionPhotoAnalyzerPPE_section.md")
  - [Detect and display elements in images](example_rekognition_Usage_DetectAndDisplayImage_section.md "example_rekognition_Usage_DetectAndDisplayImage_section.md")
  - [Detect faces in an image](example_cross_DetectFaces_section.md "example_cross_DetectFaces_section.md")
  - [Detect information in videos](example_rekognition_VideoDetection_section.md "example_rekognition_VideoDetection_section.md")
  - [Detect objects in images](example_cross_RekognitionPhotoAnalyzer_section.md "example_cross_RekognitionPhotoAnalyzer_section.md")
  - [Detect people and objects in a video](example_cross_RekognitionVideoDetection_section.md "example_cross_RekognitionVideoDetection_section.md")
  - [Save EXIF and other image information](example_cross_DetectLabels_section.md "example_cross_DetectLabels_section.md")
