

# Get the current network connection status of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getnetworkconnectionstatus"></a>

Returns the current network connection health status of the agent's connection to Connect Customer backend services.

```
async getNetworkConnectionStatus(): Promise<NetworkConnectionStatusChanged>
```

 **Output - NetworkConnectionStatusChanged** 


| **Parameter** | **Type** | **Description** | 
| --- | --- | --- | 
| status | NetworkConnectionStatus | The connection health status. One of "connected", "connecting", "disconnected", or "failed". | 
| timestamp | number | Epoch milliseconds when the status was reported. | 

 **Permissions required:** 

```
*
```