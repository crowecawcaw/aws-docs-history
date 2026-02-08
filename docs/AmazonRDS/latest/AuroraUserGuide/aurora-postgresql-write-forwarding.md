# Aurora PostgreSQL 中的本地写入转发

*本地（集群内）写入转发*支持您的应用程序直接在 Aurora 副本上发出读/写事务。然后，写入命令转发到写入器数据库实例进行提交。对于偶尔写入且要求*先写后读一致性*（即能够读取事务中的最新写入内容）的应用程序，您可以使用本地写入转发。

如果没有写入转发，您的应用程序必须完全拆分所有读取和写入流量，保持两组数据库连接才能将流量发送到相应的端点。只读副本从写入器实例异步接收更新。此外，由于不同只读副本的复制滞后可能不同，因此很难在所有副本之间实现全局读取一致性。必须在写入器数据库实例上处理任何要求先写后读一致性的读取。或者，您需要开发复杂的自定义应用程序逻辑，以利用多个只读副本在确保一致性的同时实现可扩展性。

借助写入转发，您无需拆分这些事务或将它们专门发送到写入器实例。您也不必开发复杂的应用程序逻辑来实现*先写后读一致性*。

本地写入转发在提供 Aurora PostgreSQL 的每个区域均可用。以下 Aurora PostgreSQL 版本支持该特征：

- 16.4 及更高的 16 版本
- 15.8 及更高的 15 版本
- 14.13 及更高的 14 版本
  本地写入转发用于转发来自区域内副本的写入。要转发来自全局副本的写入，请参阅 [在 Amazon Aurora Global Database 中使用写入转发](aurora-global-database-write-forwarding.md "aurora-global-database-write-forwarding.md")。

###### 主题

- [Aurora PostgreSQL 中的本地写入转发的限制和注意事项](aurora-postgresql-write-forwarding-limitations.md "aurora-postgresql-write-forwarding-limitations.md")
- [配置 Aurora PostgreSQL 以进行本地写入转发](aurora-postgresql-write-forwarding-configuring.md "aurora-postgresql-write-forwarding-configuring.md")
- [在 Aurora PostgreSQL 中使用本地写入转发](aurora-postgresql-write-forwarding-understanding.md "aurora-postgresql-write-forwarding-understanding.md")
- [监控 Aurora PostgreSQL 中的本地写入转发](aurora-postgresql-write-forwarding-monitoring.md "aurora-postgresql-write-forwarding-monitoring.md")
