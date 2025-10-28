# Language

The following discussion applies to language identifiers
applied to grammars. For more information, see [Language](https://www.w3.org/TR/speech-grammar/#S2.7 "https://www.w3.org/TR/speech-grammar/#S2.7") in the _Speech recognition
grammar specification version 1_ W3C
recommendation.

By default a grammar is a single language document with a
[language identifier](https://www.w3.org/TR/speech-grammar/#term-language "https://www.w3.org/TR/speech-grammar/#term-language") provided in the language
declaration in the [grammar
header](https://www.w3.org/TR/speech-grammar/#S4.1 "https://www.w3.org/TR/speech-grammar/#S4.1"). All tokens within that grammar, unless
otherwise declared, **will be handled
according to the grammar's language**.
Grammar-level language declarations **are
not supported**.

In the following example:

1. The grammar header declaration for the language
   "en-US" **is supported** by
   Amazon Lex V2.
2. Item-level language attachment (highlighted in
   `red`) **is not supported**. Amazon Lex V2
   throws a validation error if a language attachment is
   different from the header declaration.

```
<?xml version="1.0" encoding="ISO-8859-1"?>

<!DOCTYPE grammar PUBLIC "-//W3C//DTD GRAMMAR 1.0//EN"
                  "http://www.w3.org/TR/speech-grammar/grammar.dtd">

<!-- the default grammar language is US English -->
<grammar xmlns="http://www.w3.org/2001/06/grammar"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.w3.org/2001/06/grammar
                             http://www.w3.org/TR/speech-grammar/grammar.xsd"
         xml:lang="en-US" version="1.0">

  <!--
     single language attachment to tokens
     "yes" inherits US English language
     "oui" is Canadian French language
  -->
  <rule id="yes">
    <one-of>
      <item>yes</item>
      <item xml:lang="`fr-CA`">oui</item>
    </one-of>
  </rule>

  <!-- Single language attachment to an expansion -->
  <rule id="people1">
    <one-of xml:lang="`fr-CA`">
      <item>Michel Tremblay</item>
      <item>André Roy</item>
    </one-of>
  </rule>
</grammar>

```
