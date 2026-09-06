

# Create a new connection after failover
<a name="best-practices-gremlin-java-new-connection"></a>

In case of failover, the Gremlin Driver might continue connecting to the old writer because the cluster DNS name is resolved to an IP address. If this occurs, you can create a new `Client` object after failover.