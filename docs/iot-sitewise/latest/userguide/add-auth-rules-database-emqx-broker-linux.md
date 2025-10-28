# Configure

authorization using the built-in database with Linux

When you configure authorization rules, there are two configuration
choices that depend on your deployment setup.

- **Docker** – If
  you're running a standard Docker installation without
  Litmus Edge, use the **Docker bridge gateway**
  configuration. This is typically the case when you've only deployed
  AWS IoT SiteWise components.
- **Litmus Edge** – If you have
  Litmus Edge installed on your gateway, use the
  **Litmus Edge network subnet**
  configuration.

###### Note

If you initially configure the Docker bridge gateway
and later install Litmus Edge, reconfigure the authorization rules
using the Litmus Edge network subnet option to ensure proper
communication between all components.

###### To add basic authorization rules

1. Verify that the EMQX broker is deployed and running.
2. Start a shell session on your gateway host.

Docker without Litmus
Edge
For standard Docker installation
without Litmus Edge, run:

```
/greengrass/v2/bin/swe-emqx-cli acl init
```

Litmus Edge network subnet
If you're using Litmus Edge, determine
the Litmus Edge network subnet IP:

```
docker network inspect LitmusNetwork | grep IPAM -A9
```

Note the Subnet value from the output and run the
following command. Replace `litmus_subnet_ip`
with the Subnet value from the previous step.

```
/greengrass/v2/bin/swe-emqx-cli acl init `litmus_subnet_ip`
```

The tool automatically creates and applies authorization rules to
allow connections from the provided IP address to the broker. It
allows access to all topics. This includes the
IoT SiteWise OPC UA collector and IoT SiteWise publisher. 3. Proceed to [Update the EMQX
deployment configuration for authorization](update-emqx-broker-authorization.md "update-emqx-broker-authorization.md").
