

# Subscribe a callback function when the Connect Customer agent workspace agent's network connection status changes
<a name="3P-apps-agent-events-networkconnectionstatuschanged-sub"></a>

Subscribes a callback function to be invoked whenever the agent's network connection status changes in the Connect Customer agent workspace.

 **Signature** 

```
onNetworkConnectionStatusChanged(handler: NetworkConnectionStatusChangedHandler)
```

 **Usage** 

```
const handler: NetworkConnectionStatusChangedHandler = async (data: NetworkConnectionStatusChanged) => {
    console.log("Network connection status changed! " + data.status);
};

agentClient.onNetworkConnectionStatusChanged(handler);

// NetworkConnectionStatusChanged Structure
{
  status: NetworkConnectionStatus;
  timestamp: number;
}
```

 **Permissions required:** 

```
*
```