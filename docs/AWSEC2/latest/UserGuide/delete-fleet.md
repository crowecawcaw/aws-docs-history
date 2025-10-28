# Delete an EC2 Fleet request and the instances in the

fleet

If you no longer require an EC2 Fleet request, you can delete it. After you delete a fleet
request, all Spot requests associated with the fleet are canceled, so that no new Spot Instances
are launched.

When you delete an EC2 Fleet request, you must also specify if you want to terminate all of
its instances. These include both On-Demand Instances and Spot Instances. For `instant` fleets,
EC2 Fleet must terminate the instances when the fleet is deleted. A deleted
`instant` fleet with running instances is not supported.

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

If you specify that the instances must be terminated when the fleet request is deleted, the
fleet request enters the `deleted_terminating` state. Otherwise, it enters
the `deleted_running` state, and the instances continue to run until they are
interrupted or you terminate them manually.

###### Restrictions

- You can delete up to 25 fleets of type `instant` in a single
  operation.
- You can delete up to 100 fleets of type `maintain` or
  `request` in a single operation.
- You can delete up to 125 fleets in a single operation, provided you do not
  exceed the quota for each fleet type, as specified above.
- If you exceed the specified number of fleets to delete, no fleets are
  deleted.
- A deleted `instant` fleet with running instances is not supported.
  When you delete an `instant` fleet, Amazon EC2 automatically terminates
  all its instances. For `instant` fleets with more than 1000
  instances, the deletion request might fail. If your fleet has more than 1000
  instances, first terminate most of the instances manually, leaving 1000 or
  fewer. Then delete the fleet, and the remaining instances will be terminated
  automatically.

AWS CLI

###### To delete an EC2 Fleet request and terminate its instances

Use the [delete-fleets](../../../cli/latest/reference/ec2/delete-fleets.md "../../../cli/latest/reference/ec2/delete-fleets.md")
command with the `--terminate-instances` option.

```
aws ec2 delete-fleets \
    --fleet-ids `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --terminate-instances
```

The following is example output.

```
{
    "UnsuccessfulFleetDeletions": [],
    "SuccessfulFleetDeletions": [
        {
            "CurrentFleetState": "deleted_terminating",
            "PreviousFleetState": "active",
            "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
        }
    ]
}
```

###### To delete an EC2 Fleet request without terminating its instances

Modify the previous example by using the `--no-terminate-instances`
option instead. Note that `--no-terminate-instances` is not supported for
`instant` fleets.

```
aws ec2 delete-fleets \
    --fleet-ids `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --no-terminate-instances
```

The following is example output.

```
{
    "UnsuccessfulFleetDeletions": [],
    "SuccessfulFleetDeletions": [
        {
            "CurrentFleetState": "deleted_running",
            "PreviousFleetState": "active",
            "FleetId": "fleet-4b8aaae8-dfb5-436d-a4c6-3dafa4c6b7dcEXAMPLE"
        }
    ]
}
```

PowerShell

###### To delete an EC2 Fleet request and terminate its instances

Use the [Remove-EC2Fleet](../../../powershell/latest/reference/items/Remove-EC2Fleet.md "../../../powershell/latest/reference/items/Remove-EC2Fleet.md")
cmdlet with the `-TerminateInstance` parameter.

```
Remove-EC2Fleet `
    -FleetId "`fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`" `
    -TerminateInstance $true
```

###### To delete an EC2 Fleet request without terminating its instances

Modify the previous example by changing the value of the
`-TerminateInstance` parameter.

```
Remove-EC2Fleet `
    -FleetId "`fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`" `
    -TerminateInstance $false
```

## Troubleshoot when a fleet fails to

delete

If an EC2 Fleet request fails to delete, `UnsuccessfulFleetDeletions` in the output
returns the ID of the EC2 Fleet request, an error code, and an error message.

The error codes are:

- `ExceededInstantFleetNumForDeletion`
- `fleetIdDoesNotExist`
- `fleetIdMalformed`
- `fleetNotInDeletableState`
- `NoTerminateInstancesNotSupported`
- `UnauthorizedOperation`
- `unexpectedError`

###### Troubleshoot `ExceededInstantFleetNumForDeletion`

If you try to delete more than 25 `instant` fleets in a single
request, the `ExceededInstantFleetNumForDeletion` error is returned.
The following is example output for this error.

```
{
    "UnsuccessfulFleetDeletions": [
     {
          "FleetId": " fleet-5d130460-0c26-bfd9-2c32-0100a098f625",
          "Error": {
                  "Message": "Can’t delete more than 25 instant fleets in a single request.",
                  "Code": "ExceededInstantFleetNumForDeletion"
           }
     },
     {
           "FleetId": "fleet-9a941b23-0286-5bf4-2430-03a029a07e31",
           "Error": {
                  "Message": "Can’t delete more than 25 instant fleets in a single request.",
                  "Code": "ExceededInstantFleetNumForDeletion"
            }
     }
     .
     .
     .
     ],
     "SuccessfulFleetDeletions": []
}
```

###### Troubleshoot `NoTerminateInstancesNotSupported`

If you specify that the instances in an `instant` fleet must not be
terminated when you delete the fleet, the
`NoTerminateInstancesNotSupported` error is returned.
`--no-terminate-instances` is not supported for
`instant` fleets. The following is example output for this
error.

```
{
      "UnsuccessfulFleetDeletions": [
            {
                  "FleetId": "fleet-5d130460-0c26-bfd9-2c32-0100a098f625",
                  "Error": {
                          "Message": "NoTerminateInstances option is not supported for instant fleet",
                          "Code": "NoTerminateInstancesNotSupported"
                   }
            }
       ],
       "SuccessfulFleetDeletions": []
}
```

###### Troubleshoot `UnauthorizedOperation`

If you do not have permission to terminate instances, you get the
`UnauthorizedOperation` error when deleting a fleet that must
terminate its instances. The following is the error response.

```
<Response><Errors><Error><Code>UnauthorizedOperation</Code><Message>You are not authorized to perform this
operation. Encoded authorization failure message: VvuncIxj7Z_CPGNYXWqnuFV-YjByeAU66Q9752NtQ-I3-qnDLWs6JLFd
KnSMMiq5s6cGqjjPtEDpsnGHzzyHasFHOaRYJpaDVravoW25azn6KNkUQQlFwhJyujt2dtNCdduJfrqcFYAjlEiRMkfDHt7N63SKlweKUl
BHturzDK6A560Y2nDSUiMmAB1y9UNtqaZJ9SNe5sNxKMqZaqKtjRbk02RZu5V2vn9VMk6fm2aMVHbY9JhLvGypLcMUjtJ76H9ytg2zRlje
VPiU5v2s-UgZ7h0p2yth6ysUdhlONg6dBYu8_y_HtEI54invCj4CoK0qawqzMNe6rcmCQHvtCxtXsbkgyaEbcwmrm2m01-EMhekLFZeJLr
DtYOpYcEl4_nWFX1wtQDCnNNCmxnJZAoJvb3VMDYpDTsxjQv1PxODZuqWHs23YXWVywzgnLtHeRf2o4lUhGBw17mXsS07k7XAfdPMP_brO
PT9vrHtQiILor5VVTsjSPWg7edj__1rsnXhwPSu8gI48ZLRGrPQqFq0RmKO_QIE8N8s6NWzCK4yoX-9gDcheurOGpkprPIC9YPGMLK9tug
</Message></Error></Errors><RequestID>89b1215c-7814-40ae-a8db-41761f43f2b0</RequestID></Response>
```

To resolve the error, you must add the `ec2:TerminateInstances` action
to the IAM policy, as shown in the following example.
