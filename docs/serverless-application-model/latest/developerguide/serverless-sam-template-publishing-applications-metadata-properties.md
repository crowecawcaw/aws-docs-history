# AWS SAM

template Metadata section properties

`AWS::ServerlessRepo::Application` is a metadata key that you can use to
specify application information that you want published to the AWS Serverless Application Repository.

###### Note

CloudFormation [intrinsic
functions](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") aren't supported by the
`AWS::ServerlessRepo::Application` metadata key.

## Properties

This table provides information about the properties of the `Metadata`
section of the AWS SAM template. This section is required to publish applications to the
AWS Serverless Application Repository using the AWS SAM CLI.

| Property          | Type   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `Name`            | String | TRUE     | The name of the application.<br>Minimum length=1. Maximum length=140.<br>Pattern: `"[a-zA-Z0-9\\-]+";`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Description`     | String | TRUE     | The description of the application.<br>Minimum length=1. Maximum length=256.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Author`          | String | TRUE     | The name of the author publishing the application.<br>Minimum length=1. Maximum length=127.<br>Pattern: `"^[a-z0-9](([a-z0-9]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | -(?!-))\*[a-z0-9])?$";` |
| `SpdxLicenseId`   | String | FALSE    | A valid license identifier. To view the list of valid license<br>identifiers, see [SPDX License<br>List](https://spdx.org/licenses/ "https://spdx.org/licenses/") on the \*Software Package Data Exchange<br>(SPDX)<br>• website.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `LicenseUrl`      | String | FALSE    | The reference to a local license file, or an Amazon S3 link to a<br>license file, that matches the spdxLicenseID value of your<br>application.<br>An AWS SAM template file that hasn't been packaged using the<br>`sam package` command can have a reference to a local<br>file for this property. However, for an application to be published<br>using the `sam publish` command, this property must be a<br>reference to an Amazon S3 bucket.<br>Maximum size: 5 MB.<br>You must provide a value for this property in order to make your<br>application public. Note that you cannot update this property after<br>your application has been published. So, to add a license to an<br>application, you must either delete it first, or publish a new<br>application with a different name. |
| `ReadmeUrl`       | String | FALSE    | The reference to a local readme file or an Amazon S3 link to the readme<br>file that contains a more detailed description of the application<br>and how it works.<br>An AWS SAM template file that hasn't been packaged using the<br>`sam package` command can have a reference to a local<br>file for this property. However, to be published using the `sam<br>publish` command, this property must be a reference to an<br>Amazon S3 bucket.<br>Maximum size: 5 MB.                                                                                                                                                                                                                                                                                                                       |
| `Labels`          | String | FALSE    | The labels that improve discovery of applications in search<br>results.<br>Minimum length=1. Maximum length=127. Maximum number of labels:<br>10.<br>Pattern: `"^[a-zA-Z0-9+\\-_:\\/@]+$";`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `HomePageUrl`     | String | FALSE    | A URL with more information about the application—for example,<br>the location of your GitHub repository for the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `SemanticVersion` | String | FALSE    | The semantic version of the application. For the Semantic<br>Versioning specification, see the [Semantic Versioning](https://semver.org/ "https://semver.org/") website.<br>You must provide a value for this property in order to make your<br>application public.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SourceCodeUrl`   | String | FALSE    | A link to a public repository for the source code of your<br>application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Use cases

This section lists the use cases for publishing applications, along with the
`Metadata` properties that are processed for that use case. Properties
that are _not_ listed for a given use case are ignored.

- **Creating a new application** – A new
  application is created if there is no application in the AWS Serverless Application Repository with a matching
  name for an account.
  - `Name`
  - `SpdxLicenseId`
  - `LicenseUrl`
  - `Description`
  - `Author`
  - `ReadmeUrl`
  - `Labels`
  - `HomePageUrl`
  - `SourceCodeUrl`
  - `SemanticVersion`
  - The content of the AWS SAM template (for example, any event sources,
    resources, and Lambda function code)

- **Creating an application version** – An
  application version is created if there is already an application in the AWS Serverless Application Repository
  with a matching name for an account _and_ the SemanticVersion
  _is_ changing.
  - `Description`
  - `Author`
  - `ReadmeUrl`
  - `Labels`
  - `HomePageUrl`
  - `SourceCodeUrl`
  - `SemanticVersion`
  - The content of the AWS SAM template (for example, any event sources,
    resources, and Lambda function code)

- **Updating an application** – An
  application is updated if there is already an application in the AWS Serverless Application Repository with a
  matching name for an account _and_ the SemanticVersion
  _is not_ changing.
  - `Description`
  - `Author`
  - `ReadmeUrl`
  - `Labels`
  - `HomePageUrl`

## Example

The following is an example `Metadata` section:

```
Metadata:
  AWS::ServerlessRepo::Application:
    Name: `my-app`
    Description: `hello world`
    Author: `user1`
    SpdxLicenseId: Apache-2.0
    LicenseUrl: `LICENSE.txt`
    ReadmeUrl: `README.md`
    Labels: `['tests']`
    HomePageUrl: `https://github.com/user1/my-app-project`
    SemanticVersion: `0.0.1`
    SourceCodeUrl: `https://github.com/user1/my-app-project`
```
