# Offboard AMS accounts

AMS offers off-boarding assistance for single-account landing zone and multi-account landing zone accounts.

AMS does not unshare any AMIs from you during offboarding to avoid impact for any of your depedencies. If you want to remove AMS AMIs from
your account, you can use the `cancel-image-launch-permission` API to hide specific AMIs. For example, you can use the script below to hide all of the AMS AMIs
that were shared with your account earlier:

```
for ami in $(aws ec2 describe-images --executable-users self --owners 027415890775 --query 'Images[].ImageId' --output text) ;
    do
    aws ec2 cancel-image-launch-permission --image-id $ami ;
    done
```

You must have the AWS CLI v2 installed for the script to execute without any errors. For AWS CLI installation steps, see
[Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
For details on the `cancel-image-launch-permission` command, see
[`cancel-image-launch-permission`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html").

###### Note

The service termination date is the last day of the calendar month following the end of the 30 days requisite termination notice period. If the end of the requisite termination notice period falls after the 20th day of the calendar month, then the service termination date is the last day of the following calendar month. The following are example scenarios for termination dates.

- If the termination notice is provided on April 12, then the 30 days notice ends on May 12. The service termination date is May 31.
- If a termination notice is provided on April 29, then the 30 days notice ends on May 29. The service termination date is June 30.

###### Topics

- [Offboard from AMS single-account landing zone accounts](offboarding-salz.md "offboarding-salz.md")
- [Offboard from AMS multi-account landing zone accounts](offboarding-malz.md "offboarding-malz.md")
