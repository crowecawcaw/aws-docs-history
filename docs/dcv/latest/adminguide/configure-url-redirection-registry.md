

# Configure URL redirection using the Windows Registry Editor
<a name="configure-url-redirection-registry"></a>

As an alternative to the `dcv set-config` command, you can set the URL redirection parameters in the Windows Registry Editor. The following table lists the registry values.


**Registry values**  

| Name | Type | Value data | 
| --- | --- | --- | 
| enabled | DWORD (32-bit) Value | 1 to enable URL redirection, or 0 to disable it. | 
| host-to-client-allow-list | String Value | The URL patterns to redirect, separated by commas. For example, https://www.youtube.com/\*,https://\*.example.com/\*,mailto:\*@example.com | 
| host-to-client-deny-list | String Value | The URL patterns to keep in the session, separated by commas. For example, https://\*.internal.example.com/\*,https://localhost/\* | 
| max-url-length | DWORD (32-bit) Value | The maximum URL length, in decimal. The default is 2048. The maximum value is 65536. A larger value is clamped to 65536. Enter 0 to turn off the length check. | 

**To configure URL redirection using the Windows Registry Editor**

1. Open the Windows Registry Editor as the administrator.

1. Navigate to the `HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\` key.

1. Select the **url-redirection** key. If there is no **url-redirection** key, create one. In the left-hand pane, open the context (right-click) menu for the **dcv** key and choose **New**, **Key**. Name the key `url-redirection`.

1. For each parameter that you want to set, select the parameter in the right-hand pane. If the parameter doesn't exist, create it. Open the context (right-click) menu in the right-hand pane, choose **New**, and then choose the type shown in the preceding table. Name the parameter with the exact name shown in the table.

1. Open each parameter, enter the value in **Value data**, and choose **OK**. For **max-url-length**, choose **Decimal** for **Base**.

1. Close the Windows Registry Editor.

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).

**Note**  
In the registry, enter the allow list and the exception list as plain comma-separated text, without the quotes that the `dcv set-config` command uses.