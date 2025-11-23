# Preparing AWS IoT Jobs

AWS IoT Device Management Software Package Catalog extends AWS IoT Jobs through substitution parameters, and integration with AWS IoT fleet indexing, dynamic thing groups, and the AWS IoT thing’s reserved named shadow.

###### Note

To use all the functionality that Software Package Catalog offers, you must create these AWS Identity and Access Management (IAM) roles and policies: [AWS IoT Jobs rights to deploy package versions](preparing-security.md#job-rights-deploy-versions "preparing-security.md#job-rights-deploy-versions") and [AWS IoT Jobs rights to update the reserved named shadow](preparing-security.md#job-rights-update-reserved-named-shadow "preparing-security.md#job-rights-update-reserved-named-shadow"). For more information, see [Preparing security](preparing-security.md "preparing-security.md").

## Substitution parameters for AWS IoT jobs

You can use substitution parameters as a placeholder within your AWS IoT job document. When the job service encounters a substitution parameter, it points the job to a named software version’s attribute for the parameter value. You can use this process to create a single job document and pass the metadata into the job through general-purpose attributes. For example, you might pass an Amazon Simple Storage Service(Amazon S3) URL, a software package Amazon Resource Name (ARN), or a signature into the job document through package version attributes.

The substitution parameters should be formatted in the job document as follows:

- **Software Package Name and Package
  Version**
  - The empty string between `package::version` represents
    the software package name substitution parameter. The empty string
    between `version::attribute` represents the software
    package version substitution parameter. Refer to the following
    example for using the package name and package verion substituion
    parameters in a job document:
    `${aws:iot:package::version::attributes:`<attributekey>`}`.
  - The job document will autofill these substituion parameters using
    the _Version ARN_ from the package version
    details. If you're creating a job or job template for a
    single-package deployment using an API or CLI command, the
    _Version ARN_ for a package version is
    represented by the `destinationPackageVersions` parameter
    in `CreateJob` and `DescribeJob`.

- **All Attributes for a Software Package
  Version**
  - Refer to the following example for using the all attributes of a
    software package version substitution parameter in a job document:
    `${aws:iot:package:`<packageName>`:version:`<versionName>`:attributes}`

###### Note

The package name, package version, and all attributes substitution parameters
can be used together. Refer to the following example for using all three
substitution parameters in a job document:
`${aws:iot:package::version::attributes}`

In the following example, there is a software package named `samplePackage`
and it has a package version named `2.1.5` that has the following
attributes:

- name: `s3URL`, value: `https://EXAMPIEBUCKET.s3.us-west-2.amazonaws.com/exampleCodeFile`
  - This attribute identifies the location of the code file that’s stored within Amazon S3.

- name: `signature`, value: `aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjj`
  - This attribute provides a code signature value that the device requires as a security measure. For more information, see [Code Signing for jobs](create-manage-jobs.md#create-manage-jobs-code-signing "create-manage-jobs.md#create-manage-jobs-code-signing"). **Note:** This attribute is an example and not required as part of Software Package Catalog or jobs.

For `s3URL`, the job document parameter is written as follows:

```
{
"samplePackage": "${aws:iot:package:samplePackage1:version:2.1.5:attributes:s3URL}"
}
```

For `signature`, the job document parameter is written as follows:

```
{
"samplePackage": "${aws:iot:package:samplePackage1:version:2.1.5:attributes:signature}"
}
```

The complete job document is written as follows:

```
{
  ...
  "Steps": {
    "uninstall": ["samplePackage"],
    "download": [
      {
        "samplePackage": "${aws:iot:package:samplePackage1:version:2.1.5:attributes:s3URL}"
      },
    ],
    "signature": [
      "samplePackage" : "${aws:iot:package:samplePackage1:version:2.1.5:attributes:signature}"
    ]
  }
}
```

After the substitution is made, the following job document is deployed to the devices:

```
{
  ...
  "Steps": {
    "uninstall": ["samplePackage"],
    "download": [
      {
        "samplePackage": "https://EXAMPIEBUCKET.s3.us-west-2.amazonaws.com/exampleCodeFile"
      },
    ],
    "signature": [
      "samplePackage" : "aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiiijjjj"
    ]
  }
}
```

**Substitution Parameters (Before and After
View)**

Substitution parameters streamline the creation of a job document using various
flags such as `$default` for the default package version. This eliminates
the need to manually enter specific package version metadata for each job deployment
as those flags are autofilled with the referenced metadata in the specific package
verison. For more information on package version attributes such as
`$default` for the default package version, see [Preparing the job document and package version for deployment](#preparing-to-deploy "#preparing-to-deploy").

In the AWS Management Console, toggle the _Preview substitution_ button
in the _Deployment instruction file editor_ window during a job
deployment for a package version to view the job document with and without the
substitution parameters.

Using the "before-substitution" parameter in the `DescribeJob` and
`GetJobDocument` APIs, you can view the API response before and after
the substitution parameters are removed. Refer to the following examples with the
`DescribeJob` and `GetJobDocument` APIs:

- `DescribeJob`
  - Default view

  ```
  {
      "jobId": "<jobId>",
      "description": "<description>",
      "destinationPackageVersions": ["arn:aws:iot:us-west-2:123456789012:package/TestPackage/version/1.0.2"]
  }
  ```

  - Before substituion view

  ```
  {
      "jobId": "<jobId>",
      "description": "<description>",
      "destinationPackageVersions": ["arn:aws:iot:us-west-2:123456789012:package/TestPackage/version/$default"]
  }
  ```

- `GetJobDocument`
  - Default view

  ```
  {
      "attributes": {
          "location": "prod-artifacts.s3.us-east-1.amazonaws.com/mqtt-core",
          "signature": "IQoJb3JpZ2luX2VjEIrwEaCXVzLWVhc3QtMSJHMEUCIAofPNPpZ9cI",
          "streamName": "mqtt-core",
          "fileId": "0"
      },
  }
  ```

  - Before substituion view

  ```
  {
      "attributes": "${aws:iot:package:TestPackage:version:$default:attributes}",
  }
  ```

For more information about AWS IoT Jobs, creating job documents, and deploying jobs, see [Jobs](iot-jobs.md "iot-jobs.md").

## Preparing the job document and package version for deployment

When a package version is created, it’s in a `draft` state to indicate that
it’s being prepared for deployment. To prepare the package version for deployment,
you must create a job document, save the document in a location that the job can
access (such as Amazon S3), and confirm that the package version has the attribute values
that you want the job document to use. (Note: You can update attributes for a
package version only while it’s in the `draft` state.)

When you create an AWS IoT Job or Job template for a single-package deployment, you
have the following options to customize your job document:

**Deployment instruction file
(`recipe`)**

- The deployment instruction file for a package version contains the
  deployment instructions, including an inline job document, for deploying a
  package version to multiple devices. The file associates specific deployment
  instructions to a package version for a quick and efficient job
  deployment.

In the AWS Management Console, you can create the file in the _Deployment
instructions file preview_ window in the _Version
deployment configurations_ tab of the create new package
workflow. You can leverage AWS IoT to automatically generate an instruction
file from your package version attributes using _Start from AWS IoT
recommended file_ or use your existing job document stored in
an Amazon S3 bucket using _Use your own deployment instruction
file_.

###### Note

If you use your own job document, you can update it directly in the
_Deployment instructions file preview_ window,
but it will not automatically update your original job document stored
in your Amazon S3 bucket.

When using the AWS CLI or an API command such as
`CreatePackageVersion`, `GetPackageVersion`, or
`UpdatePackageVersion`, `recipe` represents the
deployment instruction file, which includes an inline job document.

For more information on what a job document is, see [Basic concepts](key-concepts-jobs.md#basic-concepts-jobs "key-concepts-jobs.md#basic-concepts-jobs").

Refer to the following example for the deployment instruction file as
represented by `recipe`:

```
{
    "packageName": "`sample-package-name`",
    "versionName": "`sample-package-version`",
    ...
    "recipe": "{...}"
}
```

###### Note

The deployment instruction file as represented by `recipe`
can be updated when a package version is in the `published`
status state as it's separate from the package version metadata. It
become immutable during job deployment.

**`Artifact` version attribute**

- Using the version attribute `artifact` in your software package
  version, you can add the Amazon S3 location for your package version artifacts.
  When a job deployment for your package version is triggered using AWS IoT
  Jobs, the presigned URL placeholder `${aws:iot:package:<`packageName`>:version:<`versionName`>:artifact-location:`s3-presigned-url`}`
  in the job document will be updated using the Amazon S3 bucket, bucket key, and
  version of the file stored in the Amazon S3 bucket. The Amazon S3 bucket storing the
  package version artifacts must be located in the same region where the
  package version was created.

###### Note

To store multiple object versions of the same file in your Amazon S3
bucket, you must enable versioning on your bucket. For more information,
see [Enabling versioning on buckets](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md").

To access the package version artifacts in the Amazon S3 bucket when using the
`CreatePackageVersion` or `UpdatePackageVersion`
API operation, you must have the following permissions:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObjectVersion",
 "Resource": "arn:aws:s3:::`bucket-name`/`key-name`"
 }
 ]
}`

```

For more information on the version attribute `artifact` in the
`CreatePackageVersion` and `UpdatePackageVersion`
API operations, see [CreatePackageVersion](https://amazonaws.com/iot/latest/apireference/API_CreatePackageVersion.html "https://amazonaws.com/iot/latest/apireference/API_CreatePackageVersion.html") and [UpdatePackageVersion](../apireference/API_UpdatePackageVersion.md "../apireference/API_UpdatePackageVersion.md").

Refer to the following example that shows the version attribute
`artifact` supporting the artifact location in Amazon S3 when
creating a new package version:

```
{
    "packageName": "`sample package name`",
    "versionName": "`1.0`",
    "artifact": {
        "s3Location": {
            "bucket": "`firmware`",
            "key": "`image.bin`",
            "version": "`12345`"
        }
    }
}
```

###### Note

When a package version updates from a `draft` status state
to a `published` status state, the package version attributes
and artificats location become immutable. To update this informaiton,
you need to create a new package version and perform those updates while
in the `draft` status state.

**Package Version**

- A default software package version can be denoted in the available
  versions of the software package providing a secure and stable package
  version. This serves as the baseline version of the software package when
  deploying the default package version to your device fleet using AWS IoT Jobs.
  When creating a job to deploy the `$default` package version for
  a software package, the package version in the job document and in the new
  job deployment must match as `$default`. The package version in
  the job deployment is represented by `destinationPackageVersions`
  for API and CLI commands and `VersionARN` in the AWS Management Console.
  The package version in the job document is represented by the following job
  document placeholder shown below:

```
arn:aws:iot:`<regionCode>`:`111122223333`:package/`<packageName>`/version/`$default`
```

To create a job or job template using the default package version, use the
`$default` flag in the `CreateJob` or
`CreateJobTemplate` API command as shown below:

```
"$ aws iot create-job \
    --destination-package-versions "arn:aws:iot:us-west-2:123456789012:package/TestPackage/version/$default"
    --document file://jobdoc.json
```

###### Note

The `$default` package version attribute referencing the
default version is an optional attribute that is only required when
referencing the default package version for a job deployment via AWS IoT
Jobs.

When you are satisfied with the package version, publish it either through the
software package details page in the AWS IoT console or by issuing the [UpdatePackageVersion](../apireference/API_UpdatePackageVersion.md "../apireference/API_UpdatePackageVersion.md") API operation. You can then reference the package
version when you create the job either through the AWS IoT console or by issuing the
[CreateJob](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md") API operation.

## Naming the packages and versions when deploying

To deploy a software package version to a device, confirm the software package and
package version referenced in the job document match the software package and
package version stated in the `destinationPackageVersions` parameter in
the `CreateJob` API operation. If they don't match, you will receive an
error message prompting you to make both references match. For more information on
Software Package Catalog error messages, see [General Troubleshooting Error
Messages](software-package-catalog-troubleshooting.md#spc-general-troubleshooting "software-package-catalog-troubleshooting.md#spc-general-troubleshooting").

In addition to the software packages and package versions referenced in the job
document, you can include additional software packages and package versions in the
`destinationPackageVersions` parameter in the `CreateJob`
API operation not referenced in the job document. Ensure the necessary installation
information is included in the job document for devices to properly install the
additional software package versions. For more information on the `CreateJob` API operation, see [CreateJob](https://amazonaws.com/iot/latest/apireference/API_CreateJob.html "https://amazonaws.com/iot/latest/apireference/API_CreateJob.html").

## Targeting jobs through AWS IoT dynamic thing groups

Software Package Catalog works with [fleet indexing](iot-indexing.md "iot-indexing.md"), [AWS IoT jobs](iot-jobs.md "iot-jobs.md"), and [AWS IoT dynamic thing groups](dynamic-thing-groups.md "dynamic-thing-groups.md") to filter and target devices within your fleet to select which package version to deploy to your devices. You can run a fleet indexing query based on your device's current package information and target those things for an AWS IoT job. You can also release software updates, but only to eligible target devices. For example, you can specify that you want to deploy a configuration only to those devices that currently run the `iot-device-client 1.5.09`. For more information, see [Create a dynamic thing group](dynamic-thing-groups.md#create-dynamic-thing-group "dynamic-thing-groups.md#create-dynamic-thing-group").

## Reserved named shadow and package versions

If configured, AWS IoT Jobs can update a thing’s reserved named shadow (`$package`)when the job successfully completes. If you do so, you don’t need to manually associate a package version to a thing’s reserved named shadow.

You might choose to manually associate or update a package version to the thing’s reserved named shadow in the following situations:

- You register a thing to AWS IoT Core without associating the installed package version.
- AWS IoT Jobs isn’t configured to update the thing’s reserved named shadow.
- You use an in-house process to dispatch package versions to your fleet and that process doesn’t update AWS IoT Core when it completes.

###### Note

We recommend you use AWS IoT Jobs to update the package version in the reserved named shadow (`$package`). Updating the version parameter in the `$package` shadow through other processes (such as, manual or programmatic API calls) when AWS IoT Jobs is also configured to update the shadow, can cause inconsistencies between the actual version on device and version reported to the reserved named shadow.

You can add or update a package version to a thing’s reserved named shadow (`$package`) through the console or the [`UpdateThingShadow`](../apireference/API_iotdata_UpdateThingShadow.md "../apireference/API_iotdata_UpdateThingShadow.md") API operation. For more information, see [Associating a package version to an AWS IoT thing](associating-package-version.md "associating-package-version.md").

###### Note

Associating a package version to an AWS IoT thing doesn’t directly update the device software. You must deploy the package version to the device to update the device software.

## Uninstalling a software package and its package version

`$null` is a reserved placeholder that prompts the AWS IoT Jobs service to remove the existing software package and package version from the device’s reserved named shadow `$package`. For more information, see [Reserved named shadow.](preparing-to-use-software-package-catalog.md#reserved-named-shadow "preparing-to-use-software-package-catalog.md#reserved-named-shadow")

To use this feature, replace the version name at the end of the [destinationPackageVersion](../apireference/API_CreateJobTemplate.md#iot-CreateJobTemplate-request-destinationPackageVersions "../apireference/API_CreateJobTemplate.md#iot-CreateJobTemplate-request-destinationPackageVersions") Amazon Resource Name (ARN) with `$null`. Afterward, you must instruct your service to remove the software from the device.

The authorized ARN uses the following format:

```
arn:aws:iot:`<regionCode>`:`111122223333`:package/`<packageName>`/version/$null

```

For example,

```
$ aws iot create-job \
    ... \
    --destinationPackageVersions ["arn:aws:iot:us-east-1:111122223333:package/samplePackage/version/$null"]
```
