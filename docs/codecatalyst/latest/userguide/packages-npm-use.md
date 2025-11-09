Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring and using npm

To use `npm` with CodeCatalyst, you must connect `npm` to your
package repository and provide a personal access token (PAT) for authentication. You can view
instructions for connecting `npm` to your package repository in the CodeCatalyst console.

###### Contents

- [Configuring npm with CodeCatalyst](packages-npm-use.md#npm-configure "packages-npm-use.md#npm-configure")
- [Installing npm packages from a CodeCatalyst package
  repository](packages-npm-use.md#npm-install "packages-npm-use.md#npm-install")
- [Installing npm packages from npmjs through
  CodeCatalyst](packages-npm-use.md#npm-install-npmjs "packages-npm-use.md#npm-install-npmjs")
- [Publishing npm packages to your CodeCatalyst package repository](packages-npm-use.md#npm-publish "packages-npm-use.md#npm-publish")
- [npm command support](packages-npm-use.md#npm-commands "packages-npm-use.md#npm-commands")
  - [Supported commands
    that interact with a package repository](packages-npm-use.md#supported-commands-that-interact-with-a-repository "packages-npm-use.md#supported-commands-that-interact-with-a-repository")
  - [Supported client-side commands](packages-npm-use.md#supported-client-side-commands "packages-npm-use.md#supported-client-side-commands")
  - [Unsupported commands](packages-npm-use.md#unsupported-commands "packages-npm-use.md#unsupported-commands")

## Configuring npm with CodeCatalyst

The following instructions explain how to authenticate and connect `npm`
to your CodeCatalyst package repository. For more information about npm, see the
[official npm documentation](https://docs.npmjs.com/ "https://docs.npmjs.com/").

###### To connect `npm` to your CodeCatalyst package repository

1.  Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2.  Navigate to your project.
3.  In the navigation pane, choose **Packages**.
4.  Choose your package repository from the list.
5.  Choose **Connect to repository**.
6.  In **Configuration details**, in **Package manager client**, choose **npm client**.
7.  Choose your operating system to view the corresponding configuration steps.
8.  A personal access token (PAT) is required to authenticate npm with CodeCatalyst. If
    you already have a token, you can use it. If not, you can create one using the
    following steps.
    1. **(Optional):** Update the
       **PAT name** and **Expiration date**.
    2. Choose **Create token**.
    3. Copy and store your PAT in a safe location.

    ###### Warning

    You will not be able to see or copy your PAT again after you close the dialog box.
    Credentials should be short lived to minimize the length of time an attacker can use the credentials after misappropriating them.

9.  Run the following commands from your project's root directory to configure npm with your package repository. The commands will do the following:

        * Create a project-level `.npmrc` file if your project does not have one.
        * Add the package repository endpoint information to your project-level
         `.npmrc` file.
        * Add your credentials (PAT) to your user-level `.npmrc` file.

    Replace the following values.

###### Note

If you are copying from the console instructions, the values in the following commands are updated for
you and do not need to be changed.

    * Replace `username` with your CodeCatalyst user name.
    * Replace `PAT` with your CodeCatalyst PAT.
    * Replace `space_name` with your CodeCatalyst space name.
    * Replace `proj_name` with your CodeCatalyst project name.
    * Replace `repo_name` with your CodeCatalyst package repository name.

```
npm set registry=https://packages.`region`.codecatalyst.aws/npm/`space-name`/`proj-name`/`repo-name`/ --location project
npm set //packages.`region`.codecatalyst.aws/npm/`space-name`/`proj-name`/`repo-name`/:_authToken=`username`:`PAT`
```

**For npm 6 or lower:** To make npm always pass the auth token to CodeCatalyst, even for `GET` requests, set the always-auth configuration variable with `npm config set` as follows.

```
npm set //packages.`region`.codecatalyst.aws/npm/`space-name`/`proj-name`/`repo-name`/:always-auth=true --location project
```

## Installing npm packages from a CodeCatalyst package

repository

After you connect npm to your repository by following the steps in [Configuring npm with CodeCatalyst](#npm-configure "#npm-configure"), you can run `npm` commands on your repository.

You can install an npm package that is in your CodeCatalyst package repository or one of
its upstream repositories with the `npm install` command.

```
npm install `lodash`
```

## Installing npm packages from npmjs through

CodeCatalyst

You can install npm packages from [npmjs.com](https://www.npmjs.com/ "https://www.npmjs.com/") through a CodeCatalyst repository by
configuring the repository with an upstream connection to the gateway repository connected to npmjs.com, **npm-public-registry-gateway**.
Packages installed from npmjs are ingested and stored
in the gateway repository, and the farthest downstream package repository.

###### To install packages from npmjs

1. If you haven't already done so, configure `npm` with your CodeCatalyst
   package repository by following the steps in [Configuring npm with CodeCatalyst](#npm-configure "#npm-configure").
2. Check that your repository has added the gateway repository, **npm-public-registry-gateway**, as
   an upstream connection. You can check which upstream sources are added or add
   **npm-public-registry-gateway** as an upstream source by following the
   instructions in [Adding an upstream repository](packages-upstream-repositories-add.md "packages-upstream-repositories-add.md") and choosing the
   **npm-public-registry-gateway** repository.
3. Install packages with the `npm install` command.

```
npm install `package_name`
```

For more information about requesting packages from upstream repositories, see
[Requesting a package version with upstream repositories](packages-upstream-repositories-request.md "packages-upstream-repositories-request.md").

## Publishing npm packages to your CodeCatalyst package repository

After you have completed [Configuring npm with CodeCatalyst](#npm-configure "#npm-configure"), you can run `npm` commands.

You can publish an npm package to a CodeCatalyst package repository with the `npm publish` command.

```
npm publish
```

For information about how to create npm packages, see [Creating Node.js
Modules](https://docs.npmjs.com/getting-started/creating-node-modules "https://docs.npmjs.com/getting-started/creating-node-modules") on _npm Docs_.

## npm command support

The following sections summarize the `npm` commands that are supported by CodeCatalyst
package repositories, in addition to listing specific commands that are not
supported.

###### Topics

- [Supported commands
  that interact with a package repository](#supported-commands-that-interact-with-a-repository "#supported-commands-that-interact-with-a-repository")
- [Supported client-side commands](#supported-client-side-commands "#supported-client-side-commands")
- [Unsupported commands](#unsupported-commands "#unsupported-commands")

### Supported commands

that interact with a package repository

This section lists `npm` commands where the `npm` client makes one
or more requests to the registry to which it is configured (for example, `npm
 config set registry`). These commands have been verified to function
correctly when invoked against a CodeCatalyst package repository.

| Command                                                                                                    | Description                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bugs](https://docs.npmjs.com/cli/bugs "https://docs.npmjs.com/cli/bugs")                                  | Guesses the location of a package’s bug tracker URL, and then it attempts<br>to open it.                                                            |
| [ci](https://docs.npmjs.com/cli/ci "https://docs.npmjs.com/cli/ci")                                        | Installs a project with a clean slate.                                                                                                              |
| [deprecate](https://docs.npmjs.com/cli/deprecate "https://docs.npmjs.com/cli/deprecate")                   | Deprecates a version of a package.                                                                                                                  |
| [dist-tag](https://docs.npmjs.com/cli/dist-tag "https://docs.npmjs.com/cli/dist-tag")                      | Modifies package distribution tags.                                                                                                                 |
| [docs](https://docs.npmjs.com/cli/docs "https://docs.npmjs.com/cli/docs")                                  | Guesses the location of a package’s documentation URL, and then it<br>attempts to open it by using the `--browser` config<br>parameter.             |
| [doctor](https://docs.npmjs.com/cli/doctor "https://docs.npmjs.com/cli/doctor")                            | Runs a set of checks to validate that your npm installation can manage<br>your JavaScript packages.                                                 |
| [install](https://docs.npmjs.com/cli/install "https://docs.npmjs.com/cli/install")                         | Installs a package.                                                                                                                                 |
| [install-ci-test](https://docs.npmjs.com/cli/install-ci-test "https://docs.npmjs.com/cli/install-ci-test") | Installs a project with a clean slate and runs tests. Alias: `npm<br>cit`. This command runs an `npm ci`, followed<br>immediately by an `npm test`. |
| [install-test](https://docs.npmjs.com/cli/install-test "https://docs.npmjs.com/cli/install-test")          | Installs package and runs tests. Runs an `npm install`,<br>followed immediately by an `npm test`.                                                   |
| [outdated](https://docs.npmjs.com/cli/outdated "https://docs.npmjs.com/cli/outdated")                      | Checks the configured registry to determine if any installed packages are<br>outdated.                                                              |
| [ping](https://docs.npmjs.com/cli/ping "https://docs.npmjs.com/cli/ping")                                  | Pings the configured or given npm registry and verifies<br>authentication.                                                                          |
| [publish](https://docs.npmjs.com/cli/publish "https://docs.npmjs.com/cli/publish")                         | Publishes a package version to the registry.                                                                                                        |
| [update](https://docs.npmjs.com/cli/update "https://docs.npmjs.com/cli/update")                            | Guesses the location of a package’s repository URL, and then it attempts<br>to open it by using the `--browser` config<br>parameter.                |
| [view](https://docs.npmjs.com/cli/view "https://docs.npmjs.com/cli/view")                                  | Displays package metadata. Can also be used to print metadata<br>properties.                                                                        |

### Supported client-side commands

These commands don't require any direct interaction with a package repository, so CodeCatalyst
does not require anything to support them.

| Command                                                                                                         | Description                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [bin (legacy)](https://docs.npmjs.com/cli/v8/commands/npm-bin "https://docs.npmjs.com/cli/v8/commands/npm-bin") | Displays the npm `bin` directory.                                                                                                                                                                        |
| [build](https://docs.npmjs.com/cli/v6/commands/npm-build "https://docs.npmjs.com/cli/v6/commands/npm-build")    | Builds a package.                                                                                                                                                                                        |
| [cache](https://docs.npmjs.com/cli/cache "https://docs.npmjs.com/cli/cache")                                    | Manipulates the packages cache.                                                                                                                                                                          |
| [completion](https://docs.npmjs.com/cli/completion "https://docs.npmjs.com/cli/completion")                     | Enables tab completion in all npm commands.                                                                                                                                                              |
| [config](https://docs.npmjs.com/cli/config "https://docs.npmjs.com/cli/config")                                 | Updates the contents of the user and global `npmrc`<br>files.                                                                                                                                            |
| [dedupe](https://docs.npmjs.com/cli/dedupe "https://docs.npmjs.com/cli/dedupe")                                 | Searches the local package tree and attempts to simplify the structure by<br>moving dependencies further up the tree where they can be more<br>effectively shared by multiple dependent packages.        |
| [edit](https://docs.npmjs.com/cli/edit "https://docs.npmjs.com/cli/edit")                                       | Edits an installed package. Selects a dependency in the current working<br>directory and opens the package directory in the default<br>editor.                                                           |
| [explore](https://docs.npmjs.com/cli/explore "https://docs.npmjs.com/cli/explore")                              | Browses an installed package. Spawns a subshell in the directory of the<br>specified installed package. If a command is specified, then it is run<br>in the subshell, which then immediately shuts down. |
| [help](https://docs.npmjs.com/cli/help "https://docs.npmjs.com/cli/help")                                       | Gets help on npm.                                                                                                                                                                                        |
| [help-search](https://docs.npmjs.com/cli/help-search "https://docs.npmjs.com/cli/help-search")                  | Searches npm help documentation.                                                                                                                                                                         |
| [init](https://docs.npmjs.com/cli/init "https://docs.npmjs.com/cli/init")                                       | Creates a `package.json` file.                                                                                                                                                                           |
| [link](https://docs.npmjs.com/cli/link "https://docs.npmjs.com/cli/link")                                       | Symlinks a package directory.                                                                                                                                                                            |
| [ls](https://docs.npmjs.com/cli/ls "https://docs.npmjs.com/cli/ls")                                             | Lists installed packages.                                                                                                                                                                                |
| [pack](https://docs.npmjs.com/cli/pack "https://docs.npmjs.com/cli/pack")                                       | Creates a tarball from a package.                                                                                                                                                                        |
| [prefix](https://docs.npmjs.com/cli/prefix "https://docs.npmjs.com/cli/prefix")                                 | Displays a prefix. This is the closest parent directory to contain a<br>`package.json` file, unless `-g` is<br>also specified.                                                                           |
| [prune](https://docs.npmjs.com/cli/prune "https://docs.npmjs.com/cli/prune")                                    | Removes packages that are not listed on the parent package's dependencies<br>list.                                                                                                                       |
| [rebuild](https://docs.npmjs.com/cli/rebuild "https://docs.npmjs.com/cli/rebuild")                              | Runs the `npm build` command on the matched folders.                                                                                                                                                     |
| [restart](https://docs.npmjs.com/cli/restart "https://docs.npmjs.com/cli/restart")                              | Runs a package's stop, restart, and start scripts and associated<br>pre-scripts and post-scripts.                                                                                                        |
| [root](https://docs.npmjs.com/cli/root "https://docs.npmjs.com/cli/root")                                       | Prints the effective `node_modules` directory to<br>standard out.                                                                                                                                        |
| [run-script](https://docs.npmjs.com/cli/run-script "https://docs.npmjs.com/cli/run-script")                     | Runs arbitrary package scripts.                                                                                                                                                                          |
| [shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap "https://docs.npmjs.com/cli/shrinkwrap")                     | Locks down dependency versions for publication.                                                                                                                                                          |
| [uninstall](https://docs.npmjs.com/cli/uninstall "https://docs.npmjs.com/cli/uninstall")                        | Uninstalls a package.                                                                                                                                                                                    |

### Unsupported commands

These `npm` commands are not supported by CodeCatalyst package repositories.

| Command                                                                                                      | Description                                                              | Notes                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [access](https://docs.npmjs.com/cli/access "https://docs.npmjs.com/cli/access")                              | Sets the access level on published packages.                             | CodeCatalyst uses a permission model that is different from the public npmjs<br>repository.                                                                                                                                                                                           |
| [adduser](https://docs.npmjs.com/cli/adduser "https://docs.npmjs.com/cli/adduser")                           | Adds a registry user account                                             | CodeCatalyst uses a user model that is different from the public npmjs<br>repository.                                                                                                                                                                                                 |
| [audit](https://docs.npmjs.com/cli/audit "https://docs.npmjs.com/cli/audit")                                 | Runs a security audit.                                                   | CodeCatalyst does not currently vend security vulnerability data.                                                                                                                                                                                                                     |
| [hook](https://docs.npmjs.com/cli/v9/commands/npm-hook "https://docs.npmjs.com/cli/v9/commands/npm-hook")    | Manages npm hooks, including adding, removing, listing, and<br>updating. | CodeCatalyst does not currently support any change notification<br>mechanism.                                                                                                                                                                                                         |
| [login](https://docs.npmjs.com/cli-commands/adduser.html "https://docs.npmjs.com/cli-commands/adduser.html") | Authenticates a user. This is an alias for `npm adduser`.                | CodeCatalyst uses an authentication model that is different from the public<br>npmjs repository. For information, see<br>[Configuring npm with CodeCatalyst](#npm-configure "#npm-configure").                                                                                        |
| [logout](https://docs.npmjs.com/cli/logout "https://docs.npmjs.com/cli/logout")                              | Signs out of the registry.                                               | CodeCatalyst uses an authentication model that is different from the public<br>npmjs repository. There is no way to sign out from a CodeCatalyst repository, but<br>authentication tokens expire after their configurable expiration time. The<br>default token duration is 12 hours. |
| [owner](https://docs.npmjs.com/cli/owner "https://docs.npmjs.com/cli/owner")                                 | Manages package owners.                                                  | CodeCatalyst uses a permissions model that is different from the public npmjs<br>repository.                                                                                                                                                                                          |
| [profile](https://docs.npmjs.com/cli/profile "https://docs.npmjs.com/cli/profile")                           | Changes settings on your registry profile.                               | CodeCatalyst uses a user model that is different from the public npmjs<br>repository.                                                                                                                                                                                                 |
| [search](https://docs.npmjs.com/cli/search "https://docs.npmjs.com/cli/search")                              | Searches the registry for packages matching the search terms.            | CodeCatalyst does not support the `search` command.                                                                                                                                                                                                                                   |
| [star](https://docs.npmjs.com/cli/star "https://docs.npmjs.com/cli/star")                                    | Marks your favorite packages.                                            | CodeCatalyst currently does not support any favorites mechanism.                                                                                                                                                                                                                      |
| [stars](https://docs.npmjs.com/cli/stars "https://docs.npmjs.com/cli/stars")                                 | Views packages marked as favorites.                                      | CodeCatalyst currently does not support any favorites mechanism.                                                                                                                                                                                                                      |
| [team](https://docs.npmjs.com/cli/team "https://docs.npmjs.com/cli/team")                                    | Manages teams and team memberships.                                      | CodeCatalyst uses a user and group membership model that is different from the<br>public npmjs repository.                                                                                                                                                                            |
| [token](https://docs.npmjs.com/cli/token "https://docs.npmjs.com/cli/token")                                 | Manages your authentication tokens.                                      | CodeCatalyst uses a different model for getting authentication tokens. For<br>information, see [Configuring npm with CodeCatalyst](#npm-configure "#npm-configure").                                                                                                                  |
| [unpublish](https://docs.npmjs.com/cli/unpublish "https://docs.npmjs.com/cli/unpublish")                     | Removes a package from the registry.                                     | CodeCatalyst does not support removing a package version from a repository by<br>using the npm client. You can delete a package in the console.                                                                                                                                       |
| [whoami](https://docs.npmjs.com/cli/whoami "https://docs.npmjs.com/cli/whoami")                              | Displays the npm user name.                                              | CodeCatalyst uses a user model that is different from the public npmjs<br>repository.                                                                                                                                                                                                 |
