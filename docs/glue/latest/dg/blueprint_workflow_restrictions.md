# Blueprint and workflow restrictions in

AWS Glue

The following are restrictions for blueprints and workflows.

## Blueprint restrictions

Keep the following blueprint restrictions in mind:

- The blueprint must be registered in the same AWS Region where the Amazon S3
  bucket resides in.
- To share blueprints across AWS accounts you must give the read permissions
  on the blueprint ZIP archive in Amazon S3. Customers who have read permission on a
  blueprint ZIP archive can register the blueprint in their AWS account and
  use it.
- The set of blueprint parameters is stored as a single JSON object. The
  maximum length of this object is 128 KB.
- The maximum uncompressed size of the blueprint ZIP archive is 5 MB. The
  maximum compressed size is 1 MB.
- Limit the total number of jobs, crawlers, and triggers within a workflow to
  100 or less. If you include more than 100, you might get errors when trying to
  resume or stop workflow runs.

## Workflow restrictions

Keep the following workflow restrictions in mind. Some of these comments are directed
more at a user creating workflows manually.

- The maximum batch size for an Amazon EventBridge event trigger is 100. The maximum
  window size is 900 seconds (15 minutes).
- A trigger can be associated with only one workflow.
- Only one starting trigger (on-demand or schedule) is permitted.
- If a job or crawler in a workflow is started by a trigger that is outside the
  workflow, any triggers inside the workflow that depend on job or crawler
  completion (succeeded or otherwise) do not fire.
- Similarly, if a job or crawler in a workflow has triggers that depend on job
  or crawler completion (succeeded or otherwise) both within the workflow and
  outside the workflow, and if the job or crawler is started from within a
  workflow, only the triggers inside the workflow fire upon job or crawler
  completion.
