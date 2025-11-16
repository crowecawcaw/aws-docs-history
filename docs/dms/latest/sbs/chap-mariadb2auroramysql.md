# Test the endpoints for MariaDB database migration

1. On the navigation pane, choose **Endpoints**.
2. Choose the source endpoint name (`maria-on-prem`) and do the following:
   1. Choose **Test connections**.
   2. Choose the replication instance to test (`mariadb-mysql`).
   3. Choose **Run Test** and wait for the status to be **successful**.

3. On the navigation pane, choose **Endpoints**.
4. Choose the target endpoint name (`mysqltrg-rds`) and do the following:
   1. Choose **Test Connections**.
   2. Choose the replication instance to test (`mariadb-mysql`).
   3. Choose **Run Test** and wait for the status to be **successful**.

###### Note

If **Run Test** returns a status other than **successful**, the reason for the failure is displayed. Make sure that you resolve the issue before proceeding further.
