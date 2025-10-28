# Amazon Inspector Lambda standard scanning

Amazon Inspector Lambda standard scanning identifies software vulnerabilities in the application package
dependencies you add to your Lambda function code and layers. For example, if your Lambda function
uses a version of the `python-jwt` package with a known vulnerability,
Lambda standard scanning will generate a finding for that function.

If Amazon Inspector detects a vulnerability in your Lambda function application package
dependencies, Amazon Inspector produces a detailed **Package
Vulnerability** type finding.

For instructions on activating a scan type see [Activating a scan type](activate-scans.md "activate-scans.md").

###### Note

Lambda standard scanning doesn't scan the AWS SDK dependency installed by default in the
Lambda runtime environment. Amazon Inspector only scans dependencies uploaded with the
function code or inherited from a layer.

###### Note

Deactivating Amazon Inspector Lambda standard scanning will also deactivate Amazon Inspector Lambda code scanning.
