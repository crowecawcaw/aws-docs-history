# Configuring settings and preferences in OpenSearch UI

With OpenSearch UI, you can configure settings for your entire organization, individual
workspaces, or just your personal preferences. These range from organization-wide
governance, performance, and feature settings to personal display preferences such as color
theme and time zone. A setting can be applied at more than one scope. An organization-wide
default can coexist with per-workspace defaults and personal, per-user preferences.

You manage these settings from the **Settings and setup** section of the
navigation, which provides an **Application settings** page (the full set of
settings), a **User settings** page, and a **Workspace
settings** page inside each workspace (each showing only a curated
subset).

###### Topics

- [Settings scopes and precedence](#application-settings-scopes "#application-settings-scopes")
- [Understanding where a setting value comes from](#application-settings-provenance "#application-settings-provenance")
- [Restricting who can change global settings](#application-settings-admin-control "#application-settings-admin-control")
- [Setting your personal preferences](#application-settings-user "#application-settings-user")
- [Managing workspace settings](#application-settings-workspace "#application-settings-workspace")

## Settings scopes and precedence

A setting can be defined at more than one scope. When OpenSearch UI resolves the
effective value of a setting, it uses the value from the most specific scope that defines
one. The following list shows the order of precedence, from lowest to highest:

1. **Application default** – The built-in
   default value that ships with OpenSearch UI. This value is used when no other
   scope defines the setting.
2. **Application (global)** – An
   organization-wide value set on the **Application settings**
   page. This value applies to you and all other users unless a more specific
   scope overrides it. By default, if you have permission to save objects, you can
   set this value. If you are an administrator, you can restrict this setting so
   that only administrators can change it. For more information, see [Restricting who can change global settings](#application-settings-admin-control "#application-settings-admin-control").
3. **Workspace** – A value set on the
   **Workspace settings** page that applies to everyone working
   inside that workspace.
4. **User** – A personal value that you set on
   the **User settings** page. This value applies only to you and
   takes precedence over all other scopes.

Because higher scopes override lower ones, the effective value resolves as
_User_ over _Workspace_ over
_Application_ over _Application default_. A
personal user value always wins for that user. A workspace value applies to workspace
members who have not set a personal value. The application value is the fallback for
everyone else.

## Understanding where a setting value comes from

On the **User settings** and **Workspace settings**
pages, each setting that can inherit a value from the application scope shows a badge.
The badge tells you the source of the current value:

- **Application** – This scope has no value of its own, so
  the setting is inheriting the value from the **Application
  settings** page. The control shows that inherited, effective
  value.
- **User value** (on the **User settings** page)
  or **Workspace value** (on the **Workspace
  settings** page) – This scope stores its own value, which
  overrides the application value. The control shows this scope's own value.

When a setting is inheriting the application value, you can override it by entering a
new value. When a setting shows a **User value** or **Workspace
value** badge, choose **Use Application value** to clear
your value and go back to inheriting the application value. After you do, the badge
changes back to **Application**.

###### Note

Choosing **Use Application value** returns the setting to the
inherited application value, not necessarily to the built-in default.

###### Note

Some settings on the **User settings** and **Workspace
settings** pages, such as Default workspace, do not show a badge. These
settings are available only at that single scope and have no corresponding
application value to inherit from.

## Restricting who can change global settings

By default, if you have permission to save objects, you can change global
(application) settings. The change applies to everyone in the application. As an
OpenSearch UI administrator, you can restrict global settings so that only
administrators can change them.

To do this, use the **Restrict global settings to admins** control in
the **Admin** section at the top of the **Application
settings** page. This control is visible and editable only to OpenSearch UI
administrators, and it behaves as follows:

- **Off (default)** – If you have permission
  to save objects, you can edit global settings. This is the existing
  behavior.
- **On** – Only OpenSearch UI administrators
  can edit global settings. If you don't have administrator access, you see global
  settings as read-only. You can still view the values and set your own personal
  preferences on the **User settings** page where a setting is
  available at the user scope.

## Setting your personal preferences

On the **User settings** page, you can set personal preferences that
apply only to your own experience in OpenSearch UI, without affecting other users. A
personal value overrides the application or workspace value for you only. Personal
preferences are limited to a curated set of appearance and display settings, such as the
following:

- **Dark mode** – Render the interface in dark mode. The
  setting takes effect after you refresh the page.
- **Timezone for date formatting** and **Day of
  week** – Control how dates are displayed for you.
- **Side nav style** and **Disable
  Animations** – Control navigation and animation display
  preferences.

###### To set your personal preferences

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home"), and then open your
   OpenSearch UI application.
2. In the navigation pane, under **Settings and setup**, choose
   **User settings**.
3. Locate the setting you want to change. The badge next to the setting indicates
   whether it is currently inheriting the **Application** value or
   using a **User value** that you set. For more information, see
   [Understanding where a setting value comes from](#application-settings-provenance "#application-settings-provenance").
4. Enter or select a new value. The value is saved for your user only and takes
   precedence over the application or workspace value.
5. (Optional) To stop using your personal value and go back to inheriting the
   application value, choose **Use Application value**.

###### Note

Some settings, such as **Dark mode**, take effect after you
refresh the page.

###### Note

If a setting does not appear on your **User settings** page, it is
not available as a personal preference and is managed at the application or workspace
scope instead.

## Managing workspace settings

On the **Workspace settings** page, as a workspace administrator, you
can set values that apply to everyone working inside a workspace, such as the
**Default Data Source** or **Default index** for
that workspace. A workspace value overrides the application value for members of the
workspace, but a member's personal user value still takes precedence for that
member.

To manage workspace settings, you must have the **Admin** access level
for the workspace. You can edit workspace settings only from within the workspace. For
more information about workspace access levels, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md "application-workspaces.md").

###### To manage workspace settings

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home"), and then open the
   OpenSearch UI application and the workspace that you administer.
2. In the navigation pane, choose **Manage workspace**, and then
   choose **Settings**.
3. Locate the setting you want to change, and then enter or select a new value.
   The value applies to all of the workspace members.
4. (Optional) To stop using the workspace value and go back to inheriting the
   application value, choose **Use Application value**.
