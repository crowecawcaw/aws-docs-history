

# Sequences and encapsulation

The following example shows the supported sequences. For more information, see [Sequences and encapsulation](https://www.w3.org/TR/speech-grammar/#S2.3) in the *Speech recognition grammar specification version 1* W3C recommendation. 

**Example**

```xml
<!-- sequence of tokens -->
this is a test

<!--sequence of rule references-->
<ruleref uri="#action"/> <ruleref uri="#object"/>

<!--sequence of tokens and rule references-->
the <ruleref uri="#object"/> is <ruleref uri="#color"/>

<!-- sequence container -->
<item>fly to <ruleref uri="#city"/> </item>
```