End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Step 2: View your local simulation

To view your local simulation, you can use any of the clients that are included with the
SimSpaceWeaverAppSdkDistributable. For more information on building and using the
sample clients, see the tutorials in [Getting started with SimSpace Weaver](getting-started.md "getting-started.md").

You must update the IP address and port number in the client to connect to the view app
for your local simulation. Always use the following values with SimSpace Weaver Local:

```
tcp://127.0.0.1:7000
```

Depending on the client you select, you can update the IP address and port number as follows:

- Unreal – Change the URL on line 1 of `view_app_url.txt`
- Console – Launch the client with the IP address and port number URL as a parameter
