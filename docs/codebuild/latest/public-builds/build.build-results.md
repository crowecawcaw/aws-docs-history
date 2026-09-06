

# Build results
<a name="build.build-results"></a>

The entry page for an individual build result displays information about the project.

## Build logs
<a name="build.build-logs"></a>

Displays the build logs for the build. Build logs are only available if the project administrator has enabled CloudWatch Logs or Amazon S3 log storage for the project.

## Phase details
<a name="build.phase-details"></a>

Displays the build phases and their disposition.

## Build details
<a name="build.build-details"></a>

Displays the build information for the individual build. This includes the following:

**Source**  
The source settings for the build. The contents of this section vary depending on the source provider used. For more information, see [Source](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-console.html#create-project-console-source) in the *AWS CodeBuild User Guide*.

**Environment**  
The build environment for the build. For more information, see [Build environment reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref.html) in the *AWS CodeBuild User Guide*.

**Buildspec**  
Displays the build specification (buildspec) for the build. The buildspec is a YAML file that specifies, among other things, the build commands and the artifacts for the build project. A buildspec can either be a file at the root of the source repository, or part of the project itself. If the buildspec is a file in the repository, a note is displayed. If the buildspec is part of the project, the buildspec source is displayed.  
For more information, see [Buildspec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) in the *AWS CodeBuild User Guide*.

## Artifacts
<a name="build.artifacts"></a>

Displays the artifacts produced by the build, if any. Choosing the artifact link will download the artifact.