# Build image configuration files

AWS ParallelCluster version 3 uses YAML 1.1 files for build image configuration parameters. Please confirm
that indentation is correct to reduce configuration errors. For more information, see the YAML 1.1 spec at [https://yaml.org/spec/1.1/](https://yaml.org/spec/1.1/ "https://yaml.org/spec/1.1/").

These configuration files are used to define how your custom AWS ParallelCluster AMIs are
built using EC2 Image Builder. Custom AMI building processes are triggered using the [pcluster build-image](pcluster.md "pcluster.md") command. For some
example configuration files, see [https://github.com/aws/aws-parallelcluster/tree/release-3.0/cli/tests/pcluster/schemas/test_imagebuilder_schema/test_imagebuilder_schema](https://github.com/aws/aws-parallelcluster/tree/release-3.0/cli/tests/pcluster/schemas/test_imagebuilder_schema/test_imagebuilder_schema "https://github.com/aws/aws-parallelcluster/tree/release-3.0/cli/tests/pcluster/schemas/test_imagebuilder_schema/test_imagebuilder_schema").

###### Topics

- [Build image configuration file properties](#build-image-v3.properties "#build-image-v3.properties")
- [Build section](Build-v3.md "Build-v3.md")
- [Image section](build-Image-v3.md "build-Image-v3.md")
- [DeploymentSettings section](DeploymentSettings-build-image-v3.md "DeploymentSettings-build-image-v3.md")

## Build image configuration file properties

`Region` (**Optional**,
`String`)

Specifies the AWS Region for the `build-image` operation. For example, `us-east-2`.

`CustomS3Bucket` (**Optional**,
`String`)

Specifies the name of an Amazon S3 bucket that is created in your AWS account to store resources
that are used by the custom AMI build process and to export logs. The info used by the image is
in the custom bucket for image config. AWS ParallelCluster maintains one Amazon S3 bucket in each AWS
Region that you create clusters in. By default, these Amazon S3 buckets are named
`parallelcluster-hash-v1-DO-NOT-DELETE`.
