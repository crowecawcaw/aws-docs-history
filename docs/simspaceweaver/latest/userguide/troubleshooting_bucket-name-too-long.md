End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# InvalidBucketName

You might receive the following error while creating a project:

```
An error occurred (InvalidBucketName) when calling the CreateBucket operation: The specified bucket is not valid.
```

You received this error because the name that SimSpace Weaver passed to Amazon Simple Storage Service (Amazon S3) violated
bucket naming rules (for more information, see [Bucket naming rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md")
in the _Amazon Simple Storage Service User Guide_).

The `create-project` script in the SimSpace Weaver app SDK creates bucket names
using the project name that you provide to the script. The bucket names use the
following formats:

- Version 1.13.x or later
  - `weaver-`lowercase-project-name`-`account-number`-`region``

- Version 1.12.x

      + `weaver-`lowercase-project-name`-`account-number`-app-zips-`region``
      + `weaver-`lowercase-project-name`-`account-number`-schemas-`region``

  For example, given the following project properties:

- Project name: `MyProject`
- AWS account number: `111122223333`
- AWS Region: `us-west-2`
  The project would have the following buckets:

- Version 1.13.x or later
  - `weaver-myproject-111122223333-us-west-2`

- Version 1.12.x

      + `weaver-myproject-111122223333-app-zips-us-west-2`
      + `weaver-myproject-111122223333-schemas-us-west-2`

  Your project name must not violate the Amazon S3 naming rules. You must also use a project
  name that is short enough so that the bucket names created by the
  `create-project` script do not exceed the name length limit for Amazon S3
  buckets.
