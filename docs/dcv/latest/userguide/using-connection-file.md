# Step 4: Create a connection file (optional)

Using the Windows, Linux, or macOS native client, you can create a connection file that you
can use to instantly connect to a Amazon DCV session.

###### Contents

- [Creating the connection file](#connection-file-create "#connection-file-create")
- [Supported parameters](#connection-file-params "#connection-file-params")
- [Running the connection file](#connection-file-execute "#connection-file-execute")

## Creating the connection file

The connection file is a text-based file with a `.dcv` file extension. The
format of the `.dcv` file is similar to that of an `.ini` file. The
file includes `[groups]` followed by the parameters and their values. The groups
and parameters take the following format:

```

[`group_name`]
`parameter_name`=`parameter_value`

```

For example:

```

[`options`]
`fullscreen`=`true`

```

You can create a connection file for a specific Amazon DCV session directly from the client.
Or, alternatively, you can create a connection file from scratch using a text editor.

###### Note

The procedure for creating a connection file from scratch using a text editor is the same for the
Windows, Linux, and macOS clients.

###### To create a connection file from the client

1. Open the client.
2. Connect to the server and session where you are creating the file.
3. Select the hostname for the Amazon DCV server in the top-right corner and choose **Save Connection As**.
4. In the **Save As** window, enter a file name and destination folder, and
   choose **Save**.

By default, when you create a connection file, the file includes the `format`,
`host`, `port`, `user`, and `proxytype` parameters.
These parameters are required to connect to the session that the file was created from. You can
manually customize or add parameters at any time by editing the file using a text editor.

###### To create a connection file from scratch using a text editor

1. Create a `.dcv` file with the following file name format:
   ``file_name`.dcv`
2. Open the `.dcv` file using your preferred text editor.
3. Add
   the `[version]` group and `format` parameter to the
   top of the file in the following format:

```
[version]
format=1.0
```

###### Important

If the `.dcv` file doesn't include the `[version]` group and
`format` parameter, parsing fails. 4. Add the required parameter groups using the following format:

```
[`group_name`]
```

For more information about the parameter groups, see [Supported parameters](#connection-file-params "#connection-file-params"). 5. Add the parameters and parameter values after the groups using the following
format:

```
`parameter_name`=`parameter_value`
```

###### Note

    * Parameter names are case sensitive.
    * Don't enclose string parameter values in quotation marks.

For more information about the parameters and parameter values, see [Supported parameters](#connection-file-params "#connection-file-params"). 6. Save the changes and close the `.dcv` file.

You can also use this procedure to add additional parameters to an existing connection file
at any time.

## Supported parameters

Currently, the `.dcv` file supports parameters in three parameter groups—`[version]`,
`[connect]`, and `[options]`. The following tables list the groups and their available
parameters.

###### Groups

- [[version] parameters](#param-version "#param-version")
- [[connect] parameters](#param-connect "#param-connect")
- [[options] parameters](#param-option "#param-option")
- [[debug] parameters](#param-debug "#param-debug")

### `[version]` parameters

###### Important

This is a required group. If your `.dcv` file doesn't include this group,
parsing fails.

The following table lists the parameters that can be specified in the `[version]` group.

| Parameter                   | Type    | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | ------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| format                      | string  |               | ImportantThis is a required parameter. The parameter value must be `1.0`.If your `.dcv` file doesn't include this parameter, parsing fails.                                                                                                                                                                                                                                                                                                                                                                                                                                           | ### `[connect]` parameters The following table lists the parameters that can be specified in the `[connect]` group.                                                                                                                                                                                                                                |
| Parameter                   | Type    | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                         | ---     | ---           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| host                        | String  |               | The hostname of the Amazon DCV server hosting the session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| port                        | Integer | 8443          | The port to use when connecting to the Amazon DCV server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| weburlpath                  | String  |               | A custom path on the Amazon DCV server for connection. For example, if you specify `customPath`, the client attempts to connect to `host:port/customPath`.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| sessionid                   | String  |               | The ID of the Amazon DCV session to connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| authtoken                   | String  |               | The authentication token to be used for the connection. If you specify an `authtoken`, you must also specify a `sessionid`. When using `authtoken`, you can omit the `user` and `password` parameters.                                                                                                                                                                                                                                                                                                                                                                                |
| user                        | String  |               | The user name to use when connecting to the Amazon DCV server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| password                    | String  |               | The password to use when connecting to the Amazon DCV server. The password isn't encrypted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| proxytype                   | String  | SYSTEM        | The proxy type to be used. Valid values include `HTTPS`, `HTTP`, `SOCKS5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | SOCKS`, `SYSTEM`, or `NONE                                                                                                                                                                                                                                                                                                                         | DIRECT`. If you specify `SYSTEM`, your computer's proxy settings are used. |
| proxyhost                   | String  |               | The address of the proxy server to be used if connecting through a proxy server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| proxyport                   | Integer |               | The port to be used if connecting through a proxy server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| proxyuser                   | String  |               | The user name to be used for proxy authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| proxypassword               | String  |               | The password to be used for proxy authentication. The password isn't encrypted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| transport                   | String  | `auto`        | The protocol to use for data transport. With `auto` the client first tries to connect using the QUIC (UDP) protocol. If the QUIC connection fails, transport automatically falls back to `websocket`. Specify `websocket` to use the WebSocket (TCP) protocol for data transport, or specify `quic` to use the QUIC (UDP) protocol for data transport. If you enable QUIC, the QUIC protocol is used for data transport and WebSocket is used for authentication traffic. If you enable WebSocket, the WebSocket protocol is used for both data transport and authentication traffic. |
| webport                     | Integer | 8443          | The port to use for WebSocket (TCP) traffic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| quicport                    | Integer | 8443          | The port to use for QUIC (UDP) traffic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| certificatevalidationpolicy | String  | ask-user      | The policy for validating an untrusted certificate. Values include `strict`, `accept-untrusted`, and `ask-user`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ### `[options]` parameters The following table lists the parameters that can be specified in the `[options]` group.                                                                                                                                                                                                                                |
| Parameter                   | Type    | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                         | ---     | ---           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| fullscreen                  | Boolean | false         | Indicates whether the client starts in full screen mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| useallmonitors              | Boolean | false         | Indicates whether the client uses all monitors when starting full screen mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| promptreconnect             | Boolean | true          | Indicates whether the client prompts you to reconnect after you disconnect from a session. If the parameter is set to `true`, you're redirected to the sign-in screen when you disconnect. If the parameter is set to `false`, the client closes when you disconnect.                                                                                                                                                                                                                                                                                                                 |
| enableyuv444decoding        | Boolean | false         | Indicates whether to enable the [High color accuracy (YUV 4:4:4)](using-high-color-accuracy.md "using-high-color-accuracy.md") when encoding dynamic video content.                                                                                                                                                                                                                                                                                                                                                                                                                   | ### `[debug]` parameters The following table lists the parameters that can be specified in the `[debug]` group.                                                                                                                                                                                                                                    |
| Parameter                   | Type    | Default value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                         | ---     | ---           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| loglevel                    | String  | INFO          | Value can be set to `Debug`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ## Running the connection file To run `.dcv` connection file, navigate to the file and double-click it. Or, specify the file path as an argument for the `dcvviewer` command. <br>• Windows client `` `C:\>` dcvviewer.exe `path`\`connection_file_name`.dcv `` <br>• Linux and macOS client `` `$` dcvviewer `path`/`connection_file_name`.dcv `` |
