# Choosing a system configuration

| RAISP04: How will you choose between<br>different system configurations? |
| ------------------------------------------------------------------------ |
|                                                                          |

Teams test different candidate configurations of their system,
including different versions of components or models during
development using validation sets to determine which performs
best. Different versions can come from different component
choices, hyperparameters, training settings, or model
architectures. Teams set up controlled comparisons between
versions on the same validation data, then use paired statistical
tests to determine if one version is statistically better than the
other based on release criteria. Evaluation sets stay separate
from component selection to avoid biasing final performance
measurements and release decisions.

###### Best practices

- [RAISP04-BP01 Use paired tests to choose from candidate
  designs](raisp04-bp01.md "raisp04-bp01.md")
