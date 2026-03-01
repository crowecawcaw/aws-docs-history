# Enable Dynamic App Providers

Dynamic app providers must first be enabled within an WorkSpaces Applications image. After you
enable these providers, they can manage applications for users on the streaming
instance.

To enable this capability, you must add your dynamic app provider details to
a configuration file on the image builder. The image builder must be joined to a
Microsoft Active Directory domain. Perform the following steps on an image
builder, then you can test your dynamic apps to verify that they function as
expected. Finally, finish creating your image.

###### Note

Third-party dynamic app providers may modify the configuration file during
install. For installation instructions, see the documentation for the
applicable provider.

###### To enable dynamic app providers

1. Connect to the image builder that you want to use and sign in with a
   domain account that has local administrator permissions on the image
   builder. To do so, do either of the following:
   - [Use
     the WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client
     connections)

   ###### Note

   If your organization requires smart card sign in, you must
   create a streaming URL and use the WorkSpaces Applications client for the
   connection. For information about smart card sign in, see
   [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. Navigate to
   C:\ProgramData\Amazon\AppStream\AppCatalogHelper\DynamicAppCatalog\, and
   open the **Agents.json** configuration file.
3. In the **Agents.json** file, add the following
   entries:

"DisplayName": "<Uninstall hive display name value>",

"Path": "<C:\path\to\client\application>"

`DisplayName` must match the
**DisplayName** registry value for the
**HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall**
key created for your application. 4. Install your dynamic app provider. 5. On the image builder desktop, open Image Assistant. 6. Optionally, install any other applications that you want to include in
the image. 7. In Image Assistant, on the **1. Add Apps** page,
select the **Enable dynamic app providers** check
box. 8. On the same page, if you installed other applications as described in
step 8, choose **+Add App**, and specify the
applications to add.

###### Note

When you use a dynamic app provider, you don't need to specify any
applications in the image. If you specify applications in the image,
they can't be removed by dynamic app providers. 9. Proceed to the steps in the next section to test your dynamic app
provider.
