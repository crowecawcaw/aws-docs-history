

# Configure the maximum URL length (optional)
<a name="configure-max-url-length"></a>

By default, URLs longer than 2,048 characters aren't redirected and open in the session. You can change this limit. The limit doesn't apply to `mailto:` links.

**To configure the maximum URL length**

1. Open a Command Prompt as the administrator and go to the Amazon DCV Server installation directory:

   ```
   C:\> cd "C:\Program Files\NICE\DCV\Server\bin"
   ```

1. Set the `max-url-length` parameter to the maximum number of characters. The maximum value is `65536`. Amazon DCV doesn't reject a larger value. Instead, Amazon DCV clamps the value to `65536` and writes a warning to the log. To turn off the length check, use `0`. For example:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe set-config --section url-redirection --key max-url-length 4096
   ```

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).