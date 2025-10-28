# Package group origin controls

Package origin controls are used to configure how package versions can enter a domain.
You can set up origin controls on a package group to configure how versions of every package associated with the package group can
enter specified repositories in the domain.

Package group origin control settings consist of the following:

- [Restriction settings](#package-group-origin-control-settings-restrictions "#package-group-origin-control-settings-restrictions"): These settings define if packages can enter a repository in CodeArtifact from publishing, internal upstreams,
  or external, public repositories.
- [Allowed repository lists](#package-group-origin-control-settings-repositories "#package-group-origin-control-settings-repositories"): Each restriction setting can be set to allow specific repositories. If a restriction setting is set to allow specific repositories,
  that restriction will have a corresponding allowed repository list.

###### Note

Origin control settings
for package groups are slightly different than the origin control settings for individual packages. For more information about
origin control settings for packages, see [Package origin control settings](package-origin-controls.md#package-origin-control-settings "package-origin-controls.md#package-origin-control-settings").

## Restriction settings

The restriction settings of a package group's origin control settings determine how the packages associated with that group can enter
repositories in the domain.

### PUBLISH

The `PUBLISH` setting configures whether package versions can be published directly to any repository
in the domain using package managers or similar tools.

- **ALLOW**: Package versions can be published directly to all repositories.
- **BLOCK**: Package versions cannot be published directly to any repository.
- **ALLOW_SPECIFIC_REPOSITORIES**: Package versions can only be published directly to repositories specified in the
  allowed repository list for publishing.
- **INHERIT**: The `PUBLISH` setting is inherited from the first parent package group with a setting that is not `INHERIT`.

### EXTERNAL_UPSTREAM

The `EXTERNAL_UPSTREAM` setting configures whether package versions can be ingested from external, public repositories when
requested by a package manager. For a list of supported external repositories, see
[Supported external connection
repositories](external-connection.md#supported-public-repositories "external-connection.md#supported-public-repositories").

- **ALLOW**: Any package version can be ingested into all repositories from a public source with an external connection.
- **BLOCK**: Package versions cannot be ingested into any repository from a public source with an external connection.
- **ALLOW_SPECIFIC_REPOSITORIES**: Package versions can only be ingested from a public source into repositories specified in the
  allowed repository list for external upstreams.
- **INHERIT**: The `EXTERNAL_UPSTREAM` setting is inherited from the first parent package group with a setting that is not `INHERIT`.

### INTERNAL_UPSTREAM

The `INTERNAL_UPSTREAM` setting configures whether package versions can be retained from internal upstream repositories in the same CodeArtifact domain
when requested by a package manager.

- **ALLOW**: Any package version can be retained from other CodeArtifact repositories configured as upstream repositories.
- **BLOCK**: Package versions cannot be retained from other CodeArtifact repositories configured as upstream repositories.
- **ALLOW_SPECIFIC_REPOSITORIES**: Package versions can only be retained from other CodeArtifact respositories configured as upstream repositories into repositories specified in the
  allowed repository list for internal upstreams.
- **INHERIT**: The `INTERNAL_UPSTREAM` setting is inherited from the first parent package group with a setting that is not `INHERIT`.

## Allowed repository lists

When a restriction setting is configured as `ALLOW_SPECIFIC_REPOSITORIES`, the package group contains an accompanying allowed repositories list which contains
a list of repositories allowed for that restriction setting. Therefore, a package group contains anywhere from 0 to 3 allowed repository lists, one for each setting configured as `ALLOW_SPECIFIC_REPOSITORIES`.

When you add a repository to a package group's allowed repository list, you must specify which allowed repository list to add it to.

The possible allowed repository lists are as follows:

- `EXTERNAL_UPSTREAM`: Allow or block ingestion of package versions from external repositories in the added repository.
- `INTERNAL_UPSTREAM`: Allow or block pulling package versions from another CodeArtifact repository in the added repository.
- `PUBLISH`: Allow or block direct publishing of package versions from package managers to the added repository.

## Editing package group origin control settings

To add or edit origin controls for a package group, perform the steps in the following procedure. For information about the
package group origin control settings, see
[Restriction settings](#package-group-origin-control-settings-restrictions "#package-group-origin-control-settings-restrictions") and
[Allowed repository lists](#package-group-origin-control-settings-repositories "#package-group-origin-control-settings-repositories").

###### To add or edit package group origin controls (CLI)

1. If you haven't, configure the AWS CLI by following the steps in [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md").
2. Use the `update-package-group-origin-configuration` command to add
   or edit package origin controls.
   - For `--domain`, enter the CodeArtifact domain that contains the package group you want to update.
   - For `--domain-owner`, enter the account number of the owner of the domain.
   - For `--package-group`, enter the package group you want to update.
   - For `--restrictions`, enter key-value pairs that represent the origin control restrictions.
   - For `--add-allowed-repositories`, enter a JSON object containing the restriction type
     and repository name to add to the corresponding allowed repositories list for the restriction.
   - For `--remove-allowed-repositories`, enter a JSON object containing the restriction type
     and repository name to remove from the corresponding allowed repositories list for the restriction.

```
aws codeartifact update-package-group-origin-configuration \
   --domain `my_domain` \
   --domain-owner `111122223333` \
   --package-group `'/nuget/*'` \
   --restrictions `INTERNAL_UPSTREAM`=`ALLOW_SPECIFIC_REPOSITORIES` \
   --add-allowed-repositories originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`my_repo` \
   --remove-allowed-repositories originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`my_repo2`
```

The following example adds multiple restrictions, and multiple repositories in one command.

```
aws codeartifact update-package-group-origin-configuration \
   --domain `my_domain` \
   --domain-owner `111122223333` \
   --package-group `'/nuget/*'` \
   --restrictions `PUBLISH`=`BLOCK`,`EXTERNAL_UPSTREAM`=`ALLOW_SPECIFIC_REPOSITORIES`,`INTERNAL_UPSTREAM`=`ALLOW_SPECIFIC_REPOSITORIES` \
   --add-allowed-repositories originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`my_repo` originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`my_repo2` \
   --remove-allowed-repositories originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`my_repo2`
```

## Package group origin control configuration examples

The following examples show package origin control configurations for common package management scenarios.

### Allowing packages with private names to be published, but not ingested

This scenario is likely a common scenario in package management:

- Allow packages with private names to be published to repositories in your domain from package managers, and block
  them from being ingested to repositories in your domain from external, public repositories.
- Allow all other packages to be ingested to repositories in your domain from external, public repositories, and block them
  from being published to repositories in your domain from package managers.

To achieve this, you should configure a package group with a pattern that includes the private name(s), and origin settings of
**PUBLISH: ALLOW**, **EXTERNAL_UPSTREAM: BLOCK**, and
**INTERNAL_UPSTREAM: ALLOW**. This will ensure packages with private names can be published directly, but cannot be
ingested from external repositories.

The following AWS CLI commands create and configure a package group with origin restriction settings that match the desired behavior:

To create the package group:

```
aws codeartifact create-package-group \
   --domain `my_domain` \
   --package-group `/npm/space/anycompany~` \
   --domain-owner `111122223333` \
   --contact-info `contact@email.com | URL` \
   --description `"my package group"`
```

To update the package group's origin configuration:

```
aws codeartifact update-package-group-origin-configuration \
   --domain `my_domain` \
   --domain-owner `111122223333` \
   --package-group `'/npm/space/anycompany~'` \
   --restrictions `PUBLISH`=`ALLOW`,`EXTERNAL_UPSTREAM`=`BLOCK`,`INTERNAL_UPSTREAM`=`ALLOW`
```

### Allowing ingestion from external repositories through one repository

In this scenario, your domain has multiple repositories. Of those repositories, `repoA` has an upstream
connection to `repoB`, which has an external connection to the public repository, `npmjs.com`, as shown:

`repoA --> repoB --> npmjs.com`

You want to allow ingestion of packages from a specific package group, `/npm/space/anycompany~`
from `npmjs.com` into `repoA`, but only through `repoB`. You also want to block
ingestion of packages associated with the package group into any other repositories in your domain, and block direct publishing of packages
with package managers. To achieve this, you create and configure the package group as follows:

Origin restriction settings of **PUBLISH: BLOCK**,
and **EXTERNAL_UPSTREAM: ALLOW_SPECIFIC_REPOSITORIES**, and
**INTERNAL_UPSTREAM: ALLOW_SPECIFIC_REPOSITORIES**.

`repoA` and `repoB` added to the appropriate allowed repository list:

- `repoA` should be added to the `INTERNAL_UPSTREAM` list, as it will get packages from its internal
  upstream, `repoB`.
- `repoB` should be added to the `EXTERNAL_UPSTREAM` list, as it will get packages from the
  external repository, `npmjs.com`.

The following AWS CLI commands create and configure a package group with origin restriction settings that match the desired behavior:

To create the package group:

```
aws codeartifact create-package-group \
   --domain `my_domain` \
   --package-group `/npm/space/anycompany~` \
   --domain-owner `111122223333` \
   --contact-info `contact@email.com | URL` \
   --description `"my package group"`
```

To update the package group's origin configuration:

```
aws codeartifact update-package-group-origin-configuration \
   --domain `my_domain` \
   --domain-owner `111122223333` \
   --package-group `/npm/space/anycompany~` \
   --restrictions `PUBLISH`=`BLOCK`,`EXTERNAL_UPSTREAM`=`ALLOW_SPECIFIC_REPOSITORIES`,`INTERNAL_UPSTREAM`=`ALLOW_SPECIFIC_REPOSITORIES` \
   --add-allowed-repositories originRestrictionType=`INTERNAL_UPSTREAM`,repositoryName=`repoA` originRestrictionType=`EXTERNAL_UPSTREAM`,repositoryName=`repoB`
```

## How package group origin control settings interact with package origin control settings

Because packages have origin control settings, and their associated package groups have origin control settings, it's important to understand how those two
different settings interact with one another. For information about the interaction between the settings, see
[How package origin controls interact with package group origin controls](package-origin-controls.md#package-origin-controls-interaction-package-groups "package-origin-controls.md#package-origin-controls-interaction-package-groups").
