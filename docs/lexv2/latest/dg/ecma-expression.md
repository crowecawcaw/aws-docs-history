

# Expressions
<a name="ecma-expression"></a>

You can add expressions strings to perform functions in Amazon Lex V2. This table shows the syntax and examples that can be used in SRGS expressions.


| Expression type | Syntax | Example | Supported? | 
| --- | --- | --- | --- | 
| Regular expression literal | String literal containing valid [regex special characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) | <pre>"^\d\.$"</pre> | No | 
| Function | function functionName(parameters) { functionBody} | <pre>var x = function calc() {<br />    return 10;<br />}</pre> | No | 
| Delete | delete expression | <pre>delete obj.property;</pre> | No | 
| Void | void expression | <pre>void (2 == '2');</pre> | No | 
| Typeof | typeof expression | <pre>typeof 42;</pre> | No | 
| Member index | expression [ expressions ] | <pre>var fruits = ["apple"];<br />fruits[0];</pre> | Yes | 
| Member dot | expression . identifier | <pre>out.value</pre> | yes | 
| Arguments | expression (arguments) | <pre>new Date('1994-10-11')</pre> | Yes | 
| Post increment | expression\+\+ | <pre>var x=10; x++;</pre> | Yes | 
| Post decrement | expression-- | <pre>var x=10; x--;</pre> | Yes | 
| Pre increment | \+\+expression | <pre>var x=10; ++x;</pre> | Yes | 
| Pre decrement | --expression | <pre>var x=10; --x;</pre> | Yes | 
| Unary plus / Unary minus | \+expression / -expression | <pre>+x / -x;</pre> | Yes | 
| Bit not | \~ expression | <pre>const a = 5;<br />console.log( ~a );</pre> | Yes | 
| Logical not | \! expression | <pre>!(a > 0 || b > 0)</pre> | Yes | 
| Multiplicative | expression ('\*' \| '/' \| '%') expression | <pre>(x + y) * (a / b)</pre> | Yes | 
| Additive | expression ('\+' \| '-') expression | <pre>(a + b) - (a - (a + b))</pre> | Yes | 
| Bit shift | expression ('<<' \| '>>' \| '>>>') expression | <pre>(a >> b) >>> c</pre> | Yes | 
| Relative | expression ('<' \| '>' \| '<=' \| '>=') expression | <pre>if (a > b) { ... }</pre> | Yes | 
| In | expression in expression | <pre>fruits[0] in otherFruits;</pre> | Yes | 
| Equality | expression ('==' \| '\!=' \| '===' \| '\!===') expression | <pre>if (a == b) { ... }</pre> | Yes | 
| Bit and / xor / or | expression ('&' \| '^' \| '\|') expression | <pre>a & b / a ^ b / a | b</pre> | Yes | 
| Logical and / or | expression ('&&' \| '\|\|') expression | <pre>if (a && (b ||c)) { ...}</pre> | Yes | 
| Ternary  | expression ? expression : expression | <pre>a > b ? obj.prop : 0</pre> | Yes | 
| Assignment | expression = expression | <pre>out.value = "string";</pre> | Yes | 
| Assignment operator | expression ('\*=' \| '/=' \| '\+=' \| '-=' \| '%=') expression  | <pre>a *= 10;</pre> | Yes | 
| Assignment bitwise operator | expression ('<<=' \| '>>=' \| '>>>=' \| '&=' \| '^=' \| '\|=') expression | <pre>a <<= 10;</pre> | Yes | 
| Identifier | identifierSequence where identifierSequence is a sequence of [valid characters](https://developer.mozilla.org/en-US/docs/Glossary/Identifier) | <pre>fruits=[10, 20, 30];</pre> | Yes | 
| Null literal | null | <pre>x = null;</pre> | Yes | 
| Boolean literal | true \| false | <pre>x = true;</pre> | Yes | 
| String literal | 'string' / "string" | <pre>a = 'hello',<br />b = "world";</pre> | Yes | 
| Decimal literal | integer [.] digits [exponent] | <pre>111.11 e+12</pre> | Yes | 
| Hex literal | 0 (x \| X)[0-9a-fA-F] | <pre>0x123ABC</pre> | Yes | 
| Octal literal | O [0-7] | <pre>"O51"</pre> | Yes | 
| Array literal | [ expression, ... ] | <pre>v = [a, b, c];</pre> | Yes | 
| Object literal | {property: value, ...} | <pre>out = {value: 1, flag: false};</pre> | Yes | 
| Parenthesized | ( expressions ) | <pre>x + (x + y)</pre> | Yes | 