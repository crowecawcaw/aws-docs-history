

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DROP MATERIALIZED VIEW
<a name="materialized-view-drop-sql-command"></a>

Removes a materialized view.

For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md).

## Syntax
<a name="mv_DROP_MATERIALIZED_VIEW-synopsis"></a>

```
DROP MATERIALIZED VIEW [ IF EXISTS ] mv_name [, ... ] [ CASCADE | RESTRICT ]
```

## Parameters
<a name="mv_DROP_MATERIALIZED_VIEW-parameters"></a>

IF EXISTS  
A clause that specifies to check if the named materialized view exists. If the materialized view doesn't exist, then the `DROP MATERIALIZED VIEW` command returns an error message. This clause is useful when scripting, to keep the script from failing if you drop a nonexistent materialized view.

*mv\_name*  
The name of the materialized view to be dropped.

CASCADE  
A clause that indicates to automatically drop objects that the materialized view depends on, such as other views.

RESTRICT  
A clause that indicates to not drop the materialized view if any objects depend on it. This is the default.

## Usage Notes
<a name="mv_DROP_MATERIALIZED_VIEW-usage"></a>

Only the owner of a materialized view can use `DROP MATERIALIZED VIEW` on that view. A superuser or a user who has specifically been granted DROP privileges can be exceptions to this.

When you write a drop statement for a materialized view and a view with a matching name exists, it results in an error that instructs you to use DROP VIEW. An error occurs even in a case where you use `DROP MATERIALIZED VIEW IF EXISTS`.

## Example
<a name="mv_DROP_MATERIALIZED_VIEW-examples"></a>

The following example drops the `tickets_mv` materialized view.

```
DROP MATERIALIZED VIEW tickets_mv;
```