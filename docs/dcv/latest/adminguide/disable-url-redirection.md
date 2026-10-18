

# Disable host-to-client URL redirection
<a name="disable-url-redirection"></a>

1. Open a Command Prompt as the administrator and go to the Amazon DCV Server installation directory:

   ```
   C:\> cd "C:\Program Files\NICE\DCV\Server\bin"
   ```

1. Disable URL redirection:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe set-config --section url-redirection --key enabled false
   ```

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).