# Project build results

The entry page for a project's build results displays information about the
project.

## Configuration

The **Configuration** section contains the following, if applicable.
These are configured by the CodeBuild project administrator.

**Source provider**

The source provider for the project.

**Primary repository**

The primary source repository for the project.

**Concurrent build limit**

The maximum number of builds of the project that can run concurrently.

**Description**

The description of the project.

## Build history

Displays a list of the builds for the project.

## Batch history

Displays the list of batch build runs, if any.

## Build details

Displays the build information for the project. This includes the following:

**Source**

The source settings for the project. The contents of this section vary depending
on the source provider used. For more information, see [Source](../userguide/create-project-console.md#create-project-console-source "../userguide/create-project-console.md#create-project-console-source") in the _AWS CodeBuild User Guide_.

**Environment**

The build environment for the project. For more information, see [Build
environment reference](../userguide/build-env-ref.md "../userguide/build-env-ref.md") in the _AWS CodeBuild User Guide_.

**Buildspec**

Displays the buildspec for the project. The buildspec is a YAML file that
specifies, among other things, the build commands and the artifacts for the build
project. A buildspec can either be a file at the root of the source repository, or
part of the project itself. If the buildspec is a file in the repository, a note is
displayed. If the buildspec is part of the project, the buildspec source is
displayed.

For more information, see [Buildspec reference](../userguide/build-spec-ref.md "../userguide/build-spec-ref.md") in
the _AWS CodeBuild User Guide_.

## Build triggers

Displays the build triggers for the project, if any.
