# How Image Builder uses the AWS Task Orchestrator and Executor application to manage components

EC2 Image Builder uses the AWS Task Orchestrator and Executor (AWSTOE) application to orchestrate complex workflows, modify
system configurations, and test your images without the need for additional devops scripts or code.
This application manages and runs components that implement its declarative document schema.

AWSTOE is a standalone application that Image Builder installs on its build and test instances when you
create an image. You can also install it manually on EC2 instances to create your own custom components.
It doesn't require any additional setup, and can also run on premises.

###### Contents

- [AWSTOE downloads](#toe-downloads "#toe-downloads")
- [Supported Regions](#toe-supported-regions "#toe-supported-regions")
- [AWSTOE command reference](#toe-commands "#toe-commands")
- [Manual set up to develop custom components with AWSTOE](toe-get-started.md "toe-get-started.md")
- [Use the AWSTOE component document framework for custom components](toe-use-documents.md "toe-use-documents.md")
- [Action modules supported by AWSTOE
  component manager](toe-action-modules.md "toe-action-modules.md")
- [Configure input for the AWSTOE run command](toe-run-config-input.md "toe-run-config-input.md")

## AWSTOE downloads

To install AWSTOE, choose the download link for your architecture and platform. If you attach to
a VPC endpoint for your service (Image Builder, for example), it must have a custom endpoint policy attached
that includes access to the S3 bucket for AWSTOE downloads. Otherwise, your build and test instances
will not be able to download the bootstrap script (`bootstrap.sh`) and install
the AWSTOE application. For more information see [Create a VPC endpoint policy for
Image Builder](vpc-interface-endpoints.md#vpc-endpoint-policy "vpc-interface-endpoints.md#vpc-endpoint-policy").

###### Important

AWS is phasing out support for TLS versions 1.0 and 1.1. To access the S3 bucket
for AWSTOE downloads, your client software must use TLS version 1.2 or later. For more
information, see this [AWS Security Blog post](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/").

| Architecture | Platform                                                                                                                                 | Download link                                                                           | Example                                                                                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 386          | AL 2 and 2023<br>RHEL 7, 8, and 9<br>Ubuntu 16.04, 18.04, 20.04, 22.04, and 24.04<br>CentOS 7 and 8<br>SUSE 12 and 15                    | `https://awstoe-`<region>`.s3.`<region>`.amazonaws.com/latest/linux/386/awstoe`         | [https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/386/awstoe](https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/386/awstoe "https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/386/awstoe")                         |
| AMD64        | AL 2 and 2023<br>RHEL 7, 8, and 9<br>Ubuntu 16.04, 18.04, 20.04, 22.04, and 24.04<br>CentOS 7 and 8<br>CentOS Stream 8<br>SUSE 12 and 15 | `https://awstoe-`<region>`.s3.`<region>`.amazonaws.com/latest/linux/amd64/awstoe`       | [https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/amd64/awstoe](https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/amd64/awstoe "https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/amd64/awstoe")                   |
| AMD64        | macOS 10.14.x (Mojave), 10.15.x (Catalina), 11.x (Big Sur), 12.x (Monterey)                                                              | `https://awstoe-`region`.s3.`region`.amazonaws.com/latest/darwin/amd64/awstoe`          | [https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/darwin/amd64/awstoe](https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/darwin/amd64/awstoe "https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/darwin/amd64/awstoe")                |
| AMD64        | Windows Server 2012 R2, 2016, 2019, and 2022                                                                                             | `https://awstoe-`<region>`.s3.`<region>`.amazonaws.com/latest/windows/amd64/awstoe.exe` | [https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/amd64/awstoe.exe](https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/amd64/awstoe.exe "https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/amd64/awstoe.exe") |
| ARM64        | AL 2 and 2023<br>RHEL 7, 8, and 9<br>Ubuntu 16.04, 18.04, 20.04, 22.04, and 24.04<br>CentOS 7 and 8<br>CentOS Stream 8<br>SUSE 12 and 15 | `https://awstoe-`<region>`.s3.`<region>`.amazonaws.com/latest/linux/arm64/awstoe`       | [https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/arm64/awstoe](https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/arm64/awstoe "https://awstoe-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/arm64/awstoe")                   |

## Supported Regions

AWSTOE is supported as a standalone application in the following Regions.

| AWS Region name           | AWS Region     |
| ------------------------- | -------------- |
| US East (Ohio)            | us-east-2      |
| US East (N. Virginia)     | us-east-1      |
| AWS GovCloud (US-East)    | us-gov-east-1  |
| AWS GovCloud (US-West)    | us-gov-west-1  |
| US West (N. California)   | us-west-1      |
| US West (Oregon)          | us-west-2      |
| Africa (Cape Town)        | af-south-1     |
| Asia Pacific (Hong Kong)  | ap-east-1      |
| Asia Pacific (Osaka)      | ap-northeast-3 |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Hyderabad)  | ap-south-2     |
| Asia Pacific (Singapore)  | ap-southeast-1 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Jakarta)    | ap-southeast-3 |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Canada (Central)          | ca-central-1   |
| Europe (Frankfurt)        | eu-central-1   |
| Europe (Zurich)           | eu-central-2   |
| Europe (Stockholm)        | eu-north-1     |
| Europe (Milan)            | eu-south-1     |
| Europe (Spain)            | eu-south-2     |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Paris)            | eu-west-3      |
| Israel (Tel Aviv)         | il-central-1   |
| Middle East (UAE)         | me-central-1   |
| Middle East (Bahrain)     | me-south-1     |
| South America (São Paulo) | sa-east-1      |
| China (Beijing)           | cn-north-1     |
| China (Ningxia)           | cn-northwest-1 |

## AWSTOE command reference

AWSTOE is a command line component management application that runs on Amazon EC2 instances.
When Image Builder launches an EC2 build or test instance, it installs AWSTOE on the instance. Then it
runs AWSTOE commands in the AWS CLI to install or validate the components that are specified
in the image or container recipe.

###### Note

Some AWSTOE action modules require elevated permissions to run on a Linux server.
To use elevated permissions, prefix the command syntax with **sudo**, or run the
**sudo su** command one time when you log in before running the
commands linked below. For more information about AWSTOE action modules, see
[Action modules supported by AWSTOE
component manager](toe-action-modules.md "toe-action-modules.md").

**_[run](#cmd-run "#cmd-run")_**

Use the **run** command to run the YAML document
scripts for one or more component documents.

**_[validate](#cmd-validate "#cmd-validate")_**

Run the **validate** command to validate the YAML
document syntax for one or more component documents.

### awstoe run command

This command runs the YAML component document scripts in the order
in which they are included in the configuration file specified by the
`--config` parameter, or the list of component documents
specified by the `--documents` parameter.

###### Note

You must specify exactly one of the following parameters, never both:

--config

--documents

#### Syntax

```
awstoe run [--config <file path>] [--cw-ignore-failures <?>]
      [--cw-log-group <?>] [--cw-log-region `us-west-2`] [--cw-log-stream <?>]
      [--document-s3-bucket-owner <owner>] [--documents <file path,file path,...>]
      [--execution-id <?>] [--log-directory <file path>]
      [--log-s3-bucket-name <name>] [--log-s3-bucket-owner <owner>]
      [--log-s3-key-prefix <?>] [--parameters `name1`=`value1`,`name2`=`value2`...]
      [--phases <phase name>] [--state-directory <directory path>] [--version <?>]
      [--help] [--trace]
```

#### Parameters and options

###### Parameters

**--config `./config-example.json`**

Short form: -c `./config-example.json`

The configuration file _(conditional)_.
This parameter contains the file location for the JSON file that contains
configuration settings for the components this command is running. If you
specify **run** command settings in a configuration file,
you must not specify the `--documents` parameter. For more
information about input configuration, see [Configure input for the AWSTOE run command](toe-run-config-input.md "toe-run-config-input.md").

Valid locations include:

- A local file path (`./config-example.json`)
- An S3 URI (`s3://`bucket/key``)

**--cw-ignore-failures**

Short form: N/A

Ignore logging failures from the CloudWatch Logs.

**--cw-log-group**

Short form: N/A

The `LogGroup` name for the CloudWatch Logs.

**--cw-log-region**

Short form: N/A

The AWS Region that applies to the CloudWatch Logs.

**--cw-log-stream**

Short form: N/A

The `LogStream` name for the CloudWatch Logs,
that directs AWSTOE where to stream the `console.log` file.

**--document-s3-bucket-owner**

Short form: N/A

The account ID of the bucket owner for S3 URI-based documents.

**--documents ``./doc-1.yaml`,`./doc-n.yaml``**

Short form: -d `./doc-1.yaml`,`./doc-n`

The component documents _(conditional)_.
This parameter contains a comma-separated list of file locations for the
YAML component documents to run. If you specify YAML documents for the
**run** command using the `--documents` parameter,
you must not specify the `--config` parameter.

Valid locations include:

- local file paths (`./component-doc-example.yaml`).
- S3 URIs (`s3://`bucket/key``).
- Image Builder component build version ARNs
  (arn:aws:imagebuilder:us-west-`2:123456789012`:component/`my-example-component`/2021.12.02/1).

###### Note

There are no spaces between items in the list, only commas.

**--execution-id**

Short form: -i

This is the unique ID that applies to the execution of the current
**run** command. This ID is included in output and log file names, to uniquely
identify those files, and link them to the current command execution. If this setting is left
out, AWSTOE generates a GUID.

**--log-directory**

Short form: -l

The destination directory where AWSTOE stores all of the
log files from this command execution. By default, this
directory is located inside of the following parent directory:
`TOE_<DATETIME>_<EXECUTIONID>`. If you do not
specify the log directory, AWSTOE uses the current working
directory (`.`).

**--log-s3-bucket-name**

Short form: -b

If component logs are stored in Amazon S3 (recommended), AWSTOE uploads the
component application logs to the S3 bucket named in this parameter.

**--log-s3-bucket-owner**

Short form: N/A

If component logs are stored in Amazon S3 (recommended), this is the
owner account ID for the bucket where AWSTOE writes the log files.

**--log-s3-key-prefix**

Short form: -k

If component logs are stored in Amazon S3 (recommended), this is the
S3 object key prefix for the log location in the bucket.

**--parameters `name1`=`value1`,`name2`=`value2`...**

Short form: N/A

Parameters are mutable variables that are defined in the component
document, with settings that the calling application can provide at
runtime.

**--phases**

Short form: -p

A comma-separated list that specifies which phases to run from the YAML component
documents. If a component document includes additional phases, those will
not run.

**--state-directory**

Short form: -s

The file path where state tracking files are stored.

**--version**

Short form: -v

Specifies the component application version.

###### Options

**--help**

Short form: -h

Displays a help manual for using the component management
application options.

**--trace**

Short form: -t

Enables verbose logging to the console.

### awstoe validate command

When you run this command, it validates the YAML document syntax for each
of the component documents specified by the `--documents` parameter.

#### Syntax

```
awstoe validate [--document-s3-bucket-owner <owner>]
      --documents <file path,file path,...> [--help] [--trace]
```

#### Parameters and options

###### Parameters

**--document-s3-bucket-owner**

Short form: N/A

Source account ID of S3 URI-based documents provided.

**--documents ``./doc-1.yaml`,`./doc-n.yaml``**

Short form: -d `./doc-1.yaml`,`./doc-n`

The component documents _(required)_.
This parameter contains a comma-separated list of file locations for the
YAML component documents to run. Valid locations include:

- local file paths (`./component-doc-example.yaml`)
- S3 URIs (`s3://`bucket/key``)
- Image Builder component build version ARNs
  (arn:aws:imagebuilder:us-west-`2:123456789012`:component/`my-example-component`/2021.12.02/1)

###### Note

There are no spaces between items in the list, only commas.

###### Options

**--help**

Short form: -h

Displays a help manual for using the component management
application options.

**--trace**

Short form: -t

Enables verbose logging to the console.
