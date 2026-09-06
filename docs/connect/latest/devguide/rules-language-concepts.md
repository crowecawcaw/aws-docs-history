

# Concepts
<a name="rules-language-concepts"></a>

The following terms are used in the Rules Function language.

**Operator**  
A function that is used to evaluate Operands. The very top Operator has to be either AND or OR. 

**Operands**  
An array of objects that Operator is evaluating on. The length the array and the type of each object depends on the Operator defined on the same level.

**ComparisonValue**  
A JSON path string that specifies the value field the rule is comparing.

**FilterClause**  
An object that defines additional criteria that the rule is evaluating against. Depending on **ComparisonValue**, the value of this field varies.

**Negate**  
A Boolean value that indicates if negation should be applied to the operator.