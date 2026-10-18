

# Enable host-to-client URL redirection
<a name="enable-url-redirection"></a>

You configure URL redirection with the parameters in the `url-redirection` section of the Amazon DCV Server configuration. The procedures in this topic use the `dcv set-config` command, which configures one server at a time. You can also set the parameters directly in the Windows registry, which is the way to configure many servers with Group Policy, Microsoft Intune, an image, or a startup script. For more information, see [Configure URL redirection using the Windows Registry Editor](configure-url-redirection-registry.md) and [Registry values](url-redirection-parameters.md#registry-values). For more information about the parameters, see [URL redirection parameters](url-redirection-parameters.md).

**To enable URL redirection on a Windows host**

1. Open a Command Prompt as the administrator and go to the Amazon DCV Server installation directory:

   ```
   C:\> cd "C:\Program Files\NICE\DCV\Server\bin"
   ```

1. Enable URL redirection:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe set-config --section url-redirection --key enabled true
   ```

1. Configure the URL patterns for the links that you want to redirect. If the allow list is empty, no links are redirected. For more information, see [Configure URL patterns (allow list)](configure-url-patterns-allow-list.md).

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).