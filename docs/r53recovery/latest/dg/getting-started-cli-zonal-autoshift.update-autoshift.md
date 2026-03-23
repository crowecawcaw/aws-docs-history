# Enable or disable autoshifts

You enable or disable autoshifts for a resource by updating the zonal autoshift status with the CLI.
To change the zonal autoshift status, use the `update-zonal-autoshift-configuration` command.

For example, to enable autoshifts for a resource, use a command like the following:

```
aws arc-zonal-shift update-zonal-autoshift-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:`Region`:`111122223333`:`ExampleALB123456890`" \
      --zonal-autoshift-status="ENABLED"
```

```
{
   "resourceIdentifier": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "zonalAutoshiftStatus": "ENABLED"
}
```
