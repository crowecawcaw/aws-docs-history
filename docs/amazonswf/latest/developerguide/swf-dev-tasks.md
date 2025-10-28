# Tasks in Amazon SWF

Amazon SWF interacts with activity workers and deciders by providing them with work assignments known as tasks.
There are three types of tasks in Amazon SWF:

- **Activity task** – An _Activity_ task tells an activity
  worker to perform its function, such as to check inventory or charge a credit card. The activity task contains
  all the information that the activity worker needs to perform its function.
- **Lambda task** – A _Lambda_ task is similar to an Activity
  task, but executes a Lambda function instead of a traditional Amazon SWF activity. For more information about how
  to define a Lambda task, see [AWS Lambda tasks in Amazon SWF](lambda-task.md "lambda-task.md").
- **Decision task** – A _Decision_ task tells a decider that
  the state of the workflow execution has changed so that the decider can determine the next activity that needs
  to be performed. The decision task contains the current workflow history.
  Amazon SWF schedules a decision task when the workflow starts and whenever the state of the workflow changes, such
  as when an activity task completes. Each decision task contains a paginated view of the entire workflow execution
  history. The decider analyzes the workflow execution history and responds back to Amazon SWF with a set of decisions that
  specify what should occur next in the workflow execution. Essentially, every decision task gives the decider an
  opportunity to assess the workflow and provide direction back to Amazon SWF.

To ensure that no conflicting decisions are processed, Amazon SWF assigns each decision task to exactly one decider
and allows only one decision task at a time to be active in a workflow execution.

The following table shows the relationship between the different constructs related to workflows and
deciders.

| Logical Design | Registered As | Performed By    | Receives & Performs | Generates    |
| -------------- | ------------- | --------------- | ------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workflow       | Workflow Type | Decider         | Decision Tasks      | Decisions    | When an activity worker has completed the activity task, it reports to Amazon SWF that the task was completed, and it includes any relevant results that were generated. Amazon SWF updates the workflow execution history with an event that indicates the task completed and then schedules a decision task to transmit the updated history to the decider. Amazon SWF assigns each activity task to exactly one activity worker. Once the task is assigned, no other activity worker can claim or perform that task. The following table shows the relationship between the different constructs related to activities. |
| Logical Design | Registered As | Performed By    | Receives & Performs | Generates    |
| ---            | ---           | ---             | ---                 | ---          |
| Activity       | Activity Type | Activity Worker | Activity Tasks      | Results Data |
