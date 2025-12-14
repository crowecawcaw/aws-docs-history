# Test CloudFront Connection Functions before deployment

You can test CloudFront Connection Functions in the DEVELOPMENT stage using the TestConnectionFunction API operation. Testing allows you to validate your function logic with sample connection events before publishing to the LIVE stage.

###### Topics

- [Testing process](#connection-function-testing-process "#connection-function-testing-process")
- [Test results](#connection-function-test-results "#connection-function-test-results")
- [Connection test object](#connection-test-object "#connection-test-object")

## Testing process

To test a Connection Function:

1. Create a Connection Function in the DEVELOPMENT stage
2. Prepare a test connection object that represents the TLS connection
   event
3. Use the TestConnectionFunction API operation to execute your function with
   the test data
4. Review the test results, including function output, execution logs, and
   any error messages
5. Update your function code as needed and repeat the testing process

## Test results

When you test a Connection Function, the results include:

- **Function summary** – Metadata about the
  function that was tested
- **Compute utilization** – Performance metrics
  showing resource usage
- **Execution logs** – Console output from your
  function, including any logging statements
- **Function output** – The result returned by
  your function
- **Error messages** – Any runtime errors or
  exceptions that occurred during execution

## Connection test object

The connection test object is a binary blob (up to 40KB) that represents the TLS
connection event your function will process. This object contains the certificate
and connection information that your function uses to make authentication
decisions.

###### Note

The specific structure and format of the connection test object is defined by
the CloudFront Connection Functions runtime. Consult the CloudFront Functions documentation
or contact AWS Support for details on creating appropriate test objects for your
use case.

After creating your Connection Function, you can:

- **Test the function** – Use the test
  functionality in the console or CLI to validate your function with sample
  connection events. For more information, see Connection Function
  testing.
- **Update the function** – Modify the function
  code and configuration as needed. Connection functions in the DEVELOPMENT
  stage can be updated at any time.
- **Publish the function** – When ready for
  production, publish the function to move it from DEVELOPMENT to LIVE stage.
  For more information, see associating Connection Functions.
- **Associate with a distribution** – Associate
  the published function with an mTLS-enabled distribution to handle live
  connections. For more information, see associating connection
  functions.
