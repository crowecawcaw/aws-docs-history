# Build phase transitions

Builds in AWS CodeBuild proceed in phases:

![The CodeBuild phases.](images/build-phases.png)

###### Important

The `UPLOAD_ARTIFACTS` phase is always attempted, even if the
`BUILD` phase fails.
