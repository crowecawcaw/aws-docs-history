# Tuning Aurora MySQL with wait events

The following table summarizes the Aurora MySQL wait events that most commonly indicate performance problems. The
following wait events are a subset of the list in [Aurora MySQL wait events](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").

| Wait event                                                                      | Description                                                                                                             |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [cpu](ams-waits.md "ams-waits.md")                                              | This event occurs when a thread is active in CPU or is waiting for CPU.                                                 |
| [io/aurora_redo_log_flush](ams-waits.md "ams-waits.md")                         | This event occurs when a session is writing persistent data to Aurora storage.                                          |
| [io/aurora_respond_to_client](ams-waits.md "ams-waits.md")                      | This event occurs when a thread is waiting to return a result set to a client.                                          |
| [io/redo_log_flush](ams-waits.md "ams-waits.md")                                | This event occurs when a session is writing persistent data to Aurora storage.                                          |
| [io/socket/sql/client_connection](ams-waits.md "ams-waits.md")                  | This event occurs when a thread is in the process of handling a new connection.                                         |
| [io/table/sql/handler](ams-waits.md "ams-waits.md")                             | This event occurs when work has been delegated to a storage engine.                                                     |
| [synch/cond/innodb/row_lock_wait](ams-waits.md "ams-waits.md")                  | This event occurs when one session has locked a row for an update, and another session tries to update the<br>same row. |
| [synch/cond/innodb/row_lock_wait_cond](ams-waits.md "ams-waits.md")             | This event occurs when one session has locked a row for an update, and another session tries to update the<br>same row. |
| [synch/cond/sql/MDL_context::COND_wait_status](ams-waits.md "ams-waits.md")     | This event occurs when there are threads waiting on a table metadata lock.                                              |
| [synch/mutex/innodb/aurora_lock_thread_slot_futex](ams-waits.md "ams-waits.md") | This event occurs when one session has locked a row for an update, and another session tries to update the<br>same row. |
| [synch/mutex/innodb/buf_pool_mutex](ams-waits.md "ams-waits.md")                | This event occurs when a thread has acquired a lock on the InnoDB buffer pool to access a page in<br>memory.            |
| [synch/mutex/innodb/fil_system_mutex](ams-waits.md "ams-waits.md")              | This event occurs when a session is waiting to access the tablespace memory cache.                                      |
| [synch/mutex/innodb/trx_sys_mutex](ams-waits.md "ams-waits.md")                 | This event occurs when there is high database activity with a large number of transactions.                             |
| [synch/sxlock/innodb/hash_table_locks](ams-waits.md "ams-waits.md")             | This event occurs when pages not found in the buffer pool must be read from a file.                                     |
| [synch/mutex/innodb/temp_pool_manager_mutex](ams-waits.md "ams-waits.md")       | This event occurs when a session is waiting to acquire a mutex for managing the pool of session temporary tablespaces.  |
