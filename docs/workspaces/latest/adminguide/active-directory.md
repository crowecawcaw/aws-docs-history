

# Using Active Directory with WorkSpaces Pools
<a name="active-directory"></a>

**Note**  
After careful consideration, we decided to end support for Amazon WorkSpaces Pools, effective December 31, 2027. Amazon WorkSpaces Pools will no longer accept new customers beginning July 31, 2026. As an existing customer, you can continue to use the service as normal until December 31, 2027. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](wsp-pools-end-of-support.md).

You can join your Windows WorkSpaces in WorkSpaces Pools to domains in Microsoft Active Directory and use your existing Active Directory domains, either cloud-based or on-premises, to launch domain-joined streaming instances. You can also use AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, to create an Active Directory domain and use that to support your WorkSpaces Pools resources. For more information about using AWS Managed Microsoft AD, see [Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) in the *AWS Directory Service Administration Guide*.

By joining WorkSpaces Pools to your Active Directory domain, you can:
+ Allow your users and applications to access Active Directory resources such as printers and file shares from streaming sessions.
+ Use Group Policy settings that are available in the Group Policy Management Console (GPMC) to define the end user experience.
+ Stream applications that require users to be authenticated using their Active Directory login credentials.
+ Apply your enterprise compliance and security policies to your WorkSpaces in WorkSpaces Pools.

**Topics**
+ [Overview of Active Directory Domains](active-directory-overview.md)
+ [Before You Begin Using Active Directory with WorkSpaces Pools](active-directory-prerequisites.md)
+ [Certificate-Based Authentication](pools-certificate-based-authentication.md)
+ [WorkSpaces Pools Active Directory Administration](active-directory-admin.md)
+ [More Info](active-directory-more-info.md)