# Engine-specific caching features

HealthOmics tries to provide a consistent implementation of call caching across workflow engines. There are
some differences based on how each workflow engine handles specific cases:

- Nextflow
  - Caching across different Nextflow versions is not guaranteed. For example, if you run a task in
    v23.10.0 and subsequently run the same task in v24.10.8, HealthOmics might consider the second run to be a cache
    miss.
  - You can turn off caching for individual tasks by using the cache **false** directive. For information
    about this directive, see the [Processes](https://www.nextflow.io/docs/latest/process.html#process-cache "https://www.nextflow.io/docs/latest/process.html#process-cache") in the Nextflow specification.
  - HealthOmics uses Nextflow lenient mode, but doesn't support deep caching mode.
  - Caching evaluates each individual S3 object if you use a glob pattern in the S3 path to the inputs for
    a task. If you add a new object, HealthOmics recomputes only the tasks that use the new object.
  - HealthOmics doesn't cache task retries. This behavior is consistent with Nextflow’s default behavior.

- WDL
  - HealthOmics supports the new “directory” type for inputs when you use the development version of the WDL
    workflow. For call caching, if any object in the directory changes, HealthOmics recomputes all tasks that input
    the directory.
  - HealthOmics supports task-level caching, but not workflow-level caching.

- CWL
  - Constant outputs from tasks aren't explicitly visible from the manifests. HealthOmics caches constant outputs
    as intermediate files.
