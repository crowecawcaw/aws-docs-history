# Automated backups with unsupported MySQL storage engines

For the MySQL DB engine, automated backups are only supported for the InnoDB storage
engine. Using these features with other MySQL storage engines, including MyISAM, can
lead to unreliable behavior when you're restoring from backups. Specifically, since
storage engines like MyISAM don't support reliable crash recovery, your tables can
be corrupted in the event of a crash. For this reason, we encourage you to use the
InnoDB storage engine.

- To convert existing MyISAM tables to InnoDB tables, you can use the `ALTER TABLE` command, for example: `ALTER TABLE
`table_name` ENGINE=innodb, ALGORITHM=COPY;`
- If you choose to use MyISAM, you can attempt to manually repair tables that become damaged
  after a crash by using the `REPAIR` command. For more information,
  see [REPAIR
  TABLE statement](https://dev.mysql.com/doc/refman/8.0/en/repair-table.html "https://dev.mysql.com/doc/refman/8.0/en/repair-table.html") in the MySQL documentation. However, as noted in the
  MySQL documentation, there is a good chance that you might not be able to
  recover all your data.
- If you want to take a snapshot of your MyISAM tables before restoring, follow these steps:

      1. Stop all activity to your MyISAM tables (that is, close all sessions).



      You can close all sessions by calling the [mysql.rds\_kill](Appendix.MySQL.md "Appendix.MySQL.md") command for each
       process that is returned from the `SHOW FULL PROCESSLIST` command.
      2. Lock and flush each of your MyISAM tables. For example, the following commands lock and
       flush two tables named `myisam_table1` and `myisam_table2`:




      ```
      mysql> FLUSH TABLES myisam_table, myisam_table2 WITH READ LOCK;
      ```
      3. Create a snapshot of your DB instance or Multi-AZ DB cluster. When the snapshot has
       completed, release the locks and resume activity on the MyISAM tables.
       You can release the locks on your tables using the following command:



      ```
      mysql> UNLOCK TABLES;
      ```

  These steps force MyISAM to flush data stored in memory to disk, which ensures a clean
  start when you restore from a DB snapshot. For more information on creating a DB
  snapshot, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").
