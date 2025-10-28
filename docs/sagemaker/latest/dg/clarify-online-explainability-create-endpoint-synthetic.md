# Synthetic

dataset

SageMaker Clarify uses the Kernel SHAP algorithm. Given a record (also called a sample or an
instance) and the SHAP configuration, the explainer first generates a synthetic
dataset. SageMaker Clarify then queries the model container for the predictions of the dataset,
and then computes and returns the feature attributions. The size of the synthetic
dataset affects the runtime for the Clarify explainer. Larger synthetic datasets
take more time to obtain model predictions than smaller ones.

The synthetic dataset size is determined by the following formula:

```
Synthetic dataset size = SHAP baseline size * n_samples
```

The SHAP baseline size is the number of records in the SHAP baseline data. This
information is taken from the `ShapBaselineConfig`.

The size of `n_samples` is set by the parameter
`NumberOfSamples` in the explainer configuration and the number of
features. If the number of features is `n_features`, then
`n_samples` is the following:

```
n_samples = MIN(NumberOfSamples, 2^n_features - 2)
```

The following shows `n_samples` if `NumberOfSamples` is not
provided.

```
n_samples = MIN(2*n_features + 2^11, 2^n_features - 2)
```

For example, a tabular record with 10 features has a SHAP baseline size of 1. If
`NumberOfSamples` is not provided, the synthetic dataset contains
1022 records. If the record has 20 features, the synthetic dataset contains 2088
records.

For NLP problems, `n_features` is equal to the number of non-text
features plus the number of text units.

###### Note

The `InvokeEndpoint` API has a request timeout limit. If the
synthetic dataset is too large, the explainer may not be able to complete the
computation within this limit. If necessary, use the previous information to
understand and reduce the SHAP baseline size and `NumberOfSamples`.
If your model container is set up to handle batch requests, then you can also
adjust the value of `MaxRecordCount`.
