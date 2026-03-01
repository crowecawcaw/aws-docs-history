# Using PostgreSQL hooks with your TLE extensions

A _hook_ is a callback mechanism available in PostgreSQL that
allows developers to call custom functions or other routines during regular database
operations. The TLE development kit supports PostgreSQL hooks so that you can
integrate custom functions with PostgreSQL behavior at runtime. For example, you can use
a hook to associate the authentication process with your own custom code, or to modify
the query planning and execution process for your specific needs.

Your TLE extensions can use hooks. If a hook is global in scope, it applies across all
databases. Therefore, if your TLE extension uses a global hook, then you need to create
your TLE extension in all databases that your users can access.

When you use the `pg_tle` extension to build your own Trusted Language Extensions, you can
use the available hooks from a SQL API to build out the functions of your extension. You
should register any hooks with `pg_tle`. For some hooks, you might also need
to set various configuration parameters. For example, the `passcode` check
hook can be set to on, off, or require. For more information about specific requirements
for available `pg_tle` hooks, see [Hooks reference for Trusted Language Extensions for PostgreSQL](PostgreSQL_trusted_language_extension-hooks-reference.md "PostgreSQL_trusted_language_extension-hooks-reference.md").

## Example: Creating an extension that uses a PostgreSQL hook

The example discussed in this section uses a PostgreSQL hook to check the password provided during specific SQL operations and prevents
database users from setting their passwords to any of those contained in the
`password_check.bad_passwords` table. The table contains the top-ten
most commonly used, but easily breakable choices for passwords.

To set up this example in your
RDS for PostgreSQL DB instance, you must have already installed
Trusted Language Extensions. For details, see [Setting up Trusted Language Extensions in your RDS for PostgreSQL DB instance](PostgreSQL_trusted_language_extension-setting-up.md "PostgreSQL_trusted_language_extension-setting-up.md").

###### To set up the password-check hook example

1. Use `psql` to connect to
   RDS for PostgreSQL DB instance.

```
psql --host=`db-instance-123456789012`.`aws-region`.rds.amazonaws.com
--port=`5432` --username=`postgres` --password --dbname=`labdb`
```

