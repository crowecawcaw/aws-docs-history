# Configuring smart card caching

The smart card caching feature enables the Amazon DCV server to cache smart card values. When this feature is enabled, the Amazon DCV server caches the results
of recent calls to the client's smart card. Future calls are retrieved directly from the server's cache, instead of from the client. This reduces
the amount of traffic that's transferred between the client and the server and improves performance. This is especially useful if the client has a
slow internet connection.

By default, smart card caching is disabled. Clients can manually enable smart card caching for each application they run by setting the
`DCV_PCSC_ENABLE_CACHE` environment variable. For instructions, see [Using a Smart
Card](../userguide/using-smartcard.md "../userguide/using-smartcard.md") in the _Amazon DCV User Guide_. Or, you can configure the Amazon DCV server to permanently enable or disable smart card caching,
regardless of the value specified for the `DCV_PCSC_ENABLE_CACHE` environment variable.

Linux Amazon DCV server

###### To permanently enable or disable smart card caching on a Linux Amazon DCV server

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.
2. Locate the `enable-cache` parameter in the `[smartcard]` section. To permanently enable smart card caching, enter
   `'always-on'`. To permanently disable smart card caching, enter `'always-off'`.

If there's no `enable-cache` parameter in the `[smartcard]` section, add it manually using the following
format:

```
[smartcard]
enable-cache=`'always-on'`|`'always-off'`
```

3. Save and close the file.
4. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.

Windows Amazon DCV server

###### To permanently enable or disable smart card caching on a Windows Amazon DCV server

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\smartcard\*\* key and select the
   **enable-cache\*\* parameter.

If the parameter doesn't exist, use the following steps to create it:

    1. In the left pane, open the context (right-click) menu for the **smartcard** key, and choose **New**,
     **String Value**.
    2. For **Name**, enter `enable-cache` and press **Enter**.

3. Open the **enable-cache** parameter. For **Value data**, enter `always-on` to permanently
   enable smart card caching, or enter `always-off` to permanently disable smart card caching.
4. Choose **OK** and close the Windows Registry Editor.
