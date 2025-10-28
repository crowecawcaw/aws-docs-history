# Builds in AWS CodeBuild

A _build_ represents a set of actions performed by AWS CodeBuild to create
output artifacts (for example, a JAR file) based on a set of input artifacts (for example, a
collection of Java class files).

The following rules apply when you run multiple builds:

- When possible, builds run concurrently. The maximum number of concurrently running
  builds can vary. For more information, see [Quotas for AWS CodeBuild](limits.md "limits.md").
- If the build project has a concurrent build limit set, builds return an error if
  the number of running builds reaches the concurrent build limit for the project. For
  more information, see [Enable
  concurrent build limit](create-project.md#enable-concurrent-build-limit.console "create-project.md#enable-concurrent-build-limit.console").
- If the build project does not have a concurrent build limit set, builds are queued
  if the number of running builds reaches the concurrent build limit for
  the platform and compute type. The maximum number of builds in a queue is five times
  the concurrent build limit. For more information, see [Quotas for AWS CodeBuild](limits.md "limits.md").

A build in a queue that does not start after the number of minutes specified in
its time out value is removed from the queue. The default timeout value is eight
hours. You can override the build queue timeout with a value between five minutes
and eight hours when you run your build. For more information, see [Run AWS CodeBuild builds manually](run-build.md "run-build.md").

It is not possible to predict the order in which queued builds start.

###### Note

You can access the history of a build for one year.

You can perform these tasks when working with builds:

###### Topics

- [Run AWS CodeBuild builds manually](run-build.md "run-build.md")
- [Run builds on AWS Lambda compute](lambda.md "lambda.md")
- [Run builds on reserved capacity fleets](fleets.md "fleets.md")
- [Run builds in batches](batch-build.md "batch-build.md")
- [Execute parallel tests in batch builds](parallel-test.md "parallel-test.md")
- [Cache builds to improve performance](build-caching.md "build-caching.md")
- [Debug builds in AWS CodeBuild](debug-builds.md "debug-builds.md")
- [Delete builds in AWS CodeBuild](delete-builds.md "delete-builds.md")
- [Retry builds manually in AWS CodeBuild](retry-build.md "retry-build.md")
- [Retry builds automatically in AWS CodeBuild](auto-retry-build.md "auto-retry-build.md")
- [Stop builds in AWS CodeBuild](stop-build.md "stop-build.md")
- [Stop batch builds in AWS CodeBuild](stop-batch-build.md "stop-batch-build.md")
- [Trigger AWS CodeBuild builds automatically](build-triggers.md "build-triggers.md")
- [View build details in AWS CodeBuild](view-build-details.md "view-build-details.md")
- [View a list of build IDs in AWS CodeBuild](view-build-list.md "view-build-list.md")
- [View a list of build IDs for a build project in
  AWS CodeBuild](view-builds-for-project.md "view-builds-for-project.md")
