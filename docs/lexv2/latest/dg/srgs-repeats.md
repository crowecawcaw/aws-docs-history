# Repeats

The following table shows the supported repeated expansions
for rules. For more information, see [Repeats](https://www.w3.org/TR/speech-grammar/#S2.5 "https://www.w3.org/TR/speech-grammar/#S2.5") in the _Speech recognition grammar
specification version 1_ W3C recommendation.

| XML formExample                       | Behavior                                                                                                                                                                                                     | Supported? |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| _repeat="n"_ repeat="6"               | The contained expression is repeated exactly "n" times. "n" must be "0" or a positive integer.                                                                                                               | Yes        |
| _repeat="m-n"_ repeat="4-6"           | The contained expansion is repeated between "m" and "n" times (inclusive). "m" and "n" must both be "0" or a positive integer, and "m" must be less than or equal to "n".                                    | Yes        |
| _repeat="m-"_ repeat="3-"             | The contained expansion is repeated "m" times or more (inclusive). "m" must be "0" or a postive integer. For example, "3-" declares that the contained expansion can occur three, four, five, or more times. | Yes        |
| _repeat="0-1"_                        | The contained expansion is optional.                                                                                                                                                                         | Yes        |
| <item repeat="2-4" repeat-prob="0.8"> |                                                                                                                                                                                                              | **No**     |
