# AwsEcr resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsEcr` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsEcrContainerImage

The `AwsEcrContainerImage` object provides information about an Amazon ECR
image.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEcrContainerImage` object. To view descriptions of
`AwsEcrContainerImage` attributes, see [AwsEcrContainerImageDetails](../../1.0/APIReference/API_AwsEcrContainerImageDetails.md "../../1.0/APIReference/API_AwsEcrContainerImageDetails.md") in the
_AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEcrContainerImage": {
    "RegistryId": "123456789012",
    "RepositoryName": "repository-name",
    "Architecture": "amd64"
    "ImageDigest": "sha256:a568e5c7a953fbeaa2904ac83401f93e4a076972dc1bae527832f5349cd2fb10",
    "ImageTags": ["00000000-0000-0000-0000-000000000000"],
    "ImagePublishedAt": "2019-10-01T20:06:12Z"
}
```

## AwsEcrRepository

The `AwsEcrRepository` object provides information about an Amazon Elastic Container Registry
repository.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEcrRepository` object. To view descriptions of
`AwsEcrRepository` attributes, see [AwsEcrRepositoryDetails](../../1.0/APIReference/API_AwsEcrRepositoryDetails.md "../../1.0/APIReference/API_AwsEcrRepositoryDetails.md") in the _AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEcrRepository": {
    "LifecyclePolicy": {
        "RegistryId": "123456789012",
    },
    "RepositoryName": "sample-repo",
    "Arn": "arn:aws:ecr:us-west-2:111122223333:repository/sample-repo",
    "ImageScanningConfiguration": {
        "ScanOnPush": true
    },
    "ImageTagMutability": "IMMUTABLE"
}
```
