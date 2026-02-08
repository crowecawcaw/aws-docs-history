# MSFTCOST04-BP02 Consider Babelfish for Amazon Aurora

PostgreSQL

Babelfish is an Amazon Aurora PostgreSQL feature that allows SQL
Server client applications to connect directly to PostgreSQL
databases. It works by understanding SQL Server's TDS protocol and
common SQL statements, providing a dedicated endpoint for SQL Server
connections. This functionality enables organizations to migrate
from SQL Server to PostgreSQL while maintaining application
compatibility and minimizing the need for code modifications.

**Desired outcome:** By implementing
Babelfish for Amazon Aurora PostgreSQL, we aim to efficiently
migrate our SQL Server-based applications while minimizing
development effort, reducing migration costs, and maintaining
application compatibility. This will enable a smoother transition to
PostgreSQL without extensive code refactoring.

**Common anti-patterns:**

- Complete rewrite approach: Unnecessarily rewriting entire
  applications to migrate from SQL Server to PostgreSQL, instead
  of leveraging Babelfish's compatibility features. This approach
  often leads to extended project timelines, increased costs, and
  potential introduction of new bugs.
- Ignoring dialect differences: Assuming full SQL Server
  compatibility and neglecting to test and adjust for specific
  T-SQL features not supported by Babelfish. This can result in
  unexpected behavior or errors in production after migration.

**Benefits of establishing this best
practice:**

- Reduces costs and complexity by minimizing code changes when
  transitioning from SQL Server to PostgreSQL, accelerating the
  migration process.
- Enables quick transition to Amazon Aurora PostgreSQL while
  maintaining application compatibility, allowing organizations to
  leverage cloud benefits with minimal disruption.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Begin by identifying SQL Server applications suitable for
Babelfish migration and assess their T-SQL compatibility using the
Babelfish Compass tool. Create a test environment to validate
application functionality with Babelfish-enabled Amazon Aurora
PostgreSQL cluster, focusing on critical database operations and
stored procedures. Implement the migration in phases, starting
with non-critical applications, and maintain detailed
documentation of any required code adjustments or workarounds for
unsupported features.

### Implementation steps

1. Assess application compatibility using the Babelfish Compass
   tool or the AWS Schema Convertion Tool.
2. Set up a Babelfish-enabled Amazon Aurora PostgreSQL cluster
   and configure the TDS listener port.
3. Modify application connection strings to point to the
   Babelfish endpoint instead of the SQL Server instance.
4. Test thoroughly, focusing on critical database operations,
   stored procedures, and application functionality before
   migrating production workloads.

## Resources

**Related documents:**

- [Using
  Babelfish for Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/babelfish.md "../../../AmazonRDS/latest/AuroraUserGuide/babelfish.md")
- [Migrating
  a SQL Server database to Babelfish for Aurora
  PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/babelfish-migration.md "../../../AmazonRDS/latest/AuroraUserGuide/babelfish-migration.md")
- [Prepare
  for Babelfish migration with the AWS SCT assessment
  report](https://aws.amazon.com/blogs/database/prepare-for-babelfish-migration-with-the-aws-sct-assessment-report/ "https://aws.amazon.com/blogs/database/prepare-for-babelfish-migration-with-the-aws-sct-assessment-report/")

**Related tools:**

- [Babelfish
  Compass](https://github.com/babelfish-for-postgresql/babelfish_compass "https://github.com/babelfish-for-postgresql/babelfish_compass")
- [What
  is the AWS Schema Conversion Tool?](../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md "../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md")
