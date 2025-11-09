# RDS for PostgreSQL wait events

A _wait event_ is an indication that the session is waiting for
a resource. For example, the wait event `Client:ClientRead` occurs when
RDS for PostgreSQL is waiting to receive data from the client. Sessions typically wait
for resources such as the following.

- Single-threaded access to a buffer, for example, when a session is
  attempting to modify a buffer
- A row that is currently locked by another session
- A data file read
- A log file write
  For example, to satisfy a query, the session might perform a full table scan. If
  the data isn't already in memory, the session waits for the disk I/O to complete.
  When the buffers are read into memory, the session might need to wait because other
  sessions are accessing the same buffers. The database records the waits by using a
  predefined wait event. These events are grouped into categories.

By itself, a single wait event doesn't indicate a performance problem. For
example, if requested data isn't in memory, reading data from disk is necessary. If
one session locks a row for an update, another session waits for the row to be
unlocked so that it can update it. A commit requires waiting for the write to a log
file to complete. Waits are integral to the normal functioning of a database.

On the other hand, large numbers of wait events typically show a performance
problem. In such cases, you can use wait event data to determine where sessions are
spending time. For example, if a report that typically runs in minutes now takes
hours to run, you can identify the wait events that contribute the most to total
wait time. If you can determine the causes of the top wait events, you can sometimes
make changes that improve performance. For example, if your session is waiting on a
row that has been locked by another session, you can end the locking session.
