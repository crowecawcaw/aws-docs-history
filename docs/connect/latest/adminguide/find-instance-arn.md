

# Find your Connect Customer instance ID or ARN
<a name="find-instance-arn"></a>

When you open a support ticket, you might be asked to provide your Connect Customer instance ID (also called the ARN). Use the following steps to find it. 

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

   On the **Account overview** page, in the **Distribution settings** section, you can see the full instance ARN.   
![The Distribution settings section, the full ARN.](http://docs.aws.amazon.com/connect/latest/adminguide/images/find-instance-arn.png)

   The information after **instance/** is the instance ID.   
![The characters after the last /.](http://docs.aws.amazon.com/connect/latest/adminguide/images/find-instance-id.png)

If you don't see your instance listed, double-check that you're looking in the correct Region, as shown in the following image. For a list of supported Regions, see [Connect Customer availability by Region](regions.md#amazonconnect_region). 

![The Region dropdown list.](http://docs.aws.amazon.com/connect/latest/adminguide/images/supported-regions.png)
