# Dependency caching

You can enable local caching in CodeBuild to reduce the number of dependencies that need to
be fetched from CodeArtifact for each build. For information, see [Build
Caching in AWS CodeBuild](../../../codebuild/latest/userguide/build-caching.md "../../../codebuild/latest/userguide/build-caching.md") in the _AWS CodeBuild User Guide_. After you
enable a custom local cache, add the cache directory to your project's
`buildspec.yaml` file.

For example, if you are using `mvn`, use the following.

```
cache:
  paths:
    - '/root/.m2/**/*'
```

For other tools, use the cache folders shown in this table.

| Tool                 | Cache directory             |
| -------------------- | --------------------------- |
| **`mvn`**            | `/root/.m2/**/*`            |
| **`gradle`**         | `/root/.gradle/caches/**/*` |
| **`pip`**            | `/root/.cache/pip/**/*`     |
| **`npm`**            | `/root/.npm/**/*`           |
| **`nuget`**          | `/root/.nuget/**/*`         |
| **`yarn (classic)`** | `/root/.cache/yarn/**/*`    |
