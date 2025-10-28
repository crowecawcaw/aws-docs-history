End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.NUMBER

Converts words or numbers that express a number into digits,
including decimal numbers. The following table shows how the
`AMAZON.NUMBER` slot type captures numeric
words.

| Input                                    | Response |
| ---------------------------------------- | -------- |
| one hundred twenty three point four five | 123.45   |
| one hundred twenty three dot four five   | 123.45   |
| point four two                           | 0.42     |
| point forty two                          | 0.42     |
| 232.998                                  | 232.998  |
| 50                                       | 50       |
