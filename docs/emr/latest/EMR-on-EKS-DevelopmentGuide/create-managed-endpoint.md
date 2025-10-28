# Creating an interactive endpoint for your virtual

cluster

This topic describes a couple ways to create an interactive endpoint using the AWS Command Line
Interface (AWS CLI) and includes details on available configuration parameters.

## Create an interactive endpoint with the

`create-managed-endpoint` command

Specify the parameters in the `create-managed-endpoint` command as follows.
Amazon EMR on EKS supports creating interactive endpoints with Amazon EMR releases 6.7.0 and
higher.

```
aws emr-containers create-managed-endpoint \
‐‐type JUPYTER_ENTERPRISE_GATEWAY \
‐‐virtual‐cluster‐id `1234567890abcdef0xxxxxxxx` \
‐‐name `example-endpoint-name` \
‐‐execution-role-arn arn:aws:iam::444455556666:role/`JobExecutionRole` \
‐‐release-label `emr-6.9.0-latest` \
‐‐configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "spark-defaults",
        "properties": {
            "spark.driver.memory": "2G"
        }
    }],
    "monitoringConfiguration": {
        "cloudWatchMonitoringConfiguration": {
            "logGroupName": "`log_group_name`",
            "logStreamNamePrefix": "`log_stream_prefix`"
        },
        "persistentAppUI": "ENABLED",
        "s3MonitoringConfiguration": {
            "logUri": "s3://`my_s3_log_location`"
        }
    }
}'
```

For more information, see [Parameters for creating an interactive
endpoint](#parameters-for-creating "#parameters-for-creating").

## Create an interactive endpoint with specified

parameters in a JSON file

1. Create a `create-managed-endpoint-request.json` file and specify the
   required parameters for your endpoint, as shown in the following JSON file:

```
{
    "name": "`MY_TEST_ENDPOINT`",
    "virtualClusterId": "`MY_CLUSTER_ID`",
    "type": "JUPYTER_ENTERPRISE_GATEWAY",
    "releaseLabel": "`emr-6.9.0-latest`",
    "executionRoleArn": "arn:aws:iam::444455556666:role/`JobExecutionRole`",
    "configurationOverrides":
    {
        "applicationConfiguration":
        [
            {
                "classification": "spark-defaults",
                "properties":
                {
                    "spark.driver.memory": "8G"
                }
            }
        ],
        "monitoringConfiguration":
        {
            "persistentAppUI": "ENABLED",
            "cloudWatchMonitoringConfiguration":
            {
                "logGroupName": "`my_log_group`",
                "logStreamNamePrefix": "`log_stream_prefix`"
            },
            "s3MonitoringConfiguration":
            {
                "logUri": "s3://`my_s3_log_location`"
            }
        }
    }
}
```

2. Use the `create-managed-endpoint` command with a path to the
   `create-managed-endpoint-request.json` file that is stored locally
   or in Amazon S3.

```
aws emr-containers create-managed-endpoint \
‐‐cli-input-json  file://./create-managed-endpoint-request.json ‐‐region `AWS-Region`
```

## Output of create interactive

endpoint

You should see the following output in the terminal. The output includes the name and
identifier of your new interactive endpoint:

```
{
    "id": "`1234567890abcdef0`",
    "name": "`example-endpoint-name`",
    "arn": "arn:aws:emr-containers:`us-west-2:111122223333`:/virtualclusters/`444455556666`/endpoints/`444455556666`",
    "virtualClusterId": "`111122223333xxxxxxxx`"
}
```

Running `aws emr-containers create-managed-endpoint` creates a self-signed
certificate that allows HTTPS communication between EMR Studio and the interactive
endpoint server.

If you run `create-managed-endpoint` and haven't completed the prerequisites,
Amazon EMR returns an error message with the actions that you must take to continue.

## Parameters for creating an interactive

endpoint

###### Topics

- [Required parameters for interactive
  endpoints](#parameters-for-creating-required "#parameters-for-creating-required")
- [Optional parameters for interactive
  endpoints](#parameters-for-creating-optional "#parameters-for-creating-optional")

### Required parameters for interactive

endpoints

You must specify the following parameters when you create an interactive
endpoint:

**`‐‐type`**

Use `JUPYTER_ENTERPRISE_GATEWAY`. This is the only supported
type.

**`‐‐virtual-cluster-id`**

The identifier of the virtual cluster that you registered with Amazon EMR on EKS.

**`‐‐name`**

A descriptive name for the interactive endpoint that helps EMR Studio users
select it from the dropdown list.

**`‐‐execution-role-arn`**

The Amazon Resource Name (ARN) of your IAM job execution role for Amazon EMR on EKS
that was created as part of the prerequisites.

**`‐‐release-label`**

The release label of the Amazon EMR release to use for the endpoint. For example,
`emr-6.9.0-latest`. Amazon EMR on EKS supports interactive endpoints with Amazon EMR
releases 6.7.0 and higher.

### Optional parameters for interactive

endpoints

Optionally, you can also specify the following parameters when you create an
interactive endpoint:

**`‐‐configuration-overrides`**

To override the default configurations for applications, supply a coonfiguration
object. You can use a shorthand syntax to provide the configuration, or you can
reference the configuration object in a JSON file.

Configuration objects consist of a classification, properties, and optional
nested configurations. Properties consist of the settings that you want to override
in that file. You can specify multiple classifications for multiple applications in
a single JSON object. The configuration classifications that are available vary by
Amazon EMR on EKS release. For a list of configuration classifications that are available
for each release of Amazon EMR on EKS, see [Amazon EMR on EKS releases](emr-eks-releases.md "emr-eks-releases.md"). In addition to the configuration
classifications listed for each release, interactive endpoints bring in the
additional classification `jeg-config`. For more information, see [Jupyter Enterprise Gateway (JEG) configuration
options](jeg-config-options.md "jeg-config-options.md").
