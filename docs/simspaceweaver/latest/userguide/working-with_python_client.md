End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# The sample Python client

If you use the `PythonBubblesSample` template to create
a project then your project contains a Python sample client. You can use
the sample client to view the `PythonBubblesSample` simulation.
You can also use the sample client as the starting point to create your
own Python client.

The following procedure assumes that you created a
`PythonBubblesSample` project and started its
simulation.

###### To start the Python client

1. In a **command prompt window**,
   go to the `PyBubbleClient` sample project folder.

```
cd ``sdk-folder`\Clients\HTTP\PyBubbleClient`
```

2. Run the Python client.

```
python tkinter_client.py --host `ip-address` --port `port-number`
```

###### Parameters

**host**
The IP address of your simulation. For a simulation started in the AWS Cloud, you
can find your simulation's IP address in the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") or use the procedure in
[Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md")
of the quick start tutorial. For a local simulation, use `127.0.0.1` as the IP address.

**port**
The port number of your simulation. For a simulation started in the AWS Cloud, this
is the `Actual` port number. You can find your simulation's port number
in the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver") or use the procedure in
[Get the IP address and port number of a custom app](working-with_get-ip.md "working-with_get-ip.md")
of the quick start tutorial. For a local simulation, use `7000` as the port number.

**simsize**
The maximum number of entities to display in the client.
