# Using a webcam

With Amazon DCV, you can use a webcam connected to your local client computer in a remote
application that runs in a Amazon DCV session. For each session, only one connected client can use a
webcam at a time. This is especially important in environments where multiple clients connect
to the same session.

Webcam functionality is supported with all Amazon DCV clients. However, with the web browser
client, webcam functionality is only supported with Chromium-based browsers, such as Google
Chrome or Microsoft Edge. It isn't supported on Mozilla Firefox or Apple Safari.

Webcam functionality is supported on Windows Amazon DCV servers only. It's not supported on Linux
Amazon DCV servers.

You must be authorized to use this feature. If you are not authorized, the functionality is
not available in the client. For more information, see [Configuring Amazon DCV
Authorization](../adminguide/security-authorization.md "../adminguide/security-authorization.md") in the _Amazon DCV Administrator Guide_.

If you have multiple webcams connected to your local client computer, you can select the
webcam that you want to use. The selected camera is used automatically when the webcam is
enabled using the webcam toolbar icon.

###### Topics

- [Using a webcam on Windows, Linux and macOS clients](using-webcam-native.md "using-webcam-native.md")
- [Using a webcam on the web browser client](using-webcam-web.md "using-webcam-web.md")
