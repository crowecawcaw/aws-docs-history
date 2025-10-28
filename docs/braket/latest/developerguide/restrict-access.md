# Restrict user access to certain devices

To restrict user access for certain Braket devices, you can add a
_deny permissions_ policy to a specific IAM
role.

The following actions can be restricted:

- `CreateQuantumTask` - to deny quantum task creation on specified devices.
- `CreateJob` - to deny hybrid job creation on specified devices.
- `GetDevice` - to deny getting details of specified devices.
  The following example restricts access to all QPUs for the AWS account
  `123456789012`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "braket:CreateQuantumTask",
 "braket:CreateJob",
 "braket:GetDevice"
 ],
 "Resource": [
 "arn:aws:braket:*:*:device/qpu/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": "123456789012"
 }
 }
 }
 ]
}`

```

###### Note

Exclude the `braket:GetDevice` Action from the policy to enable
a user's Read access to the device properties such as device availability, calibration
data, and pricing through the Braket console.

To adapt this code, substitute the Amazon Resource Number (ARN) of the
restricted device for the string shown in the previous example. This string provides the
**Resource** value. In Braket, a device represents
a QPU or simulator that you can call to run quantum tasks. The devices available are
listed on the [Devices page](braket-devices.md "braket-devices.md"). There are two schemas used to specify access to these
devices:

- `arn:aws:braket:<region>:*:device/qpu/<provider>/<device_id>`
- `arn:aws:braket:<region>:*:device/quantum-simulator/<provider>/<device_id>`

**Here are examples for various types of device access**

- To select all QPUs across all regions:
  `arn:aws:braket:*:*:device/qpu/*`
- To select all QPUs in the us-west-2 region ONLY:
  `arn:aws:braket:us-west-2:*:device/qpu/*`
- Equivalently, to select all QPUs in the us-west-2 region ONLY ( since devices
  are a service resource, not a customer resource):
  `arn:aws:braket:us-west-2:*:device/qpu/*`
- To restrict access to all on-demand simulator devices: `arn:aws:braket:*:*:device/quantum-simulator/*`
- To restrict access to devices from a certain provider (for example, to
  Rigetti
  QPU devices): `arn:aws:braket:*:*:device/qpu/rigetti/*`
- To restrict access to the TN1 device: `arn:aws:braket:*:*:device/quantum-simulator/amazon/tn1`
- To restrict access to all `Create` actions: `braket:Create*`
