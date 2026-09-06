

# Stop an AWS Direct Connect Resiliency Toolkit virtual interface failover test
<a name="stop_failover_test"></a>

You can stop the virtual interface failover test using the Direct Connect console, or the AWS CLI.

**To stop the virtual interface failover test from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interface, and then choose **Actions**, **Cancel test**.

1. Choose **Confirm**.

AWS restores the BGP peering session. The testing history displays "cancelled" for the test. 

**To stop the virtual interface failover test using the AWS CLI**  
Use [StopBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html).