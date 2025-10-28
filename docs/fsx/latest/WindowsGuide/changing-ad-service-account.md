# Changing the Amazon FSx service account

If you update your file system with a new service account, the new service account
must have the required permissions and privileges to join your Active Directory and has
**Full control** permissions for the existing computer
objects associated with the file system.
In addition, make sure that new service account is part of the trusted accounts with
the enabled **Group Policy** setting **Domain controller: Allow computer
account re-use during domain join**.

We strongly recommend using an Active Directory group
to manage Active Directory permissions and configurations associated with service accounts.

When changing the service account for Amazon FSx, ensure that the service accounts have the following settings:

- The new service account (or the Active Directory group it is a member of) has **Full control** permissions for the
  existing computer objects associated with the file system.
- The new and previous service accounts (or the Active Directory group they are a member of) are part of
  the trusted accounts (or trusted Active Directory group) with the
  **Domain controller: Allow computer account re-use during domain join**
  Group Policy setting enabled on all domain controllers in the Active Directory.
  If the service accounts do not meet these requirements, the following conditions could occur:

- For Single-AZ file systems, the file system could become
  **[MISCONFIGURED_UNAVAILABLE](administering-file-systems.md#file-system-lifecycle-states "administering-file-systems.md#file-system-lifecycle-states")**.
- For Multi-AZ file systems, the file system could become
  **[MISCONFIGURED](administering-file-systems.md#file-system-lifecycle-states "administering-file-systems.md#file-system-lifecycle-states")** and
  the RemotePowerShell endpoint name might change.

## Configuring a domain controller's Group Policy

The following
[Microsoft recommended procedure](https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8#bkmk_take_action "https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8#bkmk_take_action") describes how to use the domain controller Group Policy to configure the allow
list policy.

###### To configure a domain controller's allow list policy

1. Install the September 12, 2023 or later Microsoft Windows updates on all member computers and domain controllers
   in your self-managed Microsoft Active Directory.
2. In a new or existing group policy that applies to all domain controllers in your self-managed Active Directory,
   configure the following settings.
   1. Navigate to **Computer Configuration>Policies>Windows Settings>Security Settings>
      Local Policies>Security Options**.
   2. Double-click **Domain controller: Allow computer account re-use during domain join**.
   3. Select **Define this policy setting and <Edit Security…>**.
   4. Use the object picker to add users or groups of trusted computer account creators and owners to the
      **Allow** permission.
      (As a best practice, we highly recommend that you use groups for permissions.)
      **Do not add the user account that performs the domain join.**

   ###### Warning

   Limit membership to the policy to trusted users and service accounts. Do not add authenticated users,
   everyone or other large groups to this policy. Instead, add specific trusted users and service accounts to groups
   and add those groups to the policy.

3. Wait for the Group Policy refresh interval or run **gpupdate /force** on all domain controllers.
4. Verify that the HKLM\System\CCS\Control\SAM – “ComputerAccountReuseAllowList” registry key is populated with the desired SDDL.
   **Do not manually edit the registry**.
5. Attempt to join a computer that has the September 12, 2023, or later updates installed. Ensure that one of the accounts
   listed in the policy owns the computer account. Also ensure that its registry does not have the
   **NetJoinLegacyAccountReuse** key enabled (set to 1). If the domain join fails, check the
   **`c:\windows\debug\netsetup.log`**.
