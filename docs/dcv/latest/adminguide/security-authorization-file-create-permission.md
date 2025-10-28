# Adding permissions

The `[permissions]` section of the permissions file lets you control user and group access to specific features or
aliases.

To add permissions to your permissions file, first add the permissions section heading to the file.

```
[permissions]
```

You can then add your permissions under the section heading. To add a permission, specify the actor that it governs, the rule to be applied,
and the features that it applies to.

```
`actor rule features`
```

The actor can be a user, a group, or an operating system group. Groups must be prefixed with `group:`. Operating system groups
must be prefixed with `osgroup:`. Amazon DCV includes a built-in `%owner%` reference that can be used to refer to the session
owner. It can also be used to refer to a built-in `%any%` reference that can be used to refer to any user.

The following rules can be used in permissions statements:

- `allow` — Grants access to the feature.
- `disallow` — Denies access to the feature, but can be overridden by subsequent permissions.
- `deny` — Denies access to the feature and cannot be overridden by subsequent permissions.
  The features can include individual Amazon DCV features, aliases, or a combination of both. The list of features must be separated by a space.
  Amazon DCV includes a built-in `builtin` alias that includes all of the Amazon DCV features.

The following features can be referenced in the permissions file:

- `audio-in` — Insert audio from the client to the Amazon DCV server.
- `audio-out` — Play back Amazon DCV server audio on the client.
- `builtin` — All features.
- `clipboard-copy` — Copy data from the Amazon DCV server to the client clipboard.
- `clipboard-paste` — Paste data from the client clipboard to the Amazon DCV server.
- `display` — Receive visual data from the Amazon DCV server.
- `extensions-client` — Allows to start the installed extensions on the Amazon DCV client.
- `extensions-server` — Allows to start the installed extensions on the Amazon DCV server.
- `file-download` — Download files from the session storage.
- `file-upload` — Upload files to the session storage.
- `gamepad` — Use gamepads connected to a client computer in a session. Supported on version Amazon DCV 2022.0 and
  later.
- `keyboard` — Input from the client keyboard to the Amazon DCV server.
- `keyboard-sas` — Use the secure attention sequence (**CTRL+Alt+Del**). Requires the
  `keyboard` feature. Supported on version Amazon DCV 2017.3 and later.
- `mouse` — Input from the client pointer to the Amazon DCV server.
- `pointer` — View Amazon DCV server mouse position events and pointer shapes. Supported on version Amazon DCV 2017.3 and later.
- `printer` — Create PDFs or XPS files from the Amazon DCV server to the client.
- `screenshot` — Save a screenshot of the remote desktop. It's supported on version Amazon DCV 2021.2 and later.

When removing `screenshot` authorization, we recommended that you disable the `clipboard-copy` permission. This
prevents users from capturing screenshots on the clipboard of the server and then pasting them on the client. When the `screenshot`
authorization is denied, Windows and macOS will also prevent external tools from capturing a screenshot of the client. For example, using the
Windows Snipping Tool on the Amazon DCV client window will result in a black image.

- `smartcard` — Read the smart card from the client.
- `stylus` — Input from specialized USB devices, such as 3D pointing devices or graphic tablets.
- `touch` — Use native touch events. Supported on version DCV 2017.3 and later.
- `unsupervised-access` — Use to set owner-less access of users in a
  collaborative session.
- `usb` — Use USB devices from the client.
- `webcam` — Use the webcam connected to a client computer in a session. Supported on version Amazon DCV 2021.0 and
  later.
- `webauthn-redirection` — Redirect Webauthn requests from the remote browser to a local client. Supported on version Amazon DCV 2023.1 and
  later.

###### Example

The following example adds the permissions section heading and adds four permissions. The first permission grants a user named
`john` access to the `display`, `file-upload`, and `file-download` features. The second permission
denies the `observers` group access to the `audio-in` and `audio-out` features, and the
`clipboard-management` feature alias. The third permission grants the `guests` operating system group access to the
`clipboard-management` and `file-management` aliases. The fourth permission grants the session owner access to all
features.

```
[permissions]
john allow display file-upload file-download
group:observers deny audio-in audio-out clipboard-management
osgroup:guests allow clipboard-management file-management
%owner% allow builtin

```
