AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Session document schema

The following information describes the schema elements of a Session document.
AWS Systems Manager Session Manager uses Session documents to determine which type of session to start,
such as a standard session, a port forwarding session, or a session to run an
interactive command.

[schemaVersion](#version "#version")

The schema version of the Session document. Session documents only support
version 1.0.

Type: String

Required: Yes

[description](#descript "#descript")

A description you specify for the Session document. For example, "Document
to start port forwarding session with Session Manager".

Type: String

Required: No

[sessionType](#type "#type")

The type of session the Session document is used to establish.

Type: String

Required: Yes

Valid values: `InteractiveCommands` |
`NonInteractiveCommands` | `Port` |
`Standard_Stream`

[inputs](#in "#in")

The session preferences to use for sessions established using this Session
document. This element is required for Session documents that are used to
create `Standard_Stream` sessions.

Type: StringMap

Required: No

[s3BucketName](#bucket "#bucket")

The Amazon Simple Storage Service (Amazon S3) bucket you want to send session logs to at
the end of your sessions.

Type: String

Required: No

[s3KeyPrefix](#prefix "#prefix")

The prefix to use when sending logs to the Amazon S3 bucket you
specified in the `s3BucketName` input. For more
information about using a shared prefix with objects stored in
Amazon S3, see [How do I
use folders in an S3 bucket?](../../../AmazonS3/latest/user-guide/using-folders.md "../../../AmazonS3/latest/user-guide/using-folders.md") in the
_Amazon Simple Storage Service User Guide_.

Type: String

Required: No

[s3EncryptionEnabled](#s3Encrypt "#s3Encrypt")

If set to `true`, the Amazon S3 bucket you specified in
the `s3BucketName` input must be encrypted.

Type: Boolean

Required: Yes

[cloudWatchLogGroupName](#logGroup "#logGroup")

The name of the Amazon CloudWatch Logs (CloudWatch Logs) group you want to send
session logs to at the end of your sessions.

Type: String

Required: No

[cloudWatchEncryptionEnabled](#cwEncrypt "#cwEncrypt")

If set to `true`, the log group you specified in
the `cloudWatchLogGroupName` input must be
encrypted.

Type: Boolean

Required: Yes

[cloudWatchStreamingEnabled](#cwStream "#cwStream")

If set to `true`, a continual stream of session
data logs are sent to the log group you specified in the
`cloudWatchLogGroupName` input. If set to
`false`, session logs are sent to the log group
you specified in the `cloudWatchLogGroupName` input
at the end of your sessions.

Type: Boolean

Required: Yes

[kmsKeyId](#kms "#kms")

The ID of the AWS KMS key you want to use to further
encrypt data between your local client machines and the
Amazon Elastic Compute Cloud (Amazon EC2) managed nodes you connect to.

Type: String

Required: No

[runAsEnabled](#run "#run")

If set to `true`, you must specify a user account
that exists on the managed nodes you will be connecting to in
the `runAsDefaultUser` input. Otherwise, sessions
will fail to start. By default, sessions are started using the
`ssm-user` account created by the AWS Systems Manager
SSM Agent. The Run As feature is only supported for connecting to
Linux and macOS managed nodes.

Type: Boolean

Required: Yes

[runAsDefaultUser](#runUser "#runUser")

The name of the user account to start sessions with on
Linux and macOS managed nodes when the
`runAsEnabled` input is set to `true`.
The user account you specify for this input must exist on the
managed nodes you will be connecting to; otherwise, sessions
will fail to start.

Type: String

Required: No

[idleSessionTimeout](#timeout "#timeout")

The amount of time of inactivity you want to allow before a
session ends. This input is measured in minutes.

Type: String

Valid values: 1-60

Required: No

[maxSessionDuration](#maxDuration "#maxDuration")

The maximum amount of time you want to allow before a session
ends. This input is measured in minutes.

Type: String

Valid values: 1-1440

Required: No

[shellProfile](#shell "#shell")

The preferences you specify per operating system to apply
within sessions such as shell preferences, environment
variables, working directories, and running multiple commands
when a session is started.

Type: StringMap

Required: No

[windows](#win "#win")

The shell preferences, environment variables,
working directories, and commands you specify for
sessions on Windows Server managed nodes.

Type: String

Required: No

[linux](#lin "#lin")

The shell preferences, environment variables,
working directories, and commands you specify for
sessions on Linux and macOS managed
nodes.

Type: String

Required: No

[parameters](#param "#param")

An object that defines the parameters the document accepts. For more
information about defining document parameters, see **parameters** in the [Top-level data elements](documents-syntax-data-elements-parameters.md#top-level "documents-syntax-data-elements-parameters.md#top-level"). For parameters that you reference often, we
recommend that you store those parameters in Systems Manager Parameter Store and then
reference them. You can reference `String` and
`StringList` Parameter Store parameters in this section of a
document. You can't reference `SecureString` Parameter Store parameters
in this section of a document. You can reference a Parameter Store parameter using
the following format.

```
{{ssm:`parameter-name`}}
```

For more information about Parameter Store, see [AWS Systems Manager Parameter Store](systems-manager-parameter-store.md "systems-manager-parameter-store.md").

Type: StringMap

Required: No

[properties](#props "#props")

An object whose values you specify that are used in the
`StartSession` API operation.

For Session documents that are used for `InteractiveCommands`
sessions, the properties object includes the commands to run on the
operating systems you specify. You can also determine whether commands are
run as `root` using the `runAsElevated` boolean
property. For more information, see [Restrict access to commands in a session](session-manager-restrict-command-access.md "session-manager-restrict-command-access.md").

For Session documents that are used for `Port` sessions, the
properties object contains the port number where traffic should be
redirected to. For an example, see the `Port` type Session
document example later in this topic.

Type: StringMap

Required: No

`Standard_Stream` type Session document example

YAML

```
---
schemaVersion: '1.0'
description: Document to hold regional settings for Session Manager
sessionType: Standard_Stream
inputs:
  s3BucketName: ''
  s3KeyPrefix: ''
  s3EncryptionEnabled: true
  cloudWatchLogGroupName: ''
  cloudWatchEncryptionEnabled: true
  cloudWatchStreamingEnabled: true
  kmsKeyId: ''
  runAsEnabled: true
  runAsDefaultUser: ''
  idleSessionTimeout: '20'
  maxSessionDuration: '60'
  shellProfile:
    windows: ''
    linux: ''
```

JSON

```
{
    "schemaVersion": "1.0",
    "description": "Document to hold regional settings for Session Manager",
    "sessionType": "Standard_Stream",
    "inputs": {
        "s3BucketName": "",
        "s3KeyPrefix": "",
        "s3EncryptionEnabled": true,
        "cloudWatchLogGroupName": "",
        "cloudWatchEncryptionEnabled": true,
        "cloudWatchStreamingEnabled": true,
        "kmsKeyId": "",
        "runAsEnabled": true,
        "runAsDefaultUser": "",
        "idleSessionTimeout": "20",
        "maxSessionDuration": "60",
        "shellProfile": {
            "windows": "date",
            "linux": "pwd;ls"
        }
    }
}
```

`InteractiveCommands` type Session document example

YAML

```
---
schemaVersion: '1.0'
description: Document to view a log file on a Linux instance
sessionType: InteractiveCommands
parameters:
  logpath:
    type: String
    description: The log file path to read.
    default: "/var/log/amazon/ssm/amazon-ssm-agent.log"
    allowedPattern: "^[a-zA-Z0-9-_/]+(.log)$"
properties:
  linux:
    commands: "tail -f {{ logpath }}"
    runAsElevated: true
```

JSON

```
{
    "schemaVersion": "1.0",
    "description": "Document to view a log file on a Linux instance",
    "sessionType": "InteractiveCommands",
    "parameters": {
        "logpath": {
            "type": "String",
            "description": "The log file path to read.",
            "default": "/var/log/amazon/ssm/amazon-ssm-agent.log",
            "allowedPattern": "^[a-zA-Z0-9-_/]+(.log)$"
        }
    },
    "properties": {
        "linux": {
            "commands": "tail -f {{ logpath }}",
            "runAsElevated": true
        }
    }
}
```

`Port` type Session document example

YAML

```
---
schemaVersion: '1.0'
description: Document to open given port connection over Session Manager
sessionType: Port
parameters:
  paramExample:
    type: string
    description: document parameter
properties:
  portNumber: `anyPortNumber`
```

JSON

```
{
    "schemaVersion": "1.0",
    "description": "Document to open given port connection over Session Manager",
    "sessionType": "Port",
    "parameters": {
        "paramExample": {
            "type": "string",
            "description": "document parameter"
        }
    },
    "properties": {
        "portNumber": "anyPortNumber"
    }
}
```

Session document example with special characters

YAML

```
---
schemaVersion: '1.0'
description: Example document with quotation marks
sessionType: InteractiveCommands
parameters:
  Test:
    type: String
    description: Test Input
    maxChars: 32
properties:
  windows:
    commands: |
        $Test = '{{ Test }}'
        $myVariable = \"Computer name is $env:COMPUTERNAME\"
        Write-Host "Test variable: $myVariable`.`nInput parameter: $Test"
    runAsElevated: false
```

JSON

```
{
   "schemaVersion":"1.0",
   "description":"Test document with quotation marks",
   "sessionType":"InteractiveCommands",
   "parameters":{
      "Test":{
         "type":"String",
         "description":"Test Input",
         "maxChars":32
      }
   },
   "properties":{
      "windows":{
         "commands":[
            "$Test = '{{ Test }}'",
            "$myVariable = \\\"Computer name is $env:COMPUTERNAME\\\"",
            "Write-Host \"Test variable: $myVariable`.`nInput parameter: $Test\""
         ],
         "runAsElevated":false
      }
   }
}
```
