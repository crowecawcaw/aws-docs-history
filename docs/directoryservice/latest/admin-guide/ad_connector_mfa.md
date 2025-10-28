# Enabling multi-factor authentication for AD Connector

You can enable multi-factor authentication for AD Connector when you have Active Directory
running on-premises or in Amazon EC2 instances. For more information about using multi-factor
authentication with AWS Directory Service, see [AD Connector prerequisites](ad_connector_getting_started.md#prereq_connector "ad_connector_getting_started.md#prereq_connector").

###### Note

Multi-factor authentication is not available for Simple AD. However, MFA can be enabled for
your AWS Managed Microsoft AD directory. For more information, see [Enabling multi-factor authentication for AWS Managed Microsoft AD](ms_ad_mfa.md "ms_ad_mfa.md").

###### To enable multi-factor authentication for AD Connector

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. Choose the directory ID link for your AD Connector directory.
3. On the **Directory details** page, select the **Networking & security** tab.
4. In the **Multi-factor authentication** section, choose **Actions**, and then choose **Enable**.
5. On the **Enable multi-factor authentication (MFA)** page, provide the following values:

**_Display label_**

Provide a label name.

**_RADIUS server DNS name or IP addresses_**

The IP addresses of your RADIUS server endpoints, or the IP address of
your RADIUS server load balancer. You can enter multiple IP addresses by
separating them with a comma (e.g.,
`192.0.0.0,192.0.0.12`).

###### Note

RADIUS MFA is applicable only to authenticate access to the AWS Management Console, or to Amazon Enterprise applications and services such as WorkSpaces, Amazon Quick Suite, or Amazon Chime. It does not provide MFA to Windows workloads running on EC2 instances, or for signing into an EC2 instance. AWS Directory Service does not support RADIUS Challenge/Response authentication.

Users must have their MFA code at the time they enter their username and password. Alternatively, you must use a solution that performs MFA out-of-band such as SMS text verification for the user. In out-of-band MFA solutions, you must make sure you set the RADIUS time-out value appropriately for your solution. When using an out-of-band MFA solution, the sign-in page will prompt the user for an MFA code. In this case, the best practice is for users to enter their password in both the password field and the MFA field.

**_Port_**

The port that your RADIUS server is using for communications. Your
on-premises network must allow inbound traffic over the default RADIUS
server port (UDP:1812) from the AWS Directory Service servers.

**_Shared secret code_**

The shared secret code that was specified when your RADIUS endpoints
were created.

**_Confirm shared secret code_**

Confirm the shared secret code for your RADIUS endpoints.

**_Protocol_**

Select the protocol that was specified when your RADIUS endpoints were
created.

**_Server timeout (in seconds)_**

The amount of time, in seconds, to wait for the RADIUS server to
respond. This must be a value between 1 and 50.

**_Max RADIUS request retries_**

The number of times that communication with the RADIUS server is
attempted. This must be a value between 0 and 10.

Multi-factor authentication is available when the **RADIUS
Status** changes to **Enabled**. 6. Choose **Enable**.
