# Prompt users for MFA

You can use the following steps to determine how often workforce users are
prompted for multi-factor authentication (MFA) whenever they attempt to sign-in to
the AWS access portal. Before you begin, we recommend that you understand the [Available MFA types for IAM Identity Center](mfa-types.md "mfa-types.md").

###### Important

The instructions in this section apply to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"). They do
not apply to [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM).
IAM Identity Center users, groups, and user credentials are different from IAM users,
groups, and IAM user credentials. If you are looking for instructions on
deactivating MFA for IAM users, see [Deactivating MFA devices](../../../IAM/latest/UserGuide/id_credentials_mfa_disable.md "../../../IAM/latest/UserGuide/id_credentials_mfa_disable.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

If you’re using an external IdP, the **Multi-factor
authentication** section will not be available. Your external IdP
manages MFA settings, rather than IAM Identity Center managing them.

###### To configure MFA

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. In the left navigation pane, choose **Settings**.
3. On the **Settings** page, choose the
   **Authentication** tab.
4. In the **Multi-factor authentication** section, choose
   **Configure**.
5. On the **Configure multi-factor authentication** page,
   under **Prompt users for MFA**, choose one of the following
   authentication modes based on the level of security that your business
   needs:
   - **Every time they sign in
     (always-on)**

   In this mode (the default setting), IAM Identity Center requires that users with
   a registered MFA device will be prompted every time they sign in.
   This is the most secure setting and ensures that your organizational
   or compliance policies are enforced by requiring that MFA be used
   every time they sign in to the AWS access portal. For example, PCI DSS
   strongly recommends MFA during every sign-in to access applications
   that support high-risk payment transactions.
   - **Only when their sign-in context changes
     (context-aware)**

   In this mode, IAM Identity Center provides users the option to trust their
   device during sign-in. After a user indicates that they want to
   trust a device, IAM Identity Center prompts the user for MFA once and analyzes the
   sign-in context (such as device, browser, and location) for the
   user’s subsequent sign-ins. For subsequent sign-ins, IAM Identity Center
   determines if the user is signing in with a previously trusted
   context. If the user’s sign-in context changes, IAM Identity Center prompts the
   user for MFA in addition to their email address and password
   credentials.

   This mode provides ease of use for users who frequently sign in
   from their workplace but is less secure then the **always-on** option. Users are only prompted
   for MFA if their sign-in context changes.
   - **Never (disabled)**

   While in this mode, all users will sign in with their standard
   user name and password only. Choosing this option disables IAM Identity Center MFA
   and is not recommended.

   While MFA is disabled for your Identity Center directory for users,
   you cannot manage MFA devices in their user details, and Identity Center
   directory users cannot manage MFA devices from the AWS access portal.

   ###### Note

   If you are already using RADIUS MFA with Directory Service, and want to
   continue using it as your default MFA type, then you can leave
   the authentication mode as disabled to bypass MFA capabilities
   in IAM Identity Center. Changing from **Disabled** mode to
   **Context-aware** or
   **Always-on** mode will override the
   existing RADIUS MFA settings. For more information, see [RADIUS MFA](mfa-types.md#about-radius "mfa-types.md#about-radius").

6. Choose **Save changes**.

**Related Topics**

    * [Choose MFA types for user
     authentication](how-to-configure-mfa-types.md "how-to-configure-mfa-types.md")
    * [Configure MFA device
     enforcement](how-to-configure-mfa-device-enforcement.md "how-to-configure-mfa-device-enforcement.md")
    * [Allow users to register their own
     MFA devices](how-to-allow-user-registration.md "how-to-allow-user-registration.md")
