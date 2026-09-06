

# Security best practices for Device Farm
<a name="security-best-practices"></a>

 Device Farm provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 
+ Grant any continuous integration (CI) system you use the least privilege possible under IAM. Consider using temporary credentials for each CI system test so that even if a CI system is compromised, it cannot make spurious requests. For more information about temporary credentials, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerole).
+ Use `adb` commands in a custom test environment to clean up any content created by your application. For more information about custom test environments, see [Custom test environments in AWS Device Farm](custom-test-environments.md).
+ Avoid logging sensitive data, such as credentials or personal information, on the device or in your test framework. Logs, videos, screenshots, and other artifacts generated during a run are retained by Device Farm so that you can review them after the run completes. For more information on best practices in custom test environments, see [Best practices for custom test environment execution](custom-test-environments-best-practices.md).