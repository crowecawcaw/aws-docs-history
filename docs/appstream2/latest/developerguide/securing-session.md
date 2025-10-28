# Securing an AppStream 2.0 Session

## Limiting application and operating system controls

AppStream 2.0 gives the administrator the ability to specify
exactly which applications can be launched from the web page in
application streaming mode. This does not, however, guarantee
that only those applications specified can be run.

Windows utilities and applications can be launched through the
operating system through additional means. AWS recommends using
[Microsoft AppLocker](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-microsoft-applocker-to-manage-application-experience-on-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-microsoft-applocker-to-manage-application-experience-on-amazon-appstream-2-0/") to ensure that only the applications
that your organization requires can be run. The default rules
must be modified, as they grant everyone path access to critical
system directories.

###### Note

Windows Server 2016 and 2019 require the Windows Application
Identity service to be running to enforce AppLocker rules. Application
access from AppStream 2.0 using Microsoft AppLocker is detailed in the [AppStream Admin Guide.](data-protection.md#application-access "data-protection.md#application-access")

For fleet instances joined to an Active Directory domain, use
Group Policy Objects (GPOs) to deliver user and system settings
to secure the users application and resource access.
