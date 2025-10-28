# Handler fails to communicate with the broker

If there are communication failures between Handler component and Session Manager Broker, “Broker
authentication error” will appear in the browser logs or `BrokerAuthenticationException: {"error":"unauthorized_client"}` in the
handler logs. This is due to the fact that the Broker has incorrect property files or the Handler is unable to connect to
the Broker.

## Incorrect Broker properties

The Handler communicates with the Session Manager Broker using the properties specified in the `session-manager-handler.properties`
file. If the property files are incorrect, communication issues can occur between the two.

1. On the host where the Handler is installed, navigate to the Handler properties file using your preferred text editor.

```
 /etc/dcv-access-console-handler/access-console-handler.properties
```

2. Verify that the `broker-base-url points to the Broker URL with the client-to-broker-connector-https-port`.
   For more information, see [Broker configuration file](../sm-admin/broker-file.md "../sm-admin/broker-file.md")
   in the _Amazon DCV administrator guide_.
3. Verify that the `broker-auth-url` points to the Broker authentication [URL](https://broker-host:8443/oauth2/token "https://broker-host:8443/oauth2/token").
4. Verify that the `broker-client-id` and `broker-client-password` are correct. If you do not know the client-id
   and password you can register a new client using the `register-api-client` broker api.
5. Restart the Handler.

```
sudo systemctl restart dcv-access-console-handler
```

## Handler is unable to connect to the Broker

The Handler needs to connect to the Session Manager Broker on the `client-to-broker-connector-https-port` of the Broker.
To verify that the Handler can connect to the Broker, run telnet to the Broker host name and the
`client-to-broker-connector-https-port` (8443 by default) on the host where the Handler is installed.

If you are unable to connect to the host where the Broker is installed, see [Networking and connectivity](networking-connectivity.md#multiple-host-setup "networking-connectivity.md#multiple-host-setup") for requirements.

Example of a successful connection:

```
telnet broker-host 8443
Trying *broker-host ip address*...
Connected to broker-host.
Escape character is '^]'.
^]
telnet> ^C
```
