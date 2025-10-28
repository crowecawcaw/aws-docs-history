# Creating a project in AWS Device Farm

You can create a project by using the AWS Device Farm console, AWS CLI, or AWS Device Farm API.

## Prerequisites

- Complete the steps in [Setting up](setting-up.md "setting-up.md").

## Create a project (console)

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. Choose **New project**.
4. Enter a name for your project, then choose **Submit**.
5. To specify settings for the project, choose **Project settings**. These settings
   include the default timeout for test runs. After the settings are applied, they are used by all test
   runs for the project. For more information, see [Setting the execution timeout for test runs in
   AWS Device Farm](how-to-set-default-timeout-for-test-runs.md "how-to-set-default-timeout-for-test-runs.md").

## Create a project (AWS CLI)

- Run **create-project**, specifying the project name.

Example:

```
`aws devicefarm create-project --name `MyProjectName``
```

The AWS CLI response includes the Amazon Resource Name (ARN) of the project.

```
`{
 "project": {
 "name": "MyProjectName",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
 "created": 1535675814.414
 }
}`
```

For more information, see [**create-project**](../../../cli/latest/reference/devicefarm/create-project.md "../../../cli/latest/reference/devicefarm/create-project.md") and [AWS CLI reference](cli-ref.md "cli-ref.md").

## Create a project (API)

- Call the [`CreateProject`](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md") API.

For information about using the Device Farm API, see [Automating Device Farm](api-ref.md "api-ref.md").
