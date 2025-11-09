# Enable Your WorkSpaces Applications Users to Configure Their Regional

Settings

###### Note

Enabling users to configure regional settings is currently not supported in
Linux-based streaming sessions.

Users can configure their Amazon WorkSpaces Applications Windows streaming sessions to use settings that are
specific to their location or language. In particular, users can configure the following
settings:

- **Time zone** — Determines the system time used by Windows
  and any applications that rely on the operating system time. WorkSpaces Applications makes available
  the same options for this setting as the Windows Server version used in your
  fleet.
  - To sync the time zone for your streaming session to match the time zone
    set on your device, choose **Set my time zone automatically based on
    my device**. This is enabled by default for both single-session
    and multi-session fleets, and can be disabled.
  - For single-session fleets, you can choose a specific time zone for your
    streaming session instead of using automatic redirection. To set a custom
    time zone, disable the **Set my time zone automatically based on my
    device option** in **Regional settings**, and
    choose a preferred time zone from the available list.

- **Locale** (also known as culture) — Determines the
  conventions used by Windows and any applications that query the Windows culture when
  formatting dates, numbers, or currencies or when sorting strings. For a list of
  locales that WorkSpaces Applications supports, see [Supported Locales](supported-locales.md "supported-locales.md").
- **Input method** — Determines the keystroke combinations
  that can be used to input characters in another language.
  If users change regional settings during their streaming sessions, the changes are applied
  to any future streaming sessions in the same AWS Region.

###### Note

For guidance that you can provide your users to help them get started with configuring
their regional settings, see [Configure Regional Settings](regional-settings-end-user.md "regional-settings-end-user.md").

###### Contents

- [Supported Locales](supported-locales.md "supported-locales.md")
- [Enable Regional Settings for Your WorkSpaces Applications
  Users](regional-settings-enable.md "regional-settings-enable.md")
