# Adding workspace context to Amazon Q Developer chat in the IDE

When you chat with Amazon Q in the integrated development environment (IDE), you can add
`@workspace` to your question to
automatically include the most relevant chunks of your workspace code as context. Amazon Q Developer
determines relevance based on an index that is updated periodically.

With workspace context, Amazon Q has enhanced capabilities, including locating files,
understanding how code is used across files, and generating code that leverages multiple
files, including files that aren’t opened.

###### Topics

- [Setup](#setup "#setup")
- [Ask questions with workspace context](#ask-questions-workspace-context "#ask-questions-workspace-context")

## Setup

Before you continue, make sure you have the latest version of your IDE installed. You
can then complete the following setup steps.

### Enable indexing

To use your workspace as context, Amazon Q creates a local index of your workspace
repository, including code files, configuration files, and project structure. During
indexing, non-essential files like binaries or those specified in
`.gitignore` files are filtered out.

It can take 5 to 20 minutes to index a new workspace. During this time, you can
expect elevated CPU usage in your IDE. After initial indexing, the index is
incrementally updated when you make changes to your workspace.

The first time you add workspace context, you must enable indexing in your IDE.
Complete the following steps to enable indexing:

1. Add `@workspace` to your question in the Amazon Q chat
   panel.
2. Amazon Q prompts you to enable indexing. Choose
   **Settings** to be redirected to Amazon Q settings in
   your IDE.

If you aren't prompted, you can go to settings by choosing
**Amazon Q** at the bottom of your IDE. Then, choose
**Open Settings** from the Amazon Q task bar that opens. 3. Select the box next to **Workspace
Index**.

### Configure indexing (optional)

No configuration is necessary for the indexing process, however you can choose to
specify the number of threads dedicated to indexing. If you increase the number of
threads used, indexing will complete faster, and it will use more of your CPU. To
update the indexing configuration, specify the number of threads for the
**Workspace Index Worker Threads** setting. You can also set
the maximum size of the files that can be indexed for workspace context, and enable
the use of your graphics processing unit (GPU) for indexing.

## Ask questions with workspace context

To add your workspace as context to your conversation with Amazon Q, open the workspace
you want to ask questions about, and then add `@workspace` to your
question in the chat panel. You must add @workspace to any question that you want to add
workspace context to.

If you want to start chatting about a different workspace, open the workspace, and
then open a new chat tab. Include `@workspace` in your question to
add the new workspace as context.

You can ask Amazon Q about any file in your workspace, including unopened files. Amazon Q
can explain files, locate code, and generate code across files, in addition to existing
conversational coding capabilities.

Following are example questions you can ask Amazon Q that leverage workspace context in
the chat:

- @workspace where is the code that handles authorization?
- @workspace what are the key classes with application logic in this
  project?
- @workspace explain main.py
- @workspace add auth to this project
- @workspace what third-party libraries or packages are used in this project,
  and for what purpose?
- @workspace add unit tests for function `<function
name>`
