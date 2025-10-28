# Managing Deleted Resources for

AWS Config Custom Lambda Rules

Rules reporting on deleted resources should return the evaluation result of
`NOT_APPLICABLE` in order to avoid unnecessary rule evaluations.

When you delete a resource, AWS Config creates a `configurationItem` with
`ResourceDeleted` for the `configurationItemStatus`. You can
use this metadata to check if a rule reports on a deleted resource. For more information
on configuration items, see [Concepts | Configuration
Items](config-concepts.md#config-items.html "config-concepts.md#config-items.html").

Include the following code snippets to check for deleted resources and set the
evaluation result of an AWS Config custom lambda rule to `NOT_APPLICABLE` if it
reports on a deleted resource:

Custom Lambda Rules (Node.js)

```
// Check whether the resource has been deleted. If the resource was deleted, then the evaluation returns not applicable.
function isApplicable(configurationItem, event) {
    checkDefined(configurationItem, 'configurationItem');
    checkDefined(event, 'event');
    const status = configurationItem.configurationItemStatus;
    const eventLeftScope = event.eventLeftScope;
    return (status === 'OK' || status === 'ResourceDiscovered') && eventLeftScope === false;
}
```

Custom Lambda Rules (Python)

```
# Check whether the resource has been deleted. If the resource was deleted, then the evaluation returns not applicable.
def is_applicable(configurationItem, event):
    try:
        check_defined(configurationItem, 'configurationItem')
        check_defined(event, 'event')
    except:
        return True
    status = configurationItem['configurationItemStatus']
    eventLeftScope = event['eventLeftScope']
    if status == 'ResourceDeleted':
        print("Resource Deleted, setting Compliance Status to NOT_APPLICABLE.")
    return (status == 'OK' or status == 'ResourceDiscovered') and not eventLeftScope

```

###### Note

AWS Config managed rules and AWS Config custom policy rules handle this behavior by
default.

If you create an AWS Config custom lambd rule with Python using the AWS Config Development Kit
(RDK) and AWS Config Development Kit Library (RDKlib), the imported [Evaluator](https://github.com/awslabs/aws-config-rdklib/blob/master/rdklib/evaluator.py#L56 "https://github.com/awslabs/aws-config-rdklib/blob/master/rdklib/evaluator.py#L56") class will check this behavior. For information on how to
write rules with the RDK and RDKlib, see [Writing rules with the RDK and RDKlib](evaluate-config_components.md#evaluate-config_components_logic "evaluate-config_components.md#evaluate-config_components_logic").
