# Prerequisites

Before setting up the Amazon DCV Access Console Access Manager, you must first install and configure the Session Manager Agent and Broker. For more information
about setting up Amazon DCV Session Manager, see the [Amazon DCV Session
Manager Administrator Guide](../sm-admin/what-is-sm.md "../sm-admin/what-is-sm.md").

## Registering a new client with the Broker

The Access Console has three components, the Web Client, the Handler, and the Authentication Server. You can set up the Access Console by:

- Running the Access Console components on the same host as the Session Manager Broker
- Running the Access Console components on a different host. If you choose this option, you must register a new client with the Broker. Use the following steps to register a new client with the Broker.

###### To register a new client with the Broker

1. Connect to the host where you installed the Broker.
2. Run the following command to register a new client:

```
`$` sudo -u root dcv-session-manager-broker register-api-client --client-name "access-console"
```

3. Take note of the `client-id` and `client-password`. We will need these when we set up the components.
4. The Broker host will also need to have a Public DNS assigned to it. Take note of the address. The Access Console Handler will need this to communicate with the Broker
5. Make sure that the host the Broker is running on is accessible by the host the Access Console Handler will be installed on, via the Broker’s `client-to-broker-connector-https-port` and the Public DNS

###### Note

If you haven’t changed the default, this is port 8443

If the Broker is already running on the same host where you are going to install all three
components, you don’t have to do anything. The Setup Wizard will register a new client
with the broker for you.
