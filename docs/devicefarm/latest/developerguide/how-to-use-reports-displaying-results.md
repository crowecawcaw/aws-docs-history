

# Device Farm test result statuses
<a name="how-to-use-reports-displaying-results"></a>

The Device Farm console displays icons that help you quickly assess the state of your completed test run. For more information about tests in Device Farm, see [Reports in AWS Device Farm](reports.md).

**Topics**
+ [Statuses of an individual test](#how-to-use-reports-displaying-results-individual)
+ [Statuses for multiple tests](#how-to-use-reports-displaying-results-summary)

## Statuses of an individual test
<a name="how-to-use-reports-displaying-results-individual"></a>

For reports that describe an individual test, Device Farm displays an icon representing the test result status:


| Description | Icon | 
| --- | --- | 
| The test succeeded. | ![The test succeeded.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-success.png) | 
| The test failed. | ![The test failed.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-failure.png) | 
| Device Farm skipped the test. | ![The test was skipped.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-skipped.png) | 
| The test stopped. | ![The test was stopped.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-stopped.png) | 
| Device Farm returned a warning. | ![Device Farm returned a warning.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-warning.png) | 
| Device Farm returned an error. | ![Device Farm returned an error.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-error.png) | 

## Statuses for multiple tests
<a name="how-to-use-reports-displaying-results-summary"></a>

If you choose a finished run, Device Farm displays a summary graph showing the percentage of tests in various states.

![Device Farm test results summary graph.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-summary-results-graph.png)

For example, this test run results graph shows that the run had 4 stopped tests, 1 failed test, and 10 successful tests.

Graphs are always color coded and labeled.