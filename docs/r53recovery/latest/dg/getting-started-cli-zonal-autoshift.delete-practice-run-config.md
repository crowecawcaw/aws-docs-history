# Delete a practice run configuration

You can delete a practice run configuration for a resource, but you must first disable zonal
autoshift for the resource. A resource is required to have a practice run configuration to have zonal
autoshift enabled. Regular practice runs help you to make sure that your application can run normally without one
Availability Zone.

To delete a practice run configuration by using the CLI, first, disable zonal autoshift, if needed
by using the `update-zonal-autoshift` command. Then, to delete the practice run configuration, use the
`delete-practice-run-configuration` command.

First, disable zonal autoshift for the resource, using a command like the following:

```
aws arc-zonal-shift update-zonal-autoshift-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:`Region`:`111122223333`:`ExampleALB123456890`" \
      --zonal-autoshift-status="DISABLED"
```

```
{
   "resourceIdentifier": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "zonalAutoshiftStatus": "DISABLED"
}
```

Then, delete the practice run configuration, using a command like the following:

```
aws arc-zonal-shift delete-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:`Region`:`111122223333`:`ExampleALB123456890`"
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "TestResource",
   "zonalAutoshiftStatus": "DISABLED"
}
```
