# Docker images provided by CodeBuild

A _supported image_ is the latest major version of an image available in CodeBuild and is updated with
minor and patch version updates. CodeBuild optimizes the provisioning duration of builds with supported images by caching them in the machine's
[Amazon Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md#ami-using "../../../AWSEC2/latest/UserGuide/AMIs.md#ami-using"). If you want to benefit from caching and minimize the provisioning duration of your build,
select **Always use the latest image for this runtime version** in the **Image version** section of the CodeBuild console instead of a more granular version, such as
`aws/codebuild/amazonlinux-x86_64-standard:4.0-1.0.0`.

###### Topics

- [Obtain the list of current Docker images](build-env-ref-available-get.md "build-env-ref-available-get.md")
- [EC2 compute images](ec2-compute-images.md "ec2-compute-images.md")
- [Lambda compute images](lambda-compute-images.md "lambda-compute-images.md")
- [Deprecated CodeBuild images](deprecated-images.md "deprecated-images.md")
- [Available runtimes](available-runtimes.md "available-runtimes.md")
- [Runtime versions](runtime-versions.md "runtime-versions.md")

###### Topics

- [Available runtimes](available-runtimes.md "available-runtimes.md")
- [Runtime versions](runtime-versions.md "runtime-versions.md")
