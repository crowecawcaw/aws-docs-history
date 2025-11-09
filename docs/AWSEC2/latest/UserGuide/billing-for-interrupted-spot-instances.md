# Billing for interrupted Spot Instances

When a Spot Instance is interrupted, you're charged for instance and EBS volume usage, and you might
incur other charges, as follows.

## Instance usage

| Who interrupts the Spot Instance                        | Operating system                                          | Interrupted in the first hour                                                                | Interrupted in any hour after the first hour |
| ------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------- |
| If \*_you_<br>• stop or terminate the Spot Instance     | Windows and Linux (excluding SUSE)                        | Charged for the seconds used                                                                 | Charged for the seconds used                 |
| SUSE                                                    | Charged for the full hour even if you used a partial hour | Charged for the full hours used, and charged a full hour for the<br>interrupted partial hour |
| If the \*_Amazon EC2_<br>• interrupts the Spot Instance | Windows and Linux (excluding SUSE)                        | No charge                                                                                    | Charged for the seconds used                 |
| SUSE                                                    | No charge                                                 | Charged for the full hours used, but no charge for the<br>interrupted partial hour           |

## EBS volume usage

While an interrupted Spot Instance is stopped, you are charged only for the EBS volumes, which are
preserved.

With EC2 Fleet and Spot Fleet, if you have many stopped instances, you can exceed the
limit on the number of EBS volumes for your account.
