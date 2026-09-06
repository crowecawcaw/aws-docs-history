

# Unsupported statements
<a name="ecma-unsupported"></a>

Amazon Lex V2 doesn't support the following ECMAScript features.

**Topics**
+ [Empty statement](#ecma-unsupported-empty)
+ [Continue statement](#ecma-unsupported-continue)
+ [Break statement](#ecma-unsupported-break)
+ [Return statement](#ecma-unsupported-return)
+ [Throw statement](#ecma-unsupported-throw)
+ [Try statement](#ecma-unsupported-try)
+ [Debugger statement](#ecma-unsupported-debugger)
+ [Labeled statement](#ecma-unsupported-labelled)
+ [Class declaration](#ecma-unsupported-class)

## Empty statement
<a name="ecma-unsupported-empty"></a>

The empty statement is used to provide no statement. The following is the syntax for an empty statement:

```
;
```

## Continue statement
<a name="ecma-unsupported-continue"></a>

The continue statement without a label is supported with the [Iteration statement](ecma-iteration.md). The continue statement with a label isn't supported.

```
// continue with label
// this allows the program to jump to a
// labelled statement (see labelled statement below)
continue <label>;
```

## Break statement
<a name="ecma-unsupported-break"></a>

The break statement without a label is supported with the [Iteration statement](ecma-iteration.md). The break statement with a label isn't supported.

```
// break with label
// this allows the program to break out of a
// labelled statement (see labelled statement below)
break <label>;
```

## Return statement
<a name="ecma-unsupported-return"></a>

```
return expression;
```

## Throw statement
<a name="ecma-unsupported-throw"></a>

The throw statement is used to throw a user-defined exception.

```
throw expression;
```

## Try statement
<a name="ecma-unsupported-try"></a>

```
try {
  statements
}
catch (expression) {
  statements
}
finally {
  statements
}
```

## Debugger statement
<a name="ecma-unsupported-debugger"></a>

The debugger statement is used to invoke debugging functionality provided by the environment.

```
debugger;
```

## Labeled statement
<a name="ecma-unsupported-labelled"></a>

The labeled statement can be used with `break` or `continue` statements.

```
label:
   statements


// Example
let str = '';

loop1:
for (let i = 0; i < 5; i++) {
  if (i === 1) {
    continue loop1;
  }
  str = str + i;
}

console.log(str);
```

## Class declaration
<a name="ecma-unsupported-class"></a>

```
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```