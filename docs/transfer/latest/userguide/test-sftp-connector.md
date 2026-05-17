# Test an SFTP connector

After you create an SFTP connector, we recommend that you test it before you
attempt to transfer any files using your new connector.

###### To test an SFTP connector

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **SFTP Connectors**, and
   select a connector.
3. From the **Actions** menu, choose **Test connection**.

![The Transfer Family console, showing an SFTP connector selected, and the Test connectionTest connection action highlighted.](images/connector-test-choose.png)
The system returns a message, indicating whether the test passes or fails. If the test fails, the system provides an error message based on the reason the test failed.

![The SFTP connector test connection panel, showing a successful test.](images/connector-test-success.png)

![The SFTP connector test connection panel, showing a failed test: the error message indicates that the access role for the connector is incorrect.](images/connector-test-fail-role.png)

###### Note

To use the API to test your connector, see the [TestConnection](../APIReference/API_TestConnection.md "../APIReference/API_TestConnection.md") API documentation.
