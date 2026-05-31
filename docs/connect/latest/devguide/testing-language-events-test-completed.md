# Test completed

Triggered when the test execution ends. This event is observed when the test is terminated.

## Parameters

- Type - Must always be `TestCompleted`.
- Actor - Must always be `System`. This indicates that the event
  originates from the testing system.
- Properties - Empty object. No additional properties are required.

```
{
    "Identifier": "unique identifier",
    "Type": "TestCompleted",
    "Actor": "System",
    "Properties": {}
}
```
