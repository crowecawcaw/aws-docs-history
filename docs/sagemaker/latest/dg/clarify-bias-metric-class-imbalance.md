

# Class Imbalance (CI)
<a name="clarify-bias-metric-class-imbalance"></a>

**Note**  
Amazon SageMaker Clarify is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Clarify, but we do not plan to introduce new features. For more information, see [Clarify availability change](clarify-availability-change.md). 

Class imbalance (CI) bias occurs when a facet value *d* has fewer training samples when compared with another facet *a* in the dataset. This is because models preferentially fit the larger facets at the expense of the smaller facets and so can result in a higher training error for facet *d*. Models are also at higher risk of overfitting the smaller data sets, which can cause a larger test error for facet *d*. Consider the example where a machine learning model is trained primarily on data from middle-aged individuals (facet a), it might be less accurate when making predictions involving younger and older people (facet d).

The formula for the (normalized) facet imbalance measure:

        CI = (na - nd)/(na \+ nd)

Where na is the number of members of facet *a* and nd the number for facet *d*. Its values range over the interval [-1, 1]. 
+ Positive CI values indicate the facet *a* has more training samples in the dataset and a value of 1 indicates the data only contains members of the facet *a*.
+  Values of CI near zero indicate a more equal distribution of members between facets and a value of zero indicates a perfectly equal partition between facets and represents a balanced distribution of samples in the training data.
+ Negative CI values indicate the facet *d* has more training samples in the dataset and a value of -1 indicates the data only contains members of the facet *d*.
+ CI values near either of the extremes values of -1 or 1 are very imbalanced and are at a substantial risk of making biased predictions.

If a significant facet imbalance is found to exist among the facets, you might want to rebalance the sample before proceeding to train models on it.