

# Tokens
<a name="srgs-tokens"></a>

The following table shows the token specifications supported by the grammar slot type. For more information, see [ Tokens ](https://www.w3.org/TR/speech-grammar/#S2.1) in the *Speech recognition grammar specification version 1* W3C recommendation.


| Token type | Example | Supported? | 
| --- | --- | --- | 
| Single unquoted token | hello | Yes | 
| Single unquoted token: non-alphabetic | 2 | Yes | 
| Single quoted token, no white space | "hello" | Yes, drop double quotes when it only contains a single token | 
| Two tokens delimited by white space | bon voyage | Yes | 
| Four tokens delimited by white space | this is a test | Yes | 
| Single quoted token, including white space | "San Francisco | No | 
| Single XML token in <token> tag | <token>San Francisco</token> | No (same as single quoted token with white space) | 

**Notes**
+ *Single quoted token including white space* – The specification requires words enclosed in double quotes be treated as a single token. Amazon Lex V2 treats them as white space delimited tokens.
+ *Single XML token in <token>* – The specification requires words delimited by <token> to represent one token. Amazon Lex V2 treats them as white space delimited tokens.
+ Amazon Lex V2 throws a validation error when either usage is found in your grammar.

**Example**

```
<rule id="state" scope="public">
    <one-of>
        <item>FL</item>
        <item>MA</item>
        <item>NY</item>
    </one-of>
</rule>
```