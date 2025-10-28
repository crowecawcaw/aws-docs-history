# Troubleshooting

The following information can help you troubleshoot common issues in the Amazon CodeCatalyst
ADK.

###### Topics

- [Handling errors](#handling-errors "#handling-errors")
- [Running action workflows for third-party repositories](#3p-repository-actions "#3p-repository-actions")

## Handling errors

**Problem:** I see "Internal Error" when running my test
workflow but I'm not sure what the issue is.

**Possible fixes:** Your action definition YAML file may have
an error. Run the following command to catch errors in the
`action.yml` file: `adk validate`.

## Running action workflows for third-party repositories

**Problem:** My workflow run fails with a custom action's source code that is
in a third-party repository (GitHub).

**Possible fixes:** Your custom action's source code can only be in a Amazon CodeCatalyst
source repository. You can create a new repository in CodeCatalyst, move your source code to that repository, and run
your workflow again with the action. For more information, see [Step 1: Set up your project and Dev Environment](getting-started.md#set-up-workspace-first-action "getting-started.md#set-up-workspace-first-action").
