# Code examples for Amazon ECR using AWS SDKs

The following code examples show how to use Amazon ECR with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon ECR with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon ECR.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ecr.EcrClient;
import software.amazon.awssdk.services.ecr.model.EcrException;
import software.amazon.awssdk.services.ecr.model.ListImagesRequest;
import software.amazon.awssdk.services.ecr.paginators.ListImagesIterable;

public class HelloECR {

    public static void main(String[] args) {
        final String usage = """
            Usage:    <repositoryName>

            Where:
               repositoryName - The name of the Amazon ECR repository.
            """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String repoName = args[0];
        EcrClient ecrClient = EcrClient.builder()
            .region(Region.US_EAST_1)
            .build();

        listImageTags(ecrClient, repoName);
    }
    public static void listImageTags(EcrClient ecrClient, String repoName){
        ListImagesRequest listImagesPaginator = ListImagesRequest.builder()
            .repositoryName(repoName)
            .build();

        ListImagesIterable imagesIterable = ecrClient.listImagesPaginator(listImagesPaginator);
        imagesIterable.stream()
            .flatMap(r -> r.imageIds().stream())
            .forEach(image -> System.out.println("The docker image tag is: " +image.imageTag()));
    }
}


```

- For API details, see
  [listImages](../../../goto/SdkForJavaV2/ecr-2015-09-21/listImages.md "../../../goto/SdkForJavaV2/ecr-2015-09-21/listImages.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples").

```
import aws.sdk.kotlin.services.ecr.EcrClient
import aws.sdk.kotlin.services.ecr.model.ListImagesRequest
import kotlin.system.exitProcess

suspend fun main(args: Array<String>) {
    val usage = """
            Usage: <repositoryName>

            Where:
               repositoryName - The name of the Amazon ECR repository.

    """.trimIndent()

    if (args.size != 1) {
        println(usage)
        exitProcess(1)
    }

    val repoName = args[0]
    listImageTags(repoName)
}

suspend fun listImageTags(repoName: String?) {
    val listImages =
        ListImagesRequest {
            repositoryName = repoName
        }

    EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
        val imageResponse = ecrClient.listImages(listImages)
        imageResponse.imageIds?.forEach { imageId ->
            println("Image tag: ${imageId.imageTag}")
        }
    }
}


```

- For API details, see
  [listImages](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples").

```
import boto3
import argparse
from boto3 import client


def hello_ecr(ecr_client: client, repository_name: str) -> None:
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Elastic Container Registry (Amazon ECR)
    client and list the images in a repository.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param ecr_client: A Boto3 Amazon ECR Client object. This object wraps
                             the low-level Amazon ECR service API.
    :param repository_name: The name of an Amazon ECR repository in your account.
    """
    print(
        f"Hello, Amazon ECR! Let's list some images in the repository '{repository_name}':\n"
    )
    paginator = ecr_client.get_paginator("list_images")
    page_iterator = paginator.paginate(
        repositoryName=repository_name, PaginationConfig={"MaxItems": 10}
    )

    image_names: [str] = []
    for page in page_iterator:
        for schedule in page["imageIds"]:
            image_names.append(schedule["imageTag"])

    print(f"{len(image_names)} image(s) retrieved.")
    for schedule_name in image_names:
        print(f"\t{schedule_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run hello Amazon ECR.")
    parser.add_argument(
        "--repository-name",
        type=str,
        help="the name of an Amazon ECR repository in your account.",
        required=True,
    )
    args = parser.parse_args()

    hello_ecr(boto3.client("ecr"), args.repository_name)


```

- For API details, see
  [listImages](../../../goto/boto3/ecr-2015-09-21/listImages.md "../../../goto/boto3/ecr-2015-09-21/listImages.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon ECR](example_ecr_Hello_section.md "example_ecr_Hello_section.md")
  - [Learn the basics](example_ecr_Scenario_RepositoryManagement_section.md "example_ecr_Scenario_RepositoryManagement_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [CreateRepository](example_ecr_CreateRepository_section.md "example_ecr_CreateRepository_section.md")
    - [DeleteRepository](example_ecr_DeleteRepository_section.md "example_ecr_DeleteRepository_section.md")
    - [DescribeImages](example_ecr_DescribeImages_section.md "example_ecr_DescribeImages_section.md")
    - [DescribeRepositories](example_ecr_DescribeRepositories_section.md "example_ecr_DescribeRepositories_section.md")
    - [GetAuthorizationToken](example_ecr_GetAuthorizationToken_section.md "example_ecr_GetAuthorizationToken_section.md")
    - [GetRepositoryPolicy](example_ecr_GetRepositoryPolicy_section.md "example_ecr_GetRepositoryPolicy_section.md")
    - [ListImages](example_ecr_ListImages_section.md "example_ecr_ListImages_section.md")
    - [PushImageCmd](example_ecr_PushImageCmd_section.md "example_ecr_PushImageCmd_section.md")
    - [PutLifeCyclePolicy](example_ecr_PutLifeCyclePolicy_section.md "example_ecr_PutLifeCyclePolicy_section.md")
    - [SetRepositoryPolicy](example_ecr_SetRepositoryPolicy_section.md "example_ecr_SetRepositoryPolicy_section.md")
    - [StartLifecyclePolicyPreview](example_ecr_StartLifecyclePolicyPreview_section.md "example_ecr_StartLifecyclePolicyPreview_section.md")
