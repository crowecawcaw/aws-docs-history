# Repeats

The following table shows the supported repeated expansions
for rules. For more information, see [Repeats](https://www.w3.org/TR/speech-grammar/#S2.5 "https://www.w3.org/TR/speech-grammar/#S2.5") in the _Speech recognition grammar
specification version 1_ W3C recommendation.

| XML<br>formExample                       | Behavior                                                                                                                                                                                                                 | Supported? |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| _repeat="n"_<br>repeat="6"               | The contained expression is repeated exactly<br>"n" times. "n" must be "0" or a positive<br>integer.                                                                                                                     | Yes        |
| _repeat="m-n"_<br>repeat="4-6"           | The contained expansion is repeated between<br>"m" and "n" times (inclusive). "m" and "n" must<br>both be "0" or a positive integer, and "m" must<br>be less than or equal to "n".                                       | Yes        |
| _repeat="m-"_<br>repeat="3-"             | The contained expansion is repeated "m" times<br>or more (inclusive). "m" must be "0" or a<br>postive integer. For example, "3-" declares that<br>the contained expansion can occur three, four,<br>five, or more times. | Yes        |
| _repeat="0-1"_                           | The contained expansion is optional.                                                                                                                                                                                     | Yes        |
| <item repeat="2-4"<br>repeat-prob="0.8"> |                                                                                                                                                                                                                          | **No**     |
