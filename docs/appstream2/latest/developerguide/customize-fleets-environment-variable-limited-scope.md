# Create an Environment Variable That is Limited in Scope

Follow these steps to create an environment variable that is limited in scope to
the processes that are spawned off the script. This approach is useful when you need
to use the same environment variable name with different values for different
applications. For example, if you have two different applications that use the
environment variable "LIC_SERVER", but each application has a different value for
"LIC_SERVER".

###### To create an environment variable that is limited in scope

1. Connect to the image builder on which to create an environment variable
   that is limited in scope and sign in with an account that has local
   administrator permissions. To do so, do either of the following:
   - [Use the
     WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client
     connections)

   ###### Note

   If the image builder that you want to connect to is joined to
   an Active Directory domain and your organization requires smart
   card sign in, you must create a streaming URL and use the WorkSpaces Applications
   client for the connection. For information about smart card sign
   in, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

2. Create a child folder of C:\ drive for the script (for example,
   C:\Scripts).
3. Open Notepad to create the new script, and enter the following
   lines:

`set` `variable`=`value`

`start " " "C:\path\to\application.exe"`

Where:

`variable` is the variable name to be used

`value` is the value for the given variable
name

###### Note

If the application path includes spaces, the entire string must be
encapsulated within quotation marks. For example:

`start " " "C:\Program
 Files\application.exe"` 4. Choose **File**, **Save**. Name the file
and save it with the .bat extension to C:\Scripts. For example, name the
file LaunchApp.bat. 5. If needed, repeat steps 4 and 5 to create a script for each additional
application that requires its own environment variable and values. 6. On the image builder desktop, start Image Assistant. 7. Choose **Add App**, navigate to C:\Scripts, and select
one of the scripts that you created in step 5. Choose
**Open**. 8. In the **App Launch Settings** dialog box, keep or change
the settings as needed. When you're done, choose
**Save**. 9. If you created multiple scripts, repeat steps 8 and 9 for each
script. 10. Follow the necessary steps in Image Assistant to finish creating your
image. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").

The environment variable and specific value are now available for
processes that are run from the script. Other processes cannot access this
variable and value.
