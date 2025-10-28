# Generating a self-signed

certificate

Every host that is running a Amazon DCV Access Console component needs to have a
certificate. If you are bringing your own certificate, you don’t need to follow these
instructions.

###### Note

Note that this requires the OpenJDK version 1.8 to be installed on the
system.

1. Connect to the host that requires a self-signed certificate.
2. Create a directory to store the certificate.

```
`$` sudo mkdir -p /usr/local/var/dcv-access-console/security/
```

```
`$` cd/usr/local/var/dcv-access-console/security/
```

3. Create the subject of the certificate using the public DNS for the host.

```
`$` CERT_SUBJ="/CN=`public DNS`"
```

4. Set the keystore password. If you have not changed it, the password is
   `changeit`.

```
`$` CERT_PASSWORD="changeit"
```

5. Create the RootCA and use it to sign the certificate.

```
`$` sudo openssl req -new -x509 -nodes -newkey rsa:2048 -out rootCA.pem -keyout rootCA.key -subj "$CERT_SUBJ" -days 1825
```

```
`$` sudo openssl req -new -sha256 -nodes -newkey rsa:2048 -out server.csr -keyout server.key -passout pass:$CERT_PASSWORD -subj "$CERT_SUBJ"
```

```
`$` sudo openssl x509 -req -sha256 -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.pem -days 1825
```

6. Create the PKCS12 file.

```
`$` sudo openssl pkcs12 -export -nodes -in server.pem -inkey server.key -out keystore.p12 -name server -passin pass:$CERT_PASSWORD -password pass:$CERT_PASSWORD
```

7. Import the RootCA and the certificate into the keystore.

```
`$` sudo keytool -import -alias rootca -cacerts -storepass $CERT_PASSWORD -file rootCA.pem -noprompt
```

```
`$` sudo keytool -import -alias server -cacerts -storepass $CERT_PASSWORD -file server.pem -noprompt
```

Take note of the paths to:

- `server.pem`
- `server.key`
- `keystore.p12`
- `rootCA.pem`
  You will need them during configuration.
