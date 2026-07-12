# How lifecycle policy execution works

Image Builder runs enabled lifecycle policies on a recurring schedule. Each run is an
_execution_. During an execution, Image Builder evaluates your image
resources against the policy rules and performs the specified lifecycle actions.

###### Contents

- [Execution schedule](#lifecycle-execution-schedule "#lifecycle-execution-schedule")
- [Execution statuses](#lifecycle-execution-statuses "#lifecycle-execution-statuses")
- [How resources are evaluated](#lifecycle-execution-resource-evaluation "#lifecycle-execution-resource-evaluation")
- [How retention works for delete rules](#lifecycle-execution-retention "#lifecycle-execution-retention")
- [Manually managing resource state](#lifecycle-execution-manual "#lifecycle-execution-manual")
- [Canceling an execution](#lifecycle-execution-cancel "#lifecycle-execution-cancel")
- [How lifecycle policies handle externally modified resources](#lifecycle-execution-externally-modified "#lifecycle-execution-externally-modified")
- [Monitoring execution results](#lifecycle-execution-monitoring "#lifecycle-execution-monitoring")

## Execution schedule

Image Builder runs enabled lifecycle policies once per day.

- Image Builder manages the exact execution time. You cannot configure it.
- Only one execution runs per policy at a time. An in-progress or pending
  execution continues rather than starting a new one.
- Disabled policies do not run, and disabling a policy stops any pending
  execution from processing new resources.

## Execution statuses

Monitor lifecycle execution progress using the RunLog tab in the console or
the [list-lifecycle-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html")
AWS CLI command. Each execution reports one of these statuses:

`IN_PROGRESS`

Image Builder is actively evaluating resources and performing lifecycle
actions.

`PENDING`

Processing is paused. It resumes during the next
scheduled run.

`SUCCESS`

Image Builder processed all applicable resources successfully.

`FAILED`

One or more resource actions encountered an error. Use the [list-lifecycle-execution-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html") command to identify which
resources failed and why.

`CANCELLING`

Image Builder received a cancellation request and is finishing the current
processing step.

`CANCELLED`

The execution was canceled. Image Builder does not roll back resources
processed before cancellation.

## How resources are evaluated

Image Builder evaluates image resources from newest to oldest (by creation date)
using these steps:

1. **Resource selection** – Image Builder identifies
   all image resources matching the policy scope, defined by either a recipe
   filter (including version patterns) or a tag filter.
2. **Active build check** – Image Builder skips
   images with a build in progress (building, testing, or distributing state)
   and evaluates them in the next run.
3. **Rule evaluation** – Image Builder evaluates
   rules in priority order: deprecate, then disable, then delete. Only one action
   applies to each image per execution. If an image matches a deprecate rule,
   Image Builder skips the disable and delete rules for that image during the same run.

Evaluation differs by rule type:

For deprecate and disable rules

    1. AGE filter check (if configured) – Image Builder
     checks whether the image is older than the specified
     threshold.
    2. Image-level tag exclusion check
     (`exclusionRules.tagMap`) – Image Builder
     skips images that have an exclusion tag.

For delete rules

    1. AGE or COUNT filter check – For AGE, Image Builder
     checks whether the image is older than the threshold.
     For COUNT, Image Builder checks whether the retention count
     has been reached.
    2. Failed or canceled check – Images in a failed
     or canceled state qualify for deletion and do not
     consume a retention slot.
    3. Retention check – If you configured a
     `retainAtLeast` value (AGE filter) or a count
     value (COUNT filter), the newest images fill retention
     slots first. An image filling a retention slot stays
     without further evaluation.
    4. Image-level tag exclusion check
     (`exclusionRules.tagMap`) – For
     images that pass the retention check (images that
     would otherwise be deleted), Image Builder checks for an
     exclusion tag. If present, Image Builder skips the image.

###### Important

Image Builder evaluates retention before tag exclusion. An image
within the retention window remains protected regardless
of exclusion tags. Tag exclusion applies only to images
beyond the retention limit.

A tag-excluded image does not consume a retention slot and
does not affect the retention count for other images. 4. **AMI-level exclusion checks** – After
determining eligible images, Image Builder evaluates their output AMIs against
AMI-level exclusion rules (`exclusionRules.amis`). These rules
include Region exclusion, public AMI exclusion, AMI tag exclusion, shared
account exclusion, and last-launched exclusion. Image Builder reports an output AMI
that meets any exclusion criteria as `SKIPPED` with a reason
that indicates the matched condition.

###### Note

Subsequent executions apply disable or delete rules to previously
deprecated resources if they meet the criteria.

## How retention works for delete rules

Retention filters (AGE and COUNT) evaluate against Image Builder image resources,
not output AMIs or containers directly. Image Builder retains the newest images per
recipe version and marks older images for deletion.

For detailed retention calculation logic, including age-based and count-based
filter behavior, see
[How retention is calculated](image-lifecycle-rules.md#image-lifecycle-rules-retention "image-lifecycle-rules.md#image-lifecycle-rules-retention").

## Manually managing resource state

You can trigger immediate lifecycle state changes for a specific image build version
using the [start-resource-state-update](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/start-resource-state-update.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/start-resource-state-update.html") command, without waiting for the next
scheduled run.

Supported transitions:

- **Deprecate** – Mark an image as
  deprecated.
- **Disable** – Prevent an image
  from launching new instances.
- **Delete** – Delete an image and
  its associated resources (you must specify at least one
  associated resource type).
- **Available** – Return a deprecated
  or disabled image to available state.

Each manual state change creates a separate lifecycle execution. Track it
using the [list-lifecycle-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html") command.

## Canceling an execution

Cancel an in-progress or pending execution using the [cancel-lifecycle-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/cancel-lifecycle-execution.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/cancel-lifecycle-execution.html") command or the Image Builder console.

When you cancel an execution:

- The execution transitions to `CANCELLING` while finishing
  the current resource action.
- After the current action completes, the execution transitions to
  `CANCELLED`.
- Image Builder does not roll back already-processed resources. For example, an image
  deprecated before cancellation remains deprecated.
- Image Builder skips unprocessed resources.

## How lifecycle policies handle externally modified resources

You or other AWS services can modify resources in your account outside of Image Builder lifecycle policies.
Examples of external modifications:

- AMI deregistration through the Amazon EC2 console
- AMI deprecation using the Amazon EC2 API
- Container image deletion from an Amazon ECR repository
- Image Builder image resource deletion using the Image Builder API

If a resource is already deleted or already in the desired state, Image Builder
reports the action as `SUCCESS`. The policy does not fail when
resources have been cleaned up through other means.

###### Note

A `SKIPPED` status is different. Image Builder reports
`SKIPPED` only when a resource exists but an exclusion rule
prevents the action.

## Monitoring execution results

Monitor lifecycle execution results at two levels:

Execution level

View all executions for a policy, including status, start time,
and end time.

- **Console** – Open the
  lifecycle policy details page and choose the
  **RunLog** tab. For more information, see
  [RunLog tab](view-lifecycle-policy.md#view-lifecycle-policy-console-runlog-tab "view-lifecycle-policy.md#view-lifecycle-policy-console-runlog-tab").
- **AWS CLI** – Run [list-lifecycle-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-executions.html") with the lifecycle
  policy ARN.

Resource level

View per-resource outcomes within an execution.

- **Console** – In the
  **RunLog** tab, choose an execution ID to
  view processed resources.
- **AWS CLI** – Run [list-lifecycle-execution-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-lifecycle-execution-resources.html") with the
  execution ID.

Each resource entry includes:

- Resource ARN
- Action taken (or attempted)
- Resource status (`SUCCESS`, `FAILED`,
  or `SKIPPED`)
- Reason for the outcome (particularly useful for skipped or
  failed resources)
