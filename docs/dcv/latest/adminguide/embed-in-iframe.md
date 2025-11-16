# Embed the Amazon DCV web browser client inside an

iFrame

By default, to protect against clickjacking attacks, Amazon DCV doesn't allow the web
browser client to be embedded inside an iFrame. However, you can override this default
behavior to allow the web browser client to run inside an iFrame.

For more information, about preventing clickjacking attacks, see the [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html#Preventing_Clickjacking "https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html#Preventing_Clickjacking").

To allow the web browser to run inside an iFrame, you must configure the Amazon DCV server to
send the following additional HTTP response headers to the web browser client:

- `web-x-frame-options`
- `web-extra-http-headers`
  We recommend that you add both headers to ensure the best compatibility across web
  browsers.

###### Note

If connecting through a Amazon DCV Connection Gateway, the x-frame options need to be defined within the gateway configuration. This is done by using the `local-resources-http-headers` parameter within the
[`[web-resources]` section](../gw-admin/config-reference.md#config-web-resources "../gw-admin/config-reference.md#config-web-resources") of the gateway configuration.

Windows server

1. Open the Windows Registry Editor and navigate to the
   \*\*HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\connectivity\*\*
   key.
2. Open the **web-x-frame-options** parameter. For
   **Value data**, enter `"ALLOW-FROM
https://`server_hostname`"`.

###### Note

If the parameter doesn't exist, create a new String parameter
and name it `web-x-frame-options`. 3. Open the **web-extra-http-headers** parameter.
For **Value data**, enter
`[("Content-Security-Policy", "frame-ancestors
 https://`server_hostname`")]`.

###### Note

If the parameter doesn't exist, create a new String parameter
and name it `web-extra-http-headers`. 4. Close the Windows Registry Editor. 5. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.

Linux server

1.  Open `/etc/dcv/dcv.conf` with your preferred text
    editor.
2.  In the `[connectivity]` section, do the
    following:

        * For `web-x-frame-options`, enter
         `"ALLOW-FROM
         https://`server_hostname`"`.
        * For `web-extra-http-headers`, enter
         `[("Content-Security-Policy", "frame-ancestors
         https://`server_hostname`")]`.

    For example:

```
[connectivity]
web-x-frame-options="ALLOW-FROM https://`my-dcv-server.com`"
web-extra-http-headers=[("Content-Security-Policy", "frame-ancestors https://`my-dcv-server.com`")]
```

3. Save and close the file.
4. [Stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.

By default, most browsers prevent access to some features, such as microphone access
and fullscreen access. To allow access to these features, modify the iFrame element on
the webpage. For example, to allow access to the microphone and to fullscreen mode,
modify the iFrame element as follows:

```
<iframe src="..." allow="microphone; fullscreen"></iframe>
```
