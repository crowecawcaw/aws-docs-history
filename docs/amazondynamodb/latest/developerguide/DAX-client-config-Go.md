# Default client configuration for Go

This guide will walk you through the configuration options that allow you to
fine-tune your DAX client's performance, connection management, and logging
behavior. By understanding the default settings and how to customize them, you
can optimize your Go application's interaction with DAX.

###### In this section

- [DAX Go SDK Client Defaults](#DAX-client-config-Go-sdk-client-defaults "#DAX-client-config-Go-sdk-client-defaults")
- [Client creation](#DAX-client-config-Go-client-creation "#DAX-client-config-Go-client-creation")

## DAX Go SDK Client Defaults

| Parameter                                                       | Type                      | Description                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Region`<br>required                                            | `string`                  | The AWS Region to use for the DAX client (example-<br>'us-east-1'). This is a required parameter if not<br>provided through the environment.                                                                                                                                                                                                                                    |
| `HostPorts`<br>required                                         | `[] string`               | List of DAX cluster endpoints to which SDK connects.<br>For example:<br>Non-Encrypted –<br>dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com<br>Encrypted –<br>daxs://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com                                                                                                                                         |
| `MaxPendingConnectionsPerHost`<br>default 10                    | `number`                  | Number of concurrent connection attempts.<br>(Connections can be in the process of being established<br>concurrently.)                                                                                                                                                                                                                                                          |
| `ClusterUpdateThreshold`<br>default 125 \<br>• time.Millisecond | `time.Duration`           | The minimum time that must elapse between cluster<br>refreshes.                                                                                                                                                                                                                                                                                                                 |
| `ClusterUpdateInterval`<br>default 4 \<br>• time.Second         | `time.Duration`           | The interval at which the client will automatically<br>refresh the DAX cluster information.                                                                                                                                                                                                                                                                                     |
| `IdleConnectionsReapDelay`<br>default 30 \<br>• time.Second     | `time.Duration`           | The interval at which the client will close idle<br>connections in the DAX client.                                                                                                                                                                                                                                                                                              |
| `ClientHealthCheckInterval`<br>default 5 \<br>• time.Second     | `time.Duration`           | The interval at which the client will perform<br>health checks on the DAX cluster endpoints.                                                                                                                                                                                                                                                                                    |
| `Credentials`<br>default                                        | `aws.CredentialsProvider` | The AWS credentials used by the DAX client to<br>authenticate requests to the DAX service. See [Credentials and Credential<br>Providers](../../../sdk-for-go/v2/developer-guide/migrate-gosdk.md#credentials--credential-providers "../../../sdk-for-go/v2/developer-guide/migrate-gosdk.md#credentials--credential-providers").                                                |
| `DialContext`<br>default                                        | `func`                    | A custom function used by the DAX client to<br>establish connections to the DAX cluster.                                                                                                                                                                                                                                                                                        |
| `SkipHostnameVerification`<br>default false                     | bool                      | Skip hostname verification of TLS connections. This<br>setting only affects encrypted clusters. When set to<br>True, it disables hostname verification. Disabling<br>verification means you can't authenticate the identity<br>of the cluster you're connecting to, which poses<br>security risks. By default, hostname verification is<br>enabled.                             |
| `RouteManagerEnabled`<br>default false                          | `bool`                    | This flag is used to remove routes facing network<br>errors.                                                                                                                                                                                                                                                                                                                    |
| `RequestTimeout`<br>default 60 \<br>• time.Second               | `time.Duration`           | This defines the maximum time the client will wait<br>for a response from DAX.<br>Priority: Context timeout (if set) ><br>`RequestTimmeout` (if set) > Default<br>60s `RequestTimeout`.                                                                                                                                                                                         |
| `WriteRetries`<br>default 2                                     | `number`                  | The number of retries to attempt for write requests<br>that fail.                                                                                                                                                                                                                                                                                                               |
| `ReadRetries`<br>default 2                                      | `number`                  | The number of retries to attempt for read requests<br>that fail.                                                                                                                                                                                                                                                                                                                |
| `RetryDelay`<br>default 0                                       | `time.Duration`           | The delay for non-throttled errors (in seconds) for<br>retry attempts when a request fails.                                                                                                                                                                                                                                                                                     |
| `Logger`<br>optional                                            | `logging.Logger`          | Logger is an interface for logging entries at<br>certain classifications.                                                                                                                                                                                                                                                                                                       |
| `LogLevel`<br>default utils.LogOff                              | `number`                  | This loglevel is defined for DAX only. It can be<br>imported using [github.com/aws/aws-dax-go-v2/tree/main/dax/utils](https://github.com/aws/aws-dax-go-v2/tree/main/dax/utils "https://github.com/aws/aws-dax-go-v2/tree/main/dax/utils").<br>`<br>const (<br>LogOff LogLevelType = 0<br>LogDebug LogLevelType = 1<br>LogDebugWithRequestRetries<br>LogLevelType = 2<br>)<br>` |

###### Note

For `time.Duration`, the default unit is nanosecond. If we
don’t specify any unit for any parameter then it will consider that as
nano seconds: `daxCfg.ClusterUpdateInterval = 10` means 10
nano seconds. (`daxCfg.ClusterUpdateInterval = 10 *
 time.Millisecond` means 10 milliseconds).

## Client creation

###### To create a DAX client:

- Create DAX config, then create DAX client using DAX config.
  Using this, you can overwrite a DAX configuration if
  required.

```
import (
"github.com/aws/aws-dax-go-v2/dax/utils"
"github.com/aws/aws-dax-go-v2/dax"
)

// Non - Encrypted : 'dax://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com'.
// Encrypted : daxs://my-cluster.l6fzcv.dax-clusters.us-east-1.amazonaws.com'.

config := dax.DefaultConfig()
config.HostPorts = []string{endpoint}
config.Region = region
config.LogLevel = utils.LogDebug
daxClient, err := dax.New(config)
```
