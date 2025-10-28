# Change the placement for an EC2 instance

You can change the placement group for an instance as follows:

- Add an instance to a placement group
- Move an instance from one placement group to another
- Remove an instance from a placement group

###### Requirement

Before you can change the placement group for an instance, the instance must be in the
`stopped` state.

Console

###### To change the instance placement

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance.
4. Choose **Actions**,
   **Instance settings**,
   **Modify instance placement**.
5. For **Placement group**, do one of the
   following:
   - To add the instance to a placement group, choose
     the placement group.
   - To move the instance from one placement group to another,
     choose the placement group.
   - To remove the instance from the placement group, choose
     **None**.

6. Choose **Save**.

AWS CLI

###### To move an instance to a placement group

Use the following [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") command.

```
aws ec2 modify-instance-placement \
    --instance-id `i-0123a456700123456` \
    --group-name `MySpreadGroup`
```

###### To remove an instance from a placement group

Use the following [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") command. When you specify
an empty string for the placement group name, this removes
the instance from its current placement group.

```
aws ec2 modify-instance-placement \
    --instance-id `i-0123a456700123456` \
    --group-name ""
```

PowerShell

###### To move an instance to a placement group

Use the [Edit-EC2InstancePlacement](../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md "../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md") cmdlet with the
name of the placement group.

```
Edit-EC2InstancePlacement `
    -InstanceId `i-0123a456700123456` `
    -GroupName `MySpreadGroup`
```

###### To remove an instance from a placement group

Use the [Edit-EC2InstancePlacement](../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md "../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md") cmdlet with an
empty string for the name of the placement group.

```
Edit-EC2InstancePlacement `
    -InstanceId `i-0123a456700123456` `
    -GroupName ""
```
