

# Build phase transitions
<a name="view-build-details-phases"></a>

Builds in AWS CodeBuild proceed in phases:



![The CodeBuild phases.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/build-phases.png)




**Important**  
The `UPLOAD_ARTIFACTS` phase is always attempted, even if the `BUILD` phase fails.