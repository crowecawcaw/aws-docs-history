# Verifying the Connection Gateway connectivity

Let's assume that the Connection Gateway host is associated with a DNS name, for instance `dcv.gateway.domain`,
and it is listening on TCP port `8443` and UDP port `8443`. We can use the `nc` command
to test the connectivity of our gateway.

###### To check if the Connection Gateway is reacheable with TCP

Use the following command:

```
`$` nc -vz dcv.gateway.domain 8443
```

###### To check if the Connection Gateway is reacheable with UDP

Use the following command:

```
`$` nc -uvz dcv.gateway.domain 8443
```
