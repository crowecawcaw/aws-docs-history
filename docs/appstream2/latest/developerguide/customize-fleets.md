# Customize an Amazon WorkSpaces Applications Fleet to Optimize Your Users' Application Streaming Experience

By customizing WorkSpaces Applications fleet instances, you can define specific aspects of your WorkSpaces Applications
environment to optimize your users' application streaming experience. For example, you can
persist environment variables to dynamically pass settings across applications and set
default file associations that are applied to all of your users. At a high level,
customizing a fleet instance includes the following tasks:

- Connecting to an image builder and customizing it as needed.
- On the image builder, using Image Assistant to create a new image that includes
  your customizations.
- Creating a new fleet instance or modifying an existing one. When you configure the
  fleet instance, select the new customized image that you created.
- Creating a new stack or modifying an existing one and associating it with your
  fleet instance.

###### Note

For certain fleet customizations, in Active Directory environments, you might need to
use the Group Policy Management Console (GPMC) to update Group Policy object (GPO)
settings on a domain-joined computer.

###### Contents

- [Persist Environment Variables in Amazon WorkSpaces Applications](customize-fleets-persist-environment-variables.md "customize-fleets-persist-environment-variables.md")
- [Set Default File Associations for Your Users in Amazon WorkSpaces Applications](customize-fleets-set-default-file-associations.md "customize-fleets-set-default-file-associations.md")
- [Disable Internet Explorer Enhanced Security Configuration in Amazon WorkSpaces Applications](customize-fleets-disable-ie-esc.md "customize-fleets-disable-ie-esc.md")
- [Change the Default Internet Explorer Home Page for Users' Streaming Sessions in Amazon WorkSpaces Applications](customize-fleets-change-ie-homepage.md "customize-fleets-change-ie-homepage.md")
- [User and Instance Metadata for Amazon WorkSpaces Applications Fleets](customize-fleets-user-instance-metadata-fleets.md "customize-fleets-user-instance-metadata-fleets.md")
  On Linux fleet instances, these environment variables are exported through the following
  profile.d scripts:

- **User environment variables** in
  /etc/profile.d/appstream_user_vars.sh
- **System environment variables** in
  /etc/profile.d/appstream_system_vars.sh
  To access the environment variables, you must explicitly source these files in your
  applications.
