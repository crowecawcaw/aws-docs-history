# Get public build project URLs

AWS CodeBuild allows you to make the build results, logs, and artifacts for your build projects
available to the general public. This allows contributors to your source repositories to view
the results and download the artifacts of a build, without requiring them to have access to an
AWS account.

When you make your project's builds available to the public, all of a project's build
results, logs, and artifacts, including builds that were run when the project was private, are
made available to the public. Likewise, when you make a public build project private, the build
results for that project are no longer available to the public.

For information about how to change the public visibility of your project's build results,
see [Enable public build access](change-project.md#change-project-console.public-builds "change-project.md#change-project-console.public-builds").

CodeBuild provides a URL for the public builds for your project that is unique to your
project.

To obtain the public URL for your build project, use the following procedure.

###### To obtain the URL of a public build project

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Build projects**.
3. Choose the link for the build project you want to obtain the public URL for.
4. The public URL is displayed in the **Public project URL** field in the
   **Configuration** section. You can choose the link to open the URL, or
   copy the URL with the copy button.

###### Warning

The following should be kept in mind when making your project's build results public:

- All of a project's build results, logs, and artifacts, including builds that were run
  when the project was private, are available to the public.
- All build logs and artifacts are available to the public. Environment variables, source
  code, and other sensitive information may have been output to the build logs and artifacts.
  You must be careful about what information is output to the build logs. Some best practices
  are:
  - Do not store sensitive values, especially AWS access key IDs and secret access
    keys, in environment variables. We recommend that you use an Amazon EC2 Systems Manager Parameter Store
    or AWS Secrets Manager to store sensitive values.
  - Follow [Best practices for using
    webhooks](webhooks.md#webhook-best-practices "webhooks.md#webhook-best-practices") to limit which entities can trigger a build, and do
    not store the buildspec in the project itself, to ensure that your webhooks are as
    secure as possible.

- A malicious user can use public builds to distribute malicious artifacts. We recommend
  that project administrators review all pull requests to verify that the pull request is a
  legitimate change. We also recommend that you validate any artifacts with their checksums to
  make sure that the correct artifacts are being downloaded.
