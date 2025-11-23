# Enabling multi-factor authentication for AWS Managed Microsoft AD

You can enable multi-factor authentication (MFA) for your AWS Managed Microsoft AD directory to increase
security when your users specify their AD credentials to access Supported Amazon Enterprise
applications. When you enable MFA, your users enter their username and password (first factor)
as usual, and they must also enter an authentication code (the second factor) they obtain from
your virtual or hardware MFA solution. These factors together provide additional security by
preventing access to your Amazon Enterprise applications, unless users supply valid user
credentials and a valid MFA code.

To enable MFA, you must have an MFA solution that is a [Remote authentication dial-in user service](https://en.wikipedia.org/wiki/RADIUS "https://en.wikipedia.org/wiki/RADIUS")
(RADIUS) server, or you must have an MFA plugin to a RADIUS server already implemented in your
on-premises infrastructure. Your MFA solution should implement One Time Passcodes (OTP) that
users obtain from a hardware device or from software running on a device such as a cell
phone.

RADIUS is an industry-standard client/server protocol that provides authentication,
authorization, and accounting management to enable users to connect to network services.
AWS Managed Microsoft AD includes a RADIUS client that connects to the RADIUS server upon which you have
implemented your MFA solution. Your RADIUS server validates the username and OTP code. If your
RADIUS server successfully validates the user, AWS Managed Microsoft AD then authenticates the user against
Active Directory. Upon successful Active Directory authentication, users can then access the
AWS application. Communication between the AWS Managed Microsoft AD RADIUS client and your RADIUS server
require you to configure AWS security groups that enable communication over port 1812.

You can enable multi-factor authentication for your AWS Managed Microsoft AD directory by performing the
following procedure. For more information about how to configure your RADIUS server to work with
Directory Service and MFA, see [Multi-factor authentication prerequisites](ms_ad_getting_started.md#prereq_mfa_ad "ms_ad_getting_started.md#prereq_mfa_ad").

## Considerations

The following are some considerations for multi-factor authentication for your
AWS Managed Microsoft AD:

- Multi-factor authentication is not available for Simple AD. However, MFA can be
  enabled for your AD Connector directory. For more information, see [Enabling multi-factor authentication for AD Connector](ad_connector_mfa.md "ad_connector_mfa.md").
- MFA is a Regional feature of AWS Managed Microsoft AD. If you are using [Multi-Region replication](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"),
  you will only be able to use MFA in the Primary Region of your AWS Managed Microsoft AD.
- If you intend to use AWS Managed Microsoft AD for external communications, we recommend you
  configure a Network Address Translation (NAT) Internet Gateway or Internet Gateway outside
  of the AWS network for these communications.
  - If you wish to support external communications between your AWS Managed Microsoft AD and your
    RADIUS server hosted on the AWS network, please contact [Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

- All Amazon Enterprise IT applications including WorkSpaces, WorkDocs, Amazon WorkMail, Amazon Quick Suite, and
  access to AWS IAM Identity Center and AWS Management Console are supported when using AWS Managed Microsoft AD and AD Connector
  with MFA. These AWS applications using MFA are not supported in multi-regions.

For more information, see[How to enable multi-factor authentication for AWS services by using AWS Managed Microsoft AD and
on-premises credentials](https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/ "https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/").

    + For information about how to configure basic user access to Amazon Enterprise
     applications, AWS Single Sign-On and the AWS Management Console using Directory Service, see [Access to AWS applications and services
     from your AWS Managed Microsoft AD](ms_ad_manage_apps_services.md "ms_ad_manage_apps_services.md")
     and [Enabling AWS Management Console access with AWS Managed Microsoft AD
     credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md").
    + See the following this AWS Security Blog post to learn how to enable MFA for
     Amazon WorkSpaces users on your AWS Managed Microsoft AD, [How to enable multi-factor authentication for AWS services by using AWS Managed Microsoft AD
     and on-premises credentials](https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/ "https://aws.amazon.com/blogs/security/how-to-enable-multi-factor-authentication-for-amazon-workspaces-and-amazon-quicksight-by-using-microsoft-ad-and-on-premises-credentials/")

## Enable multi-factor authentication for

AWS Managed Microsoft AD

The following procedure shows you how to enable multi-factor authentication for
AWS Managed Microsoft AD.

1. Identify the IP address of your RADIUS MFA server and your AWS Managed Microsoft AD
   directory.
2. Edit your Virtual Private Cloud (VPC) security groups to enable communications over
   port 1812 between your AWS Managed Microsoft AD IP end points and your RADIUS MFA server.
3. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
4. Choose the directory ID link for your AWS Managed Microsoft AD directory.
5. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to enable MFA, and then
     choose the **Networking & security** tab. For more
     information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Networking &
     security** tab.

6. In the **Multi-factor authentication** section, choose
   **Actions**, and then choose **Enable**.
7. On the **Enable multi-factor authentication (MFA)** page, provide the
   following values:

**_Display label_**

Provide a label name.

**_RADIUS server DNS name or IP addresses_**

The IP addresses of your RADIUS server endpoints, or the IP address of your
RADIUS server load balancer. You can enter multiple IP addresses by separating them
with a comma (e.g., `192.0.0.0,192.0.0.12`).

###### Note

RADIUS MFA is applicable only to authenticate access to the AWS Management Console, or to
Amazon Enterprise applications and services such as WorkSpaces, Amazon Quick Suite, or Amazon Chime.
Amazon Enterprise applications and services are only supported in the Primary
Region if Multi-Region replication is configured for your AWS Managed Microsoft AD. It does
not provide MFA to Windows workloads running on EC2 instances, or for signing into
an EC2 instance. Directory Service does not support RADIUS Challenge/Response
authentication.

Users must have their MFA code at the time they enter their user name and
password. Alternatively, you must use a solution that performs MFA out-of-band
such as push notification or authenticator one-time passwords (OTP) for the user.
In out-of-band MFA solutions, you must make sure you set the RADIUS time-out value
appropriately for your solution. When using an out-of-band MFA solution, the
sign-in page will prompt the user for an MFA code. In this case, users must enter
their password in both the password field and the MFA field.

**_Port_**

The port that your RADIUS server is using for communications. Your on-premises
network must allow inbound traffic over the default RADIUS server port (UDP:1812)
from the Directory Service servers.

**_Shared secret code_**

The shared secret code that was specified when your RADIUS endpoints were
created.

**_Confirm shared secret code_**

Confirm the shared secret code for your RADIUS endpoints.

**_Protocol_**

Select the protocol that was specified when your RADIUS endpoints were
created.

**_Server timeout (in seconds)_**

The amount of time, in seconds, to wait for the RADIUS server to respond. This
must be a value between 1 and 50.

###### Note

We recommend configuring your RADIUS server timeout to 20 seconds or less. If
the timeout exceeds 20 seconds, the system cannot retry with another RADIUS server
and may result in a timeout failure.

**_Max RADIUS request retries_**

The number of times that communication with the RADIUS server is attempted. This
must be a value between 0 and 10.

Multi-factor authentication is available when the **RADIUS Status**
changes to **Enabled**. 8. Choose **Enable**.
