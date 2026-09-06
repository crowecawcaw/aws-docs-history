

# Use operators in formula expressions
<a name="expression-operators"></a>

You can use the following common operators in formula expressions.


| Operator | Description | 
| --- | --- | 
| `+` | If both operands are numbers, this operator adds the left and right operands.<br />If either operand is a string, this operator concatenates the left and right operands as strings. For example, the expression `1 + 2 + " is three"` evaluates to `"3 is three"`. The concatenated string can have up to 1024 characters. If the string exceeds 1024 characters, then AWS IoT SiteWise doesn't output a data point for that computation. | 
| `-` | Subtracts the right operand from the left operand.<br /><a name="operator-numbers-only"></a>You can only use this operator with numeric operands. | 
| `/` | Divides the left operand by the right operand.<br /><a name="operator-numbers-only"></a>You can only use this operator with numeric operands. | 
| `*` | Multiplies the left and right operands.<br /><a name="operator-numbers-only"></a>You can only use this operator with numeric operands. | 
| `^` | Raises the left operand to the power of the right operand (exponentiation).<br /><a name="operator-numbers-only"></a>You can only use this operator with numeric operands. | 
| `%` | Returns the remainder from dividing the left operand by the right operand. The result has the same sign as the left operand. This behavior differs from the modulo operation.<br /><a name="operator-numbers-only"></a>You can only use this operator with numeric operands. | 
| `x < y` | Returns `1` if `x` is less than `y`, otherwise `0`. | 
| `x > y` | Returns `1` if `x` is greater than `y`, otherwise `0`. | 
| `x <= y` | Returns `1` if `x` is less than or equal to `y`, otherwise `0`. | 
| `x >= y` | Returns `1` if `x` is greater than or equal to `y`, otherwise `0`. | 
| `x == y` | Returns `1` if `x` is equal to `y`, otherwise `0`. | 
| `x != y` | Returns `1` if `x` is not equal to `y`, otherwise `0`. | 
| `!x` | Returns `1` if `x` is evaluated to `0` (false), otherwise `0`.<br />`x` is evaluated to false if: +  `x` is a numeric operand and it's evaluated to `0`. <br />+  `x` is evaluated to an empty string. <br />+  `x` is evaluated to an empty array. <br />+  `x` is evaluated to `None`.  | 
| `x and y` | Returns `0` if `x` is evaluated to `0` (false). Otherwise, returns the evaluated result of `y`.<br />`x` or `y` is evaluated to false if: +  `x` or `y` is a numeric operand and it's evaluated to `0`. <br />+  `x` or `y` is evaluated to an empty string. <br />+  `x` or `y` is evaluated to an empty array. <br />+  `x` or `y` is evaluated to `None`.  | 
| `x or y` | Returns `1` if `x` is evaluated to `1` (true). Otherwise, returns the evaluated result of `y`.<br />`x` or `y` is evaluated to false if: +  `x` or `y` is a numeric operand and it's evaluated to `0`. <br />+  `x` or `y` is evaluated to an empty string. <br />+  `x` or `y` is evaluated to an empty array. <br />+  `x` or `y` is evaluated to `None`.  | 
| `not x` | Returns `1` if `x` is evaluated to `0` (false), otherwise `0`.<br />`x` is evaluated to false if: +  `x` is a numeric operand and it's evaluated to `0`. <br />+  `x` is evaluated to an empty string. <br />+  `x` is evaluated to an empty array. <br />+  `x` is evaluated to `None`.  | 
| `[]`<br />`s[index]` | Returns the character at an index `index` of the string `s`. This is equivalent to the index syntax in Python.

**Examples**  
+ `"Hello!"[1]` returns `e`.
+ `"Hello!"[-2]` returns `o`. | 
| `[]`<br />`s[start:end:step]` | Returns a slice of the string `s`. This is equivalent to the slice syntax in Python. This operator has the following arguments:+  `start` – (Optional) The inclusive start index of the slice. Defaults to `0`. <br />+  `end` – (Optional) The exclusive end index of the slice. Defaults to the length of the string. <br />+  `step` – (Optional) The number to increment for each step in the slice. For example, you can specify `2` to return a slice with every other character, or specify `-1` to reverse the slice. Defaults to `1`. <br />You can omit the `step` argument to use its default value. For example, `s[1:4:1]` is equivalent to `s[1:4]`.<br />The arguments must be integers or the [none](expression-constants.md#none-definition) constant. If you specify `none`, AWS IoT SiteWise uses the default value for that argument.

**Examples**  
+ `"Hello!"[1:4]` returns `"ell"`.
+ `"Hello!"[:2]` returns `"He"`.
+ `"Hello!"[3:]` returns `"lo!"`.
+ `"Hello!"[:-4]` returns `"He"`.
+ `"Hello!"[::2]` returns `"Hlo"`.
+ `"Hello!"[::-1]` returns `"!olleH"`. | 