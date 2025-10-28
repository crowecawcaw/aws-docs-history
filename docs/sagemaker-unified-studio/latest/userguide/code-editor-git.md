# Performing Git operations in Code Editor

The Code Editor IDE in Amazon SageMaker Unified Studio is configured with Git and initialized
with the project repository when a Code Editor space is created.

You can use Git operations after launching your Code Editor space.
To launch your project, choose **Open** next to the space you
want to open in the **Spaces** tab of your project.

When Code Editor is open, choose the **Source Control** icon
in the left navigation. You can use this window to perform Git operations such as
committing and pushing files back to the project repository,
switching your working branch or creating a new one,
and managing tags.

To fetch notebooks committed by other users, do a pull from the project repository.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to your project.
3. In the **Build** menu, choose **Spaces**.
4. Choose **Open** next to the Code Editor space you want to open.
5. In the Source Control window of your Code Editor space, choose the three-dot menu.
   Then choose **Pull**.

###### Note

When you create and enable a connection for Git access and the user accesses this
connection in the Code Editor IDE in Amazon SageMaker Unified Studio, the repository is
cloned. In other words, a local copy of the repository is created in the Amazon SageMaker Unified Studio project.
If the administrator later disables or deletes this Git connection,
the local repository remains in the user's IDE, but users can no longer push or pull files
to or from it. For more information, see [Git connections in Amazon SageMaker Unified Studio](../adminguide/git-connections.md "../adminguide/git-connections.md").
