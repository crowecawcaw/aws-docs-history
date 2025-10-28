# Troubleshooting

If issues occur when you use AppStream 2.0, your AppStream 2.0 session ID can help your administrator with troubleshooting. This section describes how to find the session ID.

The session ID is created when you request a streaming session. The session ID, and other information used by AppStream 2.0, is stored in the session storage location for your browser. You can use the developer tools that are available for your browser interface to find this location.

For information about the developer tools that are available for common web browsers, see the following resources:

- [Apple Safari Developer Help: Storage tab](https://support.apple.com/guide/safari-developer/storage-tab-dev43453fff5/mac "https://support.apple.com/guide/safari-developer/storage-tab-dev43453fff5/mac")
- [View And Edit Session Storage With Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/storage/sessionstorage "https://developers.google.com/web/tools/chrome-devtools/storage/sessionstorage")
- [Firefox Developer Tools: Local Storage / Session Storage](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector/Local_Storage_Session_Storage "https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector/Local_Storage_Session_Storage")
- [Microsoft Edge (Chromium) Developer Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium "https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium")
- [Microsoft Edge (EdgeHTML) Developer Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide "https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide")
  After you locate the developer tools for your browser, search for the session storage for the AppStream 2.0 website. The domain for the website is **https://appstream2.<`aws-region`>.aws.amazon.com**. Expand the domain, and choose **sessionStorage.as2SessionData**. The session ID is stored in the key **sessionId**.
