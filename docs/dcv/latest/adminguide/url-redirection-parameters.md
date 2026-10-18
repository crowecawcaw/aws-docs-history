

# URL redirection parameters
<a name="url-redirection-parameters"></a>

The following table describes the configuration parameters in the `url-redirection` section. On Windows Amazon DCV servers, the parameters are stored in the `HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\url-redirection` registry key. For more information, see the [Amazon DCV Server parameter reference](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref.html).


**URL redirection parameters**  

| Parameter | Type - Windows registry type | Reload context | Default value | Description | 
| --- | --- | --- | --- | --- | 
| enabled | true or false - DWORD (32-bit) | session | Windows: 0 | Whether host-to-client URL redirection is enabled — Specifies whether links opened in the session that match the allow list open on the local device. — Available since version 2026.0. | 
| host-to-client-allow-list | string - String | session | Windows: empty | URL patterns to redirect to the client — Comma-separated URL patterns for links that open on the local device. Supports the \* and ? wildcards, and mailto: patterns. If empty, no links are redirected. — Available since version 2026.0. | 
| host-to-client-deny-list | string - String | session | Windows: empty | URL patterns to keep in the session — Comma-separated URL patterns for links that always open in the session. Evaluated before the allow list. — Available since version 2026.0. | 
| max-url-length | unsigned integer - DWORD (32-bit) | session | Windows: 2048 | Maximum URL length for redirection — Maximum number of characters in a URL that can be redirected. Longer URLs open in the session. Set to 0 to turn off the check. The maximum value is 65536. A larger value isn't rejected: it's clamped to 65536, and a warning is written to the log. Doesn't apply to mailto: links. — Available since version 2026.0. | 

## Registry values
<a name="registry-values"></a>

On Windows Amazon DCV servers, the parameters are stored as values in the `HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\url-redirection` registry key. To configure many servers at once, for example with Group Policy, Microsoft Intune, an image, or a startup script, write these values directly instead of running `dcv set-config` on each server.


**Registry values**  

| Value name | Type | Example | 
| --- | --- | --- | 
| enabled | REG\_DWORD | 1 | 
| host-to-client-allow-list | REG\_SZ | https://www.youtube.com/\*,mailto:\*@example.com | 
| host-to-client-deny-list | REG\_SZ | https://\*.internal.example.com/\*,https://localhost/\* | 
| max-url-length | REG\_DWORD | 2048 | 

**Note**  
Store each list as a single REG\_SZ value that contains the patterns separated by commas, for example `https://www.youtube.com/*,mailto:*@example.com`. Don't use REG\_MULTI\_SZ, and don't store the list as an array, such as `['https://www.youtube.com/*', 'mailto:*@example.com']`. Don't add the quotes that the `dcv set-config` examples use. A value in any other format doesn't match any links.