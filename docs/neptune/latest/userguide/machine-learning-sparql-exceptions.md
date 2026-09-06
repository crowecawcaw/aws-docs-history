

# List of exceptions for Neptune ML SPARQL inference queries
<a name="machine-learning-sparql-exceptions"></a>
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference expects at least 1 value for the parameter {{(parameter name)}}, found zero.`
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference expects at most 1 value for the parameter {{(parameter name)}}, found {{(a number)}} values.`
+ **`BadRequestException`**   –   *Message*: `Invalid predicate {{(predicate name)}} provided for external service http://aws.amazon.com/neptune/vocab/v01/services/ml#inference query.`
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference expects the predicate {{(predicate name)}} to be defined`.
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference expects the value of (parameter) {{(parameter name)}} to be a variable, found: {{(type)}}"`
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference expects the input {{(parameter name)}} to be a constant, found: {{(type)}}`.
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference is expected to return only 1 value`.
+ **`BadRequestException`**   –   *Message*: `"The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference only allows StatementPatternNodes`.
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference does not allow the predicate {{(predicate name)}}`.
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference predicates cannot be variables, found: {{(type)}}`.
+ **`BadRequestException`**   –   *Message*: `The SERVICE http://aws.amazon.com/neptune/vocab/v01/services/ml#inference predicates are expected to be part of the namespace {{(namespace name)}}, found: {{(namespace name)}}`.