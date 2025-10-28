# AWS IoT Device Management Software Package Catalog

Troubleshooting

This is the troubleshooting section for AWS IoT Device Management Software Package Catalog.

## General Troubleshooting Error

Messages

This section lists common errors seen throughout the software package version
lifecycle.

**`HeadBucket` errors**

The following error messages appear when calling the [`HeadBucket` API
operation](../../../AmazonS3/latest/API/API_HeadBucket.md "../../../AmazonS3/latest/API/API_HeadBucket.md") or [`head-bucket` CLI
command](../../../cli/latest/reference/s3api/head-bucket.md "../../../cli/latest/reference/s3api/head-bucket.md") to validate the Amazon S3 bucket used for file upload during a job
deployment.

For more information on using an Amazon S3 bucket for uploading files during a job
deployment, see [Presigned URL for file
upload](create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload "create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload").

```
**InvalidRoleException**
    "Permission denied when attempting to use role %s to access bucket %s."
```

```
**InvalidRequestException**
    "Cross region S3 bucket is not supported for presigned url upload placeholder"
```

```
**InvalidRequestException**
    "S3 bucket in job document presigned url upload placeholder not found"
```

```
**InvalidRequestException**
    "Given S3 bucket name is invalid."
```

```
**InvalidRequestException**
    "Provided S3 bucket is not valid: %s. Error: %s"
```

**Amazon S3 GetObject**

The following error message occurs when an invalid argument is provided, thus causing
the Amazon S3 `GetObject` API operation to fail.

```
**InvalidRequestException**
    "Provided argument for presigned url is invalid"
```

**Amazon S3 Version ID Support**

When requesting access to an Amazon S3 bucket using versioning control, make sure to
include your `versionId` or the below error may populate.

