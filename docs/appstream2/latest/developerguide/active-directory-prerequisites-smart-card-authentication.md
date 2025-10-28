# Smart Card Authentication

AppStream 2.0 supports the use of Active Directory domain passwords or smart cards such as [Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card")
and [Personal Identity Verification (PIV)](https://piv.idmanagement.gov/ "https://piv.idmanagement.gov/")
smart cards for Windows sign in to AppStream 2.0 streaming instances. For information about how to configure your Active Directory environment to enable smart card sign in by using third-party certification authorities (CAs), see [Guidelines for enabling smart card logon with third-party certification authorities](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities "https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/enabling-smart-card-logon-third-party-certification-authorities") in the Microsoft documentation.

###### Note

AppStream 2.0 also supports the use of smart cards for in-session authentication after a user signs
in to a streaming instance. This feature is supported only for users who have
AppStream 2.0 client for Windows version 1.1.257 or later installed. For information
about additional requirements, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").
