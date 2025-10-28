# Integrating with the Amazon DCV Connection Gateway

[Amazon DCV Connection Gateway](../gw-admin/what-is-gw.md "../gw-admin/what-is-gw.md")
is an installable software package that enables users to access a fleet of Amazon DCV servers through a single access point to a LAN or VPC.

If your infrastructure includes Amazon DCV servers that are accessible through the Amazon DCV Connection Gateway,
you can configure the Session Manager to integrate the Amazon DCV Connection Gateway. By following the steps outlined in the following section, the broker
will act as a [Session Resolver](../gw-admin/session-resolver.md "../gw-admin/session-resolver.md") for the Connection Gateway.
In other words, the broker will expose an additional HTTP endpoint. The Connection Gateway will make API calls to the endpoint
to retrieve the information needed to route Amazon DCV connections to the host selected by the broker.

###### Topics

- [Set up the Session Manager Broker as a Session Resolver for the Amazon DCV Connection Gateway](#set-up-sm-broker "#set-up-sm-broker")
- [Optional - Enable TLS client authentication](#enable-tls-client-auth "#enable-tls-client-auth")
- [Amazon DCV server - DNS mapping reference](dcv-server-dns-mapping.md "dcv-server-dns-mapping.md")

## Set up the Session Manager Broker as a Session Resolver for the Amazon DCV Connection Gateway

###### Session Manager Broker side

1. Open `/etc/dcv-session-manager-broker/session-manager-broker.properties`
   using your preferred text editor and apply the following changes:
   - Set `enable-gateway = true`
   - Set `gateway-to-broker-connector-https-port` to a free TCP port (default is 8447)
   - Set `gateway-to-broker-connector-bind-host` to the IP address of the host where the Broker binds for Amazon DCV Connection Gateway connections (default is 0.0.0.0)

2. Then run the following commands to stop and restart the Broker:

```
sudo systemctl stop dcv-session-manager-broker
```

```
sudo systemctl start dcv-session-manager-broker
```

3. Retrieve a copy of the Broker's self-signed certificate and place it in your user directory.

```
sudo cp /var/lib/dcvsmbroker/security/dcvsmbroker_ca.pem $HOME
```

You'll need it when you install the Amazon DCV Connection Gateway in the next step.

###### Amazon DCV Connection Gateway side

- Please follow the [section](../gw-admin/setting-up-configuring.md#configuring-resolver "../gw-admin/setting-up-configuring.md#configuring-resolver") in the Amazon DCV Connection Gateway documentation.

Since the Amazon DCV Connection Gateway makes HTTP API calls to the broker, if the broker is using a self-signed certificate, you will need to copy
the broker certificate to the Amazon DCV Connection Gateway host (retrieved in the previous step) and set the `ca-file` parameter in the `[resolver]`
section of the Amazon DCV Connection Gateway configuration.

## Optional - Enable TLS client authentication

Once you have completed the previous step, the Session Manager and the Connection Gateway can communicate over a secure channel,
where the Connection Gateway can verify the identity of the Session Manager Brokers. If you require that also the Session Manager
Brokers validate the identity of the Connection Gateway before establishing the secure channel, you need to enable the TLS client
authentication feature, following the steps in the next section.

###### Note

If the Session Manager is behind a load balancer, TLS client authentication cannot be enabled with load balancers
that have TLS connection termination, such as Application Load Balancers (ALBs) or Gateway Load Balancers (GLBs).
Only load balancers without TLS termination can be supported, such as Network Load Balancers (NLBs).
If you use ALBs or GLBs, you can enforce that only specific security groups can contact the load balancers, ensuring an
additional level of security; more info about security groups here:
[Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")

###### Session Manager Broker side

1. To enable the TLS client authentication for the communication between the Session Manager Brokers
   and the Amazon DCV Connection Gateway, please follow the next steps:
2. Generate the required keys and certificates by running:

The output of the command will tell you the folder where the credentials have been generated and the password used for creating the TrustStore file.

```
sudo /usr/share/dcv-session-manager-broker/bin/gen-gateway-certificates.sh
```

3. Place a copy of the Amazon DCV Connection Gateway's private key and self-signed certificate in your user directory.
   You'll need it when you enable the TLS client authentication in the Amazon DCV Connection Gateway in the next step.

```
sudo cp /etc/dcv-session-manager-broker/resolver-creds/dcv_gateway_key.pem $HOME
```

```
sudo cp /etc/dcv-session-manager-broker/resolver-creds/dcv_gateway_cert.pem $HOME
```

4. Then open /etc/dcv-session-manager-broker/session-manager-broker.properties using your preferred text editor and do the following:
   - Set `enable-tls-client-auth-gateway` to `true`
   - Set `gateway-to-broker-connector-trust-store-file` to the path of the TrustStore file created in the previous step
   - Set `gateway-to-broker-connector-trust-store-pass` to the password used for creating the TrustStore file in the previous step

5. Then run the following command to stop and restart the Broker:

```
sudo systemctl stop dcv-session-manager-broker
```

```
sudo systemctl start dcv-session-manager-broker
```

###### Amazon DCV Connection Gateway side

- Please follow the [section](../gw-admin/setting-up-configuring.md "../gw-admin/setting-up-configuring.md") in the Amazon DCV Connection Gateway documentation.
  - use the full path of the certificate file that you copied in the previous step when setting the `cert-file` parameter in the `[resolver]` section
  - use the full path of the key file that you copied in the previous step when setting the `cert-key-file` parameter in the `[resolver]` section
