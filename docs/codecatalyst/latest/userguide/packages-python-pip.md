Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring pip and installing Python packages

To use `pip` with CodeCatalyst, you must connect `pip` to your package repository and provide a personal access token for authentication. You can view
instructions for connecting `pip` to your package repository in the CodeCatalyst console. After you authenticate and connect `pip` to CodeCatalyst, you can run
`pip` commands.

###### Contents

- [Installing Python packages from CodeCatalyst with
  pip](packages-python-pip.md#pip-install "packages-python-pip.md#pip-install")
- [Consuming Python packages from PyPI through
  CodeCatalyst](packages-python-pip.md#pip-install-pypi "packages-python-pip.md#pip-install-pypi")
- [pip command support](packages-python-pip.md#pip-command-support "packages-python-pip.md#pip-command-support")
  - [Supported commands
    that interact with a repository](packages-python-pip.md#supported-pip-commands-that-interact-with-a-repository "packages-python-pip.md#supported-pip-commands-that-interact-with-a-repository")
  - [Supported client-side commands](packages-python-pip.md#supported-pip-client-side-commands "packages-python-pip.md#supported-pip-client-side-commands")

## Installing Python packages from CodeCatalyst with

pip

The following instructions explain how to configure `pip` to install Python packages
from your CodeCatalyst package repository or one of its upstream repositories.

###### To configure and use `pip` to install Python packages from your CodeCatalyst package repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. On the overview page for your project, choose **Packages**.
3. Choose your package repository from the list of package repositories.
4. Choose **Connect to repository**.
5. In the **Connect to repository** dialog box, choose
   **pip** from the list of package manager
   clients.
6. You will need a personal access token (PAT) to authenticate pip with CodeCatalyst. If you already have one, you can use that. If not, you can create one here.
   1. Choose **Create token**.
   2. Choose **Copy** to copy your PAT.

   ###### Warning

   You will not be able to see or copy your PAT again after you close the dialog box.

7. Use the `pip config` command to set the CodeCatalyst registry URL and credentials. Replace the following values.

###### Note

If copying from the console instructions, the following values should be updated for you and should not be changed.

    * Replace `username` with your CodeCatalyst user name.
    * Replace `PAT` with your CodeCatalyst PAT.
    * Replace `space_name` with your CodeCatalyst space name.
    * Replace `proj_name` with your CodeCatalyst project name.
    * Replace `repo_name` with your CodeCatalyst package repository name.

```
pip config set global.index-url https://`username`:`PAT`@https://packages.`region`.codecatalyst.aws/pypi/`space_name`/`proj_name`/`repo_name`/simple/
```

8. Assuming that a package is present in your repository or one of its upstream repositories, you can
   install it with `pip install`. For example, use the following command to install
   the `requests` package.

```
pip install requests
```

Use the `-i` option to revert temporarily to installing packages
from [https://pypi.org](https://pypi.org "https://pypi.org") instead of your
CodeCatalyst package repository.

```
pip install -i https://pypi.org/simple requests
```

## Consuming Python packages from PyPI through

CodeCatalyst

You can consume Python packages from the [Python Package Index (PyPI)](https://www.pypi.org/ "https://www.pypi.org/") through a CodeCatalyst repository by
configuring the repository with an upstream connection to **PyPI**.
Packages consumed from **PyPI** are ingested and stored
in your CodeCatalyst repository.

###### To consume packages from PyPI

1. If you haven't already, configure pip with your CodeCatalyst package repository by following the steps
   in [Installing Python packages from CodeCatalyst with
   pip](#pip-install "#pip-install").
2. Ensure that your repository has added **PyPI** as an upstream source. You can check which upstream
   sources are added or add **PyPI** as an
   upstream source by following the instructions in [Adding an upstream repository](packages-upstream-repositories-add.md "packages-upstream-repositories-add.md") and choosing the
   **PyPI store** repository.

For more information about requesting packages from upstream repositories, see
[Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").

## pip command support

The following sections summarize the pip commands that are supported,
by CodeCatalyst repositories, in addition to specific commands that are not supported.

###### Topics

- [Supported commands
  that interact with a repository](#supported-pip-commands-that-interact-with-a-repository "#supported-pip-commands-that-interact-with-a-repository")
- [Supported client-side commands](#supported-pip-client-side-commands "#supported-pip-client-side-commands")

### Supported commands

that interact with a repository

This section lists `pip` commands where the `pip` client makes one
or more requests to the registry it's been configured with. These commands have been verified
to function correctly when invoked against a CodeCatalyst package repository.

| Command                                                                                                                   | Description        |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [install](https://pip.pypa.io/en/stable/reference/pip_install/ "https://pip.pypa.io/en/stable/reference/pip_install/")    | Install packages.  |
| [download](https://pip.pypa.io/en/stable/reference/pip_download/ "https://pip.pypa.io/en/stable/reference/pip_download/") | Download packages. |

CodeCatalyst does not implement `pip search`. If you have configured `pip` with a
CodeCatalyst package repository, running `pip search` will search and show packages from
[PyPI](https://pypi.org/ "https://pypi.org/").

### Supported client-side commands

These commands don't require any direct interaction with a repository, so CodeCatalyst does not
need to do anything to support them.

| Command                                                                                                                                   | Description                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [uninstall](https://pip.pypa.io/en/stable/reference/pip_uninstall/ "https://pip.pypa.io/en/stable/reference/pip_uninstall/")              | Uninstall packages.                                             |
| [freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/ "https://pip.pypa.io/en/stable/reference/pip_freeze/")                       | Output installed packages in requirements format.               |
| [list](https://pip.pypa.io/en/stable/reference/pip_list/ "https://pip.pypa.io/en/stable/reference/pip_list/")                             | List installed packages.                                        |
| [show](https://pip.pypa.io/en/stable/reference/pip_show/ "https://pip.pypa.io/en/stable/reference/pip_show/")                             | Show information about installed packages.                      |
| [check](https://pip.pypa.io/en/stable/reference/pip_check/ "https://pip.pypa.io/en/stable/reference/pip_check/")                          | Verify that installed packages have compatible<br>dependencies. |
| [config](https://pip.pypa.io/en/stable/reference/pip_config/ "https://pip.pypa.io/en/stable/reference/pip_config/")                       | Manage local and global configuration.                          |
| [wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/ "https://pip.pypa.io/en/stable/reference/pip_wheel/")                          | Build wheels from your requirements.                            |
| [hash](https://pip.pypa.io/en/stable/reference/pip_hash/ "https://pip.pypa.io/en/stable/reference/pip_hash/")                             | Compute hashes of package archives.                             |
| [completion](https://pip.pypa.io/en/stable/user_guide/#command-completion "https://pip.pypa.io/en/stable/user_guide/#command-completion") | Helps with command completion.                                  |
| [debug](https://pip.pypa.io/en/stable/reference/pip_debug/ "https://pip.pypa.io/en/stable/reference/pip_debug/")                          | Show information useful for debugging.                          |
| help                                                                                                                                      | Show help for commands.                                         |
