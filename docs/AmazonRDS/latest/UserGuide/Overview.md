# Automated backups with unsupported MariaDB storage engines

For the MariaDB DB engine, automated backups are only supported with the InnoDB
storage engine. Using these features with other MariaDB storage engines, including Aria,
can lead to unreliable behavior when you're restoring from backups. Even though Aria is
a crash-resistant alternative to MyISAM, your tables can still be corrupted in the event
of a crash. For this reason, we encourage you to use the InnoDB storage engine.

- To convert existing Aria tables to InnoDB tables, you can use the `ALTER TABLE` command.
  For example: `ALTER TABLE `table_name`
ENGINE=innodb, ALGORITHM=COPY;`
- If you choose to use Aria, you can attempt to manually repair tables that become damaged
  after a crash by using the `REPAIR TABLE` command. For more information,
  see [http://mariadb.com/kb/en/mariadb/repair-table/](http://mariadb.com/kb/en/mariadb/repair-table/ "http://mariadb.com/kb/en/mariadb/repair-table/").
- If you want to take a snapshot of your Aria tables before restoring, follow these steps:
  1.  Stop all activity to your Aria tables (that is, close all sessions).
  2.  Lock and flush each of your Aria tables.
  3.  Create a snapshot of your DB instance or Multi-AZ DB cluster. When the snapshot has
      completed, release the locks and resume activity on the Aria tables.
      These steps force Aria to flush data stored in memory to disk, thereby
      ensuring a clean start when you restore from a DB snapshot.
