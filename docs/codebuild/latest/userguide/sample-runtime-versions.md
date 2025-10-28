# Runtime versions in buildspec file sample for CodeBuild

If you use the Amazon Linux 2 (AL2) standard image version 1.0 or later, or the Ubuntu standard image version 2.0 or later,
you can specify one or more runtimes in the `runtime-versions` section of your buildspec file. The following
samples show how you can change your project runtime, specify more than one runtime, and
specify a runtime that is dependent on another runtime. For information about supported runtimes, see
[Docker images provided by CodeBuild](build-env-ref-available.md "build-env-ref-available.md").

###### Note

If you use Docker in your build container, your build must run in privileged mode.
For more information, see [Run AWS CodeBuild builds manually](run-build.md "run-build.md") and
[Create a build project in AWS CodeBuild](create-project.md "create-project.md").

###### Topics

- [Update the runtime version in the buildspec file](sample-runtime-update-version.md "sample-runtime-update-version.md")
- [Specify two runtimes](sample-runtime-two-major-version-runtimes.md "sample-runtime-two-major-version-runtimes.md")
