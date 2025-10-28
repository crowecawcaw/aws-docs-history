# Stop an AWS Direct Connect Resiliency Toolkit virtual interface failover

test

You can stop the virtual interface failover test using the AWS Direct Connect console, or the
AWS CLI.

###### To stop the virtual interface failover test from the AWS Direct Connect console

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. Choose **Virtual interfaces**.
3. Select the virtual interface, and then choose **Actions**,
   **Cancel test**.
4. Choose **Confirm**.
   AWS restores the BGP peering session. The testing history displays "cancelled" for the
   test.

###### To stop the virtual interface failover test using the AWS CLI

Use [StopBgpFailoverTest](../APIReference/API_StopBgpFailoverTest.md "../APIReference/API_StopBgpFailoverTest.md").
