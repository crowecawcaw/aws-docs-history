# Monitoring interactive endpoints

With Amazon EMR on EKS version 6.10 and later, interactive endpoints emit Amazon CloudWatch metrics for
monitoring and troubleshooting kernel lifecycle operations. Metrics are triggered by
interactive clients, such as EMR Studio or self-hosted Jupyter notebooks. Each of the
operations supported by interactive endpoints have metrics associated with them. The
operations are modeled as dimensions to each metric, as shown in the table below. Metrics
emitted by interactive endpoints are visible under a custom namespace, EMRContainers, in your
account.

| Metric              | Description                                                                                                                                                        | Unit        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| RequestCount        | Cumulative number of requests of an operation processed by the interactive<br>endpoint.                                                                            | Count       |
| RequestLatency      | The time from when a request arrived at the interactive endpoint and a response<br>was sent by the interactive endpoint.                                           | Millisecond |
| 4XXError            | Emitted when a request for an operation results in a 4xx error during<br>processing.                                                                               | Count       |
| 5XXError            | Emitted when a request for an operation results in a 5Xxx server side<br>error.                                                                                    | Count       |
| KernelLaunchSuccess | Applicable only for the CreateKernel operation. It indicates the cumulative<br>number of kernel launches that were successful up to and including this<br>request. | Count       |
| KernelLaunchFailure | Applicable only for the CreateKernel operation. It indicates the cumulative<br>number of kernel launch failures up until and including this request.               | Count       |

Each interactive endpoint metric has the following dimensions attached to it:

- **`ManagedEndpointId`** – Identifier
  for the interactive endpoint
- **`OperationName`** – The operation
  triggered by the interactive client
  Possible values for the **`OperationName`**
  dimension are shown in the following table:

| `operationName`         | Operation description                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `CreateKernel`          | Request that the interactive endpoint start a kernel.                                                                                |
| `ListKernels`           | Request that the interactive endpoint list the kernels that have been previously<br>started using the same session token.            |
| `GetKernel`             | Request that the interactive endpoint get details about a specific kernel that<br>has been previously started.                       |
| `ConnectKernel`         | Request that the interactive endpoint establish connectivity between the<br>notebook client and the kernel.                          |
| `ConfigureKernel`       | Publish `%%configure magic request` on a pyspark kernel.                                                                             |
| `ListKernelSpecs`       | Request that the interactive endpoint list the available kernel specs.                                                               |
| `GetKernelSpec`         | Request that the interactive endpoint get the kernel specs of a kernel that has<br>been previously launched.                         |
| `GetKernelSpecResource` | Request that the interactive endpoint get specific resources associated with the<br>kernel specs that have been previously launched. |

## Examples

### To access the total number of kernels launched for an

interactive endpoint on a given day:

1. Select the custom namespace: `EMRContainers`
2. Select your `ManagedEndpointId`, `OperationName –
CreateKernel`
3. `RequestCount` metric with the statistic `SUM` and period
   `1 day` will provide all the kernel launch requests made in the last 24
   hours.
4. KernelLaunchSuccess metric with statistic `SUM` and period `1
day` will provide all the successful kernel launch requests made in the last
   24 hours.

### To access the number of kernel failures for an interactive

endpoint on a given day:

1. Select the custom namespace: EMRContainers
2. Select your `ManagedEndpointId`, `OperationName –
CreateKernel`
3. `KernelLaunchFailure` metric with statistic `SUM` and period
   `1 day` will provide all the failed kernel launch requests made in the
   last 24 hours. You can also select the `4XXError` and `5XXError`
   metric to know what kind of kernel launch failure happened.
