End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Get the IP address and port number of a custom app

To view your simulation, you create a custom app and connect to it with a client. For more information, see
the tutorials in [Getting started with SimSpace Weaver](getting-started.md "getting-started.md"). You can use the following
procedure to get the IP address and port number of your custom app. Use the appropriate path separator for
your operating system (for example, `\` in Windows and `/` in Linux).

###### To get your IP address and port number

1. Use the **ListSimulations** API to get the name of your simulation.

```
aws simspaceweaver list-simulations
```

Example output:

```


{
    "Simulations": [
        {
            "Status": "STARTED",
            "CreationTime": 1664921418.09,
            "Name": "MyProjectSimulation_22-10-04_22_10_15",
            "Arn": "arn:aws:simspaceweaver:us-west-2: 111122223333:simulation/MyProjectSimulation_22-10-04_22_10_15",
            "TargetStatus": "STARTED"
        }
    ]

}
```

2. Use the **DescribeSimulation** API to get a list of domains in your simulation.

```
aws simspaceweaver describe-simulation --simulation `simulation-name`
```

Look for the
`Domains` section in the `LiveSimulationState` section of the
output.

Example output:

```


    "LiveSimulationState": {
        "Domains": [
            {
                "Type": "",
                "Name": "MySpatialSimulation",
                "Lifecycle": "Unknown"
            },
            {
                "Type": "",
                "Name": "MyViewDomain",
                "Lifecycle": "ByRequest"
            }
        ],


```

3. Use the **ListApps** API to get a list of custom apps in a domain. For example, the domain name for the
   view (custom) app in the sample project is `MyViewDomain`.
   Look for the app name in the output.

```
aws simspaceweaver list-apps --simulation `simulation-name` --domain `domain-name`
```

Example output:

```


{
    "Apps": [
        {
            "Status": "STARTED",
            "Domain": "MyViewDomain",
            "TargetStatus": "STARTED",
            "Name": "ViewApp",
            "Simulation": "MyProjectSimulation_22-10-04_22_10_15"
        }
    ]
}


```

4. Use the **DescribeApp** API to get the IP address and port number. For the sample
   project, the domain name is `MyViewDomain` and the app name is `ViewApp`.

```
aws simspaceweaver describe-app --simulation `simulation-name` --domain `domain-name` --app `app-name`
```

The IP address and port number
are in the `EndpointInfo` block in the output. The IP address is the value
of `Address` and the port number is the value of `Actual`.

Example output:

```


{
    "Status": "STARTED",
    "Domain": "MyViewDomain",
    "TargetStatus": "STARTED",
    "Simulation": "MyProjectSimulation_22-10-04_22_10_15",
    "LaunchOverrides": {
        "LaunchCommands": []
    },
    "EndpointInfo": {
        "IngressPortMappings": [
            {
                "Declared": 7000,
                "Actual": 4321
            }
        ],
        "Address": "198.51.100.135"
    },
    "Name": "ViewApp"
}


```

###### Note

The value of `Declared`
is the port number that your app code should bind to. The value of `Actual` is the port
number that SimSpace Weaver exposes to clients to connect to your app. SimSpace Weaver maps the
`Declared` port to the `Actual` port.
