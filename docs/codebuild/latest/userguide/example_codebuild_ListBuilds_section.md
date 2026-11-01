

# Use `ListBuilds` with an AWS SDK or CLI
<a name="example_codebuild_ListBuilds_section"></a>

The following code examples show how to use `ListBuilds`.

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/codebuild#code-examples). 

```
//! List the CodeBuild builds.
/*!
  \param sortType: 'SortOrderType' type.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::CodeBuild::listBuilds(Aws::CodeBuild::Model::SortOrderType sortType,
                                   const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::CodeBuild::CodeBuildClient codeBuildClient(clientConfiguration);

    Aws::CodeBuild::Model::ListBuildsRequest listBuildsRequest;
    listBuildsRequest.SetSortOrder(sortType);

    Aws::String nextToken; // Used for pagination.

    do {
        if (!nextToken.empty()) {
            listBuildsRequest.SetNextToken(nextToken);
        }

        Aws::CodeBuild::Model::ListBuildsOutcome listBuildsOutcome = codeBuildClient.ListBuilds(
                listBuildsRequest);

        if (listBuildsOutcome.IsSuccess()) {
            const Aws::Vector<Aws::String> &ids = listBuildsOutcome.GetResult().GetIds();
            if (!ids.empty()) {

                std::cout << "Information about each build:" << std::endl;
                Aws::CodeBuild::Model::BatchGetBuildsRequest getBuildsRequest;
                getBuildsRequest.SetIds(listBuildsOutcome.GetResult().GetIds());
                Aws::CodeBuild::Model::BatchGetBuildsOutcome getBuildsOutcome = codeBuildClient.BatchGetBuilds(
                        getBuildsRequest);

                if (getBuildsOutcome.IsSuccess()) {
                    const Aws::Vector<Aws::CodeBuild::Model::Build> &builds = getBuildsOutcome.GetResult().GetBuilds();
                    std::cout << builds.size() << " build(s) found." << std::endl;
                    for (auto val: builds) {
                        std::cout << val.GetId() << std::endl;
                    }
                } else {
                    std::cerr << "Error getting builds"
                              << getBuildsOutcome.GetError().GetMessage() << std::endl;
                    return false;
                }
            } else {
                std::cout << "No builds found." << std::endl;
            }

            // Get the next token for pagination.

            nextToken = listBuildsOutcome.GetResult().GetNextToken();
        } else {
            std::cerr << "Error listing builds"
                      << listBuildsOutcome.GetError().GetMessage()
                      << std::endl;
            return false;
        }

    } while (!nextToken.

            empty()

            );

    return true;
}
```
+  For API details, see [ListBuilds](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListBuilds) in *AWS SDK for C\+\+ API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To get a list of AWS CodeBuild builds IDs.**  
The following `list-builds` example gets a list of CodeBuild IDs sorted in ascending order.  

```
aws codebuild list-builds \
    --sort-order {{ASCENDING}}
```
The output includes a `nextToken` value which indicates that there is more output available.  
Output:  

```
{
    "nextToken": "4AEA6u7J...The full token has been omitted for brevity...MzY2OA==",
    "ids": [
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    ]
}
```
Run this command again and provide the `nextToken` value in the previous response as a parameter to get the next part of the output. Repeat until you don't receive a `nextToken` value in the response.  

```
aws codebuild list-builds \
    --sort-order {{ASCENDING}} \
    --next-token {{4AEA6u7J...The}} {{full}} {{token}} {{has}} {{been}} {{omitted}} {{for}} {{brevity...MzY2OA==}}
```
Output:  

```
{
    "ids": [
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
        "codebuild-demo-project:a1b2c3d4-5678-90ab-cdef-EXAMPLE66666"
    ]
}
```
For more information, see [View a list of build IDs in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-list.html) in the *AWS CodeBuild User Guide*.  
+  For API details, see [ListBuilds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-builds.html) in *AWS CLI Command Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.