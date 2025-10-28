# Enable application settings persistence for your

WorkSpaces Pools users

WorkSpaces Pools supports persistent application settings for Windows-based directories. This
means that your users' application customizations and Windows settings are automatically
saved after each streaming session and applied during the next session. Examples of
persistent application settings that your users can configure include, but are not limited
to, browser favorites, settings, webpage sessions, application connection profiles, plugins,
and UI customizations. These settings are saved to an Amazon Simple Storage Service (Amazon S3) bucket in your
account, within the AWS Region in which application settings persistence is enabled. They
are available in each WorkSpaces Pools streaming session.

###### Note

Standard Amazon S3 charges may apply to data that is stored in your S3 bucket. For more
information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Contents

- [How application settings
  persistence works](how-it-works-app-settings-persistence.md "how-it-works-app-settings-persistence.md")
- [Enabling application settings
  persistence](enabling-app-settings-persistence.md "enabling-app-settings-persistence.md")
- [Administer the VHDs for your users'
  application settings](administer-app-settings-vhds.md "administer-app-settings-vhds.md")
