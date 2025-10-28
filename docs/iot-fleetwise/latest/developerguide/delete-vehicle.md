# Delete an AWS IoT FleetWise vehicle

You can use the AWS IoT FleetWise console or API to delete vehicles.

###### Important

After a vehicle is deleted, AWS IoT FleetWise automatically removes the vehicle from the
associated fleets and campaigns. For more information, see [Manage fleets in AWS IoT FleetWise](fleets.md "fleets.md") and [Collect AWS IoT FleetWise data with campaigns](campaigns.md "campaigns.md"). However, the vehicle still exists as a thing or is still associated with a thing
in AWS IoT Core. For instructions on deleting a thing, see [Delete a
thing](../../../iot/latest/developerguide/thing-registry.md#delete-thing "../../../iot/latest/developerguide/thing-registry.md#delete-thing") in the _AWS IoT Core Developer Guide_.

## Delete a vehicle (console)

You can use the AWS IoT FleetWise console to delete a vehicle.

###### To delete a vehicle

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Vehicles**.
3. On the **Vehicles** page, select the button next to the
   vehicle you want to delete.
4. Choose **Delete**.
5. In **Delete `vehicle-name`**, enter
   the name of the vehicle, and then choose **Delete**.

## Delete a vehicle (AWS CLI)

You can use the [DeleteVehicle](../APIReference/API_DeleteVehicle.md "../APIReference/API_DeleteVehicle.md")
API operation to delete a vehicle. The following example uses AWS CLI.

To delete a vehicle, run the following command.

Replace `vehicle-name` with the ID of the vehicle that you
want to delete.

```
aws iotfleetwise delete-vehicle --vehicle-name `vehicle-name`
```

### Verify vehicle deletion

You can use the [ListVehicles](../APIReference/API_ListVehicles.md "../APIReference/API_ListVehicles.md")
API operation to verify if a vehicle was deleted. The following example uses the
AWS CLI.

To retrieve a paginated list of summaries of all vehicles, run the following
command.

```
aws iotfleetwise list-vehicles
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `ListVehicles` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
