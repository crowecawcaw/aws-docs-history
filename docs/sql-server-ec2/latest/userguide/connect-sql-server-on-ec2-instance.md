# Connect to Microsoft SQL Server on Amazon EC2

You can connect to your Microsoft SQL Server instance using one of the
following tools.

###### Topics

- [SQL Server Management Studio
  (SSMS)](#connect-sql-server-on-ec2-instance-ssms "#connect-sql-server-on-ec2-instance-ssms")
- [SQL Server
  Configuration Manager](#connect-sql-server-on-ec2-instance-configuration-manager "#connect-sql-server-on-ec2-instance-configuration-manager")

## SQL Server Management Studio

(SSMS)

By default, only the built-in local administrator account can access a SQL Server instance
launched from an AWS Windows AMI. You can use SQL Server Management Studio (SSMS) to add domain
users so that they can access and manage SQL Server.

Perform the following steps to access a SQL Server instance on Amazon EC2 as a domain user.

1. [Connect to your
   instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") as a local administrator using Remote Desktop Protocol (RDP).
2. Open SQL Server Management Studio (SSMS).
3. For **Authentication**, choose **Windows
   Authentication** to log in with the built-in local
   administrator.
4. (Optional) Allow domain users to log in.
   1. Choose **Connect**.
   2. In Object Explorer, expand **Security**.
   3. Open the context menu (right-click) for **Logins**
      then select **New Login**.
   4. For **Login name**, select **Windows
      authentication**. Enter
      **Domain\username**, replacing
      **DomainName** with your domain NetBIOS name and
      **username** with your Active Directory user
      name.
   5. On the **Server roles** page, select the [server roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/server-level-roles?view=sql-server-2017") that you want to grant to the Active Directory
      user.
   6. Select the **General** page, and then choose
      **OK**.
   7. Log out from the instance and then log in again as a domain
      user.
   8. Open SSMS. For **Authentication**, choose
      **Windows authentication** to log in with your
      domain user account.
   9. Choose **Connect**.

## SQL Server

Configuration Manager

To connect to SQL Server using SQL Server Configuration Manager, see [SQL Server Configuration Manager](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-ver15") in the Microsoft documentation.
