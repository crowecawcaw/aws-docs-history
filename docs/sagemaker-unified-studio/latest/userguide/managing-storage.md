# Managing storage resources

## Storage organization

Creating logical subfolders helps organize your work, grouping related files together for easier navigation.
Establishing and following consistent naming conventions for files and folders helps team members understand
the purpose and content of resources.

Regularly moving completed work from local to shared storage ensures team access to important files. Removing
unnecessary files periodically helps conserve storage space and maintain a clean, efficient working environment.

## Working with files across multiple tools

Within Amazon SageMaker Unified Studio, a single file may be accessible via multiple tools. If you have the same file open simultaneously
in different tools, changes made in one tool may overwrite changes made in another if not properly saved. You'll need
to explicitly reopen files to see changes made through different tools.

When executing files from local storage, any resulting output files or artifacts automatically default to the same
local storage location. For example, running a notebook that generates additional files will store these in local
storage unless otherwise specified.

## Transitioning between storage types

Currently, you cannot convert a project from S3 storage to Git-based storage or vice versa. If you need to
change storage types, you must create a new project with the desired storage configuration, copy your files to the
new project, and update any references or dependencies.

This limitation is important to consider when initially setting up your project, as the storage decision has long-term
implications for your workflow.
