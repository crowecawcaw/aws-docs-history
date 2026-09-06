

# Project build results
<a name="project.build-results"></a>

The entry page for a project's build results displays information about the project.

## Configuration
<a name="project.configuration"></a>

The **Configuration** section contains the following, if applicable. These are configured by the CodeBuild project administrator.

**Source provider**  
The source provider for the project.

**Primary repository**  
The primary source repository for the project.

**Concurrent build limit**  
The maximum number of builds of the project that can run concurrently. 

**Description**  
The description of the project.

## Build history
<a name="project.build-history"></a>

Displays a list of the builds for the project.

## Batch history
<a name="project.batch-history"></a>

Displays the list of batch build runs, if any.

## Build details
<a name="project.build-details"></a>

Displays the build information for the project. This includes the following:

**Source**  
The source settings for the project. The contents of this section vary depending on the source provider used. For more information, see [Source](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-console.html#create-project-console-source) in the *AWS CodeBuild User Guide*.

**Environment**  
The build environment for the project. For more information, see [Build environment reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref.html) in the *AWS CodeBuild User Guide*.

**Buildspec**  
Displays the buildspec for the project. The buildspec is a YAML file that specifies, among other things, the build commands and the artifacts for the build project. A buildspec can either be a file at the root of the source repository, or part of the project itself. If the buildspec is a file in the repository, a note is displayed. If the buildspec is part of the project, the buildspec source is displayed.  
For more information, see [Buildspec reference](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) in the *AWS CodeBuild User Guide*.

## Build triggers
<a name="project.build-triggers"></a>

Displays the build triggers for the project, if any.