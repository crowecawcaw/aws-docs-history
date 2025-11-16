# Managing the TLS certificate

Amazon DCV automatically generates a self-signed certificate that's used to secure traffic between the Amazon DCV client and Amazon DCV server. By default, if no
other certificate is installed, this certificate is used. The default certificate includes two files. They are the certificate itself
(`dcv.pem)` and a key (`dcv.key`). For more information, please see [Redirection clarifications with self-signed certificates](redirection-clarifications-with-self-signed-certs.md "redirection-clarifications-with-self-signed-certs.md").

When DCV client users connect to a server, they might receive server certificate warnings that they can act on to verify, before the
connection is established.

If they are using a web browser to connect, the browser might warn client users about trusting the server's certificate and that they should
contact the administrator to confirm the certificate authenticity.

Similarly, if they are using a Windows, Linux or macOS client, they might be advised to confirm a given certificate's fingerprint with the
Amazon DCV server administrator.

To verify the authenticity of their certificate fingerprints, run `dcv list-endpoints -j` and check the output against their
certificate fingerprints.

You can replace the default Amazon DCV certificate and its key with your own certificate and key.

When you generate your own certificate, select the certificate attributes that meet your specific needs. The `CN (Common Name)`
attribute in most cases must match the public hostname of the host. You also might want to specify the `SAN (Subject Alternative Name)`
attribute and set it to the IP address of the host.

For instructions on how to generate a certificate, see the documentation of your specific Certification Authority.

###### Important

If you use your own certificate and key, you must name your certificate `dcv.pem` and you must name the key
`dcv.key`.

Windows Amazon DCV server

###### To change the server's TLS certificate on Windows

- Place the certificate and its key in the following location on your Windows Amazon DCV server:

```
C:\Windows\System32\config\systemprofile\AppData\Local\NICE\dcv\
```

Linux Amazon DCV server

###### To change the server's TLS certificate on Linux

1. Place the certificate and its key in the following location on your Linux Amazon DCV server:

```
/etc/dcv/
```

2. Grant ownership of both files to the `dcv` user, and change their permissions to 600 (only the owner can read or write to
   them).

```
`$`  sudo chown dcv dcv.pem dcv.key
```

```
`$`  sudo chmod 600 dcv.pem dcv.key
```

macOS Amazon DCV server

###### To change the server's TLS certificate on macOS

1. Place the certificate and its key in the following location on your macOS Amazon DCV server:

```
/etc/dcv/
```

2. Grant ownership of both files to the `dcv` user, and change their permissions to 600 (only the owner can read or write to
   them).

```
`$`  sudo chown dcv dcv.pem dcv.key
```

```
`$`  sudo chmod 600 dcv.pem dcv.key
```

###### Note

Beginning with Amazon DCV 2022.0, if you update a certificate file while the Amazon DCV server is running, the new certificate will be automatically
reloaded. For previous versions of Amazon DCV you will need to manually [stop](manage-stop.md "manage-stop.md") and [restart](manage-start.md "manage-start.md") the Amazon DCV server.
