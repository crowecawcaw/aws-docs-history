# Authorize the Outposts server using the Outpost Configuration Tool

Use the following procedure to authorize the server. You need the Outpost Configuration Tool and the IAM
credentials from the AWS account that owns the Outpost.

###### To authorize the server

1. Plug the USB cable into your laptop first and then into the server.
2. Use a serial terminal program, such as PuTTY or **screen**, to connect
   to the server. For more information, see [Create a serial connection to the Outposts server](authorize-2.md "authorize-2.md").
3. Press **Enter** to access the Outpost Configuration Tool command prompt.

```
`Outpost>`
```

###### Note

If you see a persistent red light inside the chassis of the server on the left-hand side after
you power on and you can't connect to Outpost Configuration Tool, you might need to power down and drain the
server to proceed. To drain the server, disconnect all network and power cables,
wait five minutes, then power up and connect to the network again. 4. Use **export** to enter your IAM credentials into Outpost Configuration Tool. If you
are using a third party to install the server, you must provide them with the IAM
credentials.

To authenticate, you must export the following four variables. Export one variable at
a time. Do not include a space before or after the equal (=) sign.

    * `AWS_ACCESS_KEY_ID=``access-key-id`
    * `AWS_SECRET_ACCESS_KEY=``secret-access-key`
    * `AWS_SESSION_TOKEN=``session-token`




    	+ Use the AWS CLI `GetSessionToken` command to get the
    	 `AWS_SESSION_TOKEN`. For more information, see [get-session-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-session-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-session-token.html") in the *AWS CLI Command
    	 Reference*.


    	###### Note

    	You must have the [AWSOutpostsAuthorizeServerPolicy](../../../aws-managed-policy/latest/reference/AWSOutpostsAuthorizeServerPolicy.md "../../../aws-managed-policy/latest/reference/AWSOutpostsAuthorizeServerPolicy.md") attached to your IAM role to get
    	 the `AWS_SESSION_TOKEN`.
    	+ To install the AWS CLI, see [Installing or updating
    	 the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the *AWS CLI User Guide for
    	 Verrsion 2*.
    * `AWS_DEFAULT_REGION=``Region`


    Use the parent Region of the Outposts server as the value for
     `AWS_DEFAULT_REGION`. If you are using a third party to install the
     server, you must provide them with the parent Region.

The output in the following examples show successful exports.

```
`Outpost>``export AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE``

`result: OK
checksum: `example-checksum``
```

```
`Outpost>``export AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``

`result: OK
checksum: `example-checksum``
```

```
`Outpost>``export AWS_SESSION_TOKEN=`MIICiTCCAfICCQD6m7oRw0uXOjANBgk
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=``

`result: OK
checksum: `example-checksum``
```

```
`Outpost>``export AWS_DEFAULT_REGION=`us-west-2``

`result: OK
checksum: `example-checksum``
```

5. Use **start-connection** to create a secure connection to the
   Region.

The output in the following example shows a connection successfully started.

```
`Outpost>``start-connection`

`is_started: True
asset_id: `example-asset-id`
connection_id: `example-connection-id`
timestamp: `2021-10-01T23:30:26Z`
checksum: `example-checksum``
```

6. Wait for about 5 minutes.
7. Use **get-connection** to check if the connection to the Region has
   been established.

The output in the following example shows a successful connection.

```
`Outpost>``get-connection`

`---
keys_exchanged: True
connection_established: True
exchange_active: False
primary_peer: `xx.xx.xx.xx:xxx`
primary_status: success
primary_connection_id: `a1b2c3d4567890abcdefEXAMPLE11111`
primary_handshake_age: `1111111111`
primary_server_public_key: `AKIAIOSFODNN7EXAMPLE`
primary_client_public_key: `AKIAI44QH8DHBEXAMPLE`
primary_server_endpoint: `xx.xx.xx.xx:xxx`
secondary_peer: `xx.xxx.xx.xxx:xxx`
secondary_status: success
secondary_connection_id: `a1b2c3d4567890abcdefEXAMPLE22222`
secondary_handshake_age: `1111111111`
secondary_server_public_key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
secondary_client_public_key: `je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY`
secondary_server_endpoint: `xx.xxx.xx.xxx:xxx`
timestamp: `2023-02-22T22:19:28Z`
checksum: `0x83FA0123``
```

After `keys_exchanged` and `connection_established` changes to
`True`, the Outposts server is automatically provisioned and updated to the latest
software and configuration.

###### Note

Note the following about the provisioning process:

    * After activation completes, it can take up to 10 hours until your Outposts server is
     usable.
    * You must keep the power and network for the Outposts server connected and stable during
     this process.
    * It is normal for the service link to fluctuate during this process.
    * If `exchange_active` is `True`, the connection is still
     establishing. Retry in 5 minutes.
    * If `keys_exchanged` or `connection_established` is
     `False`, and if `exchange_active` is `True`, the
     connection is still establishing. Retry in 5 minutes.
    * If `keys_exchanged` or `connection_established` is
     `False` even after 1 hour, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
    * If the message `primary_status: No such asset id found.` appears,
     confirm the following:




    	+ You specified the correct Region.
    	+ You are using the same account as the one used to order the Outposts server.
    If the Region is correct and you are using the same account as the one used to
     order the Outposts server, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
    * The `LifeCycleStatus` attribute of the Outpost will transition from
     `Provisioning` to `Active`. You will then receive an email
     letting you know that your Outposts server is provisioned and activated.
    * You don’t need to re-authorize the Outposts server after it is activated.

8. After you make a successful connection, you can disconnect your laptop from the
   server.
