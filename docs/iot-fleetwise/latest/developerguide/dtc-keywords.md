# Diagnostic trouble code keywords

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

###### `signalsToFetch` parameter for create campaign

Use the _signalsToFetch_ syntax to configure how the signal information can be fetched on the Edge. Standard signal fetching is controlled by modeling as rules explicitly defined in a decoder manifest or custom defined through Edge First Modeling. With signals to fetch, you can define when and how data is fetched during campaigns.

Signals to fetch allows the collection of DTC information. For example, you can create a signal of string type named `DTC_Info` that can contain DTC information for every engine control unit (ECU). Or, you can filter for a specific ECU.

- `SignalFetchInformation` structure and param definitions.

```
structure SignalFetchInformation {
    @required
    fullyQualifiedName: NodePath,
    @required
    signalFetchConfig: SignalFetchConfig,
    // Conditional language version for this config
    conditionLanguageVersion: languageVersion,
    @required
    actions: EventExpressionList,
}
```

    + `fullyQualifiedName`: the fully qualified name (FQDN) of the signal that you want to use custom fetch for.
    + `signalFetchConfig`: defines rules on how the above defined signals should be fetched. It supports time-based and condition-based fetch.
    + `conditionLanguageVersion`: the conditional language version used for parsing the expression in the config.
    + `actions`: a list of all action expressions evaluated on the Edge. The Edge will get the value of the defined signal.


    ###### Important

    Actions can only use `custom_function`.

## Campaign expression keywords

The following expression takes a signal's fully qualified name supported by the vehicle and returns true if the signal doesn't have any data in the signal buffers on the Edge. Otherside, it returns false.

```
isNull(signalFqdn:String): Boolean
```

###### Example usage

```
isNull($variable.`Vehicle.ECU1.DTC_INFO`) == false

We want to make sure DTC_Info signal is being generated
on edge.
```

This expression takes the following input:

**functionName:String**

The name of the custom function that is supported by the Edge

**params: varargs`Expression`**

Parameters for `functionName`. This can be any list of expressions.

Parameters support literal type: String, Int , Boolean, or Double.

```
custom_function(functionName:String, params: varargs`Expression`): Void
```

###### Example usage

```
{
       "fullyQualifiedName":"Vehicle.ECU1.DTC_INFO",
       "signalFetchConfig":{
          "timeBased":{
             "executionFrequencyMs":2000
          }
       },
       "actions":"custom_function(“DTC_QUERY”, -1, 2, -1)"
    }
```
