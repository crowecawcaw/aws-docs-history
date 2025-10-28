# Annotation consolidation function

creation

You can choose to use your own annotation consolidation function to determine the
final labels for your labeled objects. There are many possible approaches for
writing a function and the approach that you take depends on the nature of the
annotations to consolidate. Broadly, consolidation functions look at the annotations
from workers, measure the similarity between them, and then use some form of
probabilistic judgment to determine what the most probable label should be.

If you want to use other algorithms to create annotation consolidations functions,
you can find the worker responses in the
``[project-name]`/annotations/worker-response`
folder of the Amazon S3 bucket where you direct the job output.

## Assess similarity

To assess the similarity between labels, you can use one of the following
strategies, or you can use one that meets your data labeling needs:

- For label spaces that consist of discrete, mutually exclusive
  categories, such as multi-class classification, assessing similarity can
  be straightforward. Discrete labels either match or do not match.
- For label spaces that don't have discrete values, such as bounding box
  annotations, find a broad measure of similarity. For bounding boxes, one
  such measure is the Jaccard index. This measures the ratio of the
  intersection of two boxes with the union of the boxes to assess how
  similar they are. For example, if there are three annotations, then
  there can be a function that determines which annotations represent the
  same object and should be consolidated.

## Assess the most probable

label

With one of the strategies detailed in the previous sections in mind, make
some sort of probabilistic judgment on what the consolidated label should be. In
the case of discrete, mutually exclusive categories, this can be
straightforward. One of the most common ways to do this is to take the results
of a majority vote between the annotations. This weights the annotations
equally.

Some approaches attempt to estimate the accuracy of different annotators and
weight their annotations in proportion to the probability of correctness. An
example of this is the Expectation Maximization method, which is used in the
default Ground Truth consolidation function for multi-class annotations.

For more information about creating an annotation consolidation function, see
[Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md "sms-custom-templates-step3.md").
