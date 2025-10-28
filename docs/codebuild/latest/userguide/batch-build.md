# Run builds in batches

You can use AWS CodeBuild to run concurrent and coordinated builds of a project with batch
builds.

###### Topics

- [Security role](#batch_security_role "#batch_security_role")
- [Batch build types](#batch_build_types "#batch_build_types")
- [Batch report mode](#batch-report-mode "#batch-report-mode")
- [More information](#batch_more_info "#batch_more_info")

## Security role

Batch builds introduce a new security role in the batch configuration. This new role
is required as CodeBuild must be able to call the `StartBuild`, `StopBuild`, and
`RetryBuild` actions on your behalf to run builds as part of a batch. Customers should use a new role, and
not the same role they use in their build, for two reasons:

- Giving the build role `StartBuild`, `StopBuild`, and `RetryBuild`
  permissions would allow a single build to start more builds via the buildspec.
- CodeBuild batch builds provide restrictions that restrict the number of builds and compute types that
  can be used for the builds in the batch. If the build role has these permissions, it is possible the builds
  themselves could bypass these restrictions.

## Batch build types

CodeBuild supports the following batch build types:

###### Batch build types

- [Build graph](#batch_build_graph "#batch_build_graph")
- [Build list](#batch_build_list "#batch_build_list")
- [Build matrix](#batch_build_matrix "#batch_build_matrix")
- [Build fanout](#batch_build_fanout "#batch_build_fanout")

### Build graph

A build graph defines a set of tasks that have dependencies on other tasks in the
batch.

The following example defines a build graph that creates a dependency chain.

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

In this example:

- `build1` runs first because it has no dependencies.
- `build2` has a dependency on `build1`, so
  `build2` runs after `build1` completes.
- `build3` has a dependency on `build2`, so
  `build3` runs after `build2` completes.

For more information about the build graph buildspec syntax, see [batch/build-graph](batch-build-buildspec.md#build-spec.batch.build-graph "batch-build-buildspec.md#build-spec.batch.build-graph").

### Build list

A build list defines a number of tasks that run in parallel.

The following example defines a build list. The `build1` and
`build2` builds will run in parallel.

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

For more information about the build list buildspec syntax, see [batch/build-list](batch-build-buildspec.md#build-spec.batch.build-list "batch-build-buildspec.md#build-spec.batch.build-list").

### Build matrix

A build matrix defines tasks with different configurations that run in parallel.
CodeBuild creates a separate build for each possible configuration combination.

The following example shows a build matrix with two buildspec files and three
values for an environment variable.

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

In this example, CodeBuild creates six builds:

- `matrix1.yml` with `$MY_VAR=VALUE1`
- `matrix1.yml` with `$MY_VAR=VALUE2`
- `matrix1.yml` with `$MY_VAR=VALUE3`
- `matrix2.yml` with `$MY_VAR=VALUE1`
- `matrix2.yml` with `$MY_VAR=VALUE2`
- `matrix2.yml` with `$MY_VAR=VALUE3`

Each build will have the following settings:

- `ignore-failure` set to `false`
- `env/type` set to `LINUX_CONTAINER`
- `env/image` set to
  `aws/codebuild/amazonlinux-x86_64-standard:4.0`
- `env/privileged-mode` set to `true`

These builds run in parallel.

For more information about the build matrix buildspec syntax, see [batch/build-matrix](batch-build-buildspec.md#build-spec.batch.build-matrix "batch-build-buildspec.md#build-spec.batch.build-matrix").

### Build fanout

A build fanout defines a task that will be split into multiple builds in the batch. This
can be used for running tests in parallel. CodeBuild creates a separate build for each shard
of test cases based on the value set in `parallelism` field.

The following example defines a build fanout that creates five builds that run in parallel.

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

In this example, assuming that there are 100 tests that needs to be run, CodeBuild creates five builds that each
runs 20 tests in parallel.

For more information about the build graph buildspec syntax, see [batch/build-fanout](batch-build-buildspec.md#build-spec.batch.build-fanout "batch-build-buildspec.md#build-spec.batch.build-fanout").

## Batch report mode

If the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise,
and your project is configured to report build statuses to the source provider, you can
select how you want your batch build statuses sent to the source provider. You can select
to have the statuses sent as a single aggregate status report for the batch, or have the
status of each build in the batch reported individually.

For more information, see the following topics:

- [Batch configuration (create)](create-project.md#create-project-console-batch-config "create-project.md#create-project-console-batch-config")
- [Batch configuration (update)](change-project.md#change-project-console-batch-config "change-project.md#change-project-console-batch-config")

## More information

For more information, see the following topics:

- [Batch build buildspec reference](batch-build-buildspec.md "batch-build-buildspec.md")
- [Batch configuration](create-project.md#create-project-console-batch-config "create-project.md#create-project-console-batch-config")
- [Run a batch build (AWS CLI)](run-batch-build-cli.md "run-batch-build-cli.md")
- [Stop batch builds in AWS CodeBuild](stop-batch-build.md "stop-batch-build.md")
