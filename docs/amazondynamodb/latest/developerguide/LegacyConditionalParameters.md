

# Legacy DynamoDB conditional parameters
<a name="LegacyConditionalParameters"></a>

This document provides an overview of legacy conditional parameters in DynamoDB and recommends using the new expression parameters instead. It covers details on parameters like AttributesToGet, AttributeUpdates, ConditionalOperator, Expected, KeyConditions, QueryFilter, and ScanFilter, and provides examples of how to use the new expression parameters as replacements.

**Important**  
We recommend that you use the new expression parameters instead of these legacy parameters whenever possible. For more information, see [Using expressions in DynamoDB](Expressions.md).   
Additionally, DynamoDB does not allow mixing legacy conditional parameters and expression parameters in a single call. For example, calling the `Query` operation with `AttributesToGet` and `ConditionExpression` will result in an error.

The following table shows the DynamoDB API operations that still support these legacy parameters, and which expression parameter to use instead. This table can be helpful if you are considering updating your applications so that they use expression parameters instead.




- **`BatchGetItem`**
  - **With these legacy parameters...:**  AttributesToGet 
  - **Use this expression parameter instead:**  ProjectionExpression 

- **`DeleteItem`**
  - **With these legacy parameters...:**  Expected 
  - **Use this expression parameter instead:**  ConditionExpression

- **`GetItem`**
  - **With these legacy parameters...:**  AttributesToGet 
  - **Use this expression parameter instead:**  ProjectionExpression 

- **`PutItem`**
  - **With these legacy parameters...:**  Expected 
  - **Use this expression parameter instead:**  ConditionExpression

- **`Query`**
  - **With these legacy parameters...:**  AttributesToGet  / **Use this expression parameter instead:**  ProjectionExpression 
  - **With these legacy parameters...:**  KeyConditions  / **Use this expression parameter instead:**  KeyConditionExpression 
  - **With these legacy parameters...:**  QueryFilter  / **Use this expression parameter instead:**  FilterExpression 

- **`Scan`**
  - **With these legacy parameters...:**  AttributesToGet  / **Use this expression parameter instead:**  ProjectionExpression 
  - **With these legacy parameters...:**  ScanFilter  / **Use this expression parameter instead:**  FilterExpression 

- **`UpdateItem` **
  - **With these legacy parameters...:**  AttributeUpdates  / **Use this expression parameter instead:**  UpdateExpression 
  - **With these legacy parameters...:**  Expected / **Use this expression parameter instead:**  ConditionExpression



The following sections provide more information about legacy conditional parameters.

**Topics**
+ [AttributesToGet (legacy)](LegacyConditionalParameters.AttributesToGet.md)
+ [AttributeUpdates (legacy)](LegacyConditionalParameters.AttributeUpdates.md)
+ [ConditionalOperator (legacy)](LegacyConditionalParameters.ConditionalOperator.md)
+ [Expected (legacy)](LegacyConditionalParameters.Expected.md)
+ [KeyConditions (legacy)](LegacyConditionalParameters.KeyConditions.md)
+ [QueryFilter (legacy)](LegacyConditionalParameters.QueryFilter.md)
+ [ScanFilter (legacy)](LegacyConditionalParameters.ScanFilter.md)
+ [Writing conditions with legacy parameters](LegacyConditionalParameters.Conditions.md)