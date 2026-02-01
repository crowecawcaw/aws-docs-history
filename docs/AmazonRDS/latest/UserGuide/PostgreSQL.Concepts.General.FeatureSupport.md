# Event

triggers for RDS for PostgreSQL

All current PostgreSQL versions support event triggers, and so do all available
versions of RDS for PostgreSQL. You can use the main user account (default,
`postgres`) to create, modify, rename, and delete event triggers.
Event triggers are at the DB instance level, so they can apply to all databases on
an instance.

For example, the following code creates an event trigger that prints the current
user at the end of every data definition language (DDL) command.

```
CREATE OR REPLACE FUNCTION raise_notice_func()
    RETURNS event_trigger
    LANGUAGE plpgsql AS
$$
BEGIN
    RAISE NOTICE 'In trigger function: %', current_user;
END;
$$;

CREATE EVENT TRIGGER event_trigger_1
    ON ddl_command_end
EXECUTE PROCEDURE raise_notice_func();
```

For more information about PostgreSQL event triggers, see [Event
triggers](https://www.postgresql.org/docs/current/static/event-triggers.html "https://www.postgresql.org/docs/current/static/event-triggers.html") in the PostgreSQL documentation.

There are several limitations to using PostgreSQL event triggers on Amazon RDS. These
include the following:

- You can't create event triggers on read replicas. You can, however, create
  event triggers on a read replica source. The event triggers are then copied
  to the read replica. The event triggers on the read replica don't fire
  on the read replica when changes are pushed from the source. However, if the
  read replica is promoted, the existing event triggers fire when database
  operations occur.
- To perform a major version upgrade to a PostgreSQL DB instance that uses
  event triggers, make sure to delete the event triggers before you upgrade
  the instance.
