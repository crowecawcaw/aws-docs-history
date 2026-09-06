

# Start an AWS Direct Connect Resiliency Toolkit virtual interface failover test
<a name="start_failover_test"></a>

You can start the virtual interface failover test using the Direct Connect console, or the AWS CLI.

**To start the virtual interface failover test from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interfaces and then choose **Actions**, **Bring down BGP**.

   You can run the test on a public, private, or transit virtual interface.

1. In the **Start failure test** dialog box, do the following:

   1. For **Peerings to bring down to test**, choose which peering sessions to test, for example IPv4.

   1. For **Test maximum time**, enter the number of minutes that the test will last.

      The maximum value is 4,320 minutes (72 business hours).

      The default value is 180 minutes (3 hours).

   1. For **To confirm test**, enter **Confirm**.

   1. Choose **Confirm**.

   The BGP peering session is placed in the DOWN state. You can send traffic to verify that there are no outages. If needed, you can stop the test immediately.

**To start the virtual interface failover test using the AWS CLI**  
Use [StartBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StartBgpFailoverTest.html).