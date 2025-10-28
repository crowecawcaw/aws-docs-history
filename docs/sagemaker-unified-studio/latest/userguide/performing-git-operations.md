# Performing Git operations

The JupyterLab IDE in Amazon SageMaker Unified Studio is configured with Git and initialized with the project
repository when a project is created.

To access Git operations in the Amazon SageMaker Unified Studio management console, navigate to the Code page of
your project, then choose the Git button in the JupyterLab IDE left panel as shown in the
image below.

This opens a panel where you can view commit history and perform Git operations. You can
use this Git extension to commit and push files back to the project repository, switch your
working branch or create a new one, and manage tags.

To fetch notebooks committed by other users, do a pull from the project repository.

###### Note

When you create and enable a connection for Git access and the user accesses this
connection in the JupyterLab IDE in Amazon SageMaker Unified Studio, the repository is cloned. In other words, a
local copy of the repository is created in the Amazon SageMaker Unified Studio project. If the administrator later
disables or deletes this Git connection, the local repository remains in the user's IDE, but
users can no longer push or pull files to or from it. For more information, see [Git connections in Amazon SageMaker Unified Studio](../adminguide/git-connections.md "../adminguide/git-connections.md").
