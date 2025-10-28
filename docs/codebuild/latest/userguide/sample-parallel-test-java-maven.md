# Configure parallel tests with Java (Maven)

The following is sample of a `buildspec.yml` that shows parallel test execution
with Java on an Linux platform:

```
version: 0.2

batch:
  fast-fail: false
  build-fanout:
    parallelism: 5
    ignore-failure: false

phases:
  pre_build:
    commands:
      - echo 'prebuild'
  build:
    commands:
      - echo "Running mvn test"
      - |
        codebuild-tests-run \
          --test-command 'mvn test -Dtest=$(echo "$CODEBUILD_CURRENT_SHARD_FILES" | sed "s|src/test/java/||g; s/\.java//g; s|/|.|g; s/ /,/g" | tr "\n" "," | sed "s/,$//")' \
          --files-search "codebuild-glob-search '**/test/**/*.java'"

  post_build:
    commands:
      - echo "Running post-build steps..."
      - echo "Test execution completed"
```

In the given example, the environment variable `CODEBUILD_CURRENT_SHARD_FILES` contains test files in the current shard, separated by newlines. These files are
converted into a comma-separated list of class names in the format accepted by the `-Dtest` parameter for Maven.
