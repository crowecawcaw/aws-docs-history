# Grammar slot type

With the grammar slot type, you can author your own grammar in the XML
format per the SRGS specification to collect information in a
conversation. Amazon Lex V2 recognizes utterances matched by the rules
specified in the grammar. You can also provide semantic interpretation
rules using ECMAScript tags within the grammar files. Amazon Lex then returns
properties set in the tags as resolved values when a match
occurs.

You can only create grammar slot types in the English (Australia),
English (UK), and English (US) locales.

There are two parts to a grammar slot type. The first is the grammar
itself written using the SRGS specification format. The grammar
interprets the utterance from the user. If the utterance is accepted by
the grammar it is matched, otherwise it is rejected. If an utterance is
matched it is passed on to the script if there is one.

The second is part of a grammar slot type is an optional script
written in ECMAScript that transforms the input to the resolved values
returned by the slot type. For example, you can use a script to convert
spoken numbers to digits. ECMAScript statements are enclosed in the
<tag> element.

The following example is in the XML format per the SRGS specification
that shows a valid grammar accepted by Amazon Lex V2. It defines a grammar slot
type that accepts card numbers and determines if they are for regular or
premium accounts. For more information about the acceptable syntax, see
the [Grammar definition](grammar-srgs-spec.md "grammar-srgs-spec.md") and the [Script format](grammar-ecmascript-spec.md "grammar-ecmascript-spec.md") topics.

```
<grammar version="1.0" xmlns="http://www.w3.org/2001/06/grammar"
         xml:lang="en-US" tag-format="semantics/1.0" root="card_number">

   <rule id="card_number" scope="public">
        <item repeat="0-1">
            card number
        </item>
        <item>
            seven
            <tag>out.value = "7";</tag>
         </item>
         <item>
            <one-of>
               <item>
                  two four one
                  <tag> out.value = out.value + "241"; out.card_type = "premium"; </tag>
               </item>
               <item>
                  zero zero one
                  <tag> out.value = out.value + "001"; out.card_type = "regular";</tag>
               </item>
            </one-of>
         </item>
   </rule>
</grammar>

```

The above grammar only accepts two types of card numbers: 7241 or 7001. Both of these may be optionally prefixed with “card number”. It
also contains ECMAScript tags that can be used for semantic
interpretation. With semantic interpretation, the utterance “card number
seven two four one” would return following object:

```
{
    "value": "7241",
    "card_type": "premium"
}
```

This object is returned as a JSON-serialized string in the
`resolvedValues` object returned by the
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md"),
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md"), and
[StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md") operations.

## Adding a grammar slot

type

###### To add a grammar slot type

1. Upload the XML definition of your slot type to an S3
   bucket. Make a note of the bucket name and the path to the
   file.

###### Note

The maximum file size is 100 KB. 2. Sign in to the AWS Management Console and open the Amazon Lex console at
[https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/"). 3. From the left menu, choose **Bots** and
then choose the bot to add the grammar slot type to. 4. Choose **View languages**, and then
choose the language to add the grammar slot type to. 5. Choose **View slot types**. 6. Choose **Add slot type**, and then choose
**Add grammar slot type**. 7. Give the slot type a name, and then choose
**Add**. 8. Choose the S3 bucket that contains your definition file
and enter the path to the file. Choose **Save slot
type**.
