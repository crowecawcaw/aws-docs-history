# What is

OpenLineage?

[OpenLineage](https://openlineage.io/ "https://openlineage.io/") is an open platform for
collection and analysis of data lineage. It tracks metadata about datasets, jobs,
and runs, giving users the information required to identify the root cause of
complex issues and understand the impact of changes. It is an Open Standard for
lineage metadata collection designed to record metadata for a job in
execution.

The standard defines a generic model of dataset, job, and run entities uniquely
identified using consistent naming strategies. The dataset and job entities are
identified by combination of 'namespace' and 'name' attributes whereas run is
identified by runId. The entities can be enriched with user-defined metadata via
facets (similar to metadata forms in Amazon SageMaker Unified Studio).

OpenLineage supports three types of events: RunEvent, DatasetEvent and
JobEvent.

- RunEvent: this event is generated as a result of job-run execution. It
  contains details of the run, the job it belongs to, input datasets that run
  consumes and output datasets the run produces. Reference for samples run
  events. Currently, Amazon SageMaker Unified Studio only supports RunEvents.
- DatasetEvent: this event represents the changes in dataset (like any
  static updates on the dataset)
- JobEvent: this event represents the changes in job
  configuration/details
  In the current release of Amazon SageMaker Unified Studio, OpenLineage 1.22.0+ versions are
  supported.
