

# Terminology
<a name="PostgreSQL_trusted_language_extension-terminology"></a>

To help you better understand Trusted Language Extensions, view the following glossary for terms used in this topic. 

**Trusted Language Extensions for PostgreSQL**  
*Trusted Language Extensions for PostgreSQL* is the official name of the open source development kit that's packaged as the `pg_tle` extension. It's available for use on any PostgreSQL system. For more information, see [aws/pg\_tle](https://github.com/aws/pg_tle) on GitHub.

**Trusted Language Extensions**  
*Trusted Language Extensions* is the short name for Trusted Language Extensions for PostgreSQL. This shortened name and its abbreviation (TLE) are also used in this documentation.

**trusted language**  
A *trusted language* is a programming or scripting language that has specific security attributes. For example, trusted languages typically restrict access to the file system, and they limit use of specified networking properties. The TLE development kit is designed to support trusted languages. PostgreSQL supports several different languages that are used to create trusted or untrusted extensions. For an example, see [Trusted and Untrusted PL/Perl](https://www.postgresql.org/docs/current/plperl-trusted.html) in the PostgreSQL documentation. When you create an extension using Trusted Language Extensions, the extension inherently uses trusted language mechanisms.

**TLE extension**  
A *TLE extension* is a PostgreSQL extension that's been created by using the Trusted Language Extensions (TLE) development kit. 