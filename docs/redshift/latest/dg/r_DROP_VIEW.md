

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DROP VIEW
<a name="r_DROP_VIEW"></a>

Removes a view from the database. Multiple views can be dropped with a single DROP VIEW command. This command isn't reversible.

## Required privileges
<a name="r_DROP_VIEW-privileges"></a>

Following are required privileges for DROP VIEW:
+ Superuser
+ Users with the DROP VIEW privilege
+ View owner

## Syntax
<a name="r_DROP_VIEW-synopsis"></a>

```
DROP VIEW [ IF EXISTS ] name [, ... ] [ CASCADE | RESTRICT ] 
```

## Parameters
<a name="r_DROP_VIEW-parameters"></a>

IF EXISTS  
Clause that indicates that if the specified view doesn’t exist, the command should make no changes and return a message that the view doesn't exist, rather than terminating with an error.  
This clause is useful when scripting, so the script doesn’t fail if DROP VIEW runs against a nonexistent view.

 *name*   
Name of the view to be removed.

CASCADE  
Clause that indicates to automatically drop objects that depend on the view, such as other views.  
To create a view that isn't dependent on other database objects, such as views and tables, include the WITH NO SCHEMA BINDING clause in the view definition. For more information, see [CREATE VIEW](r_CREATE_VIEW.md).  
Note that if you include CASCADE and the count of database objects dropped runs to ten or more, it's possible that your database client won't list all of the dropped objects in the summary results. This is typically because SQL client tools have default limitations on the results returned.

RESTRICT  
Clause that indicates not to drop the view if any objects depend on it. This action is the default.

## Examples
<a name="r_DROP_VIEW-examples"></a>

The following example drops the view called *event*:

```
drop view event;
```

To remove a view that has dependencies, use the CASCADE option. For example, suppose you start with a table called EVENT. You then create the eventview view of the EVENT table by using the CREATE VIEW command, as shown in the following example: 

```
create view eventview as
select dateid, eventname, catid
from event where catid = 1;
```

Now, you create a second view called *myeventview* that is based on the first view *eventview*:

```
create view myeventview as
select eventname, catid
from eventview where eventname <> ' ';
```

At this point, two views have been created: *eventview* and *myeventview*.

The *myeventview* view is a child view with*eventview* as its parent.

To delete the *eventview* view, the obvious command to use is the following: 

```
drop view eventview;
```

Notice that if you run this command in this case, you get the following error:

```
drop view eventview;
ERROR: can't drop view eventview because other objects depend on it
HINT: Use DROP ... CASCADE to drop the dependent objects too.
```

To remedy this, run the following command (as suggested in the error message): 

```
drop view eventview cascade;
```

Both *eventview* and *myeventview* have now been dropped successfully.

The following example either drops the *eventview* view if it exists, or does nothing and returns a message if it doesn't:

```
drop view if exists eventview;
```