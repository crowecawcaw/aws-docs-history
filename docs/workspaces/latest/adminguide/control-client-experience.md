# Control the WorkSpaces client experience for your users

Starting on August 25, 2026, Amazon WorkSpaces is introducing a new WorkSpaces Windows client with an
updated interface, designed to be easier to use, with a simplified connection flow,
easier-to-find settings and session tools, more helpful error messaging, and a new Session
Health feature.

The new experience (referred to as "new" in the rest of this document) will be included
in the client application installer package starting in version 5.34, and will install and
run alongside the current experience (referred to as "classic").

By default, your end users on the Amazon WorkSpaces Windows client will see an option to "Try
out" the new experience after they select a WorkSpace to connect to. If they click on this
option, they will see a confirmation dialog explaining what to expect, and if they
continue, the classic experience will close, and the new experience will open within a few
seconds. Likewise, in the new experience, they will see an option to "Switch back to
classic" at any time. While we highly encourage you to allow the default behavior, we're
introducing a Client Experience Policy feature in case you need to manage the rollout of
the new client experience for your end users.

As an administrator, using the Client Experience Policy, you can control which experience
your users see, and whether they can switch between the two. The policy is available now
— so you can decide how the new experience rolls out to your users and put the
behavior you want in place before the new client launches.

This topic explains the available policy values, how to set the policy through the WorkSpaces
API or through the Windows registry, and how the client resolves the policy when a user
connects.

###### Note

The classic experience is required to connect to PCoIP-based WorkSpaces and to WorkSpaces Pools,
and will continue to be supported in accordance with their respective end of support
notices ([PCoIP](workspaces-pcoip-end-of-support.md "workspaces-pcoip-end-of-support.md") and
[WorkSpaces Pools](wsp-pools-end-of-support.md "wsp-pools-end-of-support.md")).

## How the Client Experience Policy works

The Client Experience Policy determines which client experience a user sees when they
connect to a WorkSpace, and whether the option to switch experiences is available to
them.

You can set the policy at two levels:

