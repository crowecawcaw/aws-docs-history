# Unsupported

statements

Amazon Lex V2 doesn't support the following ECMAScript
features.

###### Topics

- [Empty
  statement](#ecma-unsupported-empty "#ecma-unsupported-empty")
- [Continue
  statement](#ecma-unsupported-continue "#ecma-unsupported-continue")
- [Break
  statement](#ecma-unsupported-break "#ecma-unsupported-break")
- [Return
  statement](#ecma-unsupported-return "#ecma-unsupported-return")
- [Throw
  statement](#ecma-unsupported-throw "#ecma-unsupported-throw")
- [Try statement](#ecma-unsupported-try "#ecma-unsupported-try")
- [Debugger
  statement](#ecma-unsupported-debugger "#ecma-unsupported-debugger")
- [Labeled
  statement](#ecma-unsupported-labelled "#ecma-unsupported-labelled")
- [Class
  declaration](#ecma-unsupported-class "#ecma-unsupported-class")

## Empty

statement

The empty statement is used to provide no statement. The
following is the syntax for an empty statement:

```
;
```

## Continue

statement

The continue statement without a label is supported with
the [Iteration statement](ecma-iteration.md "ecma-iteration.md"). The continue statement
with a label isn't supported.

```
// continue with label
// this allows the program to jump to a
// labelled statement (see labelled statement below)
continue <label>;

```

## Break

statement

The break statement without a label is supported with the
[Iteration statement](ecma-iteration.md "ecma-iteration.md"). The break statement
with a label isn't supported.

```
// break with label
// this allows the program to break out of a
// labelled statement (see labelled statement below)
break <label>;

```

## Return

statement

```
return expression;
```

## Throw

statement

The throw statement is used to throw a user-defined
exception.

```
throw expression;
```

## Try statement

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

## Debugger

statement

The debugger statement is used to invoke debugging
functionality provided by the environment.

```
debugger;
```

## Labeled

statement

The labeled statement can be used with `break`
or `continue` statements.

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

## Class

declaration

```
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

```
