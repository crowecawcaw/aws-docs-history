# Upgrading your Babelfish cluster to a new version

New versions of Babelfish become available with some new releases of the
Aurora PostgreSQL database engine after version 13.4. Each new release of Babelfish
has its own version number. As with Aurora PostgreSQL, Babelfish uses the
`major`.`minor`.`patch`
naming scheme for versions. For example, the first Babelfish release,
Babelfish version 1.0.0, became available as part of Aurora PostgreSQL 13.4.0.

Babelfish doesn't require a separate installation process. As discussed in
[Creating a Babelfish for Aurora PostgreSQL DB cluster](babelfish-create.md "babelfish-create.md"), **Turn
on Babelfish** is an option that you choose when you create an
Aurora PostgreSQL DB cluster.

Likewise, you can't upgrade Babelfish independently from the supporting
Aurora DB cluster. To upgrade an existing Babelfish for Aurora PostgreSQL DB cluster to a new version of
Babelfish, you upgrade the Aurora PostgreSQL DB cluster to a new version that
supports the version of Babelfish that you want to use. The procedure that you
follow for the upgrade depends on the version of Aurora PostgreSQL that's supporting
your Babelfish deployment, as follows.

**Major version upgrades**

You must upgrade the following Aurora PostgreSQL versions to Aurora PostgreSQL
14.6 and higher version before upgrading to Aurora PostgreSQL 15.2
version.

- Aurora PostgreSQL 13.8 and all higher versions
- Aurora PostgreSQL 13.7.1 and all higher minor versions
- Aurora PostgreSQL 13.6.4 and all higher minor versions

You can upgrade Aurora PostgreSQL 14.6 and higher versions to Aurora PostgreSQL
15.2 and higher versions.

Upgrading an Aurora PostgreSQL DB cluster to a new major version involves
several preliminary tasks. For more information, see [Performing a major version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md"). To
successfully upgrade your Babelfish for Aurora PostgreSQL DB cluster, you need to create a
custom DB cluster parameter group for the new Aurora PostgreSQL version. This
new parameter group must contain the same Babelfish parameter
settings as that of the cluster that you're upgrading. For more
information and for a table of major version upgrade sources and targets,
see [Upgrading Babelfish to a new major version](babelfish-information-upgrading-major.md "babelfish-information-upgrading-major.md").

**Minor version upgrades and patches**

Minor versions and patches don't require the creation of a new DB
cluster parameter group for the upgrade. Minor versions and patches can use
the minor version upgrade process, whether that's applied automatically
or manually. For more information and a table of version sources and
targets, see [Upgrading Babelfish to a new minor version](babelfish-information-upgrading-minor.md "babelfish-information-upgrading-minor.md").

###### Note

Before performing a major or a minor upgrade, apply all pending maintenance tasks
to your Babelfish for Aurora PostgreSQL cluster.

###### Topics

- [Upgrading Babelfish to a new minor version](babelfish-information-upgrading-minor.md "babelfish-information-upgrading-minor.md")
- [Upgrading Babelfish to a new major version](babelfish-information-upgrading-major.md "babelfish-information-upgrading-major.md")
