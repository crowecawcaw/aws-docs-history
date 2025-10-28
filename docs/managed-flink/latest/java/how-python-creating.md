Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create your Managed Service for Apache Flink Python application

## Specify your code files

Once you have created your application's code package, you upload it to an Amazon S3 bucket. You then
create your application using either the console or the
[CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md") action.

When you create your application using the
[CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md") action,
you specify the code files and archives in your zip file using a special application property group
called `kinesis.analytics.flink.run.options`. You can define the following types files:

- **python**: A text file containing a Python main method.
- **jarfile**: A Java JAR file containing Java user-defined functions.
- **pyFiles**: A Python resource file containing resources to be used by the application.
- **pyArchives**: A zip file containing resource files for the application.

For more information about Apache Flink Python code file types, see
[Command-Line Interface](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/deployment/cli/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/deployment/cli/") in the Apache Flink Documentation.

###### Note

Managed Service for Apache Flink does not support the `pyModule`, `pyExecutable`, or
`pyRequirements` file types. All of the code, requirements, and dependencies must be in your zip file. You can't specify
dependencies to be installed using pip.

The following example json snippet demonstrates how to specify file locations within your application's zip file:

```
"ApplicationConfiguration": {
    "EnvironmentProperties": {
      "PropertyGroups": [
        {
          "PropertyGroupId": "kinesis.analytics.flink.run.options",
          "PropertyMap": {
            "python": "MyApplication/main.py",
            "jarfile": "MyApplication/lib/myJarFile.jar",
            "pyFiles": "MyApplication/lib/myDependentFile.py",
            "pyArchives": "MyApplication/lib/myArchive.zip"
          }
        },
```
