# Configure Default Regional Settings

for Your AppStream 2.0 Users

###### Note

The instructions on this page only apply to Windows fleets. Default regional settings
are not supported for Elastic fleets.

In AppStream 2.0, users in a Windows stack can configure their streaming sessions to use settings
that are specific to their location or language. For more information, see [Enable Your AppStream 2.0 Users to Configure Their Regional
Settings](regional-settings.md "regional-settings.md"). You can also configure
your fleets to use default settings that are specific to your users’ location or language.
In particular, you can apply the following Windows settings to your fleets:

- **Time Zone** — Determines the system time used by Windows
  and any applications that rely on the operating system time. AppStream 2.0 makes available
  the same options for this setting as Windows Server 2012 R2, Windows Server 2016,
  and Windows Server 2019.
- **Display Language** — Determines the display language
  used by the Windows operating system and certain Windows applications.
- **System Locale** — Determines the code pages (ANSI,
  MS-DOS, and Macintosh) and bitmap font files that Windows uses for non-Unicode
  applications in different languages.
- **User Locale** (also known as culture) — Determines the
  conventions used by Windows and any applications that query the Windows culture when
  formatting dates, numbers, or currencies or when sorting strings.
- **Input Method** — Determines the keystroke combinations
  that can be used to enter characters in another language.
  Currently, AppStream 2.0 supports English and Japanese only for these language settings.

###### Contents

- [Specify a Default Time Zone](configure-default-time-zone.md "configure-default-time-zone.md")
- [Specify a Default Display
  Language](configure-default-display-language.md "configure-default-display-language.md")
- [Specify a Default System
  Locale](configure-default-system-locale.md "configure-default-system-locale.md")
- [Specify a Default User Locale](configure-default-user-locale.md "configure-default-user-locale.md")
- [Specify a Default Input Method](configure-default-input-method.md "configure-default-input-method.md")
- [Special Considerations
  for Application Settings Persistence](special-considerations-app-settings-persistence.md "special-considerations-app-settings-persistence.md")
- [Special
  Considerations for Japanese Language Settings](special-considerations-japanese-language-settings.md "special-considerations-japanese-language-settings.md")
