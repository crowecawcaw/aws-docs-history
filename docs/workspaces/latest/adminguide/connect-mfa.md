# Multi-factor authentication (AD Connector) for WorkSpaces Personal

You can enable multi-factor authentication (MFA) for your AD Connector directory. For more
information about using multi-factor authentication with AWS Directory Service, see
[Enable multi-factor authentication for AD Connector](../../../directoryservice/latest/admin-guide/ad_connector_mfa.md "../../../directoryservice/latest/admin-guide/ad_connector_mfa.md") and [AD Connector prerequisites](../../../directoryservice/latest/admin-guide/prereq_connector.md "../../../directoryservice/latest/admin-guide/prereq_connector.md").

###### Note

- Your RADIUS server can either be hosted by AWS or it can be on-premises.
- The usernames must match between Active Directory and your RADIUS server.

###### To enable multi-factor authentication

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Directories**.
3. Select your directory and then choose **Actions**,
   **Update Details**.
4. Expand **Multi-Factor Authentication** and then select
   **Enable Multi-Factor Authentication**.
5. For **RADIUS server IP address(es)**, type the IP addresses
   of your RADIUS server endpoints separated by commas, or type the IP address of
   your RADIUS server load balancer.
6. For **Port**, type the port that your RADIUS server is using for
   communications. Your on-premises network must allow inbound traffic over the default
   RADIUS server port (UDP:1812) from AD Connector.
7. For **Shared secret code** and **Confirm shared secret code**,
   type the shared secret code for your RADIUS server.
8. For **Protocol**, choose the protocol for your RADIUS server.
9. For **Server timeout**, type the time, in seconds, to wait for the
   RADIUS server to respond. This value must be between 1 and 50.
10. For **Max retries**, type the number of times to attempt communication
    with the RADIUS server. This value must be between 0 and 10.
11. Choose **Update and Exit**.
    Multi-factor authentication is available when **RADIUS status** is
    **Enabled**. While multi-factor authentication is being set up, users cannot
    log in to their WorkSpaces.
