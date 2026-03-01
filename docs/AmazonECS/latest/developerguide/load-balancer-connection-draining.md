# Optimize load balancer connection draining parameters for Amazon ECS

To allow for optimization, clients maintain a keep alive connection to the container
service. This allows subsequent requests from that client to reuse the existing
connection. When you want to stop traffic to a container, you notify the load balancer.
The load balancer periodically checks to see if the client closed the keep alive
connection. Amazon ECS monitors the load balancer, and waits for the load balancer
to report that the keep alive connection is closed (the target is in an
`UNUSED` state).

The amount of time that the load balancer waits to move the target to the
`UNUSED` state is the deregistration delay. You can configure the
following load balancer parameter to speed up your deployments.

- `deregistration_delay.timeout_seconds`: 300 (default)
  When you have a service with a response time that's under 1 second, set the parameter to
  the following value to have the load balancer only wait 5 seconds before it breaks the
  connection between the client and the back-end service:

- `deregistration_delay.timeout_seconds`: 5

###### Note

Do not set the value to 5 seconds when you have a service with long-lived
requests, such as slow file uploads or streaming connections.

## SIGTERM responsiveness

Amazon ECS first sends a stop signal to the task to notify the application needs to
finish and shut down. This signal can be defined in your container image with the STOPSIGNAL instruction
and will default to SIGTERM. Then, Amazon ECS sends a SIGKILL message. When applications ignore
the SIGTERM, the Amazon ECS service must wait to send the SIGKILL signal to terminate the
process.

The amount of time that Amazon ECS waits to send the SIGKILL message is determined by
the following Amazon ECS agent option:

- `ECS_CONTAINER_STOP_TIMEOUT`: 30 (default)

For more information about the container agent parameter, see [Amazon ECS Container Agent](https://github.com/aws/amazon-ecs-agent/blob/master/README.md "https://github.com/aws/amazon-ecs-agent/blob/master/README.md") on GitHub.

To speed up the waiting period, set the Amazon ECS agent parameter to the following
value:

- `ECS_CONTAINER_STOP_TIMEOUT`: 2

If your application takes more than 1 second, multiply the value by 2 and use
that number as the value.

In this case, the Amazon ECS waits 2 seconds for the container to shut down, and then
Amazon ECS sends a SIGKILL message when the application didn't stop.

You can also modify the application code to trap the SIGTERM signal and react to
it. The following is example in JavaScript:

```
process.on('SIGTERM', function() {
  server.close();
})
```

This code causes the HTTP server to stop listening for any new requests, finish
answering any in-flight requests, and then the Node.js process terminates because the
event loop has nothing to do. Given this, if it takes the process only 500 ms to finish
its in-flight requests, it terminates early without having to wait out the stop timeout
and get sent a SIGKILL.
