# Set IP address restrictions and session timeouts

in Amazon Connect

###### Note

This feature is in preview release and subject to change. To obtain access to this
feature, contact your Amazon Connect Solutions Architect, Technical Account Manager, or
Support.

To further lock down your contact center, for example, to comply with requirements and
regulations in your industry, you can set up IP address restrictions and session timeouts.

- IP address restrictions require agents to sign in only from your VPN, or block
  access from specific countries or subnets.
- Session timeouts require agents to log in to Amazon Connect again.
  In Amazon Connect you configure an _authentication profile_ to set IP address
  restrictions and session durations of logged in agents. An authentication profile is a
  resource that stores the authentication settings for users in your contact center.

## Getting started with authentication profiles

Your Amazon Connect instance includes a default authentication profile. This authentication
profile applies to **all users** in your
contact center by default and does not need to be assigned.

Authentication profiles are currently only configurable with the AWS SDK. To configure your default authentication profile, use the following
commands.

###### Tip

You need your Amazon Connect instance ID to run these commands. For instructions about how
to locate your instance ID, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").

1. List the authentication profiles in your instance to get the profile ID of the
   authentication profile you want to update. You can call the [ListAuthenticationProfile](../APIReference/API_ListAuthenticationProfile.md "../APIReference/API_ListAuthenticationProfile.md") API or run the
   `list-authentication-profiles` CLI command.

Following is an example `list-authentication-profiles`
command:

```
aws connect list-authentication-profiles --instance-id `your-instance-id`
```

Following is an example of the default authentication profile that is returned
by the `list-authentication-profiles` command.

```
{
    "AuthenticationProfileSummaryList": [
        {
        "Arn": "arn:aws:connect:us-west-2:`account-id`:instance/`your-instance-id`/authentication-profile/`profile-id`",
        "Id": "`profile-id`",
        "IsDefault": true,
        "LastModifiedRegion": "us-west-2",
        "LastModifiedTime": 1.719249173664E9,
        "Name": "Default Authentication Profile"
        }
    ],
    "NextToken": null
}
```

2. View the configuration of the authentication profile you want to update. You
   can call the [DescribeAuthenticationProfile](../APIReference/API_DescribeAuthenticationProfile.md "../APIReference/API_DescribeAuthenticationProfile.md") or run the
   `describe-authentication-profile` CLI command.

Following is an example `describe-authentication-profile`
command:

```
aws connect describe-authentication-profile --instance-id `your-instance-id` --profile-id `profile-id`
```

Following is an example of the information returned by the
`describe-authentication-profile` command.

```
{
    "AuthenticationProfile": {
    "AllowedIps": [],
    "Arn": "arn:aws:connect:us-west-2:`account-id`:instance/`your-instance-id`/authentication-profile/`profile-id`",
    "BlockedIps": [],
    "CreatedTime": 1.718999177811E9,
    "Description": "A basic default Authentication Profile",
    "Id": "`profile-id`",
    "IsDefault": true,
    "LastModifiedRegion": "us-west-2",
    "LastModifiedTime": 1.719249173664E9,
    "MaxSessionDuration": 720,
    "Name": "Default Authentication Profile",
    "PeriodicSessionDuration": 60,
    "SessionInactivityDuration": 60,
    "SessionInactivityHandlingEnabled": false
    }
}
```

For a description of each field, see [AuthenticationProfile](../APIReference/API_AuthenticationProfile.md "../APIReference/API_AuthenticationProfile.md") in the _Amazon Connect API
Reference_. 3. Configure the authentication profile by using the [UpdateAuthenticationProfile](../APIReference/API_UpdateAuthenticationProfile.md "../APIReference/API_UpdateAuthenticationProfile.md") API or the
`update-authentication-profile` CLI command. All fields except
`InstanceId` and `ProfileId` are optional. Only the
settings you define in the API call are changed.

