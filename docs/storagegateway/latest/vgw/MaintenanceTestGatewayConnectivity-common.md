# Testing your gateway

connection to the internet

You can use your gateway's local console to test your internet connection. This test
can be useful when you are troubleshooting network issues with your gateway.

###### To test your gateway's connection to the internet

1. Log in to your gateway's local console.
   - VMware ESXi – for more information, see [Accessing the Gateway Local
     Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common "accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
   - Microsoft Hyper-V – for more information, see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - KVM – for more information, see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. From the **AWS Storage Gateway - Configuration** main menu, enter
   the corresponding numeral to select **Test Network
   Connectivity**.

If your gateway has already been activated, the connectivity test begins
immediately. For gateways that have not yet been activated, you must specify the
endpoint type and AWS Region as described in the following steps. 3. If your gateway is not yet activated, enter the corresponding numeral to
select the endpoint type for your gateway. 4. If you selected the public endpoint type, enter the corresponding numeral to
select the AWS Region that you want to test. For supported AWS Regions and a
list of AWS service endpoints you can use with Storage Gateway, see [AWS Storage Gateway endpoints
and quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in the _AWS General Reference_.
As the test progresses, each endpoint displays either **[PASSED]** or
**[FAILED]**, indicating the status of the connection as
follows:

| Message      | Description                                         |
| ------------ | --------------------------------------------------- |
| **[PASSED]** | Storage Gateway has network connectivity.           |
| **[FAILED]** | Storage Gateway does not have network connectivity. |
