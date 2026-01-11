# Updating read

replicas with MariaDB

Read replicas are designed to support read queries, but you might need occasional updates.
For example, you might need to add an index to speed the specific types of queries
accessing the replica. You can enable updates by setting the `read_only`
parameter to **0** in the DB parameter group for the
read replica.
