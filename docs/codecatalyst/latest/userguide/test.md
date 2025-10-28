Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Integrating with universal-test-runner

Test actions integrate with the open-source command line tool
`universal-test-runner`. `universal-test-runner` uses
the [Test Execution Protocol](https://github.com/aws/universal-test-runner/blob/main/protocol/README.md "https://github.com/aws/universal-test-runner/blob/main/protocol/README.md") to run your tests for any language in a given framework.
`universal-test-runner` supports the following frameworks:

- [Gradle](https://gradle.org/ "https://gradle.org/")
- [Jest](https://jestjs.io/ "https://jestjs.io/")
- [Maven](https://maven.apache.org/ "https://maven.apache.org/")
- [pytest](https://pytest.org "https://pytest.org")
- [.NET](https://learn.microsoft.com/en-us/dotnet/core/tools/ "https://learn.microsoft.com/en-us/dotnet/core/tools/")
  `universal-test-runner` is installed only on the curated images for test
  actions. If you configure a test action to use a custom Docker Hub or Amazon ECR, you must manually install
  `universal-test-runner` to enable advanced testing features. To do so, install Node.js (14 or
  higher) on the image, then install `universal-test-runner` through `npm`
  using the shell command `- Run: npm install -g @aws/universal-test-runner`. For more
  information about installing Node.js in your container through shell commands, see [Installing and Updating Node
  Version Manager](https://github.com/nvm-sh/nvm#install--update-script "https://github.com/nvm-sh/nvm#install--update-script").

For more information about `universal-test-runner`, see [What is
universal-test-runner?](https://github.com/aws/universal-test-runner#-what-is-universal-test-runner "https://github.com/aws/universal-test-runner#-what-is-universal-test-runner")

Visual

###### To use universal-test-runner in the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow.
4. Choose **Edit**.
5. Choose **Visual**.
6. Choose **Actions**.
7. In **Actions**, choose **Test**.
8. On the **Configuration** tab, complete the **Shell
   commands** field by updating the sample code with your choice of the
   supported frameworks. For example, to use a supported framework, you would use a
   `Run` command similar to the following.

```
- Run: run-tests `<framework>`
```

If the framework you want is not supported, consider contributing a custom adapter or runner.
For a description of the **Shell commands** field, see [Steps](build-action-ref.md#build.configuration.steps "build-action-ref.md#build.configuration.steps"). 9. (Optional) Choose **Validate** to validate the workflow's YAML
code before committing. 10. Choose **Commit**, enter a commit message, and choose
**Commit** again.

YAML

###### To use universal-test-runner in the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow.
4. Choose **Edit**.
5. Choose **YAML**.
6. Choose **Actions**.
7. In **Actions**, choose **Test**.
8. Modify the YAML code according to your needs. For example, to use a supported
   framework, you would use a `Run` command similar to the following.

```
Configuration:
  Steps:
    - Run: run-tests `<framework>`

```

If the framework you want is not supported, consider contributing a custom adapter or runner. For a description
of the **Steps** property, see [Steps](build-action-ref.md#build.configuration.steps "build-action-ref.md#build.configuration.steps"). 9. (Optional) Choose **Validate** to validate the workflow's YAML
code before committing. 10. Choose **Commit**, enter a commit message, and choose
**Commit** again.
