# Identify and resolve

aggressive vacuum blockers in Aurora PostgreSQL

In PostgreSQL, vacuuming is vital for ensuring database health as it reclaims storage and
prevents [transaction ID wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND") issues. However, there are times when vacuuming can be
prevented from operating as desired, which can result in performance degradation, storage bloat,
and even impact availability of your DB instance by transaction ID wraparound. Therefore, identifying
and resolving these issues are essential for optimal database performance and availability. Read
[Understanding autovacuum in Amazon RDS for PostgreSQL environments](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/ "https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/") to learn more
about autovacuum.

The `postgres_get_av_diag()` function helps identify issues that either prevent
or delay the aggressive vacuum progress. Suggestions are provided, which may include commands to
resolve the issue where it is identifiable or guidance for further diagnostics where the issue
is not identifiable. Aggressive vacuum blockers are reported when the age exceeds RDS' [adaptive
autovacuum](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming") threshold of 500 million transaction IDs.

**What is the age of the transaction ID?**

The `age()` function for transaction IDs calculates the number of transactions
that have occurred since the oldest unfrozen transaction ID for a database
(`pg_database.datfrozenxid`) or table (`pg_class.relfrozenxid`). This
value indicates database activity since the last aggressive vacuum operation and highlights the
likely workload for upcoming VACUUM processes.

**What is an aggressive vacuum?**

An aggressive VACUUM operation conducts a comprehensive scan of all pages within a table,
including those typically skipped during regular VACUUMs. This thorough scan aims to "freeze"
transaction IDs approaching their maximum age, effectively preventing a situation known as
[transaction ID wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND").

For `postgres_get_av_diag()` to report blockers, the blocker must be at least 500
million transactions old.

###### Topics

- [Installing autovacuum monitoring and diagnostic tools in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
- [Functions
  of postgres_get_av_diag() in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
- [Resolving identifiable vacuum blockers in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
- [Resolving unidentifiable vacuum blockers in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
- [Resolving vacuum performance issues in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
- [Explanation
  of the NOTICE messages in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")
