# AWS Clean Rooms ML model evaluation metrics

Clean Rooms ML computes the _recall_ and _relevance
score_ to determine how well your model performs. Recall compares the
similarity between the lookalike data and training data. The relevance score is used
to decide how large the audience should be, not whether the model is
well-performing.

_Recall_ is an unbiased measure of how similar the lookalike
segment is to the training data. Recall is the percentage of the most similar users
(by default, the most similar 20%) from a sample of the training data that are
included in the seed audience by the audience generation job. Values range from 0-1,
larger values indicate a better audience. A recall value approximately equal to the
maximum bin percentage indicates that the audience model is equivalent to random
selection.

We consider this a better evaluation metric than accuracy, precision, and F1
scores because Clean Rooms ML doesn't have accurately labeled true negative users when
building its model.

Segment-level _relevance score_ is a measure of similarity with
values ranging from -1 (least similar) to 1 (most similar). Clean Rooms ML computes a set
of relevance scores for various segment sizes to help you determine the best segment
size for your data. Relevance scores monotonically decrease as the segment size
increases, thus as the segment size increases it can be less similar to the seed
data. When the segment-level relevance score reaches 0, the model predicts that all
users in the lookalike segment are from the same distribution as the seed data.
Increasing the output size is likely to include users in the lookalike segment that
aren't from the same distribution as the seed data.

Relevance scores are normalized within a single campaign and should not be used to
compare across campaigns. Relevancy scores shouldn't be used as a single-sourced
evidence for any business outcome because those are impacted by multiple complex
factors in addition to relevance, such as inventory quality, inventory type, timing
of advertising, and so on.

Relevance scores should not be used to judge the quality of the seed, but rather
if it can be increased or decreased. Consider the following examples:

- All positive scores – This indicates that there are more output
  users that are predicted as similar than are included in the lookalike
  segment. This is common for seed data that's part of a large market, such as
  everybody who has bought toothpaste in the past month. We recommend looking
  at smaller seed data, such as everybody who has bought toothpaste more than
  once in the past month.
- All negatives scores or negative for your desired lookalike segment size
  – This indicates that Clean Rooms ML predicts there aren't enough similar
  users in the desired lookalike segment size. This can be because the seed
  data is too specific or the market is too small. We recommend either
  applying fewer filters to the seed data or widening the market. For example,
  if the original seed data was customers that bought a stroller and car seat,
  you could expand the market to customers that bought multiple baby
  products.
  Training data providers determine whether the relevance scores are exposed and the
  bucket bins where relevance scores are computed.
