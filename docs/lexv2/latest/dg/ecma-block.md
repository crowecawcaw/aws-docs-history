# Block statement

You can add statement blocks to perform functions in Amazon Lex V2. This example shows the syntax that can be used in SRGS expressions.

```
{
   statements
}

// Example
{
    x = 10;
   if (x > 10) {
     console.log("greater than 10");
   }
}

```

**Note:** In the preceding
example, `statements` provided in the block must be
one of the supported ones from this document.
