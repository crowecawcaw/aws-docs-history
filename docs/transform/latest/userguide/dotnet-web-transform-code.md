# Transform your .NET code

In the _Transform_ phase, the agent transforms your repositories.

## Monitoring progress

You can view job progress in several ways:

- **Dashboard:** choose the Dashboard panel on the left side of the Job Plan window to see a dashboard showing repository status.
- **Chat:** the agent will let you know when repository transformations start and complete.
- **Transform panel:** Expand the Transform panel at left to view steps and progress for each repository.
- **Worklog tab:** The Worklog tab shows current agent activity in natural language.

## Checkpoint reviews

In interactive mode, you can set checkpoints for some or all repositories. Checkpoints allow you to work alongside the agent, pausing for human review after a repository is transformed. You can review transformed code, discuss it with the agent, and ask for further changes.

Checkpoints are set on the Dashboard panel. Each repository has a checkpoint toggle. After configuring checkpoints, choose **Save checkpoints**.

The agent will pause for review of each repository that has a checkpoint set. While paused at a checkpoint, you can:

- Download the transformed code and review it in your IDE.
- Ask the agent to explain changes it made.
- Ask the agent to make further changes. You can ask for minor refinements, or a full retry of the transformation with revised instructions.

You can iterate at a checkpoint until satisfied.

Whether or not you use checkpoints, you also have an opportunity to review results and ask for changes when transformation completes.

## Access transformed repositories

Repositories are transformed in parallel, grouped in a batch. You can access transformed repositories in several ways:

- **Source control:** After the agent transforms a repository, the modernized code is written to a new writable branch. If you uploaded a code zip file from an Amazon S3 bucket, a zip file of the transformed code is added to the bucket.
- **Download:** After the agent transforms a repository, the modernized code and artifacts are available for download from the dashboard or the **Artifacts** tab.
- **Beaming:** After the agent completes the transformation batch, you can [beam transformed repositories to developers](dotnet-web-final-summary.md#beam-transformed-repository "dotnet-web-final-summary.md#beam-transformed-repository") in the _Final summary_ phase.
