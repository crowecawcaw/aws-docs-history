# Troubleshooting build issues

If you encounter issues when creating or building an Amplify application, consult
the topics in this section for help.

###### Topics

- [New commits to my repository aren't triggering Amplify builds](#commits-not-triggering-builds "#commits-not-triggering-builds")
- [My repository name isn't listed in the Amplify console when creating a new application](#repo-not-listed "#repo-not-listed")
- [My build fails with the Cannot find module aws-exports error (Gen 1 apps only)](#cannot-find-aws-exports "#cannot-find-aws-exports")
- [I want to override a build timeout](#override-build-timeout "#override-build-timeout")

## New commits to my repository aren't triggering Amplify builds

If new commits to your Git repository aren't triggering Amplify builds, verify
that your webhook is still present on your repository. If it's present, check the
history of webhook requests to see if there are any failures. Amplify has a
payload size limit of 256 KB for incoming webhooks. If you push a commit to your
repository that has a large number of changed files, you might exceed this limit and
cause builds to not be triggered.

## My repository name isn't listed in the Amplify console when creating a new application

When you create a new application in the Amplify console, you can choose from
your organization's available repositories on the **Add repository and
branch** page. Your target repository might not be displayed in the
list if it hasn't been recently updated. This might occur if your organization has a
large number of repositories. To resolve this issue, push a commit to the
repository, then refresh the repository list in the console. This should cause the
repository to be displayed.

## My build fails with the `Cannot find module aws-exports` error (Gen 1 apps only)

If your app can't find the `aws-exports.js` file during a
build, the following error is returned.

```
TS2307: Cannot find module 'aws-exports'
```

The Amplify command line interface (CLI) generates the
`aws-exports.js` file during your backend build. To resolve
this error, you must create an `aws-exports.js` file for use in
the build. Add the following code to your build specification to create the
file:

```
backend:
  phases:
    build:
      commands:
        - "# Execute Amplify CLI with the helper script"
        - amplifyPush --simple
```

For a full example of the build specification settings for an Amplify app, see
[Build specification YAML syntax reference](yml-specification-syntax.md#build-yaml-syntax "yml-specification-syntax.md#build-yaml-syntax").

## I want to override a build timeout

The default build timeout is 30 minutes. You can override the default build
timeout using the `_BUILD_TIMEOUT` environment variable. The minimum
build timeout is 5 minutes. The maximum build timeout is 120 minutes.

For instructions on setting an environment variable for an app in the Amplify
console, see [Setting environment variables](setting-env-vars.md "setting-env-vars.md").
