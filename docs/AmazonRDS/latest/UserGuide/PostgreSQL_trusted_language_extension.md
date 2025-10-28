# Overview of Trusted Language Extensions for PostgreSQL

Trusted Language Extensions for PostgreSQL is a PostgreSQL extension that you install in your RDS for PostgreSQL DB instance in the same way that you set up other PostgreSQL
extensions. In the following image of an example database in the pgAdmin client tool,
you can view some of the components that comprise the `pg_tle`
extension.

![Image showing some of the components that make up the TLE development kit.](images/apg-pg_tle-installed-view-in-pgAdmin.png)
You can see the following details.

1. The Trusted Language Extensions (TLE) for PostgreSQL development kit is packaged as the
   `pg_tle` extension. As such, `pg_tle` is added to the
   available extensions for the database in which it's installed.
2. TLE has its own schema, `pgtle`. This schema contains helper functions (3) for
   installing and managing the extensions that you create.
3. TLE provides over a dozen helper functions for installing, registering, and managing
   your extensions. To learn more about these functions, see [Function reference for Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-functions-reference.md "PostgreSQL_trusted_language_extension-functions-reference.md").
   Other components of the `pg_tle` extension include the following:

- The `pgtle_admin` role – The
  `pgtle_admin` role is created when the `pg_tle`
  extension is installed. This role is privileged and should be treated as such.
  We strongly recommend that you follow the principle of _least
  privilege_ when granting the `pgtle_admin` role to
  database users. In other words, grant the `pgtle_admin` role only to
  database users that are allowed to create, install, and manage new TLE
  extensions, such as `postgres`.
- The `pgtle.feature_info` table – The
  `pgtle.feature_info` table is a protected table that contains
  information about your TLEs, hooks, and the custom stored procedures and
  functions that they use. If you have `pgtle_admin` privileges, you
  use the following Trusted Language Extensions functions to add and update that information in
  the table.
  - [pgtle.register_feature](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature")
  - [pgtle.register_feature_if_not_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature_if_not_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.register_feature_if_not_exists")
  - [pgtle.unregister_feature](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature")
  - [pgtle.unregister_feature_if_exists](PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature_if_exists "PostgreSQL_trusted_language_extension-functions-reference.md#pgtle.unregister_feature_if_exists")
