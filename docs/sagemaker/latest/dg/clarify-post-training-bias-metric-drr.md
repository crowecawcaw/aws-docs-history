# Difference in Rejection Rates

(DRR)

The difference in rejection rates (DRR) metric is the difference in the ratios of the
true negative (TN) predictions to the observed negatives (TN + FN) for facets _a_ and _d_. This metric
measures the difference in the precision of the model for predicting rejections from
these two facets. Precision measures the fraction of unqualified candidates from the
pool of unqualified candidates that are identified as such by the model. If the model
precision for predicting unqualified applicants diverges between the facets, this is a
bias and its magnitude is measured by the DRR.

The formula for difference in rejection rates between facets _a_ and _d_:

        DRR =
TNd/(TNd + FNd)

- TNa/(TNa + FNa)

The components for the previous DRR equation are as follows.

- TNd are the true negatives predicted for facet
  _d_.
- FNd are the false negatives predicted for facet
  _d_.
- TPa are the true negatives predicted for facet
  _a_.
- FNa are the false negatives predicted for facet
  _a_.
  For example, suppose the model rejects 100 middle-aged applicants (facet _a_) for a loan (predicted negative labels) of whom 80 are
  actually unqualified (observed negative labels). Also suppose the model rejects 50
  applicants from other age demographics (facet _d_) for
  a loan (predicted negative labels) of whom only 40 are actually unqualified (observed
  negative labels). Then DRR = 40/50 - 80/100 = 0, so no bias is indicated.

The range of values for DRR for binary, multicategory facet, and continuous labels is
[-1, +1].

- Positive values occur when the ratio of the predicted negatives (rejections)
  to the observed negative outcomes (unqualified applicants) for facet _d_ is larger than the same ratio for facet _a_. These values indicate a possible bias against
  the favored facet _a_ caused by the occurrence
  of relatively more false negatives in facet _a_. The larger the difference in the ratios, the more extreme the
  apparent bias.
- Values near zero occur when the ratio of the predicted negatives (rejections)
  to the observed negative outcomes (unqualified applicants) for facets _a_ and _d_ have
  similar values, indicating the observed labels for negative outcomes are being
  predicted with equal precision by the model.
- Negative values occur when the ratio of the predicted negatives (rejections)
  to the observed negative outcomes (unqualified applicants) for facet _a_ is larger than the ratio facet _d_. These values indicate a possible bias against
  the disfavored facet _d_ caused by the
  occurrence of relatively more false positives in facet _d_. The more negative the difference in the ratios, the more
  extreme the apparent bias.
