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
- [Use Nextflow profiles](#nextflow-profiles "#nextflow-profiles")
- [Export workflow-level content](#exporting-workflow-content-nextflow "#exporting-workflow-content-nextflow")
- [Export task content](#exporting-task-content-nextflow "#exporting-task-content-nextflow")
- [Generate Nextflow execution reports](#nextflow-execution-reports "#nextflow-execution-reports")
- [Specify the Nextflow syntax version](#nextflow-syntax-version "#nextflow-syntax-version")
- [Using scratch storage efficiently in Nextflow](#nextflow-scratch-storage "#nextflow-scratch-storage")
- [Nextflow v26.04 release notes](#nextflow-v26-release-notes "#nextflow-v26-release-notes")

## Use nf-schema and nf-validation plugins

###### Note

Summary of HealthOmics support for plugins:

- v22.04 – no support for plugins
- v23.10 – supports `nf-schema` and `nf-validation`
- v24.10 – supports `nf-schema`
- v25.10, v26.04 – supports `nf-schema`, `nf-core-utils`, `nf-fgbio`, and `nf-prov`

HealthOmics provides the following support for Nextflow plugins:

- For Nextflow v23.10, HealthOmics pre-installs the nf-validation@1.1.1 plugin.
- For Nextflow v23.10 and v24.10, HealthOmics pre-installs the nf-schema@2.3.0 plugin.
- For Nextflow v25.10, HealthOmics pre-installs the nf-schema@2.6.1, nf-core-utils@0.4.0, nf-prov@1.7.0, and nf-fgbio@1.0.1 plugins.
- For Nextflow v26.04, HealthOmics pre-installs the nf-schema@2.7.2, nf-core-utils@0.4.0, nf-prov@1.7.0, and nf-fgbio@1.0.1 plugins.
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

For Nextflow v23 and later, HealthOmics supports task retries if the task failed because of service errors (5XX HTTP
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
specify the maximum duration for a run. For Nextflow v23 and later workflows, you can also specify maximum task
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

## Use Nextflow profiles

Nextflow profiles are named sets of configuration settings that you can select at runtime. Define profiles in
the `profiles` block of your `nextflow.config` file:

```
profiles {
    standard {
        process.cpus = 2
        process.memory = '4 GB'
    }

    production {
        process.cpus = 16
        process.memory = '64 GB'
        params.input = 's3://bucket/production-data.bam'
    }
}
```

When you start a run, specify one or more profiles using the `engineSettings` parameter. HealthOmics passes
the `-profile` flag to the Nextflow engine. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings "starting-a-run.md#start-run-api-engine-settings").

```
aws omics start-run \
  --workflow-id `workflow-id` \
  --role-arn `role-arn` \
  --output-uri s3://`bucket`/`prefix`/ \
  --engine-settings '{"profile": "production"}'
```

When multiple profiles are specified (for example, `"test,docker"`), Nextflow applies them in the
order they are specified in the command line. Later profiles override earlier ones for conflicting settings. For
Nextflow versions lower than 26, profiles are applied in the order they are defined in the configuration file
instead of command line order.

Note the following:

- Profile support is available for all HealthOmics supported Nextflow versions.
- Profiles can contain parameters, process directives, `includeConfig` statements, and
  manifest overrides (including `manifest.nextflowVersion`).
- Explicit run parameters take precedence over profile-defined parameter values.
- If you specify a nonexistent profile, HealthOmics returns a validation error.
- Profiles must be defined in the workflow definition zip file. HealthOmics doesn't support fetching profile
  definitions from external sources.
- If you don't specify a profile, the run uses the `standard` profile if it's defined
  under profiles in the workflow definition. Otherwise, the run uses the default (top-level) configuration.
- When using profiles, we recommend pinning the Nextflow version in your workflow definition using
  `manifest.nextflowVersion` to ensure consistent profile application behavior across runs.

## Export workflow-level content

For Nextflow v25.10 and later, you can export files produced outside of individual tasks, such as
provenance reports or pipeline DAGs. To export these files, write them to
`/mnt/workflow/output/`. HealthOmics exports files placed in this directory to the
`output/` prefix in your run's Amazon S3 output location.

The following example shows how to configure the `nf-prov` plugin to write a
provenance report to `/mnt/workflow/output/`.

```
prov {
    formats {
        bco {
            file = "/mnt/workflow/output/pipeline_info/manifest.bco.json"
        }
    }
}
```

You can also pass this path as a parameter in your run's input JSON. This approach is common with nf-core
workflows that use `params.outdir`.

```
{
    "outdir": "/mnt/workflow/output/"
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

For Nextflow v25.10 and later, as an alternative to `publishDir`, you can use workflow outputs to export task content.
The following example shows how to define a workflow `output` block that
exports task results to Amazon S3.

```
process myTask {
    input:
    val data

    output:
    path 'result.txt'

    script:
    """
    echo ${data} > result.txt
    """
}

workflow {
    main:
    output_file = myTask('hello')

    publish:
    results = output_file
}

output {
    results {
        path '.'
    }
}
```

For more information about workflow outputs, see [Workflow
outputs](https://www.nextflow.io/docs/latest/workflow.html#workflow-output-def "https://www.nextflow.io/docs/latest/workflow.html#workflow-output-def") in the Nextflow documentation.

## Generate Nextflow execution reports

Nextflow can produce four built-in reports for each run: an execution report
(`report`), a timeline (`timeline`), a trace file
(`trace`), and a workflow diagram (`dag`). For HealthOmics to export
these files to your run's Amazon S3 output location, configure each one to write its
output under `/mnt/workflow/output/` in your `nextflow.config`
file:

```
report {
    enabled = true
    file = '/mnt/workflow/output/report.html'
    overwrite = true
}

timeline {
    enabled = true
    file = '/mnt/workflow/output/timeline.html'
    overwrite = true
}

trace {
    enabled = true
    file = '/mnt/workflow/output/trace.txt'
    overwrite = true
}

dag {
    enabled = true
    file = '/mnt/workflow/output/dag.html'
    overwrite = true
}
```

HealthOmics exports files written under `/mnt/workflow/output/` to the
`output/` prefix in your run's Amazon S3 output location. For more
information about this export path, see
[Export workflow-level content](#exporting-workflow-content-nextflow "#exporting-workflow-content-nextflow"). Reports written outside
`/mnt/workflow/output/` are not exported to your run's Amazon S3 output
location.

###### Task containers must include ps

When the `report`, `timeline`, or `trace`
report is enabled, Nextflow collects per-task metrics by invoking
`ps` inside each task container. The container image that you specify
with the `container` directive must include the `ps`
command. On most Linux distributions, install it with the `procps`
(Debian/Ubuntu) or `procps-ng` (Amazon Linux, Red Hat, Fedora)
package. If a process does not declare a `container` directive,
HealthOmics runs the task in a default container that already includes
`ps`.

###### Workflow diagram format

The `dag` report supports several output formats, selected by the
extension of `dag.file`. The HTML, Mermaid, and DOT formats are
rendered directly by Nextflow and do not require additional tooling. The PDF,
PNG, and SVG formats require Graphviz, which is not included in HealthOmics's Nextflow
engine. If `dag.file` is set to a PDF, PNG, or SVG path, Nextflow logs
a warning and writes the workflow diagram as a `.dot` source file in
its place; the run still completes successfully. We recommend setting
`dag.file` to a `.html`, `.mmd`, or
`.dot` path to avoid the warning and produce the requested
format.

## Specify the Nextflow syntax version

Nextflow v26.04.0 uses the strict (v2) syntax parser by default. This is a breaking change for
workflows written using the legacy (v1) syntax, which is the default in Nextflow v25.10.0 and earlier.
For information about the v2 syntax, see [Strict
syntax](https://docs.seqera.io/nextflow/strict-syntax "https://docs.seqera.io/nextflow/strict-syntax") in the Seqera Nextflow documentation.

To run a workflow authored against the legacy (v1) parser, set `engineSettings.syntaxVersion`
to `v1` in the **StartRun** request:

```
{
  "engineSettings": {
    "syntaxVersion": "v1"
  }
}
```

For Nextflow v25.10.0 and earlier, HealthOmics does not support the v2 parser.

## Using scratch storage efficiently in Nextflow

Nextflow's `scratch` directive controls where a process writes its temporary working files.
When ephemeral storage is enabled (`scratchStorageMode: LOCAL`), use the `scratch`
directive to direct scratch I/O to the fast local volume at `/tmp`.

The following table describes the supported `scratch` directive values and their behavior in
HealthOmics:

| Value                  | Behavior in HealthOmics                                                                                                                                                                             | Recommendation                  |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `scratch true`         | Uses `$TMPDIR`. Scratch I/O is directed to the local ephemeral volume when<br>`scratchStorageMode` is `LOCAL`.                                                                                      | Recommended                     |
| `scratch '/some/path'` | Uses the specified literal path as the scratch directory. To use ephemeral storage, set the path<br>to `/tmp` or a subdirectory of `/tmp`. The path must exist in the container and<br>be writable. | Works when path is under `/tmp` |
| `scratch 'ram-disk'`   | Attempts to use `/dev/shm` (tmpfs in RAM). This is not recommended for local scratch<br>storage in HealthOmics.                                                                                     | Not recommended                 |

The recommended approach is to set `scratch true` in your process definition, which
automatically uses `$TMPDIR` and requires no path configuration:

```
process my_process {
    scratch true
    disk '200 GB'
    script:
    """
    my-tool --input ${input} --output ${output}
    """
}
```

For more information about ephemeral storage and the `disk` directive, see
[Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md "workflows-ephemeral-storage.md").

## Nextflow v26.04 release notes

The following tables summarize HealthOmics support for new features, enhancements, and deprecations
released in Nextflow version 26.04.

### New features and enhancements

| Feature                                | From version | HealthOmics support | Notes                                                                                                                                                                                                                                                                                               |
| -------------------------------------- | ------------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strict syntax parser (default)         | 26.04        | Yes                 | Enabled by default from v26.04. Legacy parser available via<br>`syntaxVersion: "v1"` in engine settings.                                                                                                                                                                                            |
| Record types                           | 26.04        | Yes                 | For more information, see [Records](https://docs.seqera.io/nextflow/script#records "https://docs.seqera.io/nextflow/script#records") in the<br>Seqera Nextflow documentation.                                                                                                                       |
| Workflow output summaries              | 26.04        | Yes                 | Prints a summary of workflow outputs on run completion. Output format configurable<br>via `outputFormat` in engine settings.<br>For more information, see<br>[Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings "starting-a-run.md#start-run-api-engine-settings"). |
| Agent logging mode                     | 26.04        | Yes                 | Configurable via `agentMode` in engine settings. For more information, see<br>[Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings "starting-a-run.md#start-run-api-engine-settings").                                                                                |
| Module system (Nextflow Registry)      | 26.04        | No                  | HealthOmics workflows run in an isolated network with no outbound internet access.<br>You can include modules directly in your workflow zip.                                                                                                                                                        |
| Static typing (preview)                | 26.04        | No                  | HealthOmics does not support preview features.                                                                                                                                                                                                                                                      |
| Auto-load collection params from files | 26.04        | No                  | Requires static typing (preview), which HealthOmics does not support.                                                                                                                                                                                                                               |
| Multi-revision pipelines checkout      | 26.04        | N/A                 | Not applicable. HealthOmics does not use Git-based pipeline checkout.                                                                                                                                                                                                                               |

### Deprecations

| Deprecated item               | From version | Impact              | Recommended action                                                                                               |
| ----------------------------- | ------------ | ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `listFiles()` method          | 26.04        | Deprecation warning | Replace with `listDirectory()`.                                                                                  |
| `nextflow.enable.strict` flag | 26.04        | No longer needed    | Remove from config. Strict mode is now the default.                                                              |
| `manifest.defaultBranch`      | 26.04        | No longer needed    | Remove from config. HealthOmics does not use Git-based pipeline checkout and has<br>never supported this option. |
