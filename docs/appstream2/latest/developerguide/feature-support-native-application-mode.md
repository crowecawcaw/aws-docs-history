# Native Application Mode

###### Note

Native application mode is not available when streaming from Linux
instances, streaming in Desktop mode, or when using the WorkSpaces Applications macOS client
application.

Native application mode provides a familiar experience for your users during
their WorkSpaces Applications streaming sessions. When your users connect to WorkSpaces Applications in this mode,
they can work with their remote streaming applications in much the same way that
they work with applications that are installed on their local computer. Each
streaming application in native application mode opens in its own window, and
application icons appear on the taskbar on your users' local PC.

If you want your users to connect to WorkSpaces Applications in classic mode only, you can
configure the `NativeAppModeDisabled` registry value to disable
native application mode. For more information, see [Choose Whether to Disable Native Application Mode](install-client-configure-settings.md#disable-native-application-mode-client "install-client-configure-settings.md#disable-native-application-mode-client").

For more information about native application mode and classic mode, and for
guidance that you can provide to your users, see [WorkSpaces Applications Client Connection Modes](client-application-windows-connection-modes-user.md "client-application-windows-connection-modes-user.md").

**Feature requirements**

To enable this feature for your users, you must use an image that uses a [version of the WorkSpaces Applications agent](agent-software-versions.md "agent-software-versions.md")
released on or after February 19, 2020. In addition, version 1.1.129 or later of
the WorkSpaces Applications client must be installed on your users' PCs. For more information
about client versions, see [WorkSpaces Applications Windows Client Release Notes](client-release-versions.md "client-release-versions.md").

If WorkSpaces Applications client version 1.1.129 or later is installed on your users'
computer, but you are not using an image that uses an agent version released on
or after February 19, 2020, the client falls back to classic mode even if native
application mode is selected.

**Testing requirements**

Applications must be tested thoroughly in native application mode before
production deployment. Testing in classic mode is not sufficient, because
applications might have compatibility issues with native application mode. Key
testing areas include the following:

- Core application functionality
- Network performance
- Local device interactions
- File handling operations
- Print capabilities
- Multi-monitor support
- Audio/video features
  We recommend starting with a pilot user group and documenting any
  application-specific limitations before full deployment. Application behavior
  and performance might vary between streaming modes. Comprehensive testing helps
  ensure optimal user experience and identifies any potential limitations before
  production rollout.

**Known Issues**

When users try to dock or undock tabs in one browser window into separate
windows during a streaming session in native application mode, their remote
streaming browser doesn't work the same way as a local browser. To perform this
task during a streaming session in native application mode, users must press the
Alt key until their browser tabs are docked into separate browser windows.
