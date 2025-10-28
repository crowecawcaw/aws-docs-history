End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Developing client applications

Some of the reasons you might want to connect a client to a simulation include:

- Inject real-time traffic information into a city-scale simulation.
- Create _human-in-the-loop_ simulations, where a human
  operator controls some aspect of the simulation.
- Make it possible for users to interact with the simulation, such as for a training simulation.
  The custom apps in these examples act as the interface between the simulation
  state and the outside world. Clients connect to the custom apps to interact with the
  simulation.

SimSpace Weaver doesn't handle the client applications and their communication with your
custom apps. You're responsible for the design, creation, operation, and security
of your client applications and their communication with your custom apps. SimSpace Weaver
only exposes an IP address and port number for each of your custom apps so that clients can
connect to them.

The SimSpace Weaver app SDK provides clients for its sample application. You can use
these clients as models for your own client applications. You can find the source
code for the sample application clients in the following folder:

Docker

```
`sdk-folder`\packaging-tools\clients\PathfindingSampleClients
```

WSL

###### Important

We provide these instructions for your convenience. They are for use with
Windows Subsystem for Linux (WSL), and are unsupported. For more information,
see [Set up your local environment for SimSpace Weaver](setting-up_local.md "setting-up_local.md").

```
`sdk-folder`/packaging-tools/clients/PathfindingSampleClients
```

For more information about building and using the sample application clients, see the tutorials in
[Getting started with SimSpace Weaver](getting-started.md "getting-started.md").
