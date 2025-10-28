# Configuring in-session localization for Amazon WorkSpaces Secure Browser

When a user starts a session, WorkSpaces Secure Browser detects the user’s local browser language and time zone
settings and applies them to the session. This affects the display language during the session,
and helps ensure that the displayed time matches the current time in the user's location.

The session language is determined in the following priority order:

1. The **ForcedLanguages** policy in the web portal’s browser settings. For
   more information, see [ForcedLanguages](https://chromeenterprise.google/policies/#ForcedLanguages "https://chromeenterprise.google/policies/#ForcedLanguages").
2. The end user’s local browser language setting.
3. The default value, **English (en-US)**.
   The time zone is determined by the local time zone settings specified in the end user's
   browser. If the time zone setting isn't valid, UTC is used.

The following components in WorkSpaces Secure Browser support localization:

- WorkSpaces Secure Browser sign-in page
- WorkSpaces Secure Browser portal status messages (including loading messages and errors)
- Chrome browser
- System **Context** menu and **Save as** window

###### Topics

- [Supported language codes for Amazon WorkSpaces Secure Browser](language-codes.md "language-codes.md")
- [Selecting languages in user browser settings](local-browser-settings.md "local-browser-settings.md")
