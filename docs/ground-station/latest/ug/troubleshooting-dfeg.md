# Troubleshoot DataflowEndpointGroups not in a HEALTHY

state

Listed below are the reasons your
dataflow endpoint groups may not be in a `HEALTHY` state as well as the appropriate corrective action to take.

- `NO_REGISTERED_AGENT` - Start your EC2 instance, which will register the agent. Note that you must have a valid controller config file
  for this call to be successful. Refer to the [Use AWS Ground Station Agent](how-it-works.md "how-it-works.md") for details on configuring that file.
- `INVALID_IP_OWNERSHIP` - Use the DeleteDataflowEndpointGroup API to delete the Dataflow Endpoint Group, then use the
  CreateDataflowEndpointGroup API to recreate the Dataflow Endpoint Group using IP addresses and ports that are associated with the EC2 instance.
- `UNVERIFIED_IP_OWNERSHIP` - IP address has not been validated yet. Validation occurs periodically so this should resolve itself.
- `NOT_AUTHORIZED_TO_CREATE_SLR` - Account is not authorized to create the necessary Service-Linked Role. Check the troubleshooting steps in [Use service-linked roles for
  Ground Station](using-service-linked-roles.md "using-service-linked-roles.md")
