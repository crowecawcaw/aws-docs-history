# Nextflow workflow definition specifics

HealthOmics suppports Nextflow DSL1 and DSL2. For details, see [Nextflow version support](workflows-lang-versions.md#workflows-lang-versions-nextflow "workflows-lang-versions.md#workflows-lang-versions-nextflow").

Nextflow DSL2 is based on the Groovy programming language, so parameters are dynamic
and type coercion is possible using the same rules as Groovy. Parameters and values
supplied by the input JSON are available in the parameters (`params`) map of
the workflow.

###### Topics

- [Use nf-schema and nf-validation plugins](#schema-and-validation-plugins-nextflow "#schema-and-validation-plugins-nextflow")
- [Specify storage URIs](#storage-uris-nextflow "#storage-uris-nextflow")
- [Nextflow directives](#workflow-nexflow-directives "#workflow-nexflow-directives")
- [Export task content](#exporting-task-content-nextflow "#exporting-task-content-nextflow")

## Use nf-schema and nf-validation plugins

###### Note

Summary of HealthOmics support for plugins:

- v22.04 – no support for plugins
- v23.10 – supports `nf-schema` and `nf-validation`
- v24.10 – supports `nf-schema`

HealthOmics provides the following support for Nextflow plugins:

- For Nextflow v23.10, HealthOmics pre-installs the nf-validation@1.1.1 plugin.
- For Nextflow v23.10 and later, HealthOmics pre-installs the nf-schema@2.3.0 plugin.
- You cannot retrieve additional plugins during a workflow run. HealthOmics ignores any other plugin versions
  that you specify in the `nextflow.config` file.
- For Nextflow v24 and higher, `nf-schema` is the new version of the deprecated
  `nf-validation` plugin. For more information, see [nf-schema](https://github.com/nextflow-io/nf-schema "https://github.com/nextflow-io/nf-schema") in the Nextflow GitHub
  repository.

## Specify storage URIs

When an Amazon S3 or HealthOmics URI is used to construct a Nextflow file or path object,
it makes the matching object available to the workflow, as long as read access is
granted. The use of prefixes or directories is allowed for Amazon S3 URIs.
For examples, see [Amazon S3 input parameter formats](workflows-run-inputs.md#s3-run-input-formats "workflows-run-inputs.md#s3-run-input-formats").

HealthOmics partially supports the use of glob patterns in Amazon S3 URIs or HealthOmics Storage URIs.
Use Glob patterns in the
workflow definition for the creation of `path` or `file`
channels. For the expected behavior and exact cases, see [Nextflow Handling of Glob pattern in Amazon S3 inputs](workflows-run-inputs.md#wd-nextflow-s3-formats "workflows-run-inputs.md#wd-nextflow-s3-formats").

## Nextflow directives

You configure Nextflow directives in the Nextflow config file or workflow definition. The following list shows
the order of precedence that HealthOmics uses to apply configuration settings, from lowest to highest priority:

1. Global configuration in the config file.
2. Task section of the workflow definition.
3. Task-specific selectors in the config file.

###### Topics

- [Task retry strategy using errorStrategy](#workflow-nextflow-errorStrategy "#workflow-nextflow-errorStrategy")
- [Task retry attempts using maxRetries](#workflow-nexflow-task-retry "#workflow-nexflow-task-retry")
- [Opt out of task retry using omicsRetryOn5xx](#workflow-nextflow-retry-5xx "#workflow-nextflow-retry-5xx")
- [Task duration using the time directive](#time-directive-nextflow "#time-directive-nextflow")

### Task retry strategy using `errorStrategy`

Use the `errorStrategy` directive to define the strategy for task errors. By default, when a task
returns with an error indication (a non-zero exit status), the task stops and HealthOmics terminates the entire run. If
you set `errorStrategy` to `retry`, HealthOmics attempts one retry of the failed task. To
increase the number of retries, see [Task retry attempts using maxRetries](#workflow-nexflow-task-retry "#workflow-nexflow-task-retry").

```
process {
    label 'my_label'
    errorStrategy 'retry'

    script:
    """
    your-command-here
    """
}
```

For information about how HealthOmics handles task retries during a run, see [Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

### Task retry attempts using `maxRetries`

By default, HealthOmics doesn't attempt any retries of a failed task, or attempts one retry if you
configure `errorStrategy`. To increase the maximum number of retries, set `errorStrategy`
to `retry` and configure the maximum number of retries using the `maxRetries` directive.

The following example sets the maximum number of retries to 3 in the global configuration.

```
process {
    errorStrategy = 'retry'
    maxRetries = 3
}
```

The following example shows how to set `maxRetries` in the task section of the workflow definition.

```
process myTask {
    label 'my_label'
    errorStrategy 'retry'
    maxRetries 3

    script:
    """
    your-command-here
    """
}
```

The following example shows how to specify task-specific configuration in the Nextflow
config file, based on the name or label selectors.

```
process {
    withLabel: 'my_label' {
        errorStrategy = 'retry'
        maxRetries = 3
    }

    withName: 'myTask' {
        errorStrategy = 'retry'
        maxRetries = 3
    }
}
```

### Opt out of task retry using `omicsRetryOn5xx`

For Nextflow v23 and v24, HealthOmics supports task retries if the task failed because of service errors (5XX HTTP
status codes). By default, HealthOmics attempts up to two retries of a failed task.

You can configure `omicsRetryOn5xx` to opt out of task retry for service errors. For more
information about task retry in HealthOmics, see [Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

The following example configures `omicsRetryOn5xx` in the global configuration to opt out of task
retry.

```
process {
    omicsRetryOn5xx = false
}
```

The following example shows how to configure `omicsRetryOn5xx` in the task section of the
workflow definition.

```
process myTask {
    label 'my_label'
    omicsRetryOn5xx = false

    script:
    """
    your-command-here
    """
}
```

The following example shows how to set `omicsRetryOn5xx` as task-specific configuration in the
Nextflow config file, based on the name or label selectors.

```
process {
    withLabel: 'my_label' {
        omicsRetryOn5xx = false
    }

    withName: 'myTask' {
        omicsRetryOn5xx = false
    }
}
```

### Task duration using the `time` directive

HealthOmics provides an adjustable quota (see [HealthOmics service quotas](service-quotas.md "service-quotas.md")) to
specify the maximum duration for a run. For Nextflow v23 and v24 workflows, you can also specify maximum task
durations using the Nextflow `time` directive.

During new workflow development, setting maximum task duration helps you catch runaway tasks and
long-running tasks.

For more information about the Nextflow time directive, see [time directive](https://www.nextflow.io/docs/latest/reference/process.html#process-time "https://www.nextflow.io/docs/latest/reference/process.html#process-time") in the
Nextflow reference.

HealthOmics provides the following support for the Nextflow time directive:

1. HealthOmics supports 1 minute granularity for the time directive. You can specify a value between 60 seconds
   and the maximum run duration value.
2. If you enter a value less than 60, HealthOmics rounds it up to 60 seconds. For values above 60, HealthOmics rounds
   down to the nearest minute.
3. If the workflow supports retries for a task, HealthOmics retries the task if it times out.
4. If a task times out (or the last retry times out), HealthOmics cancels the task. This operation can have a
   duration of one to two minutes.
5. On task timeout, HealthOmics sets the run and task status to failed, and it cancels the other tasks in the
   run (for tasks in Starting, Pending, or Running status). HealthOmics exports the outputs from tasks that it
   completed before the timeout to your designated S3 output location.
6. Time that a task spends in pending status does not count toward the task duration.
7. If the run is part of a run group and the run group times out sooner than the task timer, the run and
   task transition to failed status.

Specify the timeout duration using one or more of the following units: `ms`, `s`,
`m`,`h`, or `d`.

The following example shows how to specify global configuration in the Nextflow config file. It sets a
global timeout of 1 hour and 30 minutes.

```
process {
    time = '1h30m'
}
```

The following example shows how to specify a time directive in the task section of the workflow definition.
This example sets a timeout of 3 days, 5 hours, and 4 minutes. This value takes precedence over the global value
in the config file, but doesn't take precedence over a task-specific time directive for `my_label` in
the config file.

```
process myTask {
    label 'my_label'
    time '3d5h4m'

    script:
    """
    your-command-here
    """
}
```

The following example shows how to specify task-specific time directives in the Nextflow config file, based
on the name or label selectors. This example sets a global task timeout value of 30 minutes. It sets a value of 2
hours for task `myTask` and sets a value of 3 hours for tasks with label `my_label`. For
tasks that match the selector, these values take precedence over the global value and the value in the workflow
definition.

```
process {
    time = '30m'

    withLabel: 'my_label' {
        time = '3h'
    }

    withName: 'myTask' {
        time = '2h'
    }
}
```

## Export task content

For workflows written in Nextflow, define a **publishDir** directive to export task content
to your output Amazon S3 bucket. As shown in the following example, set the **publishDir** value to
`/mnt/workflow/pubdir`. To export files to Amazon S3, the files must be in this directory.

```
 nextflow.enable.dsl=2

  workflow {
    CramToBamTask(params.ref_fasta, params.ref_fasta_index, params.ref_dict, params.input_cram, params.sample_name)
    ValidateSamFile(CramToBamTask.out.outputBam)
  }

  process CramToBamTask {
    container "<account>.dkr.ecr.us-west-2.amazonaws.com/genomes-in-the-cloud"

    publishDir "/mnt/workflow/pubdir"

    input:
        path ref_fasta
        path ref_fasta_index
        path ref_dict
        path input_cram
        val sample_name

    output:
        path "${sample_name}.bam", emit: outputBam
        path "${sample_name}.bai", emit: outputBai

    script:
    """
        set -eo pipefail

        samtools view -h -T $ref_fasta $input_cram |
        samtools view -b -o ${sample_name}.bam -
        samtools index -b ${sample_name}.bam
        mv ${sample_name}.bam.bai ${sample_name}.bai
    """
  }

  process ValidateSamFile {
    container "<account>.dkr.ecr.us-west-2.amazonaws.com/genomes-in-the-cloud"

    publishDir "/mnt/workflow/pubdir"

    input:
        file input_bam

    output:
        path "validation_report"

    script:
    """
        java -Xmx3G -jar /usr/gitc/picard.jar \
        ValidateSamFile \
        INPUT=${input_bam} \
        OUTPUT=validation_report \
        MODE=SUMMARY \
        IS_BISULFITE_SEQUENCED=false
    """
  }
```
