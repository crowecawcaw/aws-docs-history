End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Debugging simulations

You can use the following methods to get information about your simulations.

###### Topics

- [Use SimSpace Weaver Local and look at console output](#working-with_debugging_use-local "#working-with_debugging_use-local")
- [Look at your logs in Amazon CloudWatch Logs](#working-with_debugging_logs "#working-with_debugging_logs")
- [Use describe API calls](#working-with_debugging_api "#working-with_debugging_api")
- [Connect a client](#working-with_debugging_client "#working-with_debugging_client")

## Use SimSpace Weaver Local and look at console output

We recommend that you develop your simulations locally first and then run
them in the AWS Cloud. You can view console output directly when you
run with SimSpace Weaver Local. For more information, see
[Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").

## Look at your logs in Amazon CloudWatch Logs

When you run your simulation in the AWS Cloud the console output
of your apps is sent to log streams in Amazon CloudWatch Logs. Your simulation also
writes other log data. You must enable logging in your simulation schema
if you want your simulation to write log data. For more information,
see [SimSpace Weaver logs in Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md").

###### Warning

Your simulation can produce
large amounts of log data. The log data can grow very quickly. You
should watch your logs closely and stop your simulations when you don't
need them running anymore. Logging can create large costs.

## Use describe API calls

You can use the following service APIs to get information about your simulations
in the AWS Cloud.

- ListSimulations – get
  a list of all of your simulations in the AWS Cloud.

###### Example

```
aws simspaceweaver list-simulations
```

- DescribeSimulation – get
  details about a simulation.

###### Example

```
aws simspaceweaver describe-simulation --simulation MySimulation
```

- DescribeApp – get
  details about an app.

###### Example

```
aws simspaceweaver describe-app --simulation MySimulation --domain MyCustomDomain --app MyCustomApp
```

For more information about the SimSpace Weaver APIs, see [SimSpace Weaver API references](api-reference.md "api-reference.md").

## Connect a client

You can connect a client to a running custom or service app that you defined with an
`endpoint_config` in your simulation schema. The SimSpace Weaver app SDK includes
sample clients that you can use to view the sample application. You can look at the
source code for these sample clients and the sample application to see how you can
create your own clients. For more information about how to build and run the sample
clients, see the tutorials in [Getting started with SimSpace Weaver](getting-started.md "getting-started.md").

You can find the source code for the sample clients in the following folder:

- ``sdk-folder`\packaging-tools\clients\PathfindingSampleClients\`
