# Enabling session storage

Session storage is a folder on the Amazon DCV server that clients can access when they're connected to a specific Amazon DCV session. When you enable session
storage for a session, clients can download files from, and upload files to, the specified folder. This feature enables clients to share files
while connected to a session.

###### Topics

- [Enabling session storage on Windows](#manage-storage-windows "#manage-storage-windows")
- [Enabling session storage on Linux](#manage-storage-linux "#manage-storage-linux")

## Enabling session storage on a Windows Amazon DCV Server

To enable session storage, first create the folder to use for session storage. Then, configure the `storage-root` parameter using
the Windows Registry Editor.

###### To enable session storage on Windows

1.  Create the folder to use for session storage (for example, `c:\session-storage`).
2.  Configure the `storage-root` parameter.
    1. Open the Windows Registry Editor.
    2. Navigate to the
       **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\session-management\automatic-console-session** key and select
       the **storage-root** parameter.

    If there's no `storage-root` parameter in the registry key, create one as follows:

        1. In the navigation pane, open the context (right-click) menu for the **session-management/automatic-console-session**
         key. Then, choose **New**, **String**.
        2. For **Name**, enter `storage-root` and press **Enter**.

    3. Open the **storage-root** parameter. For **Value data**, enter the full path to the folder that's
       created in step 1.

    You can also use `%home%` in the path to specify the home directory of the user who's currently signed in. For example, the
    following path uses `c:\Users\`username`\storage\` as the session storage directory.

    ```
    %home%/storage/
    ```

    ###### Note

    If the specified subdirectory doesn't exist, then session storage is disabled. 4. Choose **OK** and close the Windows Registry Editor. 5. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.

3.  Start the session and specify the `--storage-root` option. For more information, see [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md").

## Enabling session storage on a Linux Amazon DCV Server

To enable session storage, create the folder to use for session storage and then configure the `storage-root` parameter in the
`dcv.conf` file.

###### To enable session storage on Linux

1. Create the folder to use for session storage (for example, `/opt/session-storage/`).
2. Configure the `storage-root` parameter.
   1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.
   2. Locate the `storage-root` parameter in the `[session-management/automatic-console-session]` section. Replace the
      existing path with the full path to the folder that you created in step 1.

   If there's no `storage-root` parameter in the `[session-management/automatic-console-session]` section, add it
   manually using the following format.

   ```
   [session-management/automatic-console-session]
   storage-root="`/opt/session-storage/`"
   ```

   You can also use `%home%` in the path to specify the home directory of the user who's currently signed in. For example, the
   following parameter uses the `$HOME/storage/` directory for session storage.

   ```
   [session-management/automatic-console-session]
   storage-root="`%home%/storage/`"
   ```

   ###### Note

   If the specified subdirectory doesn't exist, then session storage is disabled.

3. Save and close the file.
4. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.
5. Start the session and specify the `--storage-root` option. For more information, see [Starting Amazon DCV sessions](managing-sessions-start.md "managing-sessions-start.md").
