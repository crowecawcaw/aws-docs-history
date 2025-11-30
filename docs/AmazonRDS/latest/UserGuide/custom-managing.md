# Setting the NLS_LANG value in RDS Custom for Oracle

A _locale_ is a set of information addressing linguistic and cultural
requirements that corresponds to a given language and country. To specify locale behavior
for Oracle software, set the `NLS_LANG` environment variable on your client host.
This variable sets the language, territory, and character set used by the client application
in a database session.

For RDS Custom for Oracle, you can set only the language in the `NLS_LANG` variable: the
territory and character use defaults. The language is used for Oracle database messages,
collation, day names, and month names. Each supported language has a unique name, for
example, American, French, or German. If language is not specified, the value defaults to
American.

After you create your RDS Custom for Oracle database, you can set `NLS_LANG` on your client
host to a language other than English. To see a list of languages supported by Oracle
Database, log in to your RDS Custom for Oracle database and run the following query:

```
SELECT VALUE FROM V$NLS_VALID_VALUES WHERE PARAMETER='LANGUAGE' ORDER BY VALUE;
```

You can set `NLS_LANG` on the host command line. The following example sets the
language to German for your client application using the Z shell on Linux.

```
export NLS_LANG=German
```

Your application reads the `NLS_LANG` value when it starts and then
communicates it to the database when it connects.

For more information, see [Choosing a Locale with the NLS_LANG Environment Variable](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/setting-up-globalization-support-environment.html#GUID-86A29834-AE29-4BA5-8A78-E19C168B690A "https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/setting-up-globalization-support-environment.html#GUID-86A29834-AE29-4BA5-8A78-E19C168B690A") in the
_Oracle Database Globalization Support Guide_.
