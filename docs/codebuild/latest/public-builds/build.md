# Build results

The entry page for an individual build result displays information about the
project.

## Build logs

Displays the build logs for the build. Build logs are only available if the project
administrator has enabled CloudWatch Logs or Amazon S3 log storage for the project.

## Phase details

Displays the build phases and their disposition.

## Build details

Displays the build information for the individual build. This includes the
following:

**Source**

The source settings for the build. The contents of this section vary depending on
the source provider used. For more information, see [Source](../userguide/create-project-console.md#create-project-console-source "../userguide/create-project-console.md#create-project-console-source") in the _AWS CodeBuild User Guide_.

**Environment**

The build environment for the build. For more information, see [Build
environment reference](../userguide/build-env-ref.md "../userguide/build-env-ref.md") in the _AWS CodeBuild User Guide_.

**Buildspec**

Displays the build specification (buildspec) for the build. The buildspec is a
YAML file that specifies, among other things, the build commands and the artifacts for
the build project. A buildspec can either be a file at the root of the source
repository, or part of the project itself. If the buildspec is a file in the
repository, a note is displayed. If the buildspec is part of the project, the
buildspec source is displayed.

For more information, see [Buildspec reference](../userguide/build-spec-ref.md "../userguide/build-spec-ref.md") in
the _AWS CodeBuild User Guide_.

## Artifacts

Displays the artifacts produced by the build, if any. Choosing the artifact link will
download the artifact.
