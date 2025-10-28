# Configure

authorization using the built-in database with Windows

This section covers configuring authorization rules using the built-in
database for Windows deployments.

###### To add basic authorization rules

1. Verify that the EMQX broker is deployed and running.
2. Run the AWS IoT SiteWise EMQX CLI tool:

```
C:\greengrass\v2\bin\swe-emqx-cli.ps1 acl init
```

The tool automatically creates and applies ACL rules allowing
connections from localhost (127.0.0.1) to the broker. It allows
access to all topics. This includes the IoT SiteWise OPC UA collector and
IoT SiteWise publisher. 3. Proceed to [Update the EMQX
deployment configuration for authorization](update-emqx-broker-authorization.md "update-emqx-broker-authorization.md").
