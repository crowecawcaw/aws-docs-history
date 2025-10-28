# Enable parallel test execution in batch builds

To run tests in parallel, update the batch build buildspec file to include the build-fanout
field and the number of parallel builds to split the test suite in the `parallelism` field as
shown below. The `parallelism` field specifies how many independent executors are setup to execute
the test suite.

To run the tests in multiple parallel execution environments, set the `parallelism` field to a
value greater than zero. In example below, `parallelism` is set to five, meaning CodeBuild starts
five identical builds that executes a portion of the test suite in parallel.

You can use the [codebuild-tests-run](parallel-test-tests-run.md "parallel-test-tests-run.md") CLI command to split and run your tests.
Your test files will be split up, and a portion of your tests run in each build. This reduces
the overall time taken to run the full test suite. In the following example, tests will be split up into five
and the split points are calculated based on name of the tests.

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
      - npm install jest-junit --save-dev
  pre_build:
    commands:
      - echo 'prebuild'
  build:
    commands:
      - |
        codebuild-tests-run \
         --test-command 'npx jest --runInBand --coverage' \
         --files-search "codebuild-glob-search '**/_tests_/**/*.test.js'" \
         --sharding-strategy 'equal-distribution'

  post_build:
    commands:
      - codebuild-glob-search '**/*.xml'
      - echo "Running post-build steps..."
      - echo "Build completed on `date`"

reports:
  test-reports:
    files:
      - '**/junit.xml'
    base-directory: .
    discard-paths: yes
    file-format: JUNITXML
```

If reports are configured for build-fanout build, then the test reports are
generated for each build separately, which can be viewed under the **Reports** tab
of the corresponding builds in the AWS CodeBuild console.

For more information on how to execute parallel tests in batch, see
[Parallel test execution for various test frameworks sample](sample-parallel-test.md "sample-parallel-test.md").
