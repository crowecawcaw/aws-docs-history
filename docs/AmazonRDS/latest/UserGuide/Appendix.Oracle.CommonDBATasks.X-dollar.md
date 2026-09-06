

# Managing RDS\_X$ views for Oracle DB instances
<a name="Appendix.Oracle.CommonDBATasks.X-dollar"></a>

You might need to access `SYS.X$` fixed tables, which are only accessible by `SYS`. To create `SYS.RDS_X$` views on eligible `X$` tables, use the procedures in the `rdsadmin.rdsadmin_util` package. Your master user is automatically granted the privilege `SELECT … WITH GRANT OPTION` on the `RDS_X$` views. 

The `rdsadmin.rdsadmin_util` procedures are available in the following cases:
+ Existing DB instances that have never been upgraded and use the following releases:
  + `21.0.0.0.ru-2023-10.rur-2023-10.r1` and higher 21c releases
  + `19.0.0.0.ru-2023-10.rur-2023-10.r1` and higher 19c releases
+ Any new DB instance that you create
+ Any existing DB instance that you have upgraded

**Important**  
Internally, the `rdsadmin.rdsadmin_util` package creates views on `X$` tables. The `X$` tables are internal system objects that aren’t described in the Oracle Database documentation. We recommend that you test specific views in your non-production database and only create views in your production database under the guidance of Oracle Support.

## List X$ fixed tables eligible for use in RDS\_X$ views
<a name="Appendix.Oracle.CommonDBATasks.list-allowed-X-dollar"></a>

To list X$ tables that are eligible for use in `RDS_X$` views, use the RDS procedure `rdsadmin.rdsadmin_util.list_allowed_sys_x$_views`. This procedure accepts no parameters. The following statements lists all eligible `X$` tables (sample output included).

```
SQL> SET SERVEROUTPUT ON
SQL> SELECT * FROM TABLE(rdsadmin.rdsadmin_util.list_allowed_sys_x$_views);

'X$BH'
'X$K2GTE'
'X$KCBWBPD'
'X$KCBWDS'
'X$KGLLK'
'X$KGLOB'
'X$KGLPN'
'X$KSLHOT'
'X$KSMSP'
'X$KSPPCV'
'X$KSPPI'
'X$KSPPSV'
'X$KSQEQ'
'X$KSQRS'
'X$KTUXE'
'X$KQRFP'
```

The list of eligible `X$` tables can change over time. To make sure that your list of eligible `X$` fixed tables is current, rerun `list_allowed_sys_x$_views` periodically.

## Creating SYS.RDS\_X$ views
<a name="Appendix.Oracle.CommonDBATasks.create-X-dollar"></a>

To create an `RDS_X$` view on an eligible `X$` table, use the RDS procedure `rdsadmin.rdsadmin_util.create_sys_x$_view`. You can only create views for the tables listed in the output of `rdsadmin.rdsadmin_util.list_allowed_sys_x$_views`. The `create_sys_x$_view` procedure accepts the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_x$_tbl` | varchar2 | Null | Yes | A valid `X$` table name. The value must be one of the `X$` tables reported by `list_allowed_sys_x$_views`. | 
| `p_force_creation` | Boolean | FALSE | No | A value indicating whether to force creation of an `RDS_X$` view that already exists for an `X$` table. By default, RDS won't create a view if it already exists. To force creation, set this parameter to `TRUE`. | 

The following example creates the `SYS.RDS_X$KGLOB` view on the table `X$KGLOB`. The format for the view name is `RDS_{{X$tablename}}`.

```
SQL> SET SERVEROUTPUT ON
SQL> EXEC rdsadmin.rdsadmin_util.create_sys_x$_view('X$KGLOB');

PL/SQL procedure successfully completed.
```

The following data dictionary query lists the view `SYS.RDS_X$KGLOB` and shows its status. Your master user is automatically granted the privilege `SELECT ... WITH GRANT OPTION` on this view.

```
SQL> SET SERVEROUTPUT ON
SQL> COL OWNER FORMAT A30 
SQL> COL OBJECT_NAME FORMAT A30
SQL> COL STATUS FORMAT A30
SQL> SET LINESIZE 200
SQL> SELECT OWNER, OBJECT_NAME, STATUS 
FROM DBA_OBJECTS 
WHERE OWNER = 'SYS' AND OBJECT_NAME = 'RDS_X$KGLOB';

OWNER                          OBJECT_NAME                    STATUS
------------------------------ ------------------------------ ------------------------------
SYS                            RDS_X$KGLOB                    VALID
```

**Important**  
`X$` tables aren't guaranteed to stay the same before and after an upgrade. RDS for Oracle drops and recreates the `RDS_X$` views on `X$` tables during an engine upgrade. Then it grants the `SELECT ... WITH GRANT OPTION` privilege to the master user. After an upgrade, grant privileges to database users as needed on the corresponding `RDS_X$` views.

## Listing SYS.RDS\_X$ views
<a name="Appendix.Oracle.CommonDBATasks.list-created-X-dollar"></a>

To list existing `RDS_X$` views, use the RDS procedure `rdsadmin.rdsadmin_util.list_created_sys_x$_views`. The procedure lists only views that were created by the procedure `create_sys_x$_view`. The following example lists `X$` tables that have corresponding `RDS_X$` views (sample output included).

```
SQL> SET SERVEROUTPUT ON
SQL> COL XD_TBL_NAME FORMAT A30
SQL> COL STATUS FORMAT A30
SQL> SET LINESIZE 200
SQL> SELECT * FROM TABLE(rdsadmin.rdsadmin_util.list_created_sys_x$_views);

XD_TBL_NAME                    STATUS
------------------------------ ------------------------------
X$BH                           VALID
X$K2GTE                        VALID
X$KCBWBPD                      VALID

3 rows selected.
```

## Dropping RDS\_X$ views
<a name="Appendix.Oracle.CommonDBATasks.drop-X-dollar"></a>

To drop a `SYS.RDS_X$` view, use the RDS procedure `rdsadmin.rdsadmin_util.drop_sys_x$_view`. You can only drop views listed in the output of `rdsadmin.rdsadmin_util.list_allowed_sys_x$_views`. The `drop_sys_x$_view` procedure accepts the following parameter.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_x$_tbl` | varchar2 | Null | Yes | A valid `X$` fixed table name. The value must be one of the `X$` fixed tables reported by `list_created_sys_x$_views`. | 

The following example drops the `RDS_X$KGLOB` view, which was created on the table `X$KGLOB`.

```
SQL> SET SERVEROUTPUT ON
SQL> EXEC rdsadmin.rdsadmin_util.drop_sys_x$_view('X$KGLOB');

PL/SQL procedure successfully completed.
```

The following example shows that the view `SYS.RDS_X$KGLOB` has been dropped (sample output included).

```
SQL> SET SERVEROUTPUT ON
SQL> COL OWNER FORMAT A30 
SQL> COL OBJECT_NAME FORMAT A30
SQL> COL STATUS FORMAT A30
SQL> SET LINESIZE 200
SQL> SELECT OWNER, OBJECT_NAME, STATUS 
FROM DBA_OBJECTS 
WHERE OWNER = 'SYS' AND OBJECT_NAME = 'RDS_X$KGLOB';

no rows selected
```