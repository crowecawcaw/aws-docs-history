# Certificates

In order to provide a HTTPS connection between the different components, a SSL certificate
is required for each of the hosts. Customers are recommend to use their own manager
certificates on each of the host. For non-production workloads, a self-signed SSL
certificate can be used. For more information on creating a self-signed cert see [Generating a self-signed
certificate](generate-certs.md "generate-certs.md").

See instructions below on how to configure the different Amazon DCV Access Console
components to use certificates.

###### Authentication Server

1. Connect to the host that is running the Authentication Server.
2. Open
   `/etc/dcv-access-console-auth-server/access-console-auth-server-secrets.properties`
   with your preferred editor and update the following properties:
   - `server.ssl.key-store-type` – Set to `PKCS12`.
   - `server.ssl.key-store` – Set to path of the JKS keystore.
   - `server.ssl.enabled` – Set to true.
   - `server.ssl.key-store-password` – Set to key store password.

3. Restart the Authentication Server service.

```
sudo systemctl restart dcv-access-console-auth-server
```

###### Handler

1. Connect to the host that is running the Handler
2. Open
   `/etc/dcv-access-console-handler/access-console-handler-secrets.properties`
   with your preferred editor and update the following properties:
   - `server.ssl.key-store-type` – Set to `PKCS12`.
   - `server.ssl.key-store` – Set to path of the JKS key store.
   - `server.ssl.enabled` – Set to true.
   - `server.ssl.key-store-password` – Set to key store password.

3. Restart the Handler service.

```
sudo systemctl restart dcv-access-console-handler
```

###### Web Client/NGNIX

1. Connect to the host that is running NGNIX.
2. Open `/etc/nginx/conf.d/dcv-access-console.conf` with your
   preferred editor and update the following properties:
   - `ssl_certificate` – Set to path to the certificate
     for the host.
   - `ssl_certificate_key` – Set to path to the key for
     the certificate.

3. Restart the NGNIX service.

```
sudo systemctl restart ngnix
```
