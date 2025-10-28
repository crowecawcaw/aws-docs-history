# Delete a repository link

You can use the **delete-repository-link** command in the AWS Command Line Interface (AWS CLI)
to delete a repository link.

Before you can delete a repository link, you must delete all sync configurations
associated with the repository link.

###### Important

After you run the command, the repository link is deleted. No confirmation dialog box
is displayed. You can create a new repository link, but the Amazon Resource Name (ARN)
is not reused.

###### To delete a repository link

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the
  **delete-repository-link** command, specifying the ID of the
  repository link to delete.

```
aws codeconnections delete-repository-link --repository-link-id 6053346f-8a33-4edb-9397-10394b695173
```

This command returns nothing.
