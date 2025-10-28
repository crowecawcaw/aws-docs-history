Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Referencing source repository

files

If you have files that reside in a source repository, and you need to refer to these
files in one of your workflow actions, complete the following procedure.

###### Note

See also [Referencing files in an
artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md").

###### To reference a file stored in a source repository

- In the action where you want to reference a file, add code similar to the
  following:

```
Actions:
  My-action:
    Inputs:
      Sources:
        - WorkflowSource
      Configuration:
        Steps:
        - run: cd my-app && cat file1.jar
```

In the previous code, the action looks in the `my-app`
directory in the root of the `WorkflowSource` source repository to
find and display the `file1.jar` file.
