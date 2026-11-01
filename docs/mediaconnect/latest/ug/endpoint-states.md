

# MediaConnect endpoint states
<a name="endpoint-states"></a>

Each MediaConnect endpoint has a registration state and a connection state. The registration state shows whether the endpoint is in your endpoint registry. The connection state shows whether the endpoint is connected to another endpoint.

## Registration states
<a name="endpoint-registration-states"></a>

The following illustration shows how the registration state changes from the moment you register an endpoint to the moment you deregister it.

![State diagram showing MediaConnect endpoint registration states. An endpoint starts in Registering and moves to Registered or Registration failed. Both states lead to Deregistering, after which the endpoint no longer exists.](https://docs.aws.amazon.com/mediaconnect/latest/ug/images/endpoint-registration-states.png)


**Registering**  
MediaConnect is registering the endpoint.

**Registered**  
The endpoint is in your endpoint registry and is ready to connect.

**Registration failed**  
MediaConnect couldn't register the endpoint. To remove the endpoint, deregister it.

**Deregistering**  
MediaConnect is removing the endpoint from your endpoint registry. After this state, the endpoint no longer exists.

## Connection states
<a name="endpoint-connection-states"></a>

The following illustration shows how the connection state changes as you connect and disconnect an endpoint.

![State diagram showing MediaConnect endpoint connection states. An endpoint enters Disconnected when it is registered, moves through Connecting to Connected, and returns through Disconnecting to Disconnected.](https://docs.aws.amazon.com/mediaconnect/latest/ug/images/endpoint-connection-states.png)


**Disconnected**  
The endpoint isn't connected to another endpoint. An endpoint is in this state after you register or disconnect it.

**Connecting**  
MediaConnect is connecting the endpoint to another endpoint.

**Connected**  
The endpoint is connected to another endpoint, and content can flow between them.

**Disconnecting**  
MediaConnect is disconnecting the endpoint from another endpoint.