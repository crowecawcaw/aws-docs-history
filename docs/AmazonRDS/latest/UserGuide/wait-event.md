# LWLock:SubtransSLRU (LWLock:SubtransControlLock)

The `LWLock:SubtransSLRU` and `LWLock:SubtransBuffer` wait events
indicate that a session is waiting to access the simple least-recently used (SLRU) cache for
subtransaction information. This occurs when determining transaction visibility and
parent-child relationships.

- `LWLock:SubtransSLRU`: A process is waiting to access the simple
  least-recently used (SLRU) cache for a subtransaction. In RDS for PostgreSQL
  prior to version 13, this wait event is called `SubtransControlLock`.
- `LWLock:SubtransBuffer`: A process is waiting for I/O on a simple
  least-recently used (SLRU) buffer for a subtransaction. In RDS for PostgreSQL
  prior to version 13, this wait event is called `subtrans`.

###### Topics

- [Supported engine versions](#wait-event.lwlocksubtransslru.supported "#wait-event.lwlocksubtransslru.supported")
- [Context](#wait-event.lwlocksubtransslru.context "#wait-event.lwlocksubtransslru.context")
- [Likely causes of increased
  waits](#wait-event.lwlocksubtransslru.causes "#wait-event.lwlocksubtransslru.causes")
- [Actions](#wait-event.lwlocksubtransslru.actions "#wait-event.lwlocksubtransslru.actions")

## Supported engine versions

This wait event information is supported for all versions of RDS for PostgreSQL.

## Context

Understanding subtransactions – A subtransaction
is a transaction within a transaction in PostgreSQL. It's also known as a nested
transaction.

Subtransactions are typically created when you use:

- `SAVEPOINT` commands
- Exception blocks (`BEGIN/EXCEPTION/END`)

Subtransactions let you roll back parts of a transaction without affecting the entire
transaction. This gives you fine-grained control over transaction management.

Implementation details – PostgreSQL implements
subtransactions as nested structures within main transactions. Each subtransaction gets
its own transaction ID.

Key implementation aspects:

- Transaction IDs are tracked in `pg_xact`
- Parent-child relationships are stored in `pg_subtrans` subdirectory
  under `PGDATA`
- Each database session can maintain up to `64` active
  subtransactions
- Exceeding this limit causes subtransaction overflow, which requires accessing
  the simple least-recently used (SLRU) cache for subtransaction
  information

## Likely causes of increased

waits

Common causes of subtransaction SLRU contention include:

- Excessive use of SAVEPOINT and EXCEPTION
  handling – PL/pgSQL procedures with `EXCEPTION`
  handlers automatically create implicit savepoints, regardless of whether
  exceptions occur. Each `SAVEPOINT` initiates a new subtransaction.
  When a single transaction accumulates more than 64 subtransactions, it triggers
  a subtransaction SLRU overflow.
- Driver and ORM configurations –
  `SAVEPOINT` usage can be explicit in application code or implicit
  through driver configurations. Many commonly used ORM tools and application
  frameworks support nested transactions natively. Here are some common
  examples:
  - The JDBC driver parameter `autosave`, if set to
    `always` or `conservative`, generates
    savepoints before each query.
  - Spring Framework transaction definitions when set to
    `propagation_nested`.
  - Rails when `requires_new: true` is set.
  - SQLAlchemy when `session.begin_nested` is used.
  - Django when nested `atomic()` blocks are used.
  - GORM when `Savepoint` is used.
  - psqlODBC when rollback level setting is set to statement-level
    rollback (for example, `PROTOCOL=7.4-2`).

- High concurrent workloads with long-running transactions
  and subtransactions – When subtransaction SLRU overflow
  occurs during high concurrent workloads and long-running transactions and
  subtransactions, PostgreSQL experiences increased contention. This manifests as
  elevated wait events for `LWLock:SubtransBuffer` and
  `LWLock:SubtransSLRU` locks.

## Actions

We recommend different actions depending on the causes of your wait event. Some
actions provide immediate relief, while others require investigation and long-term
correction.

###### Topics

- [Monitoring
  subtransaction usage](#wait-event.lwlocksubtransslru.actions.monitor "#wait-event.lwlocksubtransslru.actions.monitor")
- [Configuring memory
  parameters](#wait-event.lwlocksubtransslru.actions.memory "#wait-event.lwlocksubtransslru.actions.memory")
- [Long-term
  actions](#wait-event.lwlocksubtransslru.actions.longterm "#wait-event.lwlocksubtransslru.actions.longterm")

### Monitoring

subtransaction usage

For PostgreSQL versions 16.1 and later, use the following query to monitor
subtransaction counts and overflow status per backend. This query joins backend
statistics with activity information to show which processes are using
subtransactions:

```

SELECT a.pid, usename, query, state, wait_event_type,
       wait_event, subxact_count, subxact_overflowed
FROM (SELECT id, pg_stat_get_backend_pid(id) pid, subxact_count, subxact_overflowed
      FROM pg_stat_get_backend_idset() id
           JOIN LATERAL pg_stat_get_backend_subxact(id) AS s ON true
     ) a
JOIN pg_stat_activity b ON a.pid = b.pid;

```

For PostgreSQL versions 13.3 and later, monitor the `pg_stat_slru` view
for subtransaction cache pressure. The following SQL query retrieves SLRU cache
statistics for the Subtrans component:

```

SELECT * FROM pg_stat_slru WHERE name = 'Subtrans';

```

A consistently increasing `blks_read` value indicates frequent disk
access for uncached subtransactions, signaling potential SLRU cache pressure.

### Configuring memory

parameters

For PostgreSQL 17.1 and later, you can configure the subtransaction SLRU cache
size using the `subtransaction_buffers` parameter. The following
configuration example shows how to set the subtransaction buffer parameter:

```

subtransaction_buffers = 128

```

This parameter specifies the amount of shared memory used to cache subtransaction
contents (`pg_subtrans`). When specified without units, the value
represents blocks of `BLCKSZ` bytes, typically 8KB each. For example,
setting the value to 128 allocates 1MB (128 \* 8kB) of memory for the subtransaction
cache.

###### Note

You can set this parameter at the cluster level so that all instances remain
consistent. Test and adjust the value to suit your specific workload
requirements and instance class. You must reboot the writer instance for
parameter changes to take effect.

### Long-term

actions

- Examine application code and configurations
  – Review your application code and database driver configurations for
  both explicit and implicit `SAVEPOINT` usage and subtransactions
  usage in general. Identify transactions potentially generating over 64
  subtransactions.
- Reduce savepoint usage – Minimize
  the use of savepoints in your transactions:
  - Review PL/pgSQL procedures and functions with EXCEPTION blocks.
    EXCEPTION blocks automatically create implicit savepoints, which can
    contribute to subtransaction overflow. Each EXCEPTION clause creates
    a subtransaction, regardless of whether an exception actually occurs
    during execution.

  Example 1: Problematic EXCEPTION block usage

  The following code example shows problematic EXCEPTION block
  usage that creates multiple subtransactions:

  ```
  CREATE OR REPLACE FUNCTION process_user_data()
  RETURNS void AS $$
  DECLARE
      user_record RECORD;
  BEGIN
      FOR user_record IN SELECT * FROM users LOOP
          BEGIN
              -- This creates a subtransaction for each iteration
              INSERT INTO user_audit (user_id, action, timestamp)
              VALUES (user_record.id, 'processed', NOW());

              UPDATE users
              SET last_processed = NOW()
              WHERE id = user_record.id;

          EXCEPTION
              WHEN unique_violation THEN
                  -- Handle duplicate audit entries
                  UPDATE user_audit
                  SET timestamp = NOW()
                  WHERE user_id = user_record.id AND action = 'processed';
          END;
      END LOOP;
  END;
  $$ LANGUAGE plpgsql;

  ```

  The following improved code example reduces subtransaction usage
  by using UPSERT instead of exception handling:

  ```

  CREATE OR REPLACE FUNCTION process_user_data()
  RETURNS void AS $$
  DECLARE
      user_record RECORD;
  BEGIN
      FOR user_record IN SELECT * FROM users LOOP
          -- Use UPSERT to avoid exception handling
          INSERT INTO user_audit (user_id, action, timestamp)
          VALUES (user_record.id, 'processed', NOW())
          ON CONFLICT (user_id, action)
          DO UPDATE SET timestamp = NOW();

          UPDATE users
          SET last_processed = NOW()
          WHERE id = user_record.id;
      END LOOP;
  END;
  $$ LANGUAGE plpgsql;

  ```

  Example 2: STRICT exception handler

  The following code example shows problematic EXCEPTION handling
  with NO_DATA_FOUND:

  ```

  CREATE OR REPLACE FUNCTION get_user_email(p_user_id INTEGER)
  RETURNS TEXT AS $$
  DECLARE
      user_email TEXT;
  BEGIN
      BEGIN
          -- STRICT causes an exception if no rows or multiple rows found
          SELECT email INTO STRICT user_email
          FROM users
          WHERE id = p_user_id;

          RETURN user_email;

      EXCEPTION
          WHEN NO_DATA_FOUND THEN
              RETURN 'Email not found';
      END;
  END;
  $$ LANGUAGE plpgsql;

  ```

  The following improved code example avoids subtransactions by
  using IF NOT FOUND instead of exception handling:

  ```

  CREATE OR REPLACE FUNCTION get_user_email(p_user_id INTEGER)
  RETURNS TEXT AS $$
  DECLARE
      user_email TEXT;
  BEGIN
       SELECT email INTO user_email
       FROM users
       WHERE id = p_user_id;

       IF NOT FOUND THEN
           RETURN 'Email not found';
       ELSE
           RETURN user_email;
       END IF;
  END;
  $$ LANGUAGE plpgsql;

  ```

  - JDBC driver – The `autosave` parameter, if set
    to `always` or `conservative`, generates
    savepoints before each query. Evaluate whether the
    `never` setting would be acceptable for your
    application.
  - PostgreSQL ODBC driver (psqlODBC) — The rollback level setting
    (for statement-level rollback) creates implicit savepoints to enable
    statement rollback functionality. Evaluate whether transaction-level
    or no rollback would be acceptable for your application.
  - Examine ORM transaction configurations
  - Consider alternative error handling strategies that don't require
    savepoints

- Optimize transaction design –
  Restructure transactions to avoid excessive nesting and reduce the
  likelihood of subtransaction overflow conditions.
- Reduce long-running transactions –
  Long-running transactions can exacerbate subtransaction issues by holding
  onto subtransaction information longer. Monitor Performance Insights metrics
  and configure the `idle_in_transaction_session_timeout` parameter
  to automatically terminate idle transactions.
- Monitor Performance Insights metrics – Track metrics including
  `idle_in_transaction_count` (number of sessions in idle in
  transaction state) and `idle_in_transaction_max_time` (duration
  of the longest running idle transaction) to detect long-running
  transactions.
- Configure `idle_in_transaction_session_timeout` – Set
  this parameter in your parameter group to automatically terminate idle
  transactions after a specified duration.
- Proactive monitoring – Monitor for high occurrences of
  `LWLock:SubtransBuffer` and `LWLock:SubtransSLRU`
  wait events to detect subtransaction-related contention before it becomes
  critical.
