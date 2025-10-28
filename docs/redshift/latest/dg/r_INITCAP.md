Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# INITCAP function

Capitalizes the first letter of each word in a specified string. INITCAP supports
UTF-8 multibyte characters, up to a maximum of four bytes per character.

## Syntax

```
INITCAP(*string*)
```

## Argument

_string_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

## Return type

VARCHAR

## Usage notes

The INITCAP function makes the first letter of each word in a string uppercase,
and any subsequent letters are made (or left) lowercase. Therefore, it is important
to understand which characters (other than space characters) function as word
separators. A _word separator_ character is any non-alphanumeric
character, including punctuation marks, symbols, and control characters. All of the
following characters are word separators:

```
! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
```

Tabs, newline characters, form feeds, line feeds, and carriage returns are also
word separators.

## Examples

The following examples use data from the CATEGORY and USERS tables in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To capitalize the initials of each word in the CATDESC column, use the following example.

````
`SELECT catid, catdesc, INITCAP(catdesc)
FROM category
ORDER BY 1, 2, 3;`

`+-------+--------------------------------------------+--------------------------------------------+
| catid | catdesc | initcap | +-------+--------------------------------------------+--------------------------------------------+
| 1 | Major League Baseball | Major League Baseball |
| 2 | National Hockey League | National Hockey League |
| 3 | National Football League | National Football League |
| 4 | National Basketball Association | National Basketball Association |
| 5 | Major League Soccer | Major League Soccer |
| 6 | Musical theatre | Musical Theatre |
| 7 | All non-musical theatre | All Non-Musical Theatre |
| 8 | All opera and light opera | All Opera And Light Opera |
| 9 | All rock and pop music concerts | All Rock And Pop Music Concerts |
| 10 | All jazz singers and bands | All Jazz Singers And Bands |
| 11 | All symphony, concerto, and choir concerts | All Symphony, Concerto, And Choir Concerts | +-------+--------------------------------------------+--------------------------------------------+` ``` To show that the INITCAP function does not preserve uppercase characters when they do not begin words, use the following example. For example, the string `MLB` becomes `Mlb`. ``` `SELECT INITCAP(catname) FROM category ORDER BY catname;` `+-----------+
| initcap | +-----------+ | Classical |
| Jazz | | Mlb |
| Mls | | Musicals |
| Nba | | Nfl |
| Nhl | | Opera |
| Plays | | Pop | +-----------+` ``` To show that non-alphanumeric characters other than spaces function as word separators, use the following example. Several letters in each string will be capitalized. ``` `SELECT email, INITCAP(email) FROM users ORDER BY userid DESC LIMIT 5;` `+------------------------------------+------------------------------------+
| email | initcap | +------------------------------------+------------------------------------+ | urna.Ut@egetdictumplacerat.edu | Urna.Ut@Egetdictumplacerat.Edu |
| nibh.enim@egestas.ca | Nibh.Enim@Egestas.Ca | | in@Donecat.ca | In@Donecat.Ca |
| sodales@blanditviverraDonec.ca | Sodales@Blanditviverradonec.Ca | | sociis.natoque.penatibus@vitae.org | Sociis.Natoque.Penatibus@Vitae.Org | +------------------------------------+------------------------------------+` ```
````
