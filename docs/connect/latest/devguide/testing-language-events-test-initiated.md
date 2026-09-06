

# Test initiated
<a name="testing-language-events-test-initiated"></a>

Triggered when the test execution begins. This is typically used to set up initial conditions such as override system behaviors before the actual flow execution starts.

## Parameters
<a name="testing-language-events-test-parameters"></a>
+ Identifier - Unique identifier for the event. (API need to specify this identifier in order for the UI to render properly)
+ Type - Must always be `TestInitiated`.
+ Actor - Must always be `System`. This indicates that the event originates from the testing system.
+ Properties - Empty object. No additional properties are required.

```
{
    "Identifier": "unique identifier",
    "Type": "TestInitiated",
    "Actor": "System",
    "Properties": {}
}
```