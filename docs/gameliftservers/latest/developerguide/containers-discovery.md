

# Discover containers on a container fleet
<a name="containers-discovery"></a>

On an Amazon GameLift Servers container fleet, each instance can run multiple containers. For example, you can run several replicas of your game server container group. You can also run a per-instance container group that provides shared, instance-wide services.

The container discovery server enables your game server processes to discover the other containers running on the same instance. Containers can then communicate with one another across container group definitions over the instance's local network.

The discovery server is a lightweight HTTP service. Amazon GameLift Servers runs it locally on every container fleet instance. The service provides the following network information for each container running on that instance:
+ The container name that you define in the container group definition.
+ The unique identifier of the container.
+ The container's local IP address on the instance.
+ The container group type, either `GAME_SERVER` (a replica of the game server container group) or `PER_INSTANCE` (the per-instance container group).

**Note**  
The container discovery server is only available on managed container fleets.

## Retrieve container network information
<a name="containers-discovery-retrieve"></a>

You can retrieve container network information in two ways: from a game server process with the Amazon GameLift Servers server SDK, or from any container by calling the discovery server directly over HTTP.

### Retrieve container information using the server SDK
<a name="containers-discovery-retrieve-sdk"></a>

If your game server process uses the Amazon GameLift Servers server SDK, call the `ListContainersNetworkInfo()` action to retrieve container network information. The server SDK locates the discovery server and makes the request for you. The action returns the network information for every container running on the same instance. On any other compute type, the action returns an unsupported compute type error.

`ListContainersNetworkInfo()` is available in server SDK version 5.5 or later for the following languages:
+ [ListContainersNetworkInfo()](integration-server-sdk-go-actions.md#integration-server-sdk-go-listcontainersnetworkinfo) (Go)
+ [ListContainersNetworkInfo()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-listcontainersnetworkinfo) (C\+\+)
+ [ListContainersNetworkInfo()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-listcontainersnetworkinfo) (C\#)

The action is also available in the Amazon GameLift Servers plugins for Unreal Engine and Unity.

### Retrieve container information by calling the discovery server directly
<a name="containers-discovery-retrieve-direct"></a>

Some containers don't use the server SDK, such as per-instance containers. These containers call the discovery server directly over HTTP. Amazon GameLift Servers pre-sets the `GAMELIFT_CONTAINER_DISCOVERY_SERVER_ENDPOINT_V1` environment variable in these containers. This variable holds the address of the discovery server, including the API version path, and it's set in both the game server and per-instance container group definitions.

To retrieve container network information, send an HTTP `GET` request to this endpoint. The following example uses `curl`:

```
curl "$GAMELIFT_CONTAINER_DISCOVERY_SERVER_ENDPOINT_V1"
```

The discovery server returns a JSON array with one entry for each container running on the instance:

```
[
  {
    "containerName": "game-server",
    "ipAddress": "172.17.0.3",
    "containerId": "b896159563df43736e5e93ad0547a24fa572648d55b70c70747642afca398b18",
    "containerGroupType": "GAME_SERVER"
  },
  {
    "containerName": "per-instance",
    "ipAddress": "172.17.0.4",
    "containerId": "3c239ae037aec28bb42212ffa2b9e02524c0c4c361db9bc31dd4c5aecc0b7943",
    "containerGroupType": "PER_INSTANCE"
  }
]
```

## Request rate limits
<a name="containers-discovery-throttling"></a>

The discovery server limits each container on the instance to 10 requests per second. It throttles requests that exceed this limit and returns an error. To stay within this limit, query the discovery server once at startup. As an alternative, query it only when you need to refresh your view of the instance. Cache the results in your container and reuse the cached values rather than querying the discovery server on a recurring basis.

Periodically refresh your cache to keep it current. A container's local IP address can change if the container crashes or exits (for example, when its game session ends).

## Example: collecting metrics from game server containers
<a name="containers-discovery-example"></a>

A common use of the discovery server is to send telemetry between containers on the same instance without leaving the instance's local network. Consider a fleet that runs multiple game server containers (`GAME_SERVER`) and a single per-instance container (`PER_INSTANCE`). The per-instance container runs a metrics collector that all of the game servers on the instance share.

You can implement metrics collection with either a push model or a pull model:
+ **Push (metrics emission)** – At startup, each game server container calls `ListContainersNetworkInfo()`. The container finds the entry with the `PER_INSTANCE` container group type. It then reads the local IP address from that entry. The game server sends its metrics directly to the per-instance collector over the instance's local network.
+ **Pull (metrics scraping)** – The reverse approach also works. The per-instance container doesn't use the server SDK, so it calls the discovery server endpoint directly. It finds the IP addresses of all `GAME_SERVER` containers on the instance. It then scrapes a metrics endpoint that each game server container exposes over the local network.

In both cases, communication stays on the instance's local network. Each container queries the discovery server only occasionally rather than on a recurring basis.

## Related topics
<a name="containers-discovery-related"></a>
+ [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md)
+ [Create a container group definition for an Amazon GameLift Servers container fleet](containers-create-groups.md)
+ [Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md)
+ [How containers work in Amazon GameLift Servers](containers-howitworks.md)