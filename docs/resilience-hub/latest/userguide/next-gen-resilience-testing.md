

# Resilience testing
<a name="next-gen-resilience-testing"></a>

In the next generation of Resilience Hub there are four AWS recommended test templates, which have been developed to help you validate your services operate and recover as expected during failures. Three tests align to the AWS fault isolation boundaries (Availability Zones and Regions) and provide a consistent way to test your services' recovery capability to failures scoped to those boundaries. There is an additional test to help you validate your services can recover when there are failures to its dependencies. Each test is built on AWS Fault Injection Service (AWS FIS), which performs the underlying fault injection. Next generation Resilience Hub scopes the test to the resources in your service and evaluates the results against your chosen success criteria to determine a pass or fail outcome. You run resilience tests at the service level.

**Topics**
+ [How resilience testing works](next-gen-resilience-testing-concepts.md)
+ [Configuring a test](next-gen-resilience-testing-configuring.md)
+ [Available tests](next-gen-resilience-testing-available-tests.md)
+ [Test runs and report](next-gen-resilience-testing-runs-and-report.md)
+ [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md)