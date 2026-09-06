# Final summary

When transformation completes, the _Final summary_ phase shows a summary of transformation. Artifacts are available for download and you can transform further, hand off transformed repositories to developers, or complete the job.

## Transformation artifacts

The following artifacts are available for download from the **Artifacts** tab:

- A zip file of the original and transformed source code.
- An HTML [transformation report](dotnet-report.md "dotnet-report.md") that documents what was changed and why.
- A [Next Steps markdown file](dotnet-next-steps.md "dotnet-next-steps.md") for hand-off to an AI code companion.

## End of transformation actions

At the end of transformation, you can:

- **Beam to IDE:** hand off the transformed repositories to developers to review and finalize.
- **Ask questions:** ask the agent about changes it made.
- **Transform more repos:** ask the agent for additional changes and start a new batch.
- **Complete job:** mark the job as complete and close this session.

## Beam a transformed repository to a developer

You can hand off transformed repositories to developers with a feature called **beaming**. This allows developers to locally build and review transformed applications.

### Beaming a repository from the web application

The agent transforms your repositories in batches. When a batch completes, the agent will prompt whether you want to beam repositories to IDE.

1. In chat, choose **Beam to IDE**.
2. Open the link to the selection panel.
3. Select the repositories to beam and choose the **Beam to IDE** button.

### Accessing a beamed repository from IDE

Developers follow these steps to retrieve a beamed repository:

1. In Visual Studio IDE, sign in to AWS Transform on the AWS Toolkit Getting Started page.
2. On the AWS Transform Dashboard, select the same workspace where the repository was beamed from.
3. Navigate to the dashboard's Beamed Repositories tab, which lists the beamed repositories.
4. Select a beamed repository and choose **Load**.
5. In the folder selection dialog that appears, select a file location for the repository files.
6. The repository solution opens in Visual Studio along with an in-progress AWS Transform job.

After a beamed repository is retrieved, it is no longer visible to other developers.
