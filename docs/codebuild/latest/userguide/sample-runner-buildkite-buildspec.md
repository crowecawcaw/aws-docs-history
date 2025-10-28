# Run buildspec commands for the

INSTALL, PRE_BUILD, and POST_BUILD phases

By default, CodeBuild ignores any buildspec commands when running a self-hosted Buildkite
runner build. To run buildspec commands during the build,

```
buildspec-override: "true"
```

can be added as a suffix to the label:

```
agents:
  project: "codebuild-`<project name>`"
  buildspec-override: "true"
```

By using this command, CodeBuild will create a folder called `buildkite-runner`
in the container's primary source folder. When the Buildkite runner starts during the
`BUILD` phase, the runner will run in the `buildkite-runner`
directory.

There are several limitations when using a buildspec override in a self-hosted
Buildkite build:

- The Buildkite agent requires that source credentials exist within the build
  environment to pull the job’s source repository. If you use CodeBuild source
  credentials for authentication, you will need to enable
  `git-credential-helper` in your buildspec. For example, you can
  use the following buildspec to enable `git-credential-helper` for
  your Buildkite builds:

```
version: 0.2
env:
  git-credential-helper: yes
phases:
  pre_build:
    commands:
       - echo "Hello World"
```

- CodeBuild will not run buildspec commands during the `BUILD` phase, as
  the self-hosted runner runs in the `BUILD` phase.
- CodeBuild does not support buildspec files for Buildkite runner builds. Only
  inline buildspecs are supported for Buildlkite self-hosted runners
- If a build command fails in the `PRE_BUILD` or `INSTALL`
  phase, CodeBuild will not start the self-hosted runner and the Buildkite job will
  need to be cancelled manually.
