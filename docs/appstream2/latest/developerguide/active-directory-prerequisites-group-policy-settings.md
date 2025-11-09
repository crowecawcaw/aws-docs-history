# Group Policy Settings

Verify your configuration for the following Group Policy settings. If required, update the
settings as described in this section so that they don't block WorkSpaces Applications from
authenticating and logging in your domain users. Otherwise, when your users try
to log in to WorkSpaces Applications the login may not succeed. Instead, a message displays, notifying users that "An unknown
error occurred."

- \*\*Computer Configuration > Administrative Templates
  > Windows Components > Windows Logon Options > Disable or
  > Enable software Secure Attention Sequence** — Set this to **Enabled** for
  > **Services\*\*.
- \*\*Computer Configuration > Administrative Templates
  > System > Logon > Exclude credential providers\**
  > — Ensure that the following CLSID are *not\* listed:
  > `e7c1bab5-4b49-4e64-a966-8d99686f8c7c` and
  > `f148bAed-5f7f-40c9-8D48-51e24e571825`
- \*\*Computer Configuration > Policies
  > Windows Settings > Security Settings > Local Policies > Security Options > Interactive Logon > Interactive Logon: Message text for users attempting to log on** — Set this to **Not defined\*\*.
- \*\*Computer Configuration > Policies
  > Windows Settings > Security Settings > Local Policies > Security Options > Interactive Logon > Interactive Logon: Message title for users attempting to log on** — Set this to **Not defined\*\*.
- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > User Rights
  Assignment > Allow log on locally** — Set this to
  **Not defined** or add the domain user/group to this
  list.
- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > User Rights
  Assignment > Deny log on locally** — Set this to
  **Not defined** or make sure that domain users/groups
  are not included in the list.
  If you are using multi-session fleets, you also need the following Group Policy
  settings, in addition to the settings specified above.

- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > User Rights
  Assignment > Allow log on through Remote Desktop Services**
  — Set this to **Not defined** or add the domain
  user/group to this list.
- **Computer Configuration > Policies > Windows
  Settings > Security Settings > Local Policies > User Rights
  Assignment > Deny log on through Remote Desktop Services**
  — Set this to **Not defined** or make sure that
  domain users/groups are not included in the list.
