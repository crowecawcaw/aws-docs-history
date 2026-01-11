# Working with Trusted Language Extensions for PostgreSQL

Trusted Language Extensions for PostgreSQL is an open source development kit for building
PostgreSQL extensions. It allows you to build high performance PostgreSQL extensions
and safely run them on your RDS for PostgreSQL DB instance.
By using Trusted Language Extensions (TLE) for PostgreSQL, you can create PostgreSQL extensions that follow the
documented approach for extending PostgreSQL functionality. For more information, see
[Packaging
Related Objects into an Extension](https://www.postgresql.org/docs/current/extend-extensions.html "https://www.postgresql.org/docs/current/extend-extensions.html") in the PostgreSQL documentation.

One key benefit of TLE is that you can use it in environments that don't provide
access to the file system underlying the PostgreSQL instance. Previously, installing a new
extension required access to the file system. TLE removes this constraint. It provides a
development environment for creating new extensions for any PostgreSQL database, including
those running on your RDS for PostgreSQL DB instances.

TLE is designed to prevent access to unsafe resources for the extensions that you create
using TLE. Its runtime environment limits the impact of any extension defect to a single
database connection. TLE also gives database administrators fine-grained control over who
can install extensions, and it provides a permissions model for running them.

TLE is supported on the following RDS for PostgreSQL versions:

- Version 17.1 and higher 17 versions
- Version 16.1 and higher 16 versions
- Version 15.2 and higher 15 versions
- Version 14.5 and higher 14 versions
- Version 13.12 and higher 13 versions
  The Trusted Language Extensions development environment and runtime are packaged as
  the `pg_tle` PostgreSQL extension, version 1.0.1. It supports creating extensions
  in JavaScript, Perl, Tcl, PL/pgSQL, and SQL.
  You install the `pg_tle` extension in your RDS for PostgreSQL DB instance in the same way that you
  install other PostgreSQL extensions. After the `pg_tle` is set up, developers can
  use it to create new PostgreSQL extensions, known as _TLE extensions_.

In the following topics, you can find information about how to set up Trusted Language Extensions
and how to get started creating your own TLE extensions.

###### Topics

- [Terminology](PostgreSQL_trusted_language_extension-terminology.md "PostgreSQL_trusted_language_extension-terminology.md")
- [Requirements for using Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-requirements.md "PostgreSQL_trusted_language_extension-requirements.md")
- [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md")
- [Overview of Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension.md "PostgreSQL_trusted_language_extension.md")
- [Creating TLE extensions for
  RDS for PostgreSQL](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md "PostgreSQL_trusted_language_extension-creating-TLE-extensions.md")
- [Dropping your TLE extensions from a database](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md "PostgreSQL_trusted_language_extension-creating-TLE-extensions.md")
- [Uninstalling Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-uninstalling-pg_tle-devkit.md "PostgreSQL_trusted_language_extension-uninstalling-pg_tle-devkit.md")
- [Using PostgreSQL hooks with your TLE extensions](PostgreSQL_trusted_language_extension.overview.md "PostgreSQL_trusted_language_extension.overview.md")
- [Using Custom Data Types in TLE](PostgreSQL_trusted_language_extension-custom-data-type.md "PostgreSQL_trusted_language_extension-custom-data-type.md")
- [Function reference for Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-functions-reference.md "PostgreSQL_trusted_language_extension-functions-reference.md")
- [Hooks reference for
  Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-hooks-reference.md "PostgreSQL_trusted_language_extension-hooks-reference.md")
