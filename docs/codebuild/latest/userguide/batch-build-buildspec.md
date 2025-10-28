# Batch build buildspec reference

This topic contains the buildspec reference for batch build properties.

## batch

Optional mapping. The batch build settings for the project.

batch/**fast-fail**

Optional. Specifies the behavior of the batch build when one or more build
tasks fail.

`false`

The default value. All running builds will complete.

`true`

All running builds will be stopped when one of the build tasks
fails.

By default, all batch build tasks run with the build settings such as `env`
and `phases`, specified in the buildspec file. You can override the default
build settings by specifying different `env` values or a different buildspec
file in the `batch/`<batch-type>`/buildspec`
parameter.

The contents of the `batch` property varies based on the type of batch
build being specified. The possible batch build types are:

- [batch/build-graph](#build-spec.batch.build-graph "#build-spec.batch.build-graph")
- [batch/build-list](#build-spec.batch.build-list "#build-spec.batch.build-list")
- [batch/build-matrix](#build-spec.batch.build-matrix "#build-spec.batch.build-matrix")
- [batch/build-fanout](#build-spec.batch.build-fanout "#build-spec.batch.build-fanout")

## `batch/build-graph`

Defines a _build graph_. A build graph defines a set
of tasks that have dependencies on other tasks in the batch. For more information, see
[Build graph](batch-build.md#batch_build_graph "batch-build.md#batch_build_graph").

This element contains an array of build tasks. Each build task contains the following
properties.

**identifier**

Required. The identifier of the task.

**buildspec**
Optional. The path and file name of the buildspec
file to use for this task. If this parameter is not specified, the current buildspec file is used.

**debug-session**

Optional. A Boolean value that indicates whether session debugging is
enabled for this batch build. For more information about session debugging,
see [Debug builds with Session Manager](session-manager.md "session-manager.md").

`false`

Session debugging is disabled.

`true`

Session debugging is enabled.

**depend-on**

Optional. An array of task identifiers that this task depends on. This task will
not run until these tasks are completed.

**env**

Optional. The build environment overrides for the task. This can contain
the following properties:

**compute-type**

The identifier of the compute type to use for the task. See
**computeType** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for possible
values.

**fleet**

The identifier of the fleet to use for the task. See
[Run builds on reserved capacity fleets](fleets.md "fleets.md") for more information.

**image**

The identifier of the image to use for the task. See
**Image identifier** in [Docker images provided by CodeBuild](build-env-ref-available.md "build-env-ref-available.md") for possible
values.

**privileged-mode**

A Boolean value that indicates whether to run the Docker
daemon inside a Docker container. Set to `true` only
if the build project is used to build Docker images. Otherwise,
a build that attempts to interact with the Docker daemon fails.
The default setting is `false`.

**type**

The identifier of the environment type to use for the task.
See **Environment type** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for possible
values.

**variables**

The environment variables that will be present in the build environment. See [env/variables](build-spec-ref.md#build-spec.env.variables "build-spec-ref.md#build-spec.env.variables") for more information.

###### Note

Note that **compute-type** and **fleet**
cannot be provided in the same identifer of a single build.

**ignore-failure**

Optional. A Boolean value that indicates if a failure of this build task
can be ignored.

`false`

The default value. If this build task fails, the batch build
will fail.

`true`

If this build task fails, the batch build can still succeed.

The following is an example of a build graph buildspec entry:

```
batch:
  fast-fail: false
  build-graph:
    - identifier: build1
      env:
        variables:
          BUILD_ID: build1
      ignore-failure: false
    - identifier: build2
      buildspec: build2.yml
      env:
        variables:
          BUILD_ID: build2
      depend-on:
        - build1
    - identifier: build3
      env:
        variables:
          BUILD_ID: build3
      depend-on:
        - build2
    - identifier: build4
      env:
        compute-type: ARM_LAMBDA_1GB
    - identifier: build5
      env:
        fleet: fleet_name

```

## `batch/build-list`

Defines a _build list_. A build list is used to
define a number of tasks that run in parallel. For more information, see [Build list](batch-build.md#batch_build_list "batch-build.md#batch_build_list").

This element contains an array of build tasks. Each build task contains the following
properties.

**identifier**

Required. The identifier of the task.

**buildspec**
Optional. The path and file name of the buildspec
file to use for this task. If this parameter is not specified, the current buildspec file is used.

**debug-session**

Optional. A Boolean value that indicates whether session debugging is
enabled for this batch build. For more information about session debugging,
see [Debug builds with Session Manager](session-manager.md "session-manager.md").

`false`

Session debugging is disabled.

`true`

Session debugging is enabled.

**env**

Optional. The build environment overrides for the task. This can contain
the following properties:

**compute-type**

The identifier of the compute type to use for the task. See
**computeType** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for possible
values.

**fleet**

The identifier of the fleet to use for the task. See
[Run builds on reserved capacity fleets](fleets.md "fleets.md") for more information.

**image**

The identifier of the image to use for the task. See
**Image identifier** in [Docker images provided by CodeBuild](build-env-ref-available.md "build-env-ref-available.md") for possible
values.

**privileged-mode**

A Boolean value that indicates whether to run the Docker
daemon inside a Docker container. Set to `true` only
if the build project is used to build Docker images. Otherwise,
a build that attempts to interact with the Docker daemon fails.
The default setting is `false`.

**type**

The identifier of the environment type to use for the task.
See **Environment type** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for possible
values.

**variables**

The environment variables that will be present in the build environment. See [env/variables](build-spec-ref.md#build-spec.env.variables "build-spec-ref.md#build-spec.env.variables") for more information.

###### Note

Note that **compute-type** and **fleet**
cannot be provided in the same identifer of a single build.

**ignore-failure**

Optional. A Boolean value that indicates if a failure of this build task
can be ignored.

`false`

The default value. If this build task fails, the batch build
will fail.

`true`

If this build task fails, the batch build can still succeed.

The following is an example of a build list buildspec entry:

```
batch:
  fast-fail: false
  build-list:
    - identifier: build1
      env:
        variables:
          BUILD_ID: build1
      ignore-failure: false
    - identifier: build2
      buildspec: build2.yml
      env:
        variables:
          BUILD_ID: build2
      ignore-failure: true
    - identifier: build3
      env:
        compute-type: ARM_LAMBDA_1GB
    - identifier: build4
      env:
        fleet: fleet_name
    - identifier: build5
      env:
        compute-type: GENERAL_LINUX_XLAGRE

```

## `batch/build-matrix`

Defines a _build matrix_. A build matrix defines
tasks with different configurations that run in parallel. CodeBuild creates a separate build
for each possible configuration combination. For more information, see [Build matrix](batch-build.md#batch_build_matrix "batch-build.md#batch_build_matrix").

**static**

The static properties apply to all build tasks.

**ignore-failure**

Optional. A Boolean value that indicates if a failure of this
build task can be ignored.

`false`

The default value. If this build task fails, the
batch build will fail.

`true`

If this build task fails, the batch build can
still succeed.

**env**

Optional. The build environment overrides for all tasks.

**privileged-mode**

A Boolean value that indicates whether to run the Docker
daemon inside a Docker container. Set to `true` only
if the build project is used to build Docker images. Otherwise,
a build that attempts to interact with the Docker daemon fails.
The default setting is `false`.

**type**

The identifier of the environment type to use for the task.
See **Environment type** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for possible
values.

**dynamic**

The dynamic properties define the build matrix.

**buildspec**

Optional. An array that contains the path and file names of
the buildspec files to use for these tasks. If this parameter is
not specified, the current buildspec file is used.

**env**

Optional. The build environment overrides for these
tasks.

**compute-type**

An array that contains the identifiers of the
compute types to use for these tasks. See
**computeType** in [Build environment compute modes and types](build-env-ref-compute-types.md "build-env-ref-compute-types.md") for
possible values.

**image**

An array that contains the identifiers of the
images to use for these tasks. See **Image
identifier** in [Docker images provided by CodeBuild](build-env-ref-available.md "build-env-ref-available.md") for possible
values.

**variables**

An array that contains the environment variables
that will be present in the build environments for
these tasks. See [env/variables](build-spec-ref.md#build-spec.env.variables "build-spec-ref.md#build-spec.env.variables") for more
information.

The following is an example of a build matrix buildspec entry:

```

batch:
  build-matrix:
    static:
      ignore-failure: false
    dynamic:
      buildspec:
        - matrix1.yml
        - matrix2.yml
      env:
        variables:
          MY_VAR:
            - VALUE1
            - VALUE2
            - VALUE3
```

For more information, see [Build matrix](batch-build.md#batch_build_matrix "batch-build.md#batch_build_matrix").

## `batch/build-fanout`

Defines a _build fanout_. A build fanout is
used to define a task that is split into multiple builds that runs in parallel. For more information, see [Execute parallel tests in batch builds](parallel-test.md "parallel-test.md").

This element contains an build task that can be split into multiple builds. The `build-fanout`
section contains the following properties.

**parallelism**

Required. The number of builds that will run tests in parallel.

**ignore-failure**

Optional. A boolean value that indicates if failure in any of the fanout build tasks can be ignored.
This value of **ignore-failure** will be applied to all the fanout builds.

**false**

The default value. If any fanout build task fails, the batch build will fail.

**true**

If any fanout build task fails, the batch build can still succeed.

The following is an example of a build fanout buildspec entry:

```
version: 0.2

batch:
   fast-fail: false
   build-fanout:
     parallelism: 5
     ignore-failure: false

phases:
  install:
    commands:
      - npm install
   build:
    commands:
      - mkdir -p test-results
      - cd test-results
      - |
        codebuild-tests-run \
         --test-command 'npx jest --runInBand --coverage' \
         --files-search "codebuild-glob-search '**/test/**/*.test.js'" \
         --sharding-strategy 'equal-distribution'
```

For more information, see [Build fanout](batch-build.md#batch_build_fanout "batch-build.md#batch_build_fanout") and [Use the codebuild-tests-run CLI command](parallel-test-tests-run.md "parallel-test-tests-run.md").
