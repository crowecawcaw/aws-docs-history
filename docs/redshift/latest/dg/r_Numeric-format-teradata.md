

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Teradata-style formatting characters for numeric data
<a name="r_Numeric-format-teradata"></a>

Following, you can find how the TEXT\_TO\_INT\_ALT and TEXT\_TO\_NUMERIC\_ALT functions interpret the characters in the input *expression* string. You can also find a list of the characters that you can specify in the *format* phrase. In addition, you can find a description of the differences between Teradata-style formatting and Amazon Redshift for the *format* option. 


| Format  | Description  | 
| --- | --- | 
| G  | Not supported as a group separator in the input expression string. You can't specify this character in the format phrase.  | 
| D | Radix symbol. You can specify this character in the *format* phrase. This character is equivalent to the . (period).<br />The Radix symbol can't appear in a *format* phrase that contains any of the following characters:+ . (period)<br />+ S (uppercase 's')<br />+ V (uppercase 'v') | 
| / , : % | Insertion characters / (forward slash), comma (,), : (colon), and % (percent sign).<br />You can't include these characters in the *format* phrase.<br />Amazon Redshift ignores these characters in the input *expression* string. | 
| .  | Period as a radix character, that is a decimal point.<br />This character can't appear in a *format* phrase that contains any of the following characters:+ D (uppercase 'd')<br />+ S (uppercase 's')<br />+ V (uppercase 'v') | 
| B | You can't include the blank space character (B) in the *format* phrase. In the input *expression* string, leading and trailing spaces are ignored and spaces between digits aren't allowed. | 
| \+ - | You can't include the plus sign (\+) or minus sign (-) in the *format* phrase. However, the plus sign (\+) and minus sign (-) are parsed implicitly as part of numeric value if they appear in the input *expression* string. | 
| V  | Decimal point position indicator.<br />This character can't appear in a *format* phrase that contains any of the following characters:+ D (uppercase 'd')<br />+ . (period) | 
| Z  | Zero-suppressed decimal digit. Amazon Redshift trims leading zeros. The Z character can't follow a 9 character. The Z character must be to the left of the radix character if the fraction part contains the 9 character. | 
| 9  | Decimal digit. | 
| CHAR(n)  | For this format, you can specify the following: + CHAR consists of Z or 9 characters. Amazon Redshift doesn't support a \+ (plus) or - (minus) in the CHAR value. <br />+ *n* is an integer constant, I, or F. For I, this is the number of characters necessary to display the integer portion of numeric or integer data. For F, this is the number of characters necessary to display the fractional portion of numeric data.  | 
| -  | Hyphen (-) character. <br />You can't include this character in the *format* phrase.<br />Amazon Redshift ignores this character in the input *expression* string. | 
| S | Signed Zoned Decimal. The S character must follow the last decimal digit in the *format* phrase. The last character of the input *expression* string and the corresponding numeric conversion are listed in [Data formatting characters for Signed Zone Decimal, Teradata–style numeric data formatting ](#r_Numeric-format-teradata-signed-zone).<br />The S character can't appear in a *format* phrase that contains any of the following characters:+ \+ (plus sign)<br />+ . (period)<br />+ D (uppercase 'd')<br />+ Z (uppercase 'z')<br />+ F (uppercase 'f')<br />+ E (uppercase 'e') | 
| E | Exponential notation. The input *expression* string can include the exponent character. You can't specify E as an exponent character in *format* phrase. | 
| FN9 | Not supported in Amazon Redshift. | 
| FNE | Not supported in Amazon Redshift. | 
| $, USD, US Dollars  | Dollar sign ($), ISO currency symbol (USD), and the currency name US Dollars.<br />The ISO currency symbol USD and the currency name US Dollars are case-sensitive. Amazon Redshift supports only the USD currency. The input *expression* string can include spaces between the USD currency symbol and the numeric value, for example ‘$ 123E2’ or ‘123E2 $’. | 
| L | Currency symbol. This currency symbol character can only appear once in the *format* phrase. You can't specify repeated currency symbol characters. | 
| C  | ISO currency symbol. This currency symbol character can only appear once in the *format* phrase. You can't specify repeated currency symbol characters. | 
| N | Full currency name. This currency symbol character can only appear once in the *format* phrase. You can't specify repeated currency symbol characters. | 
| O | Dual currency symbol. You can't specify this character in the *format* phrase. | 
| U | Dual ISO currency symbol. You can't specify this character in the *format* phrase. | 
| A | Full dual currency name. You can't specify this character in the *format* phrase. | 

## Data formatting characters for Signed Zone Decimal, Teradata–style numeric data formatting
<a name="r_Numeric-format-teradata-signed-zone"></a>

You can use the following characters in the *format* phrase of the TEXT\_TO\_INT\_ALT and TEXT\_TO\_NUMERIC\_ALT functions for a signed zoned decimal value. 


| Last character of the input string  | Numeric conversion | 
| --- | --- | 
| { or 0 | n … 0  | 
| A or 1 | n … 1 | 
| B or 2  | n … 2 | 
| C or 3 | *n* … 3 | 
| D or 4  | *n* … 4 | 
| E or 5 | *n* … 5 | 
| F or 6 | *n* … 6 | 
| G or 7  | n … 7 | 
| H or 8  | n … 8 | 
| I or 9  | n … 9 | 
| }  | -n … 0  | 
| J  | -n … 1 | 
| K  | -n … 2  | 
| L  | -n … 3  | 
| M  | -n … 4 | 
| N  | -n … 5 | 
| O  | -n … 6 | 
| P  | -n … 7 | 
| Q  | -n … 8 | 
| R  | -*n* … 9 | 