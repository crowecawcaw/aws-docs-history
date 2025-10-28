# Using multiple monitors

###### Note

When collaborating on Amazon DCV sessions, the multiple monitor function is disabled.

Amazon DCV is capable of extending full screen resolution across a single monitor, a set of selected monitors, or all available monitors.

If the requested layout is not supported by the server, the layout might be adjusted to
match the display limits of your server. If the layout cannot be adjusted, the request fails
and the changes are not applied.

You can also manually specify custom display layouts. For more information, see [Managing the
Amazon DCV Session Display Layout](../adminguide/managing-session-display.md "../adminguide/managing-session-display.md") in the _Amazon DCV Administrator
Guide_.

Amazon DCV can configure a resolution according to the settings and the server system configuration.

- Web client resolution is limited by default to 1920x1080 (from web-client-max-head-resolution server setting).
- Native clients are limited by default to 4096x2160 (from max-head-resolution).

###### Note

Maximum supported per-monitor resolution is 4096x4096 for up to 4 monitors. Higher resolutions or more than 4 monitors are not supported in any configuration.

Make sure to follow the
[prerequisites guide](../adminguide/setting-up-installing.md "../adminguide/setting-up-installing.md") to properly
setup the system environment and drivers for best performance.

###### Topics

- [Extending full-screen across all monitors](full-screen-all-monitors.md "full-screen-all-monitors.md")
- [Extending full-screen across selected monitors](full-screen-selected-monitors.md "full-screen-selected-monitors.md")
- [Exiting full screen on multiple monitors](exiting-full-screen-multiple-monitors.md "exiting-full-screen-multiple-monitors.md")
