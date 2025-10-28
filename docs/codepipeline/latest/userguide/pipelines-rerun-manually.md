# Start a pipeline manually

By default, a pipeline starts automatically when it is created and any time a change
is made in a source repository. However, you might want to rerun the most recent
revision through the pipeline a second time. You can use the CodePipeline console or the AWS CLI
and **start-pipeline-execution** command to manually rerun the most
recent revision through your pipeline.

###### Topics

- [Start a pipeline manually
  (console)](#pipelines-rerun-manually-console "#pipelines-rerun-manually-console")
- [Start a pipeline manually
  (CLI)](#pipelines-rerun-manually-cli "#pipelines-rerun-manually-cli")

## Start a pipeline manually

(console)

###### To manually start a pipeline and run the most recent revision through a

pipeline

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").
2. In **Name**, choose the name of the pipeline you want to
   start.
3. On the pipeline details page, choose
   **Release change**. If the pipeline is configured
   to pass parameters (pipeline variables), then choosing **Release
   change** opens the **Release change** window.
   In **Pipeline variables**, in the field or fields for the
   variables at the pipeline level, enter the value or values you want to pass
   for this pipeline execution. For more information, see [Variables reference](reference-variables.md "reference-variables.md").

This starts the most recent revision available in each source location
specified in a source action through the pipeline.

## Start a pipeline manually

(CLI)

###### To manually start a pipeline and run the most recent version of an artifact

through a pipeline

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
   to run the **start-pipeline-execution** command, specifying
   the name of the pipeline you want to start. For example, to start running
   the last change through a pipeline named
   `MyFirstPipeline`:

```
aws codepipeline start-pipeline-execution --name `MyFirstPipeline`
```

To start a pipeline where variables are configured at the pipeline level,
use the **start-pipeline-execution** command with the
optional **--variables** argument to start the pipeline and
add the variables that will be used in the execution. For example, to add a
variable `var1` with a value of `1`, use the following
command:

```
aws codepipeline start-pipeline-execution --name `MyFirstPipeline` --variables name=var1,value=1
```

2. To verify success, view the returned object. This command returns an
   execution ID, similar to the following:

```
{
    "pipelineExecutionId": `"c53dbd42-This-Is-An-Example"`
}

```

###### Note

After you have started the pipeline, you can monitor its progress in
the CodePipeline console or by running the
**get-pipeline-state** command. For more information,
see [View pipelines (console)](pipelines-view-console.md "pipelines-view-console.md") and [View pipeline details and history (CLI)](pipelines-view-cli.md "pipelines-view-cli.md").
