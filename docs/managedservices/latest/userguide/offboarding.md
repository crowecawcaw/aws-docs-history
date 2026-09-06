

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Offboard AMS accounts
<a name="offboarding"></a>

AMS offers off-boarding assistance for single-account landing zone and multi-account landing zone accounts.

AMS does not unshare any AMIs from you during offboarding to avoid impact for any of your depedencies. If you want to remove AMS AMIs from your account, you can use the `cancel-image-launch-permission` API to hide specific AMIs. For example, you can use the script below to hide all of the AMS AMIs that were shared with your account earlier:

```
for ami in $(aws ec2 describe-images --executable-users self --owners 027415890775 --query 'Images[].ImageId' --output text) ; 
    do
    aws ec2 cancel-image-launch-permission --image-id $ami ; 
    done
```

You must have the AWS CLI v2 installed for the script to execute without any errors. For AWS CLI installation steps, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). For details on the `cancel-image-launch-permission` command, see [`cancel-image-launch-permission`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html).

**Note**  
The service termination date is the last day of the calendar month following the end of the 30 days requisite termination notice period. If the end of the requisite termination notice period falls after the 20th day of the calendar month, then the service termination date is the last day of the following calendar month. The following are example scenarios for termination dates.  
If the termination notice is provided on April 12, then the 30 days notice ends on May 12. The service termination date is May 31.
If a termination notice is provided on April 29, then the 30 days notice ends on May 29. The service termination date is June 30.

**Topics**
+ [Offboard from AMS single-account landing zone accounts](offboarding-salz.md)
+ [Offboard from AMS multi-account landing zone accounts](offboarding-malz.md)