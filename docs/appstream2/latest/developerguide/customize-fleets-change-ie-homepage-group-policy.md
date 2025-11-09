# Use Group Policy

to Change the Default Internet Explorer Home Page

In Active Directory environments, you use the Group Policy Management (GPMC)
MMC-snap-in to set a default home page that users can't change. If Active Directory
is not in your environment, you can use Local Group Policy Editor to perform this
task. To set a home page that users can change, you must use the GPMC.

To use the GPMC, do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the GPMC. For more information, see [Installing or Removing Remote Server Administration Tools for Windows
  7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with permissions to create GPOs. Link GPOs to the
  appropriate organizational units (OUs).

###### To change the default Internet Explorer home page by using a Group Policy

administrative template

You can use a Group Policy administrative template to set a default home page
that users can't change. For more information about administrative templates,
see [Edit Administrative Template Policy Settings](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771479(v=ws.11)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc771479(v=ws.11)") in the Microsoft
documentation.

1.  Open the WorkSpaces Applications console at
    [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2.  If you are not using Active Directory in your environment, open Local
    Group Policy Editor. If you are using Active Directory, open the GPMC.
    Locate the **Scripts (Logon\Logoff)** policy setting:
    - Local Group Policy Editor:

    On your image builder, open the command prompt as an
    administrator, type `gpedit.msc`, and then press ENTER.

    Under **User Configuration**, expand
    **Administrative Templates**, **Windows
    Components**, and then choose **Internet
    Explorer**.
    - GPMC:

    In your directory or on a domain controller, open the command
    prompt as an administrator, type `gpmc.msc`, and then
    press ENTER.

    In the left console tree, select the OU in which you want to
    create a new GPO, or use an existing GPO, and then do either of the
    following: :

        + Create a new GPO by opening the context (right-click) menu
         and choosing **Create a GPO in this domain, Link it
         here**. For **Name**, provide
         a descriptive name for this GPO.
        + Select an existing GPO.

    Open the context menu for the GPO, and choose
    **Edit**.

    Under **User Configuration**, expand
    **Policies**, **Administrative
    Templates**, **Windows Components**,
    and then choose **Internet Explorer**.

3.  Double-click **Disable changing home page settings**,
    choose **Enabled**, and in **Home Page**,
    enter a URL.
4.  Choose **Apply**, **OK**.
5.  Close Local Group Policy Editor or the GPMC.