2. Copy the code from the [Password-check hook code listing](#PostgreSQL_trusted_language_extension-example-hook_code_listing "#PostgreSQL_trusted_language_extension-example-hook_code_listing") and paste it into your database.

```
SELECT pgtle.install_extension (
  'my_password_check_rules',
  '1.0',
  'Do not let users use the 10 most commonly used passwords',
$_pgtle_$
  CREATE SCHEMA password_check;
  REVOKE ALL ON SCHEMA password_check FROM PUBLIC;
  GRANT USAGE ON SCHEMA password_check TO PUBLIC;

  CREATE TABLE password_check.bad_passwords (plaintext) AS
  VALUES
    ('123456'),
    ('password'),
    ('12345678'),
    ('qwerty'),
    ('123456789'),
    ('12345'),
    ('1234'),
    ('111111'),
    ('1234567'),
    ('dragon');
  CREATE UNIQUE INDEX ON password_check.bad_passwords (plaintext);

  CREATE FUNCTION password_check.passcheck_hook(username text, password text, password_type pgtle.password_types, valid_until timestamptz, valid_null boolean)
  RETURNS void AS $$
    DECLARE
      invalid bool := false;
    BEGIN
      IF password_type = 'PASSWORD_TYPE_MD5' THEN
        SELECT EXISTS(
          SELECT 1
          FROM password_check.bad_passwords bp
          WHERE ('md5' || md5(bp.plaintext || username)) = password
        ) INTO invalid;
        IF invalid THEN
          RAISE EXCEPTION 'Cannot use passwords from the common password dictionary';
        END IF;
      ELSIF password_type = 'PASSWORD_TYPE_PLAINTEXT' THEN
        SELECT EXISTS(
          SELECT 1
          FROM password_check.bad_passwords bp
          WHERE bp.plaintext = password
        ) INTO invalid;
        IF invalid THEN
          RAISE EXCEPTION 'Cannot use passwords from the common password dictionary';
        END IF;
      END IF;
    END
  $$ LANGUAGE plpgsql SECURITY DEFINER;

  GRANT EXECUTE ON FUNCTION password_check.passcheck_hook TO PUBLIC;

  SELECT pgtle.register_feature('password_check.passcheck_hook', 'passcheck');
$_pgtle_$
);
```

When the extension has been loaded into your database, you see the output such as the
following.

```
 install_extension
-------------------
 t
(1 row)
```

3. While still connected to the database, you can now create the extension.

```
CREATE EXTENSION my_password_check_rules;
```

4. You can confirm that the extension has been created in the database by using the
   following `psql` metacommand.

```
\dx
 `List of installed extensions
 Name | Version | Schema | Description
-------------------------+---------+------------+-------------------------------------------------------------
 my_password_check_rules | 1.0 | public | Prevent use of any of the top-ten most common bad passwords
 pg_tle | 1.0.1 | pgtle | Trusted-Language Extensions for PostgreSQL
 plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
(3 rows)`
```

5. Open another terminal session to work with the AWS CLI. You need to modify your custom DB
   parameter group to turn on the password-check hook. To do so, use the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") CLI command as shown in the following
   example.

```
aws rds modify-db-parameter-group \
    --region `aws-region` \
    --db-parameter-group-name `your-custom-parameter-group` \
    --parameters "ParameterName=pgtle.enable_password_check,ParameterValue=on,ApplyMethod=immediate"
```

When the parameter is successfully turned on, you see the output such as
the following.

```
(
    "DBParameterGroupName": "docs-lab-parameters-for-tle"
}
```

It might take a few minutes for the change to the parameter group setting to take effect. This parameter is dynamic, however, so you
don't need to restart the
RDS for PostgreSQL DB instance for the setting to take effect. 6. Open the `psql` session and query the database to verify that the password_check
hook has been turned on.

```
`labdb=>` SHOW pgtle.enable_password_check;
`pgtle.enable_password_check
-----------------------------
on
(1 row)`
```

The password-check hook is now active. You can test it by creating a new role and using one of
the bad passwords, as shown in the following example.

```
CREATE ROLE test_role PASSWORD 'password';
ERROR:  Cannot use passwords from the common password dictionary
CONTEXT:  PL/pgSQL function password_check.passcheck_hook(text,text,pgtle.password_types,timestamp with time zone,boolean) line 21 at RAISE
SQL statement "SELECT password_check.passcheck_hook(
    $1::pg_catalog.text,
    $2::pg_catalog.text,
    $3::pgtle.password_types,
    $4::pg_catalog.timestamptz,
    $5::pg_catalog.bool)"
```

The output has been formatted for readability.

The following example shows that `pgsql` interactive metacommand `\password` behavior
is also affected by the password_check hook.

```
`postgres=>` SET password_encryption TO 'md5';
`SET`
`postgres=>` \password
`Enter new password for user "postgres":``*****`
`Enter it again:``*****`
`ERROR: Cannot use passwords from the common password dictionary
CONTEXT: PL/pgSQL function password_check.passcheck_hook(text,text,pgtle.password_types,timestamp with time zone,boolean) line 12 at RAISE
SQL statement "SELECT password_check.passcheck_hook($1::pg_catalog.text, $2::pg_catalog.text, $3::pgtle.password_types, $4::pg_catalog.timestamptz, $5::pg_catalog.bool)"`
```

You can drop this TLE extension and uninstall its source files if you want. For more
information, see [Dropping your TLE extensions from a database](PostgreSQL_trusted_language_extension-creating-TLE-extensions.md "PostgreSQL_trusted_language_extension-creating-TLE-extensions.md").

### Password-check hook code listing

The example code shown here defines the specification for the
`my_password_check_rules` TLE extension. When you copy this code
and paste it into your database, the code for the
`my_password_check_rules` extension is loaded into the database,
and the `password_check` hook is registered for use by the
extension.

```
SELECT pgtle.install_extension (
  'my_password_check_rules',
  '1.0',
  'Do not let users use the 10 most commonly used passwords',
$_pgtle_$
  CREATE SCHEMA password_check;
  REVOKE ALL ON SCHEMA password_check FROM PUBLIC;
  GRANT USAGE ON SCHEMA password_check TO PUBLIC;

  CREATE TABLE password_check.bad_passwords (plaintext) AS
  VALUES
    ('123456'),
    ('password'),
    ('12345678'),
    ('qwerty'),
    ('123456789'),
    ('12345'),
    ('1234'),
    ('111111'),
    ('1234567'),
    ('dragon');
  CREATE UNIQUE INDEX ON password_check.bad_passwords (plaintext);

  CREATE FUNCTION password_check.passcheck_hook(username text, password text, password_type pgtle.password_types, valid_until timestamptz, valid_null boolean)
  RETURNS void AS $$
    DECLARE
      invalid bool := false;
    BEGIN
      IF password_type = 'PASSWORD_TYPE_MD5' THEN
        SELECT EXISTS(
          SELECT 1
          FROM password_check.bad_passwords bp
          WHERE ('md5' || md5(bp.plaintext || username)) = password
        ) INTO invalid;
        IF invalid THEN
          RAISE EXCEPTION 'Cannot use passwords from the common password dictionary';
        END IF;
      ELSIF password_type = 'PASSWORD_TYPE_PLAINTEXT' THEN
        SELECT EXISTS(
          SELECT 1
          FROM password_check.bad_passwords bp
          WHERE bp.plaintext = password
        ) INTO invalid;
        IF invalid THEN
          RAISE EXCEPTION 'Cannot use passwords from the common password dictionary';
        END IF;
      END IF;
    END
  $$ LANGUAGE plpgsql SECURITY DEFINER;

  GRANT EXECUTE ON FUNCTION password_check.passcheck_hook TO PUBLIC;

  SELECT pgtle.register_feature('password_check.passcheck_hook', 'passcheck');
$_pgtle_$
);
```
