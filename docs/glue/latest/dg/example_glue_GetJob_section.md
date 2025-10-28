# Use `GetJob` with an AWS SDK or CLI

The following code examples show how to use `GetJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_glue_Scenario_GetStartedCrawlersJobs_section.md "example_glue_Scenario_GetStartedCrawlersJobs_section.md")

CLI

**AWS CLI**

**To retrieve information about a job**

The following `get-job` example retrieves information about a job.

```
`aws glue get-job \
 --job-name `my-testing-job``

```

Output:

```
{
    "Job": {
        "Name": "my-testing-job",
        "Role": "Glue_DefaultRole",
        "CreatedOn": 1602805698.167,
        "LastModifiedOn": 1602805698.167,
        "ExecutionProperty": {
            "MaxConcurrentRuns": 1
        },
        "Command": {
            "Name": "gluestreaming",
            "ScriptLocation": "s3://janetst-bucket-01/Scripts/test_script.scala",
            "PythonVersion": "2"
        },
        "DefaultArguments": {
            "--class": "GlueApp",
            "--job-language": "scala"
        },
        "MaxRetries": 0,
        "AllocatedCapacity": 10,
        "MaxCapacity": 10.0,
        "GlueVersion": "1.0"
    }
}
```

For more information, see [Jobs](aws-glue-api-jobs-job.md "aws-glue-api-jobs-job.md") in the _AWS Glue Developer Guide_.

- For API details, see
  [GetJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/glue#code-examples").

```
const getJob = (jobName) => {
  const client = new GlueClient({});

  const command = new GetJobCommand({
    JobName: jobName,
  });

  return client.send(command);
};


```

- For API details, see
  [GetJob](../../../AWSJavaScriptSDK/v3/latest/client/glue/command/GetJobCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/glue/command/GetJobCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
