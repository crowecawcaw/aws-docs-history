Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP VIEW

Removes a view from the database. Multiple views can be dropped with a single DROP VIEW
command. This command isn't reversible.

## Required privileges

Following are required privileges for DROP VIEW:

- Superuser
- Users with the DROP VIEW privilege
- View owner

## Syntax

```
DROP VIEW [ IF EXISTS ] *name* [, ... ] [ CASCADE | RESTRICT ]
```

## Parameters

IF EXISTS

Clause that indicates that if the specified view doesn’t exist, the command
should make no changes and return a message that the view doesn't exist,
rather than terminating with an error.

This clause is useful when scripting, so the script doesn’t fail if DROP
VIEW runs against a nonexistent view.

_name_

Name of the view to be removed.

CASCADE

Clause that indicates to automatically drop objects that depend on the view,
such as other views.

To create a view that isn't dependent on other database objects, such
as views and tables, include the WITH NO SCHEMA BINDING clause in the view
definition. For more information, see [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md").

Note that if you include CASCADE and the count of database objects dropped
runs to ten or more, it's possible that your database client won't list all of
the dropped objects in the summary results. This is typically because SQL
client tools have default limitations on the results returned.

RESTRICT

Clause that indicates not to drop the view if any objects depend on it. This
action is the default.

## Examples

The following example drops the view called _event_:

```
drop view event;
```

To remove a view that has dependencies, use the CASCADE option. For example, say we
start with a table called EVENT. We then create the eventview view of the EVENT table,
using the CREATE VIEW command, as shown in the following example:

```
create view eventview as
select dateid, eventname, catid
from event where catid = 1;
```

Now, we create a second view called _myeventview_, that is based
on the first view _eventview_:

```
create view myeventview as
select eventname, catid
from eventview where eventname <> ' ';
```

At this point, two views have been created: _eventview_ and
_myeventview_.

The _myeventview_ view is a child view
with*eventview* as its parent.

To delete the _eventview_ view, the obvious command to use is the
following:

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

Both _eventview_ and _myeventview_ have now
been dropped successfully.

The following example either drops the _eventview_ view if it
exists, or does nothing and returns a message if it doesn't:

```
drop view if exists eventview;
```
