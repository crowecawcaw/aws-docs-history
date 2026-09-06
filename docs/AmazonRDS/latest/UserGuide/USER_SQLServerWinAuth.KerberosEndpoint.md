

# Creating the endpoint for Kerberos authentication
<a name="USER_SQLServerWinAuth.KerberosEndpoint"></a>

Kerberos-based authentication requires that the endpoint be the customer-specified host name, a period, and then the fully qualified domain name (FQDN). For example, the following is an example of an endpoint you might use with Kerberos-based authentication. In this example, the SQL Server DB instance host name is `ad-test` and the domain name is `corp-ad.company.com`. 

```
ad-test.corp-ad.company.com
```

If you want to make sure your connection is using Kerberos, run the following query: 

```
1. SELECT net_transport, auth_scheme 
2.   FROM sys.dm_exec_connections 
3.  WHERE session_id = @@SPID;
```