For more information on Amazon S3 buckets using versioning control, see [Using versioning in
Amazon S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md")

```
**InvalidRequestException**
    "VersionId not found when attempting to access s3 url"
```

**Placeholders inside of a Presigned URL for file
upload**

The following error messages appear when encountering issues with a placeholder inside
of a presigned URL used for uploading files to a destination Amazon S3 bucket during a job
deployment. For more information on using an Amazon S3 bucket for uploading files during a job
deployment and what a local placeholder is, see [Presigned URL for file
upload](create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload "create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload").

The below error message appears when the local placeholder is not recognized.

```
**InvalidJobDocumentException**
    "Undefined placeholder, ${...}, inside of presign url upload parameter"
```

The below error message appears when attempting to use the local placeholder in a
presigned URL not meant for file upload.

```
**InvalidJobDocumentException**
    "Local placeholder, ${...}, is only valid inside of presign url upload"
```

**Amazon S3 URL Nested Incorrectly**

The following error message appears when the Amazon S3 URL is incorrectly nested inside of
another placeholder.

```
**InvalidJobDocumentException**
    "${aws:%s[...]} should not be the second layer pattern."
```

**Package Version Artifact Nesting**

The following error message appears when the package version artifact presigned URL is
incorrectly nested inside of another placeholder.

```
**InvalidJobDocumentException**
    "${aws:iot:package:[...]:artifact:s3-presigned-url} cannot be nested inside another placeholder."
```

**Missing Package Version Artifact**

The following error message appears when the referenced package version artifact is
not found.

```
**InvalidJobDocumentException**
    "Package %s version %s does not have an associated artifact to generate an S3 presigned url."
```

**Software Package and Package Verion
Placeholders**

The following error message appears when the job document placeholder for software
package and package version can't resolve to the desired valid values for the job
deployment due to multiple software packages and package versions referenced in the
`destinationPackageVersions` parameter or the _Version
ARN_ tab on the _Package Version_ details page.

```
**InvalidJobDocumentException**
    "Cannot resolve empty package name and version name given multiple elements in destination package versions."
```

**Using Empty Software Package and Package
Version**

The following error message appears when you attempt to attempt to use an empty
package or package version without the other in a job document.

```
**InvalidJobDocumentException**
    "Empty package name and version name have to be used in pair."
```

**Null Use in Job Document**

The following error message appears when you attempt to specify `$null` as
a package version in the job document. `$null` can only be used inside of the
`destinationPackageVersions` parameter when using the `CreateJob`
API operation.

```
**InvalidJobDocumentException**
    "$null is not allowed to be referenced as a package version in job documents."
```

**All Attributes in a Package Version**

The following error message appears when you attempt to use all attributes in a
package version and surround it with additional text or placeholders.

For more information on using all attributes in a software package version, see [Substitution parameters for AWS IoT jobs](preparing-jobs-for-service-package-catalog.md#substitution-parameters "preparing-jobs-for-service-package-catalog.md#substitution-parameters")

```
**InvalidJobDocumentException**
    "The package version attribute placeholder for all attributes has to be a json value by itself and not appended with other strings or nested with other placeholders."
```

**Local Placeholder Limit in Presigned URL for File
Upload**

The following error message appears when you exceed the limit for number of local
placeholders used in a presigned URL for file upload during a job deployment.

For more information on using a presigned URL for file upload during a job deployment,
see [Presigned URL for file
upload](create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload "create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload")

```
**InvalidJobDocumentException**
    "The occurrence of local placeholder %s within S3 presigned url upload placeholder exceeds limit of %d."
```

**Local Placeholders in an Amazon S3 Bucket**

The following error message appears when you attempt to place a local placeholder URL
in the Amazon S3 bucket name for a presigned URL placeholder used for file upload during a job
deployment.

For more information on using a presigned URL for file upload during a job deployment,
see [Presigned URL for file
upload](create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload "create-manage-jobs.md#create-manage-jobs-presigned-URLs-upload")

```
**InvalidJobDocumentException**
    "S3 bucket name in presigned url upload is not allowed to contain any placeholders"
```

**Opening and Closing Brackets**

The following error message appears when you add a parameter or placeholder to a job
document without a closing brace "}".

```
**InvalidJobDocumentException**
    "One or more parameters or placeholders are not terminated."
```

**IAM role with Amazon S3 Presigned URL**

The following error message appears when you attempt to use an Amazon S3 presigned URL in a
job document without an IAM role.

For more information on Amazon S3 presigned URLs, see [Working with presigned URLs](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md").

```
**InvalidRequestException**
    "presignedUrlConfig role ARN is required to generate an S3 presigned url in job document."
```

**IAM role with Amazon S3 Presigned URL for Package Version
Artifact**

The following error message appears when you attempt to use an Amazon S3 presigned URL
representing a package version artifact in a job document without an IAM role.

```
**InvalidRequestException**
    "presignedUrlConfig role ARN is required to generate an S3 presigned url in job document for package %s version %s artifact."
```

## Software Bill of Materials Error

Messages

This section lists common errors associated with a software bill of materials (SBOM)
linked to a package version.

**Input Validation for SBOM Association Request**

The following error message appears when using the
`AssociateSbomWithPackageVersion` API operation and the
`s3Location` parameter is null.

```
**InvalidRequestException** "Associate request needs to include SBOM reference"
```

For more information on the `AssociateSbomWithPackageVersion` API
operation, see [AssociateSbomWithPackageVersion](https://amazonaws.com/iot/latest/apireference/API_AssociateSbomWithPackageVersion.html "https://amazonaws.com/iot/latest/apireference/API_AssociateSbomWithPackageVersion.html").

**SBOM Validation Errors**

This section lists common errors seen during the initial validaiton of the software
bill of materials (SBOM) when associated with a software package version.

The following error message appears when using the
`AssociateSbomWithPackageVersion` API operation and `bucket` in
the `s3Location` parameter is null.

```
**InvalidRequestException** "S3 bucket name for SBOM cannot be null"
```

The following error message appears when the string in `bucket` in the
`s3Location` parameter for the `AssociateSbomWithPackageVersion`
API operation is too long.

```
**InvalidRequestException** "S3 bucket name for SBOM is illegal. String length exceeds limit"
```

The following error message appears when the `key` parameter is
null.

```
**InvalidRequestException** "S3 key name for SBOM cannot be null"
```

The following error message appears when the string in `key` in the
`s3Location` parameter for the `AssociateSbomWithPackageVersion`
API operation is too long.

```
**InvalidRequestException** "S3 key name for SBOM is illegal. String length exceeds limit"
```

The following error message appears when the string in `version` in the
`s3Location` parameter for the `AssociateSbomWithPackageVersion`
API operation is null.

```
**InvalidRequestException** "S3 object version for SBOM cannot be null"
```

The following error message appears when the string in `version` in the
`s3Location` parameter for the `AssociateSbomWithPackageVersion`
API operation is too long.

```
**InvalidRequestException** "S3 object version for SBOM is illegal. String length exceeds limit"
```

The following error message appears when the the size of the SBOM zip archive file
stored in the Amazon S3 bucket is too big.

```
**InvalidRequestException** "S3 object file size exceeds limit"
```

The following error message appears when you use the
`AssociateSbomWithPackageVersion` API operation and the current number of
SBOM validations in progress is already at the maximum limit.

```
**LimitExceededException** "Too many ongoing SBOM validation workflows. Please wait and retry"
```

**Access Issues with SBOM File in Amazon S3 bucket**

The following error message appears when another entity fails to access the Amazon S3
bucket due to the Amazon S3 bucket not existing or the proper permissions have not been granted
for accessing the Amazon S3 bucket.

For more information on the required permissions policy for accessing the Amazon S3 bucket,
see [Software Bill of Materials Storage](preparing-to-use-software-package-catalog.md#spc-sbom-storage "preparing-to-use-software-package-catalog.md#spc-sbom-storage").

```
**InvalidRequestException** "SBOM not accessible by the service. Please make sure the bucket exists and S3 permission is granted."
```

The following error message appears when another entity fails to access the SBOM zip
archive file in the `key` parameter due to the Amazon S3 bucket not existing or the
proper permissions have not been granted for accessing content stored in the Amazon S3
bucket.

```
**InvalidRequestException** "SBOM not accessible by the service. Please make sure the key exists and S3 permission is granted."
```

The following error message appears when another entity fails to access the Amazon S3
bucket due to the bucket, key, and version ID not existing or the proper permissions have
not been granted for accessing the Amazon S3 bucket. Additionally, this error message can
appear if the permissions granted are insufficient for accessing the SBOM zip archive file
in the Amazon S3 bucket.

```
**InvalidRequestException** "SBOM not accessible by the service. Please make sure the bucket/key/version exists and S3 permission is granted."
```

The following error message appears when another entity fails to access the Amazon S3
bucket due to the bucket being located in another region.

```
**InvalidRequestException** "Cross-region S3 bucket for %s is not supported."
```

The following error message appears when another entity fails to access the Amazon S3
bucket due to the `bucket`, `key`, or `version`
parameters being spelled incorrectly when using the
`AssociateSbomWithPackageVersion` API operation.

```
**InvalidRequestException** "Please make sure SBOM S3 bucket name/key length/version is valid"
```
