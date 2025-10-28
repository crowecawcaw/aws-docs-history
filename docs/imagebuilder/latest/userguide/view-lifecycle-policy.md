# View lifecycle policy details

The lifecycle policy detail page in the Image Builder console includes a summary section, with
additional information grouped into tabs. The page heading is the name of the policy.

On the lifecycle policy details page in the Image Builder console, you can view details for a specific
lifecycle policy. You can also use commands or actions with the Image Builder API, SDKs, or
AWS CLI to get policy details.

###### Contents

- [View lifecycle policy details
  in the Image Builder console](#view-lifecycle-policy-details-console "#view-lifecycle-policy-details-console")

## View lifecycle policy details

in the Image Builder console

The image detail page in the Image Builder console includes a summary section, with
additional information grouped into tabs. The page heading is the
name and build version of the recipe that created the image.

###### Console detail sections and tabs

- [Summary section](#view-lifecycle-policy-console-summary "#view-lifecycle-policy-console-summary")
- [Rules tab](#view-lifecycle-policy-console-rules-tab "#view-lifecycle-policy-console-rules-tab")
- [Scope tab](#view-lifecycle-policy-console-scope-tab "#view-lifecycle-policy-console-scope-tab")
- [RunLog tab](#view-lifecycle-policy-console-runlog-tab "#view-lifecycle-policy-console-runlog-tab")

### Summary section

The summary section spans the width of the page and includes the following details.
These details are always displayed.

**Policy status**

Whether the policy is active or inactive.

**Type**

The type of output image that Image Builder distributes when you create
a new image version (AMI or container image).

**Date created**

The timestamp from the creation of the lifecycle policy.

**Date modified**

The last time the lifecycle policy was updated.

**Last run date**

The last time the lifecycle policy ran.

**IAM role**

The IAM role that Image Builder uses to perform lifecycle actions.

**ARN**

The Amazon Resource Name (ARN) of the lifecycle policy resource.

**Description**

The description for the lifecycle policy, if entered.

### Rules tab

The **Rules** tab displays the lifecycle rules that you
configured for the policy you're viewing. The tab includes the following details:

- **Name** – The name of the rule. These names are
  static, based on policy actions you can configure.
  - `Deprecation rule`
  - `Disable rule`
  - `Deletion rule`

- **Rule** – A short description of the action
  that's configured for the rule.
- **Rule conditions** – Lists configuration for
  associated resource handling, exceptions to the rule, and retention
  settings, if applicable.

For more information about rule configuration, see [How lifecycle rules work](image-lifecycle-rules.md "image-lifecycle-rules.md").

### Scope tab

The **Scope** tab displays the resource selection criteria that are
configured for the policy you're viewing. The tab includes the following details:

- **Filter: `type of filter`** –
  The filter type you used to define the scope. The filter type can be one of the
  following:
  - `recipes` – The recipes that were used to create
    the images that the lifecycle policy applies to.
  - `tags` – A set of tags that Image Builder uses to select
    image resources that the lifecycle policy applies to.

- A search bar – You can filter the list by **Name** to
  streamline results that display in the tab.
- **Name** – Each row contains a name or tag that you've
  configured for the filter criteria.
- **Version** – If you've configured a recipe filter, Image Builder
  displays the recipe version.

### RunLog tab

Each time you run the policy for your configured resources, Image Builder saves runtime details.
Each row in the table represents a single runtime instance. The tab includes the following
details:

- **Execution ID** – Identifies the lifecycle policy
  runtime instance.
- **Execution status** – Runtime status that reports if the
  policy action is currently running, ran successfully, failed, or was canceled.
- **Resource impacted** – Indicates whether the runtime
  instance identified any image resources for lifecycle actions.
- **Start date** – The timestamp when the runtime
  instance started.
- **End date** – The timestamp when the runtime
  instance ended.
