# Build specification reference

The build specification (buildspec) for an Amplify application is a collection of YAML settings and
build commands that Amplify uses to run your build. The following list describes these
settings and how they are used.

**version**

The Amplify YAML version number.

**appRoot**

The path within the repository that this application resides in. _Ignored unless multiple applications are defined._

**env**

Add environment variables to this section. You can also add environment variables
using the console.

**backend**

Run Amplify CLI commands to provision a backend, update Lambda functions, or
GraphQL schemas as part of continuous deployment.

**frontend**

Run frontend build commands.

**test**

Run commands during a test phase. Learn how to [add
tests to your app](running-tests.md "running-tests.md").

**build phases**

The frontend, backend, and test have three _phases_ that
represent the commands run during each sequence of the build.

- **preBuild** - The preBuild script runs before the
  actual build starts, but after Amplify installs dependencies.
- **build** - Your build commands.
- **postBuild** - The post-build script runs after the
  build has finished and Amplify has copied all the necessary artifacts to the
  output directory.

**buildpath**

The path to use to run the build. Amplify uses this path to locate your build
artifacts. If you don't specify a path, Amplify uses the monorepo app root, for
example `apps/app`.

**artifacts>base-directory**

The directory in which your build artifacts exist.

**artifacts>files**

Specify files from your artifacts you want to deploy. Enter `**/*` to
include all files.

**cache**

Specifies build-time dependencies such as the _node_modules_ folder. During the first build, paths provided here are
cached. On subsequent builds, Amplify restores the cache to the same paths before it runs your
commands.

Amplify considers all provided cache paths to be relative to your project root.
However, Amplify doesn't allow traversing outside of the project root. For example, if you
specify an absolute path, the build will succeed without an error, but the path won't be
cached.

The following example of a build specification demonstrates the basic YAML
syntax.

```
version: 1
env:
  variables:
    key: value
backend:
  phases:
    preBuild:
      commands:
        - *enter command*
    build:
      commands:
        - *enter command*
    postBuild:
        commands:
        - *enter command*
frontend:
  buildpath:
  phases:
    preBuild:
      commands:
        - cd react-app
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    files:
        - location
        - location
    discard-paths: yes
    baseDirectory: location
  cache:
    paths:
        - path # A cache path relative to the project root
        - path # Traversing outside of the project root is not allowed
test:
  phases:
    preTest:
      commands:
        - *enter command*
    test:
      commands:
        - *enter command*
    postTest:
      commands:
        - *enter command*
  artifacts:
    files:
        - location
        - location
    configFilePath: *location*
    baseDirectory: *location*

```
