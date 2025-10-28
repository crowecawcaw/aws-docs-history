# Migrating from Neo4j to Amazon Neptune

Neo4j and Amazon Neptune are both graph databases, designed for online, transactional
graph workloads that support the labeled property graph data model. These similarities
make Neptune a common choice for customers seeking to migrate their current Neo4j
applications. However, these migrations are not simply lift and shift, because there
are differences in languages and feature support, operational characteristics, server
architecture, and storage capabilities between the two databases.

This page frames the migration process and brings up things to consider
before migrating a Neo4j graph application to Neptune. These considerations
apply generally to any Neo4j graph application, whether powered by a Community,
Enterprise, or Aura database. Although each solution is unique and may require
additional procedures, all migrations follow the same general pattern.

Each of the steps described in the following sections includes considerations
and recommendations to simplify the migration process. Additionally, there are
[open-source tools, and blog posts](migration-resources.md "migration-resources.md") that
describe the process, and a [feature
compatibility section](migration-compatibility.md "migration-compatibility.md") with recommended architectural options.

###### Topics

- [General information about migrating from Neo4j to Neptune](migrating-from-neo4j-general.md "migrating-from-neo4j-general.md")
- [Preparing to migrate from Neo4j to Neptune](preparing-to-migrate-from-neo4j.md "preparing-to-migrate-from-neo4j.md")
- [Provisioning infrastructure when migrating from Neo4j to Neptune](migration-provisioning-infrastructure.md "migration-provisioning-infrastructure.md")
- [Data migration from Neo4j to Neptune](migration-data-migration.md "migration-data-migration.md")
- [Application migration from Neo4j to Neptune](migration-app-migration.md "migration-app-migration.md")
- [Neptune compatibility with Neo4j](migration-compatibility.md "migration-compatibility.md")
- [Rewriting Cypher queries to run in openCypher on Neptune](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md")
- [Resources for migrating from Neo4j to Neptune](migration-resources.md "migration-resources.md")
