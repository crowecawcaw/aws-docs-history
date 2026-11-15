

# Engine-specific caching features
<a name="workflow-cache-per-engine"></a>

HealthOmics tries to provide a consistent implementation of call caching across workflow engines. There are some differences based on how each workflow engine handles specific cases:

**Declare only the files that a task creates as its outputs.** In all three workflow languages, it's possible to re-declare a task *input* (such as a reference genome) as a task *output* so that the next task receives it. Avoid this pattern when you use call caching. The run cache stores a complete copy of every declared output for every cached task. A shared input that is passed through many tasks is stored once per task, which multiplies your cache size by the number of tasks:
+ **Longer export times** — each task's copy of the file is written to the run cache during the export phase, which can extend the run's export time by hours.
+ **Higher Amazon S3 storage costs** — all copies remain in the run cache Amazon S3 location until you delete them.
+ **Slower resume** — on a cache hit, each task downloads its own copy of the file again.

For example, if 500 tasks each re-declare a 3 GiB reference genome as an output, the run cache stores about 1.5 TiB of identical copies of that one file.

Instead, pass shared files to each task directly from the workflow inputs. Workflow inputs are read from their Amazon S3 source and are never stored in the run cache. The sections below show the pattern to avoid in each language.
+ Nextflow
  + Don't declare a process input in the `output:` block, and don't use `includeInputs: true`, when the run uses call caching. Every cached task stores its own copy of the input file in the run cache. Connect downstream processes to the original channel instead. See the example following this list.
  + Caching across different Nextflow versions is not guaranteed. If you run a task on one Nextflow version and then run the same task on a different Nextflow version, HealthOmics might consider the second run to be a cache miss.
  + You can turn off caching for individual tasks by using the cache **false** directive. For information about this directive, see the [ Processes](https://www.nextflow.io/docs/latest/process.html#process-cache) in the Nextflow specification.
  + HealthOmics uses Nextflow lenient mode, but doesn't support deep caching mode. 
  + Caching evaluates each individual S3 object if you use a glob pattern in the S3 path to the inputs for a task. If you add a new object, HealthOmics recomputes only the tasks that use the new object.
  + HealthOmics doesn't cache task retries. This behavior is consistent with Nextflow’s default behavior.

  **Avoid: passing the reference through each process**

  Here, `ALIGN` re-declares the reference as an output so that `CALL_VARIANTS` can receive it. When this workflow runs with 500 samples, every `ALIGN` task stores its own copy of the reference in the run cache.

  ```
  workflow {
      ALIGN(reads_ch, reference)        // reference is a workflow input
      CALL_VARIANTS(ALIGN.out)          // receives the reference from ALIGN's outputs
  }
  
  process ALIGN {
      input:
      path reads
      path reference
  
      output:
      tuple path("aligned.bam"), path(reference)   // Avoid: re-declares an input as an output
  
      script:
      """
      aligner ${reads} ${reference} > aligned.bam
      """
  }
  ```

  **Recommended: pass the reference to each process directly**

  Each process takes the reference from the workflow input. Only the files each task creates go into the run cache.
+ WDL
  + HealthOmics supports the new “directory” type for inputs when you use the development version of the WDL workflow. For call caching, if any object in the directory changes, HealthOmics recomputes all tasks that input the directory.
  + HealthOmics supports task-level caching, but not workflow-level caching. 
  + You can disable caching for individual tasks by using the **volatile** attribute. For more information, see [Disable task-level caching with the volatile attribute](workflow-languages-wdl.md#workflow-wdl-volatile-attribute).
+ CWL
  + Constant outputs from tasks aren't explicitly visible from the manifests. HealthOmics caches constant outputs as intermediate files.
  + You can control caching for individual tasks by using the [WorkReuse](https://www.commonwl.org/v1.1/Workflow.html#WorkReuse) feature.