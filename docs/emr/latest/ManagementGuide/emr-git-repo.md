# Associating Git-based repositories with

EMR Notebooks

You can associate Git-based repositories with your Amazon EMR notebooks to save your
notebooks in a version controlled environment. You can associate up to three
repositories with a notebook. The following Git-based services are supported:

- [AWS CodeCommit](https://aws.amazon.com/codecommit "https://aws.amazon.com/codecommit")
- [GitHub](https://www.github.com "https://www.github.com")
- [Bitbucket](https://bitbucket.org/ "https://bitbucket.org/")
- [GitLab](https://about.gitlab.com/ "https://about.gitlab.com/")

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

Associating Git-based repositories with your notebook has the following
benefits.

- **Version control** – You can record code
  changes in a version-control system so that you can review the history of your
  changes and selectively reverse them.
- **Collaboration** – Colleagues working in
  diﬀerent notebooks can share code through remote Git-based repositories.
  Notebooks can clone or merge code from remote repositories and push changes back
  to those remote repositories.
- **Code reuse** – Many Jupyter notebooks
  that demonstrate data analysis or machine learning techniques are available in
  publicly hosted repositories, such as GitHub. You can associate your notebooks
  with a repository to reuse the Jupyter notebooks contained in a
  repository.
  To use Git-based repositories with EMR Notebooks, you add the repositories as resources
  in the Amazon EMR console, associate credentials for repositories that require
  authentication, and link them with your notebooks. You can view a list of repositories
  that are stored in your account and details about each repository in the Amazon EMR console.
  You can associate an existing Git-based repository with a notebook when you create it.

###### Topics

- [Prerequisites and
  considerations when integrating an EMR notebook with a repository](emr-managed-notebooks-git-considerations.md "emr-managed-notebooks-git-considerations.md")
- [Add a Git-based repository to Amazon EMR](emr-git-repo-add.md "emr-git-repo-add.md")
- [Update or delete a Git-based
  repository from an EMR Studio Workspace](emr-git-repo-delete.md "emr-git-repo-delete.md")
- [Link or unlink a Git-based repository in EMR Studio](emr-git-repo-link.md "emr-git-repo-link.md")
- [Create a new Notebook with an
  associated Git repository in EMR Studio](emr-git-repo-create-notebook.md "emr-git-repo-create-notebook.md")
- [Use Git repositories in an EMR Studio Notebook](emr-git-repo-open.md "emr-git-repo-open.md")
