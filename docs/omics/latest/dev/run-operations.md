

# Run operations in HealthOmics
<a name="run-operations"></a>

You can start, rerun, clone, cancel, delete, or get information on a run:
+ **Start** – HealthOmics creates a new run using the configuration settings you specify and then starts the run.
+ **Get run information** – You can retrieve the status, configuration, and task-level details of any run you have executed, using the **get-run** API or the HealthOmics console. You can also list all runs, list the tasks within a run, and access run metadata in CloudWatch Logs.
+ **Rerun** – HealthOmics creates a new run that's a duplicate of the run that you specify. You can rerun a deleted run using the HealthOmics **rerun** tool.
+ **Clone** – You can clone an existing run using the console. The console opens the **Clone run** page and prefills the configuration fields using the values from the existing run. You can modify the values as required and start the cloned run.
+ **Cancel** – You can cancel a run that hasn't completed yet. When you cancel a run, HealthOmics doesn't save any of the run outputs.
+ **Delete** – You can delete completed runs manually, or set the run retention mode for HealthOmics to delete the oldest runs automatically. For more information about retention mode, see [Run retention mode for HealthOmics runs](run-retention.md).

**Topics**
+ [Start a run in HealthOmics](starting-a-run.md)
+ [Get run information](getinfo-about-runs.md)
+ [Rerun a run in HealthOmics](rerun-a-run.md)
+ [Clone a run in HealthOmics](workflows-run-clone.md)
+ [Cancel a run in HealthOmics](canceling-runs.md)
+ [Delete a run in HealthOmics](deleting-runs.md)