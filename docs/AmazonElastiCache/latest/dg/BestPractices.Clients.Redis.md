# Configure a server-side idle timeout (Valkey and Redis OSS)

We have observed cases when a customer's application has a high number of idle clients connected, but isn't actively sending commands. In such scenarios, you can exhaust all 65,000 connections with a high number of idle clients.
To avoid such scenarios, configure the timeout setting appropriately on the server via [Valkey and Redis OSS parameters](ParameterGroups.md#ParameterGroups.Redis "ParameterGroups.md#ParameterGroups.Redis"). This ensures that the server actively disconnects idle clients to avoid
an increase in the number of connections. This setting is not available on serverless caches.
