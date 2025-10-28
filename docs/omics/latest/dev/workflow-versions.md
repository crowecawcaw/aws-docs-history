AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Workflow versioning in HealthOmics

If you need to make a changes to a workflow, you can create either a new workflow or a new workflow version.
Versions are immutable, except for allowed configuration changes that don’t impact the execution logic.

Workflow versions provide the following benefits:

- Versions form a logical group of workflows that are related. You can add a user-defined name to each
  workflow version to manage them more easily (especially for a workflow with a large number of versions).
- You can run multiple versions of a workflow at the same time.
- All versions of a workflow share the same workflow ID and base ARN, which can simplify pipeline management
  after you modify a workflow.
- Workflow versions provide the same level of data provenance as workflows. Versions are immutable, and HealthOmics
  creates a unique ARN for each workflow version. The version ARN includes the workflow ID and the version name,
  as shown in the following example:

`arn:aws:omics:us-west-2:123456789012:workflow/1234567/version/myUniqueVersionName`

- If you own a shared workflow, you can update the workflow without disrupting the subscribers (who can
  continue to use the previous version). Subscribers can access all workflow versions. If you create a new
  version, you don't need to reshare the workflow.
- When you start a workflow run, you can specify the workflow version.
  - Users can choose to remain on a stable version for production runs, and try out the latest version for a
    test run.
  - Users can revert to the previous version of a workflow, if they encounter problems with the new
    version.
  - Subscribers of a shared workflow can choose which version to use.

###### Topics

- [Default workflow version](workflows-default-version.md "workflows-default-version.md")
- [Create a workflow version](workflows-version-create.md "workflows-version-create.md")
- [Update a workflow version](workflows-version-update.md "workflows-version-update.md")
- [Delete a workflow version](workflows-version-delete.md "workflows-version-delete.md")
