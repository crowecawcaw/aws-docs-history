# Finding the Organizational Unit Distinguished Name

When you register your Active Directory domain with WorkSpaces Applications, you must provide an
organizational unit (OU) distinguished name. Create an OU for this purpose. The
default Computers container is not an OU and cannot be used by WorkSpaces Applications. The following
procedure shows how to obtain this name.

###### Note

The distinguished name must start with `OU=` or
it cannot be used for computer objects.

Before you complete this procedure, you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Active Directory User and Computers MMC snap-in. For more
  information, see [Installing or Removing Remote Server Administration Tools for Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx")
  in the Microsoft documentation.
- Log in as a domain user with appropriate permissions to read the OU
  security properties.

###### To find the distinguished name of an OU

1. Open **Active Directory Users and Computers** in your
   domain or on your domain controller.
2. Under **View**, ensure that **Advanced Features** is enabled.
3. In the left navigation pane, select the first OU to use for WorkSpaces Applications
   streaming instance computer objects, open the context (right-click) menu,
   and then choose **Properties**.
4. Choose **Attribute Editor**.
5. Under **Attributes**, for **distinguishedName**, choose
   **View**.
6. For **Value**, select the distinguished name, open the
   context menu, and then choose **Copy**.
