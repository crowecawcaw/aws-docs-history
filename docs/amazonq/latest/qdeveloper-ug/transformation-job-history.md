# Viewing transformation job history

Amazon Q provides a comprehensive overview of your Java transformation job history, allowing you
to track and review your transformation jobs in both IDEs and the command line.

Transformation job history includes the following information about a job:

- **Date** – When the transformation job was executed
- **Project name** – The name of the project that was transformed
- **Status** – The current status of the transformation job
- **Duration** – How long the transformation took to complete
- **Job ID** – A unique identifier for the transformation job
- **Diff patch** – A link or path to the final diff patch file showing all code changes
- **Summary** – A link or path to the transformation summary file with details about the changes made

###### Note

Only transformations run since this feature was released will be available in the
job history. For the feature release date, see [Document history for Amazon Q Developer User Guide](doc-history.md "doc-history.md").

## Viewing job history in IDEs

###### Note

This feature is currently available in Visual Studio Code only.

The Transformation Hub in Visual Studio Code provides a comprehensive view of your Java transformation
job history.

A table in the Transformation Hub lists your 10 most recent transformation jobs from
the last 30 days. From the table, you can access transformation artifacts and refresh
jobs to track progress and get missing artifacts.

### Retrieve transformation artifacts

You can access transformation artifacts, such as the diff patches and summary
files, from the job history table. Choose the appropriate links to open the diff or summary in your IDE.

Artifacts are stored locally in the `.aws/transform` directory,
so you can also access previously downloaded transformation artifacts from past jobs.

### Refresh job status

You can refresh the job status from the job history table. Refresh a failed job to
get an updated status from the server side that may not have reached your server
yet, such as when Amazon Q is able to resume a failed job. You can also refresh
completed jobs to download artifacts that may not have appeared yet.

### How job history is stored for jobs run in the IDE

For Visual Studio Code, all transformation job information and artifacts are stored locally in the
`.aws/transform` directory. The storage is organized as follows:

```

.aws/transform/
├── [project-name-1]/
│   ├── [job-id-1]/
│   │   ├── diff.patch
│   │   ├── [summary-1]/
│   │   │   └── summary.md
│   │   │   └── buildCommandOutput.log
│   └── [job-id-2]/
│       ├── diff.patch
│       ├── [summary-2]/
│       │   └── summary.md
│       │   └── buildCommandOutput.log
└── [project-name-2]/
    └── [job-id-3]/
        ├── diff.patch
        ├── [summary-3]/
        │   └── summary.md
        │   └── buildCommandOutput.log

```

## Viewing job history on the command line

For transformations on the command line, the **qct history** command provides access to your
transformation job history with customization options.

For the CLI, transformation job history information is stored locally in the
`.aws/qcodetransform/history/` directory.

### Using the qct history command

The basic command to view your transformation job history is:

```
qct history
```

By default, this command displays the 10 most recent transformation jobs,
in addition to any paused or in-progress jobs.

You can also specify how many job history entries to display with the **--limit** flag. For example, to show 20 jobs, run:

```
qct history --limit 20
```
