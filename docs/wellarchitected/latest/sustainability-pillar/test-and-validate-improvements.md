# Test and validate improvements

Perform small tests with minimized investment to reduce the risk
of a large-scale effort.

Implement a representative copy of your workload in your testing
environment to limit the cost and risk to perform testing and
validation. Perform a predefined set of test transactions, measure
the provisioned resources, and determine the resources used per
unit of work to establish a testing baseline.

Implement your target improvement in the testing environment and
repeat the test using the same methodology under the same
conditions. Then measure the provisioned resources and resources
used per unit of work with your improvement in place.

Calculate the percentage change from your baseline of the
resources provisioned per unit of work, and determine the expected
quantitative reduction in resources provisioned in your production
environment. Compare these values against the anticipated values.
Determine if the result is an acceptable level of improvement.
Evaluate if any trade-offs in additional resources consumed make
the net benefit from the improvement unacceptable.

Determine if the improvement is a success and if resources should
be invested in implementing the change in production. If the
change is evaluated as unsuccessful at this time, redirect your
resources to test and validate your next target and continue your
improvement cycle.

| **% Reduction in provisioned resources per unit of work** | **Quantitative reduction in provisioned resources** | **Action**                     |
| --------------------------------------------------------- | --------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Met expectations                                          | Met expectations                                    | Proceed with improvement       |
| Did not meet expectations                                 | Met expectations                                    | Proceed with improvement       |
| Met expectations                                          | Did not meet expectations                           | Pursue alternative improvement |
| Did not meet expectations                                 | Did not meet expectations                           | Pursue alternative improvement | Applying this step to the [Example scenario](improvement-process.md#example-scenario "improvement-process.md#example-scenario"), you perform tests to validate success. After you perform the tests on the improved compression algorithm, the percentage reduction in resources provisioned per unit of work (the storage required for both the original image and the modified image) met expectations with an average 30% reduction in provisioned storage and negligible increased compute load. You determine that the additional compute resources required to apply the improved compression algorithm to existing files in production is insignificant compared to the reduction in storage achieved. You confirmed success with the quantitative reduction in resources required (TBs of storage), and the improvement is approved for production deployment. |
