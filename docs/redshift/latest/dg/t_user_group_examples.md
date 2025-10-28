Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Example for controlling user and group

access

This example creates user groups and users and then grants them various
permissions for an Amazon Redshift database that connects to a web application client. This
example assumes three groups of users: regular users of a web application, power users of a
web application, and web developers.

For information about how to remove a user from a group, see
[ALTER GROUP](r_ALTER_GROUP.md "r_ALTER_GROUP.md").

1. Create the groups where the users will be assigned. The following set of
   commands creates three different user groups:

```
create group webappusers;

create group webpowerusers;

create group webdevusers;

```

2.  Create several database users with different permissions and add them
    to the groups.
    1. Create two users and add them to the WEBAPPUSERS group:

    ```
    create user webappuser1 password 'webAppuser1pass'
    in group webappusers;

    create user webappuser2 password 'webAppuser2pass'
    in group webappusers;

    ```

    2. Create a web developer user and add it to the WEBDEVUSERS group:

    ```
    create user webdevuser1 password 'webDevuser2pass'
    in group webdevusers;

    ```

    3. Create a superuser. This user will have administrative rights
       to create other users:

    ```
    create user webappadmin  password 'webAppadminpass1'
    createuser;

    ```

3.  Create a schema to be associated with the database tables used by the web
    application, and grant the various user groups access to this schema:

        1. Create the WEBAPP schema:




        ```
        create schema webapp;

        ```
        2. Grant USAGE permissions to the WEBAPPUSERS group:




        ```
        grant usage on schema webapp to group webappusers;

        ```
        3. Grant USAGE permissions to the WEBPOWERUSERS group:




        ```
        grant usage on schema webapp to group webpowerusers;

        ```
        4. Grant ALL permissions to the WEBDEVUSERS group:




        ```
        grant all on schema webapp to group webdevusers;

        ```

    The basic users and groups are now set up. You can now alter the users and groups.

4.  For example, the following command alters the search_path parameter for the
    WEBAPPUSER1.

```
alter user webappuser1 set search_path to webapp, public;

```

The SEARCH_PATH specifies the schema search order for database objects, such as
tables and functions, when the object is referenced by a simple name with no schema
specified. 5. You can also add users to a group after creating the group, such as adding
WEBAPPUSER2 to the WEBPOWERUSERS group:

```
alter group webpowerusers add user webappuser2;

```
