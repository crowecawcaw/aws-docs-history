# Using pgAdmin to connect to a

RDS for PostgreSQL DB instance

You can use the open-source tool pgAdmin to connect to your RDS for PostgreSQL DB instance.
You can download and install pgAdmin from [http://www.pgadmin.org/](http://www.pgadmin.org/ "http://www.pgadmin.org/") without having a local instance of PostgreSQL on
your client computer.

###### To connect to your RDS for PostgreSQL DB instance using pgAdmin

1. Launch the pgAdmin application on your client computer.
2. On the **Dashboard** tab, choose **Add New
   Server**.
3. In the **Create - Server** dialog box, type a name on the
   **General** tab to identify the server in pgAdmin.
4. On the **Connection** tab, type the following information
   from your DB instance:
   - For **Host**, type the endpoint, for example
     `mypostgresql.c6c8dntfzzhgv0.us-east-2.rds.amazonaws.com`.
   - For **Port**, type the assigned port.
   - For **Username**, type the user name that you entered
     when you created the DB instance (if you changed the 'master
     username' from the default, `postgres`).
   - For **Password**, type the password that you entered
     when you created the DB instance.

![Type the password that you entered when creating the DB instance](images/Postgres-Connect01.png) 5. Choose **Save**.

If you have any problems connecting, see [Troubleshooting
connections to your RDS for PostgreSQL instance](USER_ConnectToPostgreSQLInstance.md "USER_ConnectToPostgreSQLInstance.md"). 6. To access a database in the pgAdmin browser, expand
**Servers**, the DB instance, and
**Databases**. Choose the DB instance's database
name.

![Choose the DB instance's database name in the pgAdmin browser](images/Postgres-Connect02.png) 7. To open a panel where you can enter SQL commands, choose
**Tools**, **Query Tool**.
