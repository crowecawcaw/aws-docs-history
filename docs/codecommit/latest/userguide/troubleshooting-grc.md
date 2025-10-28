AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Troubleshooting git-remote-codecommit and AWS CodeCommit

The following information might help you troubleshoot issues with **git-remote-codecommit** when connecting with
AWS CodeCommit repositories.

###### Topics

- [I see an error: git: 'remote-codecommit' is not a git command](#troubleshooting-grc-syn1 "#troubleshooting-grc-syn1")
- [I see an error: fatal: Unable to find remote helper for 'codecommit'](#troubleshooting-grc-syn2 "#troubleshooting-grc-syn2")
- [Cloning error: I cannot clone a CodeCommit repository from an IDE](#troubleshooting-grc-ide1 "#troubleshooting-grc-ide1")
- [Push or pull error: I cannot push or pull commits from an IDE to a CodeCommit
  repository](#troubleshooting-grc-ide2 "#troubleshooting-grc-ide2")
- [Installation error: I see an externally-managed-environment error when I
  try to install git-remote-codecommit](#troubleshooting-grc-pm1 "#troubleshooting-grc-pm1")

## I see an error: git: 'remote-codecommit' is not a git command

**Problem:** When you try to use git-remote-codecommit, you see an error that git-remote-codecommit is not a git command. See 'git --help'".

**Possible fixes:** The most common reason for this error
is that either you
have not added the git-remote-codecommit executable to your PATH, or that the string
contains
a syntax error. This can happen where a hyphen is missing between git and
remote-codecommit, or when an extra git is placed before git-remote-codecommit.

You might also encounter this error if you have updated your local installation to an unsupported version. For more information about supported versions of Python, see [git-remote-codecommit](https://pypi.org/project/git-remote-codecommit/ "https://pypi.org/project/git-remote-codecommit/").

For more information about setting up and using git-remote-codecommit, see [Setup steps for HTTPS connections to AWS CodeCommit with
git-remote-codecommit](setting-up-git-remote-codecommit.md "setting-up-git-remote-codecommit.md").

## I see an error: fatal: Unable to find remote helper for 'codecommit'

**Problem:** When you try to use git-remote-codecommit, you see an error stating "fatal: Unable to find remote helper for 'codecommit'".

**Possible fixes:** The most common reasons for this error
are:

- The setup is not complete for git-remote-codecommit
- You have installed git-remote-codecommit in a location that is not in your path or not configured as part of the `Path` environment variable
- Python is not in your path or not configured as part of the `Path` environment variable
- You are using a terminal or command line window that has not been restarted
  since the installation of git-remote-codecommit completed

For more information about setting up and using git-remote-codecommit, see [Setup steps for HTTPS connections to AWS CodeCommit with
git-remote-codecommit](setting-up-git-remote-codecommit.md "setting-up-git-remote-codecommit.md").

## Cloning error: I cannot clone a CodeCommit repository from an IDE

**Problem:** When you try to clone a CodeCommit repository in
an IDE, you see an error that says the endpoint or URL is not valid.

**Possible fixes:** Not all IDEs support the URL used by
**git-remote-codecommit** during cloning. Clone the repository
locally from the terminal or command line, and then add that local repo to your IDE. For
more information, see [Step 3: Connect to the CodeCommit console and clone
the repository](setting-up-git-remote-codecommit.md#setting-up-git-remote-codecommit-connect-console "setting-up-git-remote-codecommit.md#setting-up-git-remote-codecommit-connect-console").

## Push or pull error: I cannot push or pull commits from an IDE to a CodeCommit

repository

**Problem:** When you try to pull or push code from an IDE, you see a connection error.

**Possible fixes:** The most common reason for this error
is that the IDE is not compatible with Git remote helpers such as **git-remote-codecommit**. Instead of using the IDE
functionality to commit, push, and pull code, update the local repo manually from the command line or terminal using Git commands.

For more information about remote helpers and Git, see the
[Git documentation](https://git-scm.com/docs/gitremote-helpers "https://git-scm.com/docs/gitremote-helpers").

## Installation error: I see an externally-managed-environment error when I

try to install git-remote-codecommit

**Problem:** When you try to run the `pip install git-remote-codecommit` command, you see an error indicating that the
environment is externally managed.

**Possible fixes:** The most common reason for this error
is that you're running a distrobution (distro) of Python that define an EXTERNALLY-MANAGED marker file. The best solution for this is to create and use a virtual
environment.

For more information about externally managed environments and Python, see [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/#externally-managed-environments "https://packaging.python.org/en/latest/specifications/externally-managed-environments/#externally-managed-environments")
and [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ "https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/") in the Python documentation.
