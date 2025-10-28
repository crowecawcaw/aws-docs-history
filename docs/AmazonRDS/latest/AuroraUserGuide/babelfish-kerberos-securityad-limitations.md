# Limitations

- Dump/Restore utility doesn’t support dumping the pg_ad_mapping extension
  mappings. You will need to recreate those mappings after restore.
- Blue-Green deployment isn't supported for Babelfish and Aurora PostgreSQL
  instances with `pg_ad_mapping`.
- Implicit schema creation is not supported. DDL statements that requires
  implicit schema creation isn't supported.
- Server-level DDLs ALTER AUTHORIZATION ON DATABASE , CREATE DATABASE, CREATE
  LOGIN, ALTER LOGIN, ALTER SERVER ROLE, ALTER DATABASE are not supported in a
  Group AD authenticated session when individual Windows login doesn’t exist, only
  group Windows login exists. To workaround this limitation, It is recommended to
  perform these operations in a password authenticated session or create
  individual Windows login.
- Implicit user creation isn't supported. Ideal T-SQL behavior [not yet
  supported in Babelfish]; In some cases like DDL and access-control statements
  like GRANT/REVOKE where AD user’s name is specified in the command but it
  doesn’t exist in database then database user named as AD user get implicitly
  created.
- For DDLs in PL/pgSQL Procedures or Functions which are created from PSQL
  endpoint and gets executed from TDS endpoint in Group AD authenticated
  session:
  - ALTER/DROP statements will be supported.
  - CREATE TABLE, CREATE VIEW, CREATE INDEX, CREATE FUNCTION/PROC, CREATE
    TYPE, CREATE SEQUENCE, CREATE TRIGGER, SELECT INTO, CREATE FULLTEXT
    INDEX , CREATE UNIQUE INDEX will throw an error if schema is not
    provided explicitly and default schema is null for current
    session.
  - CREATE DATABASE , CREATE EXTENSION and all other CREATE statements for
    PG(not in T-SQL) specific objects CREATE subscription, CREATE
    tablespace, CREATE policy, CREATE conversion will not be
    supported.

- DDLs from PostgreSQL endpoint is not supported in Group AD authenticated
  session. As a workaround, you can always connect using master user or any other
  user using password based authentication mechanism.
- System objects like SUSER_SID(), IS_SRVROLEMEMBER(), IS_MEMBER(),
  sys.dm_exec_sessions has following limitations.
  - SUSER_SID() won’t return the SID when AD User or AD Security Group is
    supplied.
  - IS_SRVROLEMEMBER() won’t consider the role membership if current AD
    user is inheriting the server role membership from any Windows group
    login’s server role membership.
  - IS_MEMBER() will return false for any Windows Group related
    query.
  - sys.dm_exec_sessions won’t show expected values login_name,
    nt_user_name columns.
