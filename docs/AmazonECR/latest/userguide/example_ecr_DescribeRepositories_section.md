# Use `DescribeRepositories` with an AWS SDK or CLI

The following code examples show how to use `DescribeRepositories`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_ecr_Scenario_RepositoryManagement_section.md "example_ecr_Scenario_RepositoryManagement_section.md")

CLI

**AWS CLI**

**To describe the repositories in a registry**

This example describes the repositories in the default registry for an account.

Command:

```
`aws ecr describe-repositories`

```

Output:

```
{
    "repositories": [
        {
            "registryId": "012345678910",
            "repositoryName": "ubuntu",
            "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/ubuntu"
        },
        {
            "registryId": "012345678910",
            "repositoryName": "test",
            "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/test"
        }
    ]
}
```

- For API details, see
  [DescribeRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecr#code-examples").

```
    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     * @throws EcrException        if there is an error retrieving the repository information.
     * @throws CompletionException if the asynchronous operation completes exceptionally.
     */
    public void getRepositoryURI(String repoName) {
        DescribeRepositoriesRequest request = DescribeRepositoriesRequest.builder()
            .repositoryNames(repoName)
            .build();

        CompletableFuture<DescribeRepositoriesResponse> response = getAsyncClient().describeRepositories(request);
        response.whenComplete((describeRepositoriesResponse, ex) -> {
            if (ex != null) {
                Throwable cause = ex.getCause();
                if (cause instanceof InterruptedException) {
                    Thread.currentThread().interrupt();
                    String errorMessage = "Thread interrupted while waiting for asynchronous operation: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                } else if (cause instanceof EcrException) {
                    throw (EcrException) cause;
                } else {
                    String errorMessage = "Unexpected error: " + cause.getMessage();
                    throw new RuntimeException(errorMessage, cause);
                }
            } else {
                if (describeRepositoriesResponse != null) {
                    if (!describeRepositoriesResponse.repositories().isEmpty()) {
                        String repositoryUri = describeRepositoriesResponse.repositories().get(0).repositoryUri();
                        System.out.println("Repository URI found: " + repositoryUri);
                    } else {
                        System.out.println("No repositories found for the given name.");
                    }
                } else {
                    System.err.println("No response received from describeRepositories.");
                }
            }
        });
        response.join();
    }


```

- For API details, see
  [DescribeRepositories](../../../goto/SdkForJavaV2/ecr-2015-09-21/DescribeRepositories.md "../../../goto/SdkForJavaV2/ecr-2015-09-21/DescribeRepositories.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/ecr#code-examples").

```

    /**
     * Retrieves the repository URI for the specified repository name.
     *
     * @param repoName the name of the repository to retrieve the URI for.
     * @return the repository URI for the specified repository name.
     */
    suspend fun getRepositoryURI(repoName: String?): String? {
        require(!(repoName == null || repoName.isEmpty())) { "Repository name cannot be null or empty" }
        val request =
            DescribeRepositoriesRequest {
                repositoryNames = listOf(repoName)
            }

        EcrClient.fromEnvironment { region = "us-east-1" }.use { ecrClient ->
            val describeRepositoriesResponse = ecrClient.describeRepositories(request)
            if (!describeRepositoriesResponse.repositories?.isEmpty()!!) {
                return describeRepositoriesResponse?.repositories?.get(0)?.repositoryUri
            } else {
                println("No repositories found for the given name.")
                return ""
            }
        }
    }


```

- For API details, see
  [DescribeRepositories](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecr#code-examples").

```
class ECRWrapper:
    def __init__(self, ecr_client: client):
        self.ecr_client = ecr_client

    @classmethod
    def from_client(cls) -> "ECRWrapper":
        """
        Creates a ECRWrapper instance with a default Amazon ECR client.

        :return: An instance of ECRWrapper initialized with the default Amazon ECR client.
        """
        ecr_client = boto3.client("ecr")
        return cls(ecr_client)


    def describe_repositories(self, repository_names: list[str]) -> list[dict]:
        """
        Describes ECR repositories.

        :param repository_names: The names of the repositories to describe.
        :return: The list of repository descriptions.
        """
        try:
            response = self.ecr_client.describe_repositories(
                repositoryNames=repository_names
            )
            return response["repositories"]
        except ClientError as err:
            logger.error(
                "Couldn't describe repositories. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DescribeRepositories](../../../goto/boto3/ecr-2015-09-21/DescribeRepositories.md "../../../goto/boto3/ecr-2015-09-21/DescribeRepositories.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecr#code-examples").

```
async fn show_repos(client: &aws_sdk_ecr::Client) -> Result<(), aws_sdk_ecr::Error> {
    let rsp = client.describe_repositories().send().await?;

    let repos = rsp.repositories();

    println!("Found {} repositories:", repos.len());

    for repo in repos {
        println!("  ARN:  {}", repo.repository_arn().unwrap());
        println!("  Name: {}", repo.repository_name().unwrap());
    }

    Ok(())
}


```

- For API details, see
  [DescribeRepositories](https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.describe_repositories "https://docs.rs/aws-sdk-ecr/latest/aws_sdk_ecr/client/struct.Client.html#method.describe_repositories")
  in _AWS SDK for Rust API reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ecr#code-examples").

```
    TRY.
        " it_repository_names = VALUE #( ( NEW /aws1/cl_ecrrepositorynamels00( iv_value = 'my-repository' ) ) )
        oo_result = lo_ecr->describerepositories(
          it_repositorynames = it_repository_names ).
        DATA(lt_repositories) = oo_result->get_repositories( ).
        MESSAGE |Found { lines( lt_repositories ) } repositories.| TYPE 'I'.
      CATCH /aws1/cx_ecrrepositorynotfndex.
        MESSAGE 'Repository not found.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [DescribeRepositories](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon ECR with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
