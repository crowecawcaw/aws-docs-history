

# Test control actions
<a name="testing-simulation-action-test-commands"></a>

Test Control actions manage the test execution itself, providing debugging capabilities and explicit control over when tests end.

## End test
<a name="testing-simulation-action-end-test"></a>

Explicitly terminates the test execution at a specific point. Use this when you want to stop the test after validating certain conditions rather than waiting for the flow to complete naturally.

Configuration options:
+ **Action** – Select "Test commands"
+ **Test control type** – Choose "End test"

Use cases:
+ Stopping the test after critical validations are complete
+ Preventing unnecessary execution after the main test objectives are achieved

![Action block configuration showing Test commands with End test control type selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-end-test.png)


## Log data
<a name="testing-simulation-action-log-data"></a>

Captures and records specific attribute values during test execution. The logged information appears in your test results, helping you understand what was happening at different points in the test.

Configuration options:
+ **Action** – Select "Test commands"
+ **Test control type** – Choose "Log data"
+ **Log data** – Define one or more key-value pairs:
  + **Log identifier** – A descriptive name for the logged value (for example, "Current Queue Name")
  + **Log value** – JSONPath to the attribute you want to log (for example, $.Queue.Name) along with any descriptive text

Use cases:
+ Debugging test failures by seeing intermediate values
+ Tracking how attributes change throughout the test
+ Recording important data points for test documentation

![Action block configuration showing Test commands with Log data control type and key-value pair fields.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-log-data.png)


Example logging configuration:
+ Log identifier: "Contact ID and Queue name" → Log value: This is the contact id: $.ContactId with the Queue name: $.Queue.Name

This would capture both values at the point where the Log Data action executes, making them visible in your test results.

![Example log data configuration showing Contact ID and Queue name logging with JSONPath expressions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-log-data-example.png)
