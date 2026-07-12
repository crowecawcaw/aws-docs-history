# View lifecycle policy details

Use the EC2 Image Builder console, the AWS CLI, or the API to view lifecycle policy
configuration, execution history, and rule definitions.

###### Contents

- [View lifecycle policy details in the Image Builder console](#view-lifecycle-policy-details-console "#view-lifecycle-policy-details-console")

## View lifecycle policy details in the Image Builder console

The lifecycle policy detail page displays a summary section and
tabs with additional information.

###### Console detail sections and tabs

- [Summary section](#view-lifecycle-policy-console-summary "#view-lifecycle-policy-console-summary")
- [Rules tab](#view-lifecycle-policy-console-rules-tab "#view-lifecycle-policy-console-rules-tab")
- [Scope tab](#view-lifecycle-policy-console-scope-tab "#view-lifecycle-policy-console-scope-tab")
- [RunLog tab](#view-lifecycle-policy-console-runlog-tab "#view-lifecycle-policy-console-runlog-tab")

### Summary section

The summary section shows these details:

**Policy status**

Active (policy runs on schedule) or Inactive (policy is paused).

**Type**

Output image type: AMI or container image.

**Date created**

Timestamp when you created the policy.

**Date modified**

Timestamp of the most recent policy update.

**Last run date**

Timestamp of the most recent policy execution.

**IAM role**

IAM role that Image Builder assumes to perform lifecycle actions.

**ARN**

Amazon Resource Name (ARN) of the lifecycle policy.

**Description**

Policy description, if provided.

### Rules tab

The **Rules** tab displays the lifecycle rules
configured for this policy:

- **Name** – A fixed name that matches the
  policy action type:

  - `Deprecation rule`
  - `Disable rule`
  - `Deletion rule`

- **Rule** – Short description of the
  configured action.
- **Rule conditions** – Resource handling
  configuration, rule exceptions, and retention settings.

For more information about rule configuration, see [How lifecycle rules work](image-lifecycle-rules.md "image-lifecycle-rules.md").

### Scope tab

The **Scope** tab displays the resource selection
criteria for this policy:

- **Filter: `type of filter`** –
  The filter type that defines the scope:

  - `recipes` – Recipes used to create the
    images this policy applies to.
  - `tags` – Tags that Image Builder uses to select
    images this policy applies to.

- **Search** bar – Filters the list by
  **Name**.
- **Name** – Name or tag configured as
  filter criteria.
- **Version** – Recipe version
  (recipe filter only).

### RunLog tab

Image Builder saves runtime details for each policy execution. Each table
row represents one execution:

- **Execution ID** – Unique identifier
  for the execution instance.
- **Execution status** – Current execution
  state.
- **Resource impacted** – Indicates whether the
  execution identified image resources for lifecycle actions.
- **Start date** – Timestamp when the
  execution started.
- **End date** – Timestamp when the
  execution ended. This field is empty if the execution is in progress or pending.

For execution status descriptions, see
[Execution statuses](lifecycle-policy-execution.md#lifecycle-execution-statuses "lifecycle-policy-execution.md#lifecycle-execution-statuses").

###### Viewing per-resource details

Run the [list-lifecycle-execution-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html") AWS CLI command with the
execution ID to view individual resource outcomes. Each entry shows
the action taken, its result (succeeded, failed, or skipped), and
the reason.
