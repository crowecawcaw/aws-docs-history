# Use `StartLifecyclePolicyPreview` with an AWS SDK or CLI

The following code examples show how to use `StartLifecyclePolicyPreview`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_ecr_Scenario_RepositoryManagement_section.md "example_ecr_Scenario_RepositoryManagement_section.md")

CLI

**AWS CLI**

**To create a lifecycle policy preview**

The following `start-lifecycle-policy-preview` example creates a lifecycle policy preview defined by a JSON file for the specified repository.

```
`aws ecr start-lifecycle-policy-preview \
 --repository-name `"project-a/amazon-ecs-sample"` \
 --lifecycle-policy-text `"file://policy.json"``

```

Contents of `policy.json`:

```
{
   "rules": [
       {
           "rulePriority": 1,
           "description": "Expire images older than 14 days",
           "selection": {
               "tagStatus": "untagged",
               "countType": "sinceImagePushed",
               "countUnit": "days",
               "countNumber": 14
           },
           "action": {
               "type": "expire"
           }
       }
   ]
}
```

Output:

```
{
   "registryId": "012345678910",
   "repositoryName": "project-a/amazon-ecs-sample",
   "lifecyclePolicyText": "{\n    \"rules\": [\n        {\n            \"rulePriority\": 1,\n            \"description\": \"Expire images older than 14 days\",\n            \"selection\": {\n                \"tagStatus\": \"untagged\",\n                \"countType\": \"sinceImagePushed\",\n                \"countUnit\": \"days\",\n                \"countNumber\": 14\n            },\n            \"action\": {\n                \"type\": \"expire\"\n            }\n        }\n    ]\n}\n",
   "status": "IN_PROGRESS"
}
```

- For API details, see
  [StartLifecyclePolicyPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-lifecycle-policy-preview.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-lifecycle-policy-preview.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples").

```
    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     * @throws EcrException             if there is an error retrieving the image information from Amazon ECR.
     * @throws CompletionException      if the asynchronous operation completes exceptionally.
     */
    public void verifyImage(String repositoryName, String imageTag) {
        DescribeImagesRequest request = DescribeImagesRequest.builder()
            .repositoryName(repositoryName)
            .imageIds(ImageIdentifier.builder().imageTag(imageTag).build())
            .build();

        CompletableFuture<DescribeImagesResponse> response = getAsyncClient().describeImages(request);
        response.whenComplete((describeImagesResponse, ex) -> {
            if (ex != null) {
                if (ex instanceof CompletionException) {
                    Throwable cause = ex.getCause();
                    if (cause instanceof EcrException) {
                        throw (EcrException) cause;
                    } else {
                        throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
                    }
                } else {
                    throw new RuntimeException("Unexpected error: " + ex.getCause());
                }
            } else if (describeImagesResponse != null && !describeImagesResponse.imageDetails().isEmpty()) {
                System.out.println("Image is present in the repository.");
            } else {
                System.out.println("Image is not present in the repository.");
            }
        });

        // Wait for the CompletableFuture to complete.
        response.join();
    }


```

- For API details, see
  [StartLifecyclePolicyPreview](../../../goto/SdkForJavaV2/ecr-2015-09-21/StartLifecyclePolicyPreview.md "../../../goto/SdkForJavaV2/ecr-2015-09-21/StartLifecyclePolicyPreview.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples").

```

    /**
     * Verifies the existence of an image in an Amazon Elastic Container Registry (Amazon ECR) repository asynchronously.
     *
     * @param repositoryName The name of the Amazon ECR repository.
     * @param imageTag       The tag of the image to verify.
     */
    suspend fun verifyImage(
        repoName: String?,
        imageTagVal: String?,
    ) {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        require(!(imageTagVal == null || imageTagVal.isEmpty())) { "Image tag cannot be null or empty" }

        val imageId =
            ImageIdentifier {
                imageTag = imageTagVal
            }
        val request =
            DescribeImagesRequest {
                repositoryName = repoName
                imageIds = listOf(imageId)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeImagesResponse = ecrClient.describeImages(request)
            if (describeImagesResponse != null && !describeImagesResponse.imageDetails?.isEmpty()!!) {
                println("Image is present in the repository.")
            } else {
                println("Image is not present in the repository.")
            }
        }
    }


```

- For API details, see
  [StartLifecyclePolicyPreview](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon ECR with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
