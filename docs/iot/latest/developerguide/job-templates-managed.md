# Use AWS managed templates to deploy common

remote operations

AWS managed templates are job templates provided by AWS. They're used for
frequently performed remote actions such as rebooting, downloading a file, or installing
an application on your devices. These templates have a predefined job document for each
remote action so you don't have to create your own job document.

You can choose from a set of predefined configurations and create jobs using these
templates without writing any additional code. Using managed templates, you can view the
job document deployed to your fleets. You can create a job using these templates and
create a custom job template that you can reuse for your remote operations.

## What do managed templates

contain?

Each AWS managed template contains:

- The environment to run the commands in the job document.
- A job document that specifies the name of the operation and its
  parameters. For example, if you use a **Download file**
  template, the operation name is _Download
  file_ and the parameters can be:

      + The URL of the file that you want to download to your device. This
       can be an internet resource or a public or pre-signed
       Amazon Simple Storage Service((Amazon S3) URL.
      + A local file path on the device to store the downloaded
       file.

  For more information about the job documents and its parameters, see [Managed template remote actions and
  job documents](#job-template-manage-actions "#job-template-manage-actions").

## Prerequisites

For your devices to run the remote actions specified by the managed template job
document, you must:

- Install the specific software on your
  device

Use your own device software and job handlers, or the AWS IoT Device Client.
Depending on your business case, you can also run them both so that they
perform different functions.

    + Use your own device software and job handlers


    You can write your own code for the devices by using the AWS IoT Device SDK
     and its library of handlers that support the remote operations. To
     deploy and run jobs, verify that the device agent libraries have
     been installed correctly and are running on the devices.


    You can also choose to use your own handlers that support the
     remote operations. For more information, see [Sample job handlers](https://github.com/awslabs/aws-iot-device-client/tree/main/sample-job-handlers "https://github.com/awslabs/aws-iot-device-client/tree/main/sample-job-handlers") in the AWS IoT Device Client GitHub
     repository.
    + Use the AWS IoT Device Client


    Or, you can install and run the AWS IoT Device Client on your devices because it supports using all managed templates directly from the console by default.


    The Device Client is an open-source software written in C++ that you can
     compile and install on your embedded Linux-based IoT devices. The Device
     Client has a *base client* and discrete
     *client-side features*. The base client
     establishes connectivity with AWS IoT over MQTT protocol and can connect with
     the different client-side features.


    To perform remote operations on your devices, use the *client-side Jobs feature* of the Device Client. This
     feature contains a parser to receive the job document and job handlers that
     implement the remote actions specified in the job document. For more information
     about the Device Client and its features, see [AWS IoT
     Device Client](https://github.com/awslabs/aws-iot-device-client#readme "https://github.com/awslabs/aws-iot-device-client#readme").


    When running on devices, the Device Client receives the job
     document and has a platform-specific implementation that it uses to
     run commands in the document. For more information about setting up
     the Device Client and using the Jobs feature, see [AWS IoT tutorials](iot-tutorials.md "iot-tutorials.md").

- Use a supported environment

For each managed template, you'll find information about the environment
that you can use to run the remote actions. We recommend that you use the
template with a supported Linux environment as specified in the template.
Use the AWS IoT Device Client to run the managed template remote actions
because it supports common microprocessors and Linux environments, like
Debian and Ubuntu.

## Managed template remote actions and

job documents

The following section lists the different AWS managed templates for AWS IoT Jobs,
and describes the remote actions that can be performed on the devices. The following
section has information about the job document and a description of the job document
parameters for each remote action. Your device-side software uses the template name
and the parameters to perform the remote action.

AWS managed templates accept input parameters for which you specify a value when
creating a job using the template. All managed templates have two optional input
parameters in common: `runAsUser` and `pathToHandler`. Except
for the `AWS-Reboot` template, the templates require additional input
parameters for which you must specify a value when creating a job using the
template. These required input parameters vary depending on the template that you
choose. For example, if you choose the `AWS-Download-File` template, you
must specify a list of packages to install, and a URL to download files from.

Specify a value for the input parameters when using the AWS IoT console or the
AWS Command Line Interface (AWS CLI) to create a job that uses a managed template. When using the CLI,
provide these values by using the `document-parameters` object. For more
information, see [documentParameters](../apireference/API_CreateJob.md#iot-CreateJob-request-documentParameters "../apireference/API_CreateJob.md#iot-CreateJob-request-documentParameters").

###### Note

Use `document-parameters` only when creating jobs from AWS
managed templates. This parameter can't be used with custom job templates or to
create jobs from them.

The following shows a description of the common optional input parameters. You'll
see a description of other input parameters that each managed template requires in
the next section.

`runAsUser`

This parameter specifies whether to run the job handler as another
user. If it's not specified during job creation, the job handler is run
as the same user as the Device Client. When you run the job handler as
another user, specify a string value that's not longer than 256
characters.

`pathToHandler`

The path to the job handler running on the device. If it's not
specified during job creation, the Device Client uses the current
working directory.

The following shows the different remote actions, their job documents, and
parameters that they accept. All these templates support the Linux environment for
running the remote operation on the device.

###### Template name

`AWS–Download–File`

###### Template description

A managed template provided by AWS for downloading a file.

###### Input parameters

This template has the following required parameters. You can also specify
the optional parameters `runAsUser` and `pathToHandler`.

`downloadUrl`

The URL to download the file from. This can be an internet
resource, an object in Amazon S3 that can be publicly accessed, or an
object in Amazon S3 that can only be accessed by your device using a
presigned URL. For more information about using presigned URLs
and granting permissions, see [Presigned URLs](create-manage-jobs.md#create-manage-jobs-presigned-URLs "create-manage-jobs.md#create-manage-jobs-presigned-URLs").

`filePath`

A local file path that shows the location in the device to
store the downloaded file.

###### Device behavior

The device downloads the file from the specified location,
verifies that the download is complete, and stores it
locally.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`download-file.sh`, that the job handler must run to
download the file. It also shows the required parameters
`downloadUrl` and `filePath`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Download-File",
        "type": "runHandler",
        "input": {
          "handler": "download-file.sh",
          "args": [
            "${aws:iot:parameter:downloadUrl}",
            "${aws:iot:parameter:filePath}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Install–Application`

###### Template description

A managed template provided by AWS for installing one or more
applications.

###### Input parameters

This template has the following required parameter,
`packages`. You can also specify the optional parameters
`runAsUser` and `pathToHandler`.

`packages`

A space-separated list of one or more applications to be
installed.

###### Device behavior

The device installs the applications as specified in the job
document.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`install-packages.sh`, that the job handler must run to
download the file. It also shows the required parameter
`packages`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Install-Application",
        "type": "runHandler",
        "input": {
          "handler": "install-packages.sh",
          "args": [
            "${aws:iot:parameter:packages}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Reboot`

###### Template description

A managed template provided by AWS for rebooting your device.

###### Input parameters

This template has no required parameters. You can specify the optional
parameters `runAsUser` and `pathToHandler`.

###### Device behavior

The device reboots successfully.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`reboot.sh`, that the job handler must run to reboot the
device.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Reboot",
        "type": "runHandler",
        "input": {
          "handler": "reboot.sh",
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Remove–Application`

###### Template description

A managed template provided by AWS for uninstalling one or more
applications.

###### Input parameters

This template has the following required parameter,
`packages`. You can also specify the optional parameters
`runAsUser` and `pathToHandler`.

`packages`

A space-separated list of one or more applications to be
uninstalled.

###### Device behavior

The device uninstalls the applications as specified in the job
document.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`remove-packages.sh`, that the job handler must run to
download the file. It also shows the required parameter
`packages`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Remove-Application",
        "type": "runHandler",
        "input": {
          "handler": "remove-packages.sh",
          "args": [
            "${aws:iot:parameter:packages}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Restart–Application`

###### Template description

A managed template provided by AWS for stopping and restarting one
or more services.

###### Input parameters

This template has the following required parameter,
`services`. You can also specify the optional parameters
`runAsUser` and `pathToHandler`.

###### Services

A space-separated list of one or more applications to be restarted.

###### Device behavior

The specified applications are stopped and then restarted on
the device.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`restart-services.sh`, that the job handler must run to
restart the system services. It also shows the required parameter
`services`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Restart-Application",
        "type": "runHandler",
        "input": {
          "handler": "restart-services.sh",
          "args": [
            "${aws:iot:parameter:services}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS-Start-Application`

###### Template description

A managed template provided by AWS for starting one or more
services.

###### Input parameters

This template has the following required parameter,
`services`. You can also specify the optional parameters
`runAsUser` and `pathToHandler`.

`services`

A space-separated list of one or more applications to be
started.

###### Device behavior

The specified applications start running on the device.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`start-services.sh`, that the job handler must run to
start the system services. It also shows the required parameter
`services`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Start-Application",
        "type": "runHandler",
        "input": {
          "handler": "start-services.sh",
          "args": [
            "${aws:iot:parameter:services}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Stop–Application`

###### Template description

A managed template provided by AWS for stopping one or more
services.

###### Input parameters

This template has the following required parameter,
`services`. You can also specify the optional parameters
`runAsUser` and `pathToHandler`.

`services`

A space-separated list of one or more applications to be
stopped.

###### Device behavior

The specified applications stop running on the device.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job handler and the shell script,
`stop-services.sh`, that the job handler must run to stop
the system services. It also shows the required parameter
`services`.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Stop-Application",
        "type": "runHandler",
        "input": {
          "handler": "stop-services.sh",
          "args": [
            "${aws:iot:parameter:services}"
          ],
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Template name

`AWS–Run–Command`

###### Template description

A managed template provided by AWS for running a shell
command.

###### Input parameters

This template has the following required parameter,
`command`. You can also specify the optional parameter
`runAsUser`.

`command`

A comma separated string of command. Any comma contained in the command
itself must be escaped.

###### Device behavior

The device runs the shell command as specified in the job
document.

###### Job document

The following shows the job document and its latest version. The
template shows the path to the job command and the command that you
provided which the device will run.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Run-Command",
        "type": "runCommand",
        "input": {
          "command": "${aws:iot:parameter:command}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

###### Topics

- [Create a job from AWS managed
  templates by using the AWS Management Console](job-template-manage-console-create.md "job-template-manage-console-create.md")
- [Create a job from AWS managed
  templates by using the AWS CLI](job-template-manage-cli-create.md "job-template-manage-cli-create.md")
