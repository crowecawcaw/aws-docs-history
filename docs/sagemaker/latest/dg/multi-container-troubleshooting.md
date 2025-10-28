# Troubleshoot multi-container

endpoints

The following sections can help you troubleshoot errors with multi-container
endpoints.

## Ping Health Check Errors

With multiple containers, endpoint memory and CPU are under higher pressure
during endpoint creation. Specifically, the `MemoryUtilization` and
`CPUUtilization` metrics are higher than for single-container
endpoints, because utilization pressure is proportional to the number of containers.
Because of this, we recommend that you choose instance types with enough memory and
CPU to ensure that there is enough memory on the instance to have all the models
loaded (the same guidance applies to deploying an inference pipeline). Otherwise,
your endpoint creation might fail with an error such as `XXX did not pass the
 ping health check`.

## Missing accept-bind-to-port=true

Docker label

The containers in a multi-container endpoints listen on the port specified in the
`SAGEMAKER_BIND_TO_PORT` environment variable instead of port 8080.
When a container runs in a multi-container endpoint, SageMaker AI automatically provides
this environment variable to the container. If this environment variable isn't
present, containers default to using port 8080. To indicate that your container
complies with this requirement, use the following command to add a label to your
Dockerfile:

```

LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true

```

Otherwise, You will see an error message such as `Your Ecr Image XXX does
 not contain required
 com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true Docker
 label(s).`

If your container needs to listen on a second port, choose a port in the range
specified by the `SAGEMAKER_SAFE_PORT_RANGE` environment variable.
Specify the value as an inclusive range in the format
`XXXX`-`YYYY`, where XXXX and
YYYY are multi-digit integers. SageMaker AI provides this value automatically when you run
the container in a multi-container endpoint.
