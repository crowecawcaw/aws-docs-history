# Buildkite manual webhooks

Currently, CodeBuild requires all Buildkite webhooks to be created manually. CodeBuild
returns a payload URL as part of the call to create the webhook, which can be used to
manually create the webhook within Buildkite.

Use the following procedure to create a Buildkite manual webhook.

###### To create a CodeBuild project with a webhook

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console") and
   [Run a build (console)](run-build-console.md "run-build-console.md").
3. In **Project configuration**, choose **Runner
   project**.

In **Runner**:

    * For **Runner provider**, choose
     **Buildkite**.
    * For **Buildkite agent token**, choose **Create a
     new agent token by using the create secret page**. You will be
     prompted to create a new secret in AWS Secrets Manager with a secret value
     equal to the Buildkite agent token you generated above.
    * (Optional) If you would like to use CodeBuild managed credentials for your
     job, select your job’s source repository provider under **Buildkite
     source credential options** and verify that credentials are
     configured for your account. Additionally, verify that your Buildkite
     pipeline uses **Checkout using HTTPS**.

4. - In **Environment**:
     - Choose a supported **Environment image** and
       **Compute**. Note that you have the option to
       override the image and instance settings by using a label in your
       GitHub Actions workflow YAML. For more information, see [Step 2: Update your GitHub
       Actions workflow YAML](action-runner.md#sample-github-action-runners-update-yaml "action-runner.md#sample-github-action-runners-update-yaml")

   - In **Buildspec**:
     - Note that your buildspec will be ignored unless
       `buildspec-override:true` is added as a label.
       Instead, CodeBuild will override it to use commands that will setup the
       self-hosted runner.

5. Continue with the default values and then choose **Create build
   project**.
6. Save the **Payload URL** and **Secret** values
   from the **Create Webhook** popup. Follow the
   instructions in the popup to create a new Buildkite organization webhook.