- **[Option 1:
  Per directory, through the WorkSpaces API](#client-experience-policy-api "#client-experience-policy-api")**
  — Applies to all users who connect to WorkSpaces registered in that directory.
  Set this using the `ModifyClientProperties` API operation. This is
  the recommended method for most administrators because it does not require
  managing the client machine.
- **[Option 2:
  Per machine, through the Windows registry](#client-experience-policy-registry "#client-experience-policy-registry")**
  — Applies to all users on a specific Windows machine. Deploy this using
  Group Policy (GPO) or a configuration management tool such as SCCM. Use this
  method when you manage client devices centrally and want machine-level
  control.

If you take no action, the policy defaults to `USER_CHOICE`: your end
users using the Amazon WorkSpaces Windows client version 5.34 or higher will default to the
classic experience but can opt into the new experience themselves, by clicking on the
"Try out" option in the client.

## Policy values

The Client Experience Policy accepts the following values.

| Value           | Behavior                                                       | Can the user switch?                |
| --------------- | -------------------------------------------------------------- | ----------------------------------- |
| `FORCE_CLASSIC` | Users always see the classic experience.                       | No — the switch option is hidden.   |
| `FORCE_UI_2026` | Users always see the new experience.                           | No — the switch option is hidden.   |
| `USER_CHOICE`   | Users choose which experience to use and can switch<br>freely. | Yes — the switch option is visible. |

###### Important

If you have end users that need to connect to PCoIP-based WorkSpaces or to WorkSpaces Pools,
we recommend not using the `FORCE_UI_2026` option, as the new client
experience does not support these services. In this scenario, setting the value to
`USER_CHOICE` will allow your end users that are not on these services
to opt in to the new client experience, while your users on PCoIP and WorkSpaces Pools
will still have the ability to use the classic client experience.

## Policy resolution order

When a user selects a WorkSpace to connect to, the client resolves the effective
policy by checking each source in the following order. The first source that has a
value set wins and supersedes all lower-priority sources. If neither the API nor the
registry has a value set, the client applies the default `USER_CHOICE`
behavior.

1. **Centralized policy (WorkSpaces API)** — the
   per-directory policy you set with
   `ModifyClientProperties`.
2. **Local machine policy (HKLM registry)** —
   the per-machine policy you deploy through GPO or SCCM.
3. **User preference** — the experience the
   user last chose (only applies when the effective policy is
   `USER_CHOICE`, which is the default when no policy has been
   set).
4. **Client version default** — the
   experience hardcoded in the client build (see the following table).

| Client version   | Default experience | Supported experiences                       |
| ---------------- | ------------------ | ------------------------------------------- |
| 5.33 and earlier | Classic            | Classic only (New experience not supported) |
| 5.34 and later   | Classic            | Classic and new                             |

###### Note

Client versions 5.33 and earlier do not support the new experience and ignore the
policy. Users on those versions always see the classic experience.

## When the policy takes effect

The client applies the policy in the pre-session phase — after a user selects a
WorkSpace to connect to, but before they sign in. Switching experiences requires a
client restart. If the resolved experience differs from the one currently running, the
client will prompt the user to restart the client in order to proceed connecting to
their selected WorkSpace. The policy is not evaluated during an active session. If you
change a policy while a user is connected, the change takes effect the next time the
user starts the client or signs out and back in.

## Option 1: Set the policy through the WorkSpaces API

Use the [`ModifyClientProperties`](../api/API_ModifyClientProperties.md "../api/API_ModifyClientProperties.md")
API operation to set the policy for a directory. The
`ClientExperiencePolicy` field is part of the [`ClientProperties`](../api/API_ClientProperties.md "../api/API_ClientProperties.md")
object.

###### Note

At launch, this setting is available through the AWS CLI and SDKs only. WorkSpaces
console support is planned for a future update.

### AWS CLI example

The following command sets the policy for a directory to
`USER_CHOICE`, allowing users to choose their experience:

```
aws workspaces modify-client-properties \
    --resource-id d-1234567890 \
    --client-properties ClientExperiencePolicy=USER_CHOICE
```

To force all users in a directory to the new experience:

```
aws workspaces modify-client-properties \
    --resource-id d-1234567890 \
    --client-properties ClientExperiencePolicy=FORCE_UI_2026
```

### View the current policy

Use the `DescribeClientProperties` API operation to view the policy
currently set for a directory:

```
aws workspaces describe-client-properties \
    --resource-ids d-1234567890
```

The response includes the `ClientExperiencePolicy` field if a policy
has been set. If no policy has ever been set for the directory, the field is
omitted and the client falls back to the machine-level registry policy (if set) or
the default `USER_CHOICE` behavior.

```
{
    "ClientPropertiesList": [
        {
            "ResourceId": "d-1234567890",
            "ClientProperties": {
                "ReconnectEnabled": "ENABLED",
                "LogUploadEnabled": "ENABLED",
                "ClientExperiencePolicy": "USER_CHOICE"
            }
        }
    ]
}
```

###### Notes

- You cannot clear the `ClientExperiencePolicy` value after
  you set it. To restore the default behavior, set the value to
  `USER_CHOICE`.
- If you submit an unrecognized value, the API returns an
  `InvalidParameterValuesException`.

## Option 2: Set the policy through the Windows registry

If you manage client machines centrally, you can set a per-machine policy using the
following registry value. Deploy it through Group Policy or a configuration management
tool.

```
Path:  HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\Amazon WorkSpaces Client
Name:  ClientExperiencePolicy
Type:  REG_SZ
Value: FORCE_CLASSIC | FORCE_UI_2026 | USER_CHOICE
```

This registry path is consistent with other WorkSpaces client machine settings, such as
`clientUpgradeDisabled` and `WSUseDualStackIPv6`.

To set the value from an elevated command prompt, use the following command. This
example forces the new experience:

```
reg add "HKLM\SOFTWARE\Amazon\Amazon WorkSpaces Client" /v ClientExperiencePolicy /t REG_SZ /d FORCE_UI_2026 /f
```

To remove the value:

```
reg delete "HKLM\SOFTWARE\Amazon\Amazon WorkSpaces Client" /v ClientExperiencePolicy /f
```

The registry policy applies only when no per-directory API policy is set for the
directory the user connects to. A per-directory API policy always takes precedence over
the machine-level registry policy.

###### Important

Once a per-directory policy has been set through the API, it cannot be removed
and always takes precedence over the registry policy — including when it is
set to `USER_CHOICE`. If you rely on machine-level registry policies,
avoid setting the per-directory policy for those directories.

## What your users will experience

- **When you set `USER_CHOICE` (or take no
  action, since `USER_CHOICE` is the default):** Users see a
  link in the client that lets them switch
  between the classic and new experiences. Switching prompts them to restart the
  client before the newly chosen experience opens (within a few
  seconds).
- **When you set `FORCE_CLASSIC` or
  `FORCE_UI_2026`:** Users see the experience you selected,
  and the switch option is hidden. If a user switches to a WorkSpace in a
  directory with a different forced policy, the client prompts them to restart
  into the experience you have set via the Client Experience Policy.

## Plan your rollout

We recommend the following approach when adopting the new experience:

1. **Evaluate your end users' needs.** If you have
   end users that need to connect to PCoIP-based WorkSpaces or WorkSpaces Pools, consider how
   to incorporate that into your overall strategy.
2. **Decide your default posture.** Choose whether
   to let users opt in (`USER_CHOICE`), standardize on the new
   experience (`FORCE_UI_2026`), or hold on the classic experience
   during the transition (`FORCE_CLASSIC`).
3. **Ensure clients are current.** The policy is
   honored only by client versions 5.34 and later. Confirm your users are on a
   supported version before relying on the policy.
4. **Communicate with your users.** Let users know
   when the new experience will become available and whether they can
   switch.
5. **Make any necessary adjustments.** Once the new
   experience is available, conduct a more detailed evaluation, get feedback from
   your end users, and implement any posture changes if needed.

## Related topics

- [Modify client
  properties](../api/API_ModifyClientProperties.md "../api/API_ModifyClientProperties.md")
- [Describe client
  properties](../api/API_DescribeClientProperties.md "../api/API_DescribeClientProperties.md")
- [ClientProperties data
  type](../api/API_ClientProperties.md "../api/API_ClientProperties.md")
