# Host network mode

In `host` mode, tasks share the host's network namespace directly. The
container's networking configuration is tied to the underlying Amazon ECS Managed Instances host
instance that you specify using the `networkConfiguration` parameter when you
create an Amazon ECS Managed Instances capacity provider.

There are significant drawbacks to using this network mode. You can’t run more than a
single instantiation of a task on each host. This is because only the first task can
bind to its required port on the Amazon EC2 instance. There's also no way to remap a
container port when it's using `host` network mode. For example, if an
application needs to listen on a particular port number, you can't remap the port number
directly. Instead, you must manage any port conflicts through changing the application
configuration.

There are also security implications when using the `host` network mode.
This mode allows containers to impersonate the host, and it allows containers to connect
to private loopback network services on the host.

Use host mode only when you need direct access to host networking or when migrating
applications that require host-level network access.
