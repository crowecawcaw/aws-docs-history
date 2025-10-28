# GitLab manual webhooks

You can configure manual GitLab webhooks to prevent CodeBuild from automatically
attempting to create a webhook within GitLab. CodeBuild returns a payload URL in as part of the call to
create the webhook and can be used to manually create the webhook within GitLab. Even if CodeBuild is not allowlisted
to create a webhook in your GitLab account, you can still manually create a webhook for your build project.

Use the following procedure to create a GitLab manual webhook.

###### To create a GitLab manual webhook

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console") and
   [Run a build (console)](run-build-console.md "run-build-console.md").
   - In **Source**:
     - For **Source provider**, choose
       **GitLab**.
     - For **Repository**, choose **Repository in my GitLab account**.
     - For **Repository URL**, enter
       `https://gitlab.com/`user-name`/`repository-name``.

   - In **Primary source webhook events**:
     - For **Webhook - optional**, choose
       **Rebuild every time a code change is pushed to this repository**.
     - Choose **Additional configuration** and for **Manual creation - optional**,
       choose **Manually create a webhook for this repository in GitLab console.**.

3. Continue with the default values and then choose **Create build project**. Take note of the
   **Payload URL** and **Secret** values as you will use these later.
4. Open the GitLab console at
   `https://gitlab.com/`user-name`/`repository-name`/-/hooks`
   and choose **Add new webhook**.
   - For **URL**, enter the Payload URL value you took note of earlier.
   - For **Secret token**, enter the Secret value you took note of earlier.
   - Configure the individual events that will send a webhook payload to CodeBuild. For **Trigger**,
     choose from the following events: **Push events**, **Merge request events**, **Releases events**, and
     **Job events**. To learn more about event types supported by CodeBuild, see [GitLab webhook events](gitlab-webhook.md "gitlab-webhook.md").

5. Choose **Add webhook**.
