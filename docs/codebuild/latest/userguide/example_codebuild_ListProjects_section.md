# Use `ListProjects` with an AWS SDK or CLI

The following code examples show how to use `ListProjects`.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/codebuild#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/codebuild#code-examples").

```
//! List the CodeBuild projects.
/*!
  \param sortType: 'SortOrderType' type.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::CodeBuild::listProjects(Aws::CodeBuild::Model::SortOrderType sortType,
                                     const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::CodeBuild::CodeBuildClient codeBuildClient(clientConfiguration);

    Aws::CodeBuild::Model::ListProjectsRequest listProjectsRequest;
    listProjectsRequest.SetSortOrder(sortType);

    Aws::String nextToken; // Next token for pagination.
    Aws::Vector<Aws::String> allProjects;

    do {
        if (!nextToken.empty()) {
            listProjectsRequest.SetNextToken(nextToken);
        }

        Aws::CodeBuild::Model::ListProjectsOutcome outcome = codeBuildClient.ListProjects(
                listProjectsRequest);

        if (outcome.IsSuccess()) {
            const Aws::Vector<Aws::String> &projects = outcome.GetResult().GetProjects();
            allProjects.insert(allProjects.end(), projects.begin(), projects.end());
            nextToken = outcome.GetResult().GetNextToken();
        }

        else {
            std::cerr << "Error listing projects" << outcome.GetError().GetMessage()
                      << std::endl;
        }

    } while (!nextToken.empty());

    std::cout << allProjects.size() << " project(s) found." << std::endl;
    for (auto project: allProjects) {
        std::cout << project << std::endl;
    }

    return true;
}


```

- For API details, see
  [ListProjects](../../../goto/SdkForCpp/codebuild-2016-10-06/ListProjects.md "../../../goto/SdkForCpp/codebuild-2016-10-06/ListProjects.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To get a list of AWS CodeBuild build project names.**

The following `list-projects` example gets a list of CodeBuild build projects sorted by name in ascending order.

```
`aws codebuild list-projects --sort-by `NAME` --sort-order `ASCENDING``

```

The output includes a `nextToken` value which indicates that there is more output available.

```
{
    "nextToken": "Ci33ACF6...The full token has been omitted for brevity...U+AkMx8=",
    "projects": [
        "codebuild-demo-project",
        "codebuild-demo-project2",
            ... The full list of build project names has been omitted for brevity ...
        "codebuild-demo-project99"
    ]
}
```

Run this command again and provide the `nextToken` value from the previous response as a parameter to get the next part of the output. Repeat until you don't receive a `nextToken` value in the response.

```
`aws codebuild list-projects --sort-by `NAME` --sort-order `ASCENDING` --next-token `Ci33ACF6...The` `full` `token` `has` `been` `omitted` `for` `brevity...U+AkMx8=`

`{`
 "projects": `[`
 "codebuild-demo-project100",
 "codebuild-demo-project101",
 `...` `The` `full` `list` `of` `build` `project` `names` `has` `been` `omitted` `for` `brevity` `...`
 `"codebuild-demo-project122"`
 `]`
`}``

```

For more information, see [View a List of Build Project Names (AWS CLI)](view-project-list.md#view-project-list-cli "view-project-list.md#view-project-list-cli") in the _AWS CodeBuild User Guide_.

- For API details, see
  [ListProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-projects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-projects.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
