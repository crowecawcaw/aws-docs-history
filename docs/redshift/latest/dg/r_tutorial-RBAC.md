Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorial: Creating roles and querying with RBAC

With RBAC, you can create roles with permissions to run commands that used to require superuser permissions. Users can run these commands, as long as they are authorized with a role that includes these permissions.

In this tutorial, you use role-based access control (RBAC) to manage permissions in a database you create. You then connect to the database and query the database from two different roles to test the functionality of RBAC.

The two roles that you create and use to query the database are the `sales_ro` and `sales_rw`. You create the `sales_ro` role and query data as a user with the `sales_ro` role. The `sales_ro` user can only use the SELECT command but cannot use the UPDATE command. Then, you create the `sales_rw` role and query data as a user with the `sales_rw` role. The `sales_rw` user can use the SELECT command and the UPDATE command.

Additionally, you can create roles to limit the access to certain commands, and assign the role to either superusers or users.

**Tasks**

- [Prerequisites](#tutorial-rbac-prereqs "#tutorial-rbac-prereqs")
- [Step 1: Create an administrator user](#tutorial-rbac-step1 "#tutorial-rbac-step1")
- [Step 2: Set up schemas](#tutorial-rbac-step2 "#tutorial-rbac-step2")
- [Step 3: Create a read-only user](#tutorial-rbac-step3 "#tutorial-rbac-step3")
- [Step 4: Query the data as the read-only user](#tutorial-rbac-step4 "#tutorial-rbac-step4")
- [Step 5: Create a read-write user](#tutorial-rbac-step5 "#tutorial-rbac-step5")
- [Step 6: Query the data as the user with the inherited read-only role](#tutorial-rbac-step6 "#tutorial-rbac-step6")
- [Step 7: Grant update and insert permissions to the read-write role](#tutorial-rbac-step7 "#tutorial-rbac-step7")
- [Step 8: Query the data as the read-write user](#tutorial-rbac-step8 "#tutorial-rbac-step8")
- [Step 9: Analyze and vacuum tables in a database as the administrator user](#tutorial-rbac-step9 "#tutorial-rbac-step9")
- [Step 10: Truncate tables as the read-write user](#tutorial-rbac-step10 "#tutorial-rbac-step10")
- [System functions for RBAC (optional)](#tutorial-rbac-system-functions "#tutorial-rbac-system-functions")
- [System views for RBAC (optional)](#tutorial-rbac-system-views "#tutorial-rbac-system-views")
- [Use row-level security with RBAC (optional)](#tutorial-rbac-rls "#tutorial-rbac-rls")

## Prerequisites

- Create an Amazon Redshift cluster or serverless workgroup that is loaded with the TICKIT sample database. To create a serverless workgroup, see [Get started with Redshift Serverless data warehouses](../gsg/new-user-serverless.md "../gsg/new-user-serverless.md"). To create a cluster, see [Create a sample Amazon Redshift cluster](../gsg/rs-gsg-launch-sample-cluster.md "../gsg/rs-gsg-launch-sample-cluster.md"). For more information about the TICKIT sample database, see [Sample database](c_sampledb.md "c_sampledb.md").
- Have access to a user with superuser or role administrator permissions. Only superusers or role administrators can grant or revoke roles. For more information about permissions required for RBAC, see [System permissions for RBAC](r_roles-system-privileges.md "r_roles-system-privileges.md").
- Review the [Considerations for role usage in RBAC](r_role-usage-notes.md "r_role-usage-notes.md").

## Step 1: Create an administrator user

To set up for this tutorial, you create a database admin role and attach it to a database administrator user in this step. You must create the database administrator as a superuser or role administrator.

Run all queries in the Amazon Redshift [query editor v2](../mgmt/query-editor-v2-using.md "../mgmt/query-editor-v2-using.md").

1. To create the administrator role db_admin, use the following example.

```
CREATE ROLE db_admin;
```

2. To create a database user named dbadmin, use the following example.

```
CREATE USER dbadmin PASSWORD 'Test12345';
```

3. To grant the system defined role named sys:dba to the db_admin role, use the following example. When granted the sys:dba role, the dbadmin user can create schemas and tables. For more information, see [Amazon Redshift system-defined roles](r_roles-default.md "r_roles-default.md").

## Step 2: Set up schemas

In this step, you connect to your database as the database administrator. Then, you create two schemas and add data to them.

1. Connect to the dev database as the dbadmin user using query editor v2. For more information about connecting to a database, see [Working with query editor v2](../mgmt/query-editor-v2-using.md "../mgmt/query-editor-v2-using.md").
2. To create the sales and marketing database schemas, use the following example.

```
CREATE SCHEMA sales;
CREATE SCHEMA marketing;
```

3. To create and insert values into tables in the sales schema, use the following example.

```
CREATE TABLE sales.cat(
catid smallint,
catgroup varchar(10),
catname varchar(10),
catdesc varchar(50)
);
INSERT INTO sales.cat(SELECT * FROM category);

CREATE TABLE sales.dates(
dateid smallint,
caldate date,
day char(3),
week smallint,
month char(5),
qtr char(5),
year smallint,
holiday boolean
);
INSERT INTO sales.dates(SELECT * FROM date);

CREATE TABLE sales.events(
eventid integer,
venueid smallint,
catid smallint,
dateid smallint,
eventname varchar(200),
starttime timestamp
);
INSERT INTO sales.events(SELECT * FROM event);

 CREATE TABLE sales.sale(
salesid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp
);
INSERT INTO sales.sale(SELECT * FROM sales);
```

4. To create and insert values into tables in the marketing schema, use the following example.

```
CREATE TABLE marketing.cat(
catid smallint,
catgroup varchar(10),
catname varchar(10),
catdesc varchar(50)
);
INSERT INTO marketing.cat(SELECT * FROM category);

CREATE TABLE marketing.dates(
dateid smallint,
caldate date,
day char(3),
week smallint,
month char(5),
qtr char(5),
year smallint,
holiday boolean
);
INSERT INTO marketing.dates(SELECT * FROM date);

CREATE TABLE marketing.events(
eventid integer,
venueid smallint,
catid smallint,
dateid smallint,
eventname varchar(200),
starttime timestamp
);
INSERT INTO marketing.events(SELECT * FROM event);

CREATE TABLE marketing.sale(
marketingid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp
);
INSERT INTO marketing.sale(SELECT * FROM marketing);
```

## Step 3: Create a read-only user

In this step, you create a read-only role and a salesanalyst user for the read-only role. The sales analyst only needs read-only access to the tables in the sales schema to accomplish their assigned task of finding the events that resulted in the largest commissions.

1. Connect to the database as the dbadmin user.
2. To create the sales_ro role, use the following example.

```
CREATE ROLE sales_ro;
```

3. To create the salesanalyst user, use the following example.

```
CREATE USER salesanalyst PASSWORD 'Test12345';
```

4. To grant the sales_ro role usage and select access to objects of the sales schema, use the following example.

```
GRANT USAGE ON SCHEMA sales TO ROLE sales_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA sales TO ROLE sales_ro;
```

5. To grant the salesanalyst user the sales_ro role, use the following example.

```
GRANT ROLE sales_ro TO salesanalyst;
```

## Step 4: Query the data as the read-only user

In this step, the salesanalyst user queries data from the sales schema. Then, the salesanalyst user attempts to update a table and read tables in the marketing schema.

1. Connect to the database as the salesanalyst user.
2. To find the 10 sales with the highest commissions, use the following example.

````
`SET SEARCH_PATH TO sales;
SELECT DISTINCT events.dateid, sale.commission, cat.catname
FROM sale, events, dates, cat
WHERE events.dateid=dates.dateid AND events.dateid=sale.dateid AND events.catid = cat.catid
ORDER BY 2 DESC LIMIT 10;`

`+--------+------------+----------+
| dateid | commission | catname | +--------+------------+----------+
| 1880 | 1893.6 | Pop |
| 1880 | 1893.6 | Opera |
| 1880 | 1893.6 | Plays |
| 1880 | 1893.6 | Musicals |
| 1861 | 1500 | Plays |
| 2003 | 1500 | Pop |
| 1861 | 1500 | Opera |
| 2003 | 1500 | Plays |
| 1861 | 1500 | Musicals |
| 1861 | 1500 | Pop | +--------+------------+----------+` ``` 3. To select 10 events from the events table in the sales schema, use the following example. ``` `SELECT * FROM sales.events LIMIT 10;` `+---------+---------+-------+--------+--------------------+---------------------+
| eventid | venueid | catid | dateid | eventname | starttime | +---------+---------+-------+--------+--------------------+---------------------+
| 4836 | 73 | 9 | 1871 | Soulfest | 2008-02-14 19:30:00 |
| 5739 | 41 | 9 | 1871 | Fab Faux | 2008-02-14 19:30:00 |
| 627 | 229 | 6 | 1872 | High Society | 2008-02-15 14:00:00 |
| 2563 | 246 | 7 | 1872 | Hamlet | 2008-02-15 20:00:00 |
| 7703 | 78 | 9 | 1872 | Feist | 2008-02-15 14:00:00 |
| 7903 | 90 | 9 | 1872 | Little Big Town | 2008-02-15 19:30:00 |
| 7925 | 101 | 9 | 1872 | Spoon | 2008-02-15 19:00:00 |
| 8113 | 17 | 9 | 1872 | Santana | 2008-02-15 15:00:00 |
| 463 | 303 | 8 | 1873 | Tristan und Isolde | 2008-02-16 19:00:00 |
| 613 | 236 | 6 | 1873 | Pal Joey | 2008-02-16 15:00:00 | +---------+---------+-------+--------+--------------------+---------------------+` ``` 4. To attempt to update the eventname for eventid 1, run the following example. This example will result in a permission denied error because the salesanalyst user only has SELECT permissions on the events table in the sales schema. To update the events table, you must grant the sales\_ro role permissions to UPDATE. For more information about granting permissions to update a table, see the UPDATE parameter for [GRANT](r_GRANT.md "r_GRANT.md"). For more information about the UPDATE command, see [UPDATE](r_UPDATE.md "r_UPDATE.md"). ``` `UPDATE sales.events SET eventname = 'Comment event' WHERE eventid = 1;` `ERROR: permission denied for relation events` ``` 5. To attempt to select all from the events table in the marketing schema, use the following example. This example will result in a permission denied error because the salesanalyst user only has SELECT permissions for the events table in the sales schema. To select data from the events table in the marketing schema, you must grant the sales\_ro role SELECT permissions on the events table in the marketing schema. ``` `SELECT * FROM marketing.events;` `ERROR: permission denied for schema marketing` ``` ## Step 5: Create a read-write user In this step, the sales engineer who is responsible for building the extract, transform, and load (ETL) pipeline for data processing in the sales schema will be given read-only access, but will later be given read and write access to perform their tasks. 1. Connect to the database as the dbadmin user. 2. To create the sales\_rw role in the sales schema, use the following example. ``` CREATE ROLE sales_rw; ``` 3. To create the salesengineer user, use the following example. ``` CREATE USER salesengineer PASSWORD 'Test12345'; ``` 4. To grant the sales\_rw role usage and select access to objects of the sales schema by assigning the sales\_ro role to it, use the following example. For more information on how roles inherit permissions in Amazon Redshift, see [Role hierarchy](t_role_hierarchy.md "t_role_hierarchy.md"). ``` GRANT ROLE sales_ro TO ROLE sales_rw; ``` 5. To assign the sales\_rw role to the salesengineer user, use the following example. ``` GRANT ROLE sales_rw TO salesengineer; ``` ## Step 6: Query the data as the user with the inherited read-only role In this step, the salesengineer user attempts to update the events table before they are granted read permissions. 1. Connect to the database as the salesengineer user. 2. The salesengineer user can successfully read data from the events table of the sales schema. To select the event with eventid 1 from the events table in the sales schema, use the following example. ``` `SELECT * FROM sales.events where eventid=1;` `+---------+---------+-------+--------+-----------------+---------------------+
| eventid | venueid | catid | dateid | eventname | starttime | +---------+---------+-------+--------+-----------------+---------------------+
| 1 | 305 | 8 | 1851 | Gotterdammerung | 2008-01-25 14:30:00 | +---------+---------+-------+--------+-----------------+---------------------+` ``` 3. To attempt to select all from the events table in the marketing schema, use the following example. The salesengineer user doesn’t have permissions for tables in the marketing schema, so this query will result in a permission denied error. To select data from the events table in the marketing schema, you must grant the sales\_rw role SELECT permissions on the events table in the marketing schema. ``` `SELECT * FROM marketing.events;` `ERROR: permission denied for schema marketing` ``` 4. To attempt to update the eventname for eventid 1, run the following example. This example will result in a permission denied error because the salesengineer user only has select permissions on the events table in the sales schema. To update the events table, you must grant the sales\_rw role permissions to UPDATE. ``` `UPDATE sales.events SET eventname = 'Comment event' WHERE eventid = 1;` `ERROR: permission denied for relation events` ``` ## Step 7: Grant update and insert permissions to the read-write role In this step, you grant update and insert permissions to the sales\_rw role. 1. Connect to the database as the dbadmin user. 2. To grant UPDATE, INSERT, and DELETE permissions to the sales\_rw role, use the following example. ``` `GRANT UPDATE, INSERT, ON ALL TABLES IN SCHEMA sales TO role sales_rw;` ``` ## Step 8: Query the data as the read-write user In this step, the salesengineer successfully updates the table after their role is granted insert and update permissions. Next, the salesengineer attempts to analyze and vacuum the events table but fails to do so. 1. Connect to the database as the salesengineer user. 2. To update the eventname for eventid 1, run the following example. ``` UPDATE sales.events SET eventname = 'Comment event' WHERE eventid = 1; ``` 3. To view the change made in the previous query, use the following example to select the event with eventid 1 from the events table in the sales schema. ``` `SELECT * FROM sales.events WHERE eventid=1;` `+---------+---------+-------+--------+---------------+---------------------+
| eventid | venueid | catid | dateid | eventname | starttime | +---------+---------+-------+--------+---------------+---------------------+
| 1 | 305 | 8 | 1851 | Comment event | 2008-01-25 14:30:00 | +---------+---------+-------+--------+---------------+---------------------+` ``` 4. To analyze the updated events table in the sales schema, use the following example. This example will result in a permission denied error because the salesengineer user does not have the necessary permissions and isn’t the owner of the events table in the sales schema. To analyze the events table, you must grant the sales\_rw role permissions to ANALYZE using the GRANT command. For more information about the ANALYZE command, see [ANALYZE](r_ANALYZE.md "r_ANALYZE.md"). ``` `ANALYZE sales.events;` `ERROR: skipping "events" --- only table or database owner can analyze` ``` 5. To vacuum the updated events table, use the following example. This example will result in a permission denied error because the salesengineer user does not have the necessary permissions and isn’t the owner of the events table in the sales schema. To vacuum the events table, you must grant the sales\_rw role permissions to VACUUM using the GRANT command. For more information about the VACUUM command, see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md"). ``` `VACUUM sales.events;` `ERROR: skipping "events" --- only table or database owner can vacuum it` ``` ## Step 9: Analyze and vacuum tables in a database as the administrator user In this step, the dbadmin user analyzes and vacuums all of the tables. The user has administrator permissions on this database, so they are able to run these commands. 1. Connect to the database as the dbadmin user. 2. To analyze the events table in the sales schema, use the following example. ``` ANALYZE sales.events; ``` 3. To vacuum the events table in the sales schema, use the following example. ``` VACUUM sales.events; ``` 4. To analyze the events table in the marketing schema, use the following example. ``` ANALYZE marketing.events; ``` 5. To vacuum the events table in the marketing schema, use the following example. ``` VACUUM marketing.events; ``` ## Step 10: Truncate tables as the read-write user In this step, the salesengineer user attempts to truncate the events table in the sales schema, but only succeeds when granted truncate permissions by the dbadmin user. 1. Connect to the database as the salesengineer user. 2. To try to delete all of the rows from the events table in the sales schema, use the following example. This example will result in an error because the salesengineer user does not have the necessary permissions and isn’t the owner of the events table in the sales schema. To truncate the events table, you must grant the sales\_rw role permissions to TRUNCATE using the GRANT command. For more information about the TRUNCATE command, see [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md"). ``` `TRUNCATE sales.events;` `ERROR: must be owner of relation events` ``` 3. Connect to the database as the dbadmin user. 4. To grant truncate table privileges to the sales\_rw role, use the following example. ``` GRANT TRUNCATE TABLE TO role sales_rw; ``` 5. Connect to the database as the salesengineer user using query editor v2. 6. To read the first 10 events from the events table in the sales schema, use the following example. ``` `SELECT * FROM sales.events ORDER BY eventid LIMIT 10;` `+---------+---------+-------+--------+-----------------------------+---------------------+
| eventid | venueid | catid | dateid | eventname | starttime | +---------+---------+-------+--------+-----------------------------+---------------------+
| 1 | 305 | 8 | 1851 | Comment event | 2008-01-25 14:30:00 |
| 2 | 306 | 8 | 2114 | Boris Godunov | 2008-10-15 20:00:00 |
| 3 | 302 | 8 | 1935 | Salome | 2008-04-19 14:30:00 |
| 4 | 309 | 8 | 2090 | La Cenerentola (Cinderella) | 2008-09-21 14:30:00 |
| 5 | 302 | 8 | 1982 | Il Trovatore | 2008-06-05 19:00:00 |
| 6 | 308 | 8 | 2109 | L Elisir d Amore | 2008-10-10 19:30:00 |
| 7 | 309 | 8 | 1891 | Doctor Atomic | 2008-03-06 14:00:00 |
| 8 | 302 | 8 | 1832 | The Magic Flute | 2008-01-06 20:00:00 |
| 9 | 308 | 8 | 2087 | The Fly | 2008-09-18 19:30:00 |
| 10 | 305 | 8 | 2079 | Rigoletto | 2008-09-10 15:00:00 | +---------+---------+-------+--------+-----------------------------+---------------------+` ``` 7. To truncate the events table in the sales schema, use the following example. ``` TRUNCATE sales.events; ``` 8. To read the data from the updated events table in the sales schema, use the following example. ``` `SELECT * FROM sales.events ORDER BY eventid LIMIT 10;` +---------+---------+-------+--------+-----------------------------+---------------------+
| eventid | venueid | catid | dateid |          eventname          |      starttime      | +---------+---------+-------+--------+-----------------------------+---------------------+ ``` ### Create read-only and read-write roles for the marketing schema (optional) In this step, you create read-only and read-write roles for the marketing schema. 1. Connect to the database as the dbadmin user. 2. To create read-only and read-write roles for the marketing schema, use the following example. ``` CREATE ROLE marketing_ro; CREATE ROLE marketing_rw; GRANT USAGE ON SCHEMA marketing TO ROLE marketing_ro, ROLE marketing_rw; GRANT SELECT ON ALL TABLES IN SCHEMA marketing TO ROLE marketing_ro; GRANT ROLE marketing_ro TO ROLE marketing_rw; GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA marketing TO ROLE marketing_rw; CREATE USER marketinganalyst PASSWORD 'Test12345'; CREATE USER marketingengineer PASSWORD 'Test12345'; GRANT ROLE marketing_ro TO marketinganalyst; GRANT ROLE marketing_rw TO marketingengineer; ``` ## System functions for RBAC (optional) Amazon Redshift has two functions to provide system information about user membership and role membership in additional groups or roles: role\_is\_member\_of and user\_is\_member\_of. These functions are available to superusers and regular users. Superusers can check all role memberships. Regular users can only check membership for roles that they have been granted access to. To use the role\_is\_member\_of function 1. Connect to the database as the salesengineer user. 2. To check if the sales\_rw role is a member of the sales\_ro role, use the following example. ``` `SELECT role_is_member_of('sales_rw', 'sales_ro');` `+-------------------+
| role_is_member_of | +-------------------+ | true | +-------------------+` ``` 3. To check if the sales\_ro role is a member of the sales\_rw role, use the following example. ``` `SELECT role_is_member_of('sales_ro', 'sales_rw');` `+-------------------+ | role_is_member_of | +-------------------+ | false | +-------------------+` ``` To use the user\_is\_member\_of function 1. Connect to the database as the salesengineer user. 2. The following example attempts to check the user membership for the salesanalyst user. This query results in an error because salesengineer does not have access to salesanalyst. To run this command successfully, connect to the database as the salesanalyst user and use the example. ``` `SELECT user_is_member_of('salesanalyst', 'sales_ro');` `ERROR` ``` 3. Connect to the database as a superuser. 4. To check the membership of the salesanalyst user when connected as a superuser, use the following example. ``` `SELECT user_is_member_of('salesanalyst', 'sales_ro');` `+-------------------+
| user_is_member_of | +-------------------+ | true | +-------------------+` ``` 5. Connect to the database as the dbadmin user. 6. To check the membership of the salesengineer user, use the following example. ``` `SELECT user_is_member_of('salesengineer', 'sales_ro');` `+-------------------+ | user_is_member_of | +-------------------+ | true | +-------------------+` `SELECT user_is_member_of('salesengineer', 'marketing_ro');` `+-------------------+
| user_is_member_of | +-------------------+ | false | +-------------------+` `SELECT user_is_member_of('marketinganalyst', 'sales_ro');` `+-------------------+ | user_is_member_of | +-------------------+ | false | +-------------------+` ``` ## System views for RBAC (optional) To view the roles, the assignment of roles to users, the role hierarchy, and the privileges for database objects via roles, use the system views for Amazon Redshift. These views are available to superusers and regular users. Superusers can check all role details. Regular users can only check details for roles that they have been granted access to. 1. To view a list of users that are explicitly granted roles in the cluster, use the following example. ``` SELECT * FROM svv_user_grants; ``` 2. To view a list of roles that are explicitly granted roles in the cluster, use the following example. ``` SELECT * FROM svv_role_grants; ``` For the full list of system views, refer to [SVV metadata views](svv_views.md "svv_views.md"). ## Use row-level security with RBAC (optional) To have granular access control over your sensitive data, use row-level security (RLS). For more information about RLS, see [Row-level security](t_rls.md "t_rls.md"). In this section, you create a RLS policy that gives the `salesengineer` user permissions to only view rows in the `cat` table that have the `catdesc` value of Major League Baseball. You then query the database as the `salesengineer` user. 1. Connect to the database as the `salesengineer` user. 2. To view the first 5 entries in the `cat` table, use the following example. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+---------------------------------+
| catid | catgroup | catname | catdesc | +-------+----------+---------+---------------------------------+ | 1 | Sports | MLB | Major League Baseball |
| 2 | Sports | NHL | National Hockey League | | 3 | Sports | NFL | National Football League |
| 4 | Sports | NBA | National Basketball Association | | 5 | Sports | MLS | Major League Soccer | +-------+----------+---------+---------------------------------+` ``` 3. Connect to the database as the `dbadmin` user. 4. To create a RLS policy for the `catdesc` column in the `cat` table, use the following example. ``` `CREATE RLS POLICY policy_mlb_engineer WITH (catdesc VARCHAR(50)) USING (catdesc = 'Major League Baseball');` ``` 5. To attach the RLS policy to the `sales_rw` role, use the following example. ``` `ATTACH RLS POLICY policy_mlb_engineer ON sales.cat TO ROLE sales_rw;` ``` 6. To alter the table to turn on RLS, use the following example. ``` `ALTER TABLE sales.cat ROW LEVEL SECURITY ON;` ``` 7. Connect to the database as the `salesengineer` user. 8. To attempt to view the first 5 entries in the `cat` table, use the following example. Note that only entries only appear when the `catdesc` column is `Major League Baseball`. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+-----------------------+
| catid | catgroup | catname | catdesc | +-------+----------+---------+-----------------------+ | 1 | Sports | MLB | Major League Baseball | +-------+----------+---------+-----------------------+` ``` 9. Connect to the database as the `salesanalyst` user. 10. To attempt to view the first 5 entries in the `cat` table, use the following example. Note that no entries appear because the default deny all policy is applied. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+-----------------------+
| catid | catgroup | catname | catdesc | +-------+----------+---------+-----------------------+` ``` 11. Connect to the database as the `dbadmin` user. 12. To grant the IGNORE RLS permission to the `sales_ro` role, use the following example. This grants the `salesanalyst` user the permissions to ignore RLS policies since they are a member of the `sales_ro` role. ``` `GRANT IGNORE RLS TO ROLE sales_ro;` ``` 13. Connect to the database as the `salesanalyst` user. 14. To view the first 5 entries in the `cat` table, use the following example. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+---------------------------------+ | catid | catgroup | catname | catdesc | +-------+----------+---------+---------------------------------+
| 1 | Sports | MLB | Major League Baseball | | 2 | Sports | NHL | National Hockey League |
| 3 | Sports | NFL | National Football League | | 4 | Sports | NBA | National Basketball Association |
| 5 | Sports | MLS | Major League Soccer | +-------+----------+---------+---------------------------------+` ``` 15. Connect to the database as the `dbadmin` user. 16. To revoke the IGNORE RLS permission from the `sales_ro` role, use the following example. ``` `REVOKE IGNORE RLS FROM ROLE sales_ro;` ``` 17. Connect to the database as the `salesanalyst` user. 18. To attempt to view the first 5 entries in the `cat` table, use the following example. Note that no entries appear because the default deny all policy is applied. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+-----------------------+ | catid | catgroup | catname | catdesc | +-------+----------+---------+-----------------------+` ``` 19. Connect to the database as the `dbadmin` user. 20. To detach the RLS policy from the `cat` table, use the following example. ``` `DETACH RLS POLICY policy_mlb_engineer ON cat FROM ROLE sales_rw;` ``` 21. Connect to the database as the `salesanalyst` user. 22. To attempt to view the first 5 entries in the `cat` table, use the following example. Note that no entries appear because the default deny all policy is applied. ``` `SELECT * FROM sales.cat ORDER BY catid ASC LIMIT 5;` `+-------+----------+---------+---------------------------------+
| catid | catgroup | catname | catdesc | +-------+----------+---------+---------------------------------+ | 1 | Sports | MLB | Major League Baseball |
| 2 | Sports | NHL | National Hockey League | | 3 | Sports | NFL | National Football League |
| 4 | Sports | NBA | National Basketball Association | | 5 | Sports | MLS | Major League Soccer | +-------+----------+---------+---------------------------------+` ``` 23. Connect to the database as the `dbadmin` user. 24. To drop the RLS policy, use the following example. ``` `DROP RLS POLICY policy_mlb_engineer;` ``` 25. To remove RLS, use the following example. ``` `ALTER TABLE cat ROW LEVEL SECURITY OFF;` ``` ## Related topics For more information about RBAC, see the following documentation: <br>• [Role hierarchy](t_role_hierarchy.md "t_role_hierarchy.md") <br>• [Role assignment](t_role_assignment.md "t_role_assignment.md") <br>• [Database object permissions](r_roles-database-privileges.md "r_roles-database-privileges.md") <br>• [ALTER DEFAULT PRIVILEGES for RBAC](r_roles-alter-default-privileges.md "r_roles-alter-default-privileges.md")
````
