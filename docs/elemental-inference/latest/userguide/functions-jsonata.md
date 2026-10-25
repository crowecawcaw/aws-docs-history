

# JSONata reference for functions
<a name="functions-jsonata"></a>

This section is a reference for the syntax, operators, and built-in functions you can use in a function's request and response expressions. For guidance on what to put in each expression, see [Writing function expressions](functions-expressions.md).

The whole value of `requestExpression` and `responseExpression` is an expression – there are no delimiters, and no mixing of literal text with expression syntax. To include static text in the result, write it as a string literal in the expression, and join it with the `&` operator.

**Note**  
Elemental Inference uses the same JSONata implementation as AWS Elemental MediaTailor functions. If you have written an expression for MediaTailor, the language here is the same. The input data, the required output, and the allowed built-in functions differ, and Elemental Inference expressions have no delimiters. For the MediaTailor reference, see [JSONata expression reference for Functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html) in the *AWS Elemental MediaTailor User Guide*.

**Topics**
+ [Language basics](functions-jsonata-basics.md)
+ [Operators](functions-jsonata-operators.md)
+ [Allowed built-in functions](functions-jsonata-allowed.md)
+ [Common patterns](functions-jsonata-patterns.md)