# Connecting to your Amazon RDS for Db2 DB instance with DBeaver

You can use third-party tools such as DBeaver to connect to Amazon RDS for Db2 DB
instances. To download this utility, see [DBeaver Community](https://dbeaver.io/ "https://dbeaver.io/").

To connect to your RDS for Db2 DB instance, you need its DNS name and port number. For
information about finding them, see [Finding the endpoint](db2-finding-instance-endpoint.md "db2-finding-instance-endpoint.md"). You also need to know the
database name, master username, and master password that you defined when you created your
RDS for Db2 DB instance. For more information about finding them, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").

###### To connect to an RDS for Db2 DB instance with DBeaver

1. Start **DBeaver**.
2. Choose the **New Connection** icon in the toolbar and then choose
   **Db2 for LUW**.

![The menu that lists engine types in DBeaver.](images/dbeaver-add-connection.png) 3. In the **Connect to a database** window, provide information for
your RDS for Db2 DB instance.

    1. Enter the following information:




    	* For **Host**, enter the DNS name of the DB
    	 instance.
    	* For **Port**, enter the port number for the DB
    	 instance.
    	* For **Database**, enter the name of the
    	 database.
    	* For **Username**, enter the name of the database
    	 administrator for the DB instance.
    	* For **Password**, enter the password of the
    	 database administrator for the DB instance.
    2. Select **Save password**.
    3. Choose **Driver Settings**.

![The Connect to a database window with various connection settings populated in DBeaver.](images/dbeaver-connect-database.png) 4. In the **Edit Driver** window, specify additional security
properties.

    1. Choose the **Driver properties** tab.
    2. Add two **User Properties**.


    	1. Open the context (right-click) menu, and then choose **Add
    	 new property**.
    	2. For **Property Name**, add
    	 **encryptionAlgorithm**, and then choose
    	 **OK**.
    	3. With the **encryptionAlgorithm** row selected,
    	 choose the **Value** column and add
    	 **2**.
    	4. Open the context (right-click) menu, and then choose **Add
    	 new property**.
    	5. For **Property Name**, add
    	 **securityMechanism**, and then choose
    	 **OK**.
    	6. With the **securityMechanism** row selected,
    	 choose the **Value** column and add
    	 **7**.
    3. Choose **OK**.



    ![The Driver properties tab in the Edit Driver window in DBeaver.](images/dbeaver-driver-properties-tab.png)

5. In the **Connect to a database** window, choose **Test
   Connection**. If you don't have a DB2 JBDC driver installed on your
   computer, then the driver automatically downloads.
6. Choose **OK**.
7. Choose **Finish**.
8. In the **Database Navigation** tab, choose the name of the
   database. You can now explore objects.
   You are now ready to run SQL commands.

###### To run SQL commands and view the results

1. In the top menu, choose **SQL**. This opens a SQL script
   panel.
2. In the **Script** panel, enter a SQL command.
3. To run the command, choose the **Execute SQL query**
   button.
4. In the SQL results panel, view the results of your SQL queries.

![Window showing how to run a SQL command and view the results in DBeaver.](images/dbeaver-sql-run-example.png)
