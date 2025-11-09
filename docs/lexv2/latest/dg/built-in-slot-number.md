# AMAZON.Number

Converts words or numbers that express a number into digits,
including decimal numbers. The following table shows how the
`AMAZON.Number` slot type captures numeric
words.

| Input                                       | Response |
| ------------------------------------------- | -------- |
| one hundred twenty three point four<br>five | 123.45   |
| one hundred twenty three dot four<br>five   | 123.45   |
| point four two                              | 0.42     |
| point forty two                             | 0.42     |
| 232.998                                     | 232.998  |
| 50                                          | 50       |
| -15                                         | -15      |
| minus 15                                    | -15      |
| minus fifteen point two four five           | -15.245  |
