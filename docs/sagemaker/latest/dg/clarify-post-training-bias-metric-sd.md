# Specificity difference

(SD)

The specificity difference (SD) is the difference in specificity between the favored
facet _a_ and disfavored facet _d_. Specificity measures how often the model correctly predicts a
negative outcome (y'=0). Any difference in these specificities is a potential form of
bias.

Specificity is perfect for a facet if all of the y=0 cases are correctly predicted for
that facet. Specificity is greater when the model minimizes false positives, known as a
Type I error. For example, the difference between a low specificity for lending to facet
_a_, and high specificity for lending to facet
_d_, is a measure of bias against facet _d_.

The following formula is for the difference in the specificity for facets _a_ and _d_.

        SD =
TNd/(TNd + FPd)

- TNa/(TNa + FPa) =
  TNRd - TNRa

The following variables used to calculated SD are defined as follows:

- TNd are the true negatives predicted for facet
  _d_.
- FPd are the false positives predicted for facet
  _d_.
- TNd are the true negatives predicted for facet
  _a_.
- FPd are the false positives predicted for facet
  _a_.
- TNRa =
  TNa/(TNa +
  FPa) is the true negative rate, also known as the
  specificity, for facet _a_.
- TNRd =
  TNd/(TNd +
  FPd) is the true negative rate, also known as the
  specificity, for facet _d_.
  For example, consider the following confusion matrices for facets _a_ and _d_.

Confusion matrix for the favored facet `a`

| Class a predictions | Actual outcome 0 | Actual outcome 1 | Total |
| ------------------- | ---------------- | ---------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                   | 20               | 5                | 25    |
| 1                   | 10               | 65               | 75    |
| Total               | 30               | 70               | 100   | Confusion matrix for the disfavored facet `d`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Class d predictions | Actual outcome 0 | Actual outcome 1 | Total |
| ---                 | ---              | ---              | ---   |
| 0                   | 18               | 7                | 25    |
| 1                   | 5                | 20               | 25    |
| Total               | 23               | 27               | 50    | The value of the specificity difference is `SD = 18/(18+5) - 20/(20+10) = 0.7826 <br>• 0.6667 = 0.1159`, which indicates a bias against facet _d_. The range of values for the specificity difference between facets _a_ and _d_ for binary and multicategory classification is `[-1, +1]`. This metric is not available for the case of continuous labels. Here is what different values of SD imply: <br>• Positive values are obtained when there is higher specificity for facet _d_ than for facet _a_. This suggests that the model finds less false positives for facet _d_ than for facet _a_. A positive value indicates bias against facet _d_. <br>• Values near zero indicate that the specificity for facets that are being compared is similar. This suggests that the model finds a similar number of false positives in both of these facets and is not biased. <br>• Negative values are obtained when there is higher specificity for facet _a_ than for facet _d_. This suggests that the model finds more false positives for facet _a_ than for facet _d_. A negative value indicates bias against facet _a_. |
