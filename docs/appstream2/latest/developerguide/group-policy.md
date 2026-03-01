# Using Group Policy preferences

You can use Group Policy preferences to grant local administrator rights to
Active Directory users or groups and to all computer objects in the specified
OU. The Active Directory users or groups to which you want to grant local
administrator permissions must already exist. To use Group Policy preferences,
you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Group Policy Management Console (GPMC) MMC snap-in. For more information,
  see [Installing or Removing Remote Server Administration Tools for
  Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with permissions to create Group Policy
  objects (GPOs). Link GPOs to the appropriate OUs.

###### To use Group Policy preferences to grant local administrator permissions

1. In your directory or on a domain controller, open the command prompt
   as an administrator, type `gpmc.msc`, and then press
   ENTER.
2. In the left console tree, select the OU where you will create a new GPO or use an existing
   GPO, and then do either of the following:
   - Create a new GPO by opening the context (right-click) menu and choosing **Create a GPO in this domain, Link it here**. For **Name**, provide a descriptive name for this
     GPO.
   - Select an existing GPO.

3. Open the context menu for the GPO, and choose
   **Edit**.
4. In the console tree, choose **Computer
   Configuration**, **Preferences**,
   **Windows Settings**, **Control Panel
   Settings**, and **Local Users and
   Groups**.
5. Select **Local Users and Groups** selected, open the
   context menu , and choose **New**, **Local
   Group**.
6. For **Action**, choose
   **Update**.
7. For **Group name**, choose **Administrators
   (built-in)**.
8. Under **Members**, choose **Add…**
   and specify the Active Directory users or groups to which to assign
   local administrator rights on the streaming instance. For
   **Action**, choose **Add to this
   group**, and choose **OK**.
9. To apply this GPO to other OUs, select the additional OU, open the
   context menu and choose **Link an Existing
   GPO**.
10. Using the new or existing GPO name that you specified in step 2,
    scroll to find the GPO, and then choose **OK**.
11. Repeat steps 9 and 10 for additional OUs that should have this
    preference.
12. Choose **OK** to close the **New Local Group
    Properties** dialog box.
13. Choose **OK** again to close the GPMC.
    To apply the new preference to the GPO, you must stop and restart any running
    image builders or fleets. The Active Directory users and groups that you
    specified in step 8 are automatically granted local administrator rights on the
    image builders and fleets in the OU to which the GPO is linked.