Following is an example `update-authentication-profile` command. It
configures the default authentication profile that's automatically assigned to
all users. It allows some IP addresses, blocks others, enables automatic logouts
on user inactivity, and sets the [session
inactivity duration](#configure-session-timeouts "#configure-session-timeouts") to 60 minutes.

```
aws connect update-authentication-profile
    --instance-id `your-instance-id`
    --profile-id `profile-id`
    --name "Default Authentication Profile"
    --description "A basic default Authentication Profile"
    --allowed-ips "ip-range-1" "ip-range-2" ...
    --blocked-ips "ip-range-3" "ip-range-4" ...
    --session-inactivity-handling-enabled
    --session-inactivity-duration 60
```

## Configure IP-based access control

If you want to configure access to your contact center based on IP addresses, you can
use the IP-based access control feature of your authentication profile.

There are two types of IP configurations that you can configure in an authentication
profile: allowed IP address ranges and blocked IP address ranges. The following points
describe how IP-based access control works.

- IP addresses can be in both IPV4 _and_ IPV6 formats.
- You can define both individual IP addresses _and_ IP
  address ranges in CIDR notation.
- Blocked IP configurations always take precedence.
- If IP addresses are defined in the Allowed IP list, _only_
  those IP addresses are allowed.
  - These IP addresses can be scoped down by the Blocked IP list.

- If only Blocked IP addresses are defined, any IP address can access the
  instance, _except_ those defined in the block list.
- If IP addresses are defined in both allowed and blocked IP address lists,
  _only_ the IP addresses defined in the allowed range are
  allowed, _minus_ any IP addresses in the blocked
  range.

###### Note

IP address based access control does not apply to the [emergency admin login](emergency-admin-login.md "emergency-admin-login.md"). To apply
restrictions on this user, you can [apply
`SourceIp` restrictions in your IAM policies](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") for the API
`connect:AdminGetEmergencyAccessToken`.

When a user's IP address is determined to be blocked by the instance, the user's
session will be invalidated. A logout event is published in the [Login/Logout report](login-logout-reports.md "login-logout-reports.md").

### What users experience when their IP address check

fails

**Agents**

When an agent is active in the Contact Control Panel (CCP), their IP address is
checked periodically.

Following is what happens if the IP address fails the check:

- If the agent is not on an active call, the agent is signed out if their IP
  address changes to a disallowed address.
- If the agent is on an active call, the agent's session is invalidated.
  However, this does not end the currently active call. Here's what
  happens:
  1.  The agent loses the ability to take any action, such as changing
      agent status, transferring calls, putting the call on hold, ending
      the call, or creating a case.
  2.  The agent is notified that their ability to take action in the CCP
      is restricted.
  3.  If they log in successfully after their session is invalidated,
      they are placed back into the active call and can take action
      again.

**Admins and users using the Amazon Connect admin website**

When the IP address check fails for admins and other users taking actions on the
Amazon Connect admin website, such as saving updates to resources or barging in to active calls, they are
automatically logged out.

## Example IP address configurations

### Example 1: IP addresses only defined in the allowed IP

list

- AllowedIps: [ `111.222.0.0/16` ]
- BlockedIps: [ ]

Outcome:

- Only IP addresses between `111.222.0.0` and
  `111.222.255.255` are allowed to access the instance.

### Example 2: IP addresses only defined in the blocked IP

list

- AllowedIps: [ ]
- BlockedIps: [`155.155.155.0/24` ]

Outcome:

- All IP addresses are allowed, _except_ the IP address
  range `155.155.155.0 - 155.155.155.255` inclusive.

### Example 3: IP addresses defined in both the allowed IP

list and the blocked IP list

- AllowedIps: [ `200.255.0.0/16` ]
- BlockedIps: [`200.255.10.0/24, 200.255.40.50, 192.123.211.211`
  ]

Outcome:

- IP addresses between `200.255.0.0 - 200.255.255.255` are
  allowed, minus `(200.255.10.0 - 200.255.10.255 AND
200.255.40.50)`.
- Effectively, `200.255.0.0 - 200.255.9.255, 200.255.11.0 -
200.255.40.49, 200.255.40.51 - 200.255.255.255` are
  allowed.
- `192.123.211.211` is effectively ignored since it is not within
  range of the Allowed range.

### Example 4: No IP addresses defined in either the

allowed IP list or the blocked IP list

- AllowedIps: [ ]
- BlockedIps: [ ]

In this case, there are no restrictions.

###### Important

The `allowedIps` list defines the range of possible IPs allowed in
your contact center only _if_ it is not empty. If it is
empty, _any_ IP address is allowed to access your contact
center unless explicitly blocked by the `blockedIps` list.

## Configure user session timeouts

An Amazon Connect session is defined as a continuous period of authenticated access to your
contact center’s website. There are two session timeouts that apply to user sessions in
your contact center:

- **Maximum session duration**: This value represents the
  maximum time period a contact center user can be logged in before being forced
  to sign-in again. This value defaults to 12 hours and isn't configurable.
- **Session inactivity duration:** : This value represents
  the period before an agent is automatically signed out of the contact center
  when they go inactive.

By default, users in your Amazon Connect instance remain signed in until the maximum
session duration of 12 hours elapses, with no automatic logout for inactivity. However,
organizations with stricter security and compliance requirements can leverage
authentication profiles to enable automatic sign-out when users become inactive. Once
enabled, this feature monitors user activity patterns and automatically ends
sessions after the configured session inactivity duration has passed.

A contact center user is considered active when performing any of the following actions:

- Mouse and keyboard activity on the Contact Control Panel (CCP), Agent Workspace, or Admin Website
- Presence of an active voice contact

If the user is determined to be inactive, a pop-up will appear on the screen
warning the user that their session is about to expire due to inactivity. A user can choose to remain logged in or log out.

To opt-in to automatic logout on user inactivity, perform the following API calls on an authentication profile in your instance using the Amazon Connect SDK.

```
aws connect update-authentication-profile
    --instance-id <your-instance-id>
    --profile-id <profile-id>
    --session-inactivity-handling-enabled
    --session-inactivity-duration <minutes between 15 and 720>
```

###### Note

Customers who integrate their contact center with a third-party vendor (such as
Salesforce Service Cloud Voice (SCV)) should refer to the vendor documentation to
determine if this feature is supported before enabling automatic log-outs on
inactivity.

###### Note

Customers who leverage AmazonConnectStreams or the AmazonConnectSDK to integrate their
existing web applications with Amazon Connect must implement activity handling as part
of their integration before enabling automatic log-out on user inactivity. See the
AmazonConnectStreams or AmazonConnectSDK documentation for more information.

###### Note

Automatic log-out on user inactivity is not supported when using Amazon Connect in a
[Virtual
Desktop Infrastructure (VDI) with a split CCP model](using-ccp-vdi.md#use-split-ccp "using-ccp-vdi.md#use-split-ccp").
