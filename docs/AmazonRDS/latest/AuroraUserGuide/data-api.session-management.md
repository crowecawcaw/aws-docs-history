

# Session management with Amazon RDS Data API
<a name="data-api.session-management"></a>

RDS Data API maintains a pool of database connections and reuses them across calls to reduce connection overhead. Before reusing a connection, RDS Data API resets session state. The reset differs by database engine: on PostgreSQL, RDS Data API runs the `DISCARD ALL` statement to clear session state such as temporary tables, prepared statements, and session-level parameters; on MySQL, RDS Data API resets the connection (equivalent to `COM_RESET_CONNECTION`).

These resets cover session-level attributes that the engine owns, but state created by an extension is not guaranteed to be included. Extensions may not behave in the same manner as other session-level attributes when these cleanups are executed, and their state can persist on the database connection after the reset. Because RDS Data API reuses connections, state left behind by an extension is not limited to the call that created it and can still be present when a later call reuses the same connection.

`dblink` is one example of this behavior: `DISCARD ALL` does not close connections opened by the `dblink` extension, so a named `dblink` connection opened in one call can remain open when the connection is reused. Other extensions that hold resources outside the engine's session state can behave similarly.

If you use extensions with RDS Data API, do not rely on the session reset to release extension-owned state. Create and release that state within the same transaction, using the extension's own teardown function. For `dblink`, close each connection with `dblink_disconnect`.