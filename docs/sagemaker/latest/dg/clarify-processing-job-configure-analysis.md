# Analysis Configuration Files

To analyze your data and models for explainability and bias using SageMaker Clarify, you must
configure a processing job. Part of the configuration for this processing job includes the
configuration of an analysis file. The analysis file specifies the parameters for bias
analysis and explainability. See [Configure a SageMaker Clarify Processing Job](clarify-processing-job-configure-parameters.md "clarify-processing-job-configure-parameters.md") to learn how to configure
a processing job and analysis file.

This guide describes the schema and parameters for this analysis configuration file. This
guide also includes examples of analysis configuration files for computing bias metrics for
a tabular dataset, and generating explanations for natural language processing (NLP),
computer vision (CV), and time series (TS) problems.

You can create the analysis configuration file or use the [SageMaker Python SDK](https://sagemaker.readthedocs.io/ "https://sagemaker.readthedocs.io/") to generate one for you
with the [SageMaker ClarifyProcessor](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SageMakerClarifyProcessor "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SageMakerClarifyProcessor") API. Viewing the file contents can be helpful for understanding
the underlying configuration used by the SageMaker Clarify job.

###### Topics

- [Schema for the analysis
  configuration file](#clarify-processing-job-configure-schema "#clarify-processing-job-configure-schema")
- [Example analysis
  configuration files](#clarify-processing-job-configure-analysis-examples "#clarify-processing-job-configure-analysis-examples")

## Schema for the analysis

configuration file

The following section describes the schema for the analysis configuration file
including requirements and descriptions of parameters.

### Requirements

for the analysis configuration file

The SageMaker Clarify processing job expects the analysis configuration file to be structured
with the following requirements:

- The processing input name must be `analysis_config.`
- The analysis configuration file is in JSON format, and encoded in
  UTF-8.
- The analysis configuration file is an Amazon S3 object.

You can specify additional parameters in the analysis configuration file. The
following section provides various options to tailor the SageMaker Clarify processing job for
your use case and desired types of analysis.

In the analysis configuration file, you can specify the following
parameters.

- version – (Optional) The version
  string of the analysis configuration file schema. If a version is not
  provided, SageMaker Clarify uses the latest supported version. Currently, the only
  supported version is `1.0`.
- dataset_type – The format of the
  dataset. The input dataset format can be any of the following
  values:
  - Tabular
    - `text/csv` for CSV
    - `application/jsonlines` for [SageMaker AI JSON Lines dense format](cdf-inference.md#cm-jsonlines "cdf-inference.md#cm-jsonlines")
    - `application/json` for JSON
    - `application/x-parquet` for Apache Parquet
    - `application/x-image` to activate explainability
      for computer vision problems

  - Time series forecasting model explanations
    - `application/json` for JSON

- dataset_uri – (Optional) The
  uniform resource identifier (URI) of the main dataset. If you provide a
  S3 URI prefix, the SageMaker Clarify processing job recursively collects all S3
  files located under the prefix. You can provide either a S3 URI prefix
  or a S3 URI to an image manifest file for computer vision problems. If
  `dataset_uri` is provided, it takes precedence over the
  dataset processing job input. For any format type except image and time
  series use cases, the
  SageMaker Clarify processing job loads the input dataset into a tabular data frame,
  as a **tabular dataset**. This format
  allows SageMaker AI to easily manipulate and analyze the input dataset.
- headers – (Optional)
  - **Tabular:** An array of
    strings containing the column names of a tabular dataset. If a value is
    not provided for `headers`, the SageMaker Clarify processing job
    reads the headers from the dataset. If the dataset doesn’t have headers,
    then the Clarify processing job automatically generates placeholder
    names based on zero-based column index. For example, placeholder names
    for the first and second columns will be
    `column_0`, `column_1`, and
    so on.

  ###### Note

  By convention, if `dataset_type` is
  `application/jsonlines` or
  `application/json`, then `headers` should
  contain the following names in order:

      1. feature names
      2. label name (if `label` is specified)
      3. predicted label name (if `predicted_label`
       is specified)An example for

  `headers` for an `application/jsonlines`
  dataset type if `label` is specified is:
  `["feature1","feature2","feature3","target_label"]`.
  - **Time series:** A list of
    column names in the dataset. If not provided, Clarify generates headers to
    use internally. For time series explainability cases, provide headers
    in the following order:
    1. item id
    2. timestamp
    3. target time series
    4. all related time series columns
    5. all static covariate columns

- label – (Optional) A string or a
  zero-based integer index. If provided, `label` is used to
  locate the ground truth label, also known as an observed label or target
  attribute in a tabular dataset. The ground truth label is used to
  compute bias metrics. The value for `label` is specified
  depending on the value of the `dataset_type` parameter as
  follows.
  - If `dataset_type` is
    `text/csv`, `label` can be
    specified as either of the following:
    - A valid column name
    - An index that lies within the range of dataset
      columns

  - If `dataset_type` is
    `application/parquet`,
    `label` must be a valid column name.
  - If `dataset_type` is
    `application/jsonlines`,
    `label` must be a [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression
    written to extract the ground truth label from the dataset. By
    convention, if `headers` is specified, then it should
    contain the label name.
  - If `dataset_type` is
    `application/json`, `label`
    must be a [JMESPath](https://jmespath.org/ "https://jmespath.org/")
    expression written to extract the ground truth label for each
    record in the dataset. This JMESPath expression must produce a
    list of labels where the ith label
    correlates to the ith record.

- predicted_label – (Optional) A
  string or a zero-based integer index. If provided,
  `predicted_label` is used to locate the column containing
  the predicted label in a tabular dataset. The predicted label is used to
  compute post-training **bias metrics**. The
  parameter `predicted_label` is optional if the dataset
  doesn’t include predicted label. If predicted labels are required for
  computation, then the SageMaker Clarify processing job will get predictions from the
  model.

The value for `predicted_label` is specified depending on
the value of the `dataset_type` as follows:

    + If `dataset_type` is
     `text/csv`,
     `predicted_label` can be specified as either of
     the following:




    	- A valid column name. If
    	 `predicted_label_dataset_uri` is
    	 specified, but `predicted_label` is not
    	 provided, the default predicted label name is
    	 "predicted\_label".
    	- An index that lies within the range of dataset
    	 columns. If `predicted_label_dataset_uri` is
    	 specified, then the index is used to locate the
    	 predicted label column in the predicted label
    	 dataset.
    + If dataset\_type is
     `application/x-parquet`,
     `predicted_label` must be a valid column
     name.
    + If dataset\_type is
     `application/jsonlines`,
     `predicted_label` must be a valid [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression
     written to extract the predicted label from the dataset. By
     convention, if `headers` is specified, then it should
     contain the predicted label name.
    + If `dataset_type` is
     `application/json`,
     `predicted_label` must be a [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression
     written to extract the predicted label for each record in the
     dataset. The JMESPath expression should produce a list of
     predicted labels where the ith
     predicted label is for the ith
     record.

- features – (Optional) Required
  for non-time-series use cases if
  `dataset_type` is `application/jsonlines` or
  `application/json`. A JMESPath string expression written
  to locate the features in the input dataset. For
  `application/jsonlines`, a JMESPath expression will be
  applied to each line to extract the features for that record. For
  `application/json`, a JMESPath expression will be applied
  to the whole input dataset. The JMESPath expression should extract a
  list of lists, or a 2D array/matrix of features where the
  ith row contains the features that
  correlate to the ith record. For a
  `dataset_type` of `text/csv` or
  `application/x-parquet`, all columns except for the
  ground truth label and predicted label columns are automatically
  assigned to be features.
- predicted_label_dataset_uri –
  (Optional)
  Only applicable when dataset_type is `text/csv`. The S3 URI
  for a dataset containing predicted labels used to compute post-training
  **bias metrics**. The SageMaker Clarify processing
  job will load the predictions from the provided URI instead of getting
  predictions from the model. In this case, `predicted_label`
  is required to locate the predicted label column in the predicted label
  dataset. If the predicted label dataset or the main dataset is split
  across multiple files, an identifier column must be specified by
  `joinsource_name_or_index` to join the two datasets.
- predicted_label_headers –
  (Optional) Only
  applicable when `predicted_label_dataset_uri` is specified.
  An array of strings containing the column names of the predicted label
  dataset. Besides the predicted label header,
  `predicted_label_headers` can also contain the header of
  the identifier column to join the predicted label dataset and the main
  dataset. For more information, see the following description for the
  parameter `joinsource_name_or_index`.
- joinsource_name_or_index –
  (Optional) The
  name or zero-based index of the column in tabular datasets to be used as
  a identifier column while performing an inner join. This column is only
  used as an identifier. It isn't used for any other computations like
  bias analysis or feature attribution analysis. A value for
  `joinsource_name_or_index` is needed in the following
  cases:
  - There are multiple input datasets, and any one is split across
    multiple files.
  - Distributed processing is activated by setting the SageMaker Clarify
    processing job [InstanceCount](../APIReference/API_ProcessingClusterConfig.md#sagemaker-Type-ProcessingClusterConfig-InstanceCount "../APIReference/API_ProcessingClusterConfig.md#sagemaker-Type-ProcessingClusterConfig-InstanceCount") to a value greater than
    `1`.

- excluded_columns – (Optional) An
  array of names or zero-based indices of columns to be excluded from
  being sent to the model as input for predictions. Ground truth label and
  predicted label are automatically excluded already. This feature is not
  supported for time series.
- probability_threshold –
  (Optional) A floating point number above which,
  a label or object is
  selected. The default value is `0.5`. The SageMaker Clarify processing
  job uses `probability_threshold` in the following
  cases:
  - In post-training bias analysis,
    `probability_threshold` converts a numeric model
    prediction (probability value or score) to a binary label, if
    the model is a binary classifier. A score greater than the
    threshold is converted to `1`. Whereas, a score less
    than or equal to the threshold is converted to
    `0`.
  - In computer vision explainability problems, if model_type is
    `OBJECT_DETECTION``,
probability_threshold` filters out objects detected
    with confidence scores lower than the threshold value.

- label_values_or_threshold –
  (Optional) Required for bias analysis.
  An array of label values or a threshold
  number, which indicate positive outcome for ground truth and predicted
  labels for bias metrics. For more information, see positive label values
  in [Amazon SageMaker Clarify Terms for Bias and
  Fairness](clarify-detect-data-bias.md#clarify-bias-and-fairness-terms "clarify-detect-data-bias.md#clarify-bias-and-fairness-terms"). If the label is
  numeric, the threshold is applied as the lower bound to select the
  positive outcome. To set `label_values_or_threshold` for
  different problem types, refer to the following examples:
  - For a binary classification problem, the label has two
    possible values, `0` and `1`. If label
    value `1` is favorable to a demographic group
    observed in a sample, then
    `label_values_or_threshold` should be set to
    `[1]`.
  - For a multiclass classification problem, the label has three
    possible values, `bird`,
    `cat`, and `dog`.
    If the latter two define a demographic group that bias favors,
    then `label_values_or_threshold` should be set to
    `["cat","dog"]`.
  - For a regression problem, the label value is continuous,
    ranging from `0` to `1`. If a value
    greater than `0.5` should designate a sample as
    having a positive result, then
    `label_values_or_threshold` should be set to
    `0.5`.

- facet – (Optional) Required for bias
  analysis. An array of facet objects, which are composed of sensitive
  attributes against which bias is measured. You can use facets to
  understand the bias characteristics of your dataset and model even if
  your model is trained without using sensitive attributes. For more
  information, see **Facet** in [Amazon SageMaker Clarify Terms for Bias and
  Fairness](clarify-detect-data-bias.md#clarify-bias-and-fairness-terms "clarify-detect-data-bias.md#clarify-bias-and-fairness-terms"). Each facet object
  includes the following fields:
  - name_or_index – (Optional) The name
    or zero-based index of the sensitive attribute column in a
    tabular dataset. If `facet_dataset_uri` is specified,
    then the index refers to the facet dataset instead of the main
    dataset.
  - value_or_threshold –
    (Optional) Required if
    `facet` is numeric and
    `label_values_or_threshold` is applied as the
    lower bound to select the sensitive group). An array of facet
    values or a threshold number, that indicates the sensitive
    demographic group that bias favors. If facet data type is
    categorical and `value_or_threshold` is not provided,
    bias metrics are computed as one group for every unique value
    (rather than all values). To set `value_or_threshold`
    for different `facet` data types, refer to the
    following examples:
    - For a binary facet data type, the feature has two
      possible values, `0` and `1`. If
      you want to compute the bias metrics for each value,
      then `value_or_threshold` can be either
      omitted or set to an empty array.
    - For a categorical facet data type, the feature has
      three possible values `bird`,
      `cat`, and
      `dog`. If the first two define
      a demographic group that bias favors, then
      `value_or_threshold` should be set to
      `["bird", "cat"]`. In this example, the
      dataset samples are split into two demographic groups.
      The facet in the advantaged group has value
      `bird` or
      `cat`, while the facet in the
      disadvantaged group has value
      `dog`.
    - For a numeric facet data type, the feature value is
      continuous, ranging from `0` to
      `1`. As an example, if a value greater
      than `0.5` should designate a sample as
      favored, then `value_or_threshold` should be
      set to `0.5`. In this example, the dataset
      samples are split into two demographic groups. The facet
      in the advantaged group has value greater than
      `0.5`, while the facet in the
      disadvantaged group has value less than or equal to
      `0.5`.

- group_variable – (Optional) The name or
  zero-based index of the column that indicates the subgroup to be used
  for the bias metric [Conditional Demographic Disparity
  (CDD)](clarify-data-bias-metric-cddl.md "clarify-data-bias-metric-cddl.md") or [Conditional Demographic
  Disparity in Predicted Labels (CDDPL)](clarify-post-training-bias-metric-cddpl.md "clarify-post-training-bias-metric-cddpl.md").
- facet_dataset_uri – (Optional) Only
  applicable when dataset_type is `text/csv`. The S3 URI for a
  dataset containing sensitive attributes for bias analysis. You can use
  facets to understand the bias characteristics of your dataset and model
  even if your model is trained without using sensitive attributes.

###### Note

If the facet dataset or the main dataset is split across multiple
files, an identifier column must be specified by
`joinsource_name_or_index` to join the two datasets.
You must use the parameter `facet` to identify each facet
in the facet dataset.

- facet_headers – (Optional) Only applicable
  when `facet_dataset_uri` is specified. An array of strings
  containing column names for the facet dataset, and optionally, the
  identifier column header to join the facet dataset and the main dataset,
  see `joinsource_name_or_index`.
- time_series_data_config –
  (Optional) Specifies the configuration to use for data processing of
  a time series.

      + item\_id –
       A string or a zero-based integer index. This field is used to locate an item
       id in the shared input dataset.
      + timestamp –
       A string or a zero-based integer index. This field is used to locate a
       timestamp in the shared input dataset.
      + dataset\_format –
       Possible values are `columns`,
       `item_records`, or `timestamp_records`.
       This field is used to describe the format of a JSON dataset,
       which is the only format supported for time series
       explainability.
      + target\_time\_series –
       A JMESPath string or a zero-based integer index. This field is used to locate
       the target time series in the shared input dataset. If this
       parameter is a string, then all other parameters except `dataset_format`
       must be strings or lists of strings. If this parameter is an integer, then
       all other parameters except `dataset_format` must be integers or
       lists of integers.
      + related\_time\_series –
       (Optional) An array of JMESPath expressions.
       This field is used to locate all related time series in the shared input dataset,
       if present.
      + static\_covariates –
       (Optional) An array of JMESPath expressions.
       This field is used to locate all static covariate fields in the shared input dataset,
       if present.

  For examples, see [Time series
  dataset config examples](clarify-processing-job-data-format-time-series.md#clarify-processing-job-data-format-time-series-ex "clarify-processing-job-data-format-time-series.md#clarify-processing-job-data-format-time-series-ex").

- methods – An object containing
  one or more analysis methods and their parameters. If any method is
  omitted, it is neither used for analysis nor reported.
  - pre_training_bias –
    Include this method if you want to compute pre-training bias
    metrics. The detailed description of the metrics can be found in
    [Pre-training Bias Metrics](clarify-measure-data-bias.md "clarify-measure-data-bias.md"). The object has
    the following parameters:
    - methods – An
      array that contains any of the pre-training bias metrics
      from the following list that you want to compute. Set
      `methods` to `all`
      to compute all pre-training bias metrics. As an example,
      the array `["CI", "DPL"]` will compute
      **Class Imbalance** and
      **Difference in Proportions of
      Labels**.
      - `CI` for [Class Imbalance (CI)](clarify-bias-metric-class-imbalance.md "clarify-bias-metric-class-imbalance.md")
      - `DPL` for [Difference in
        Proportions of Labels (DPL)](clarify-data-bias-metric-true-label-imbalance.md "clarify-data-bias-metric-true-label-imbalance.md")
      - `KL` for [Kullback-Leibler Divergence
        (KL)](clarify-data-bias-metric-kl-divergence.md "clarify-data-bias-metric-kl-divergence.md")
      - `JS` for [Jensen-Shannon
        Divergence (JS)](clarify-data-bias-metric-jensen-shannon-divergence.md "clarify-data-bias-metric-jensen-shannon-divergence.md")
      - `LP` for [Lp-norm
        (LP)](clarify-data-bias-metric-lp-norm.md "clarify-data-bias-metric-lp-norm.md")
      - `TVD` for [Total Variation
        Distance (TVD)](clarify-data-bias-metric-total-variation-distance.md "clarify-data-bias-metric-total-variation-distance.md")
      - `KS` for [Kolmogorov-Smirnov
        (KS)](clarify-data-bias-metric-kolmogorov-smirnov.md "clarify-data-bias-metric-kolmogorov-smirnov.md")
      - `CDDL` for [Conditional Demographic Disparity
        (CDD)](clarify-data-bias-metric-cddl.md "clarify-data-bias-metric-cddl.md")

  - post_training_bias –
    Include this method if you want to compute post-training bias
    metrics. The detailed description of the metrics can be found in
    [Post-training Data and Model
    Bias Metrics](clarify-measure-post-training-bias.md "clarify-measure-post-training-bias.md"). The
    `post_training_bias` object has the following
    parameters.
    - methods – An
      array that contains any of the post-training bias
      metrics from the following list that you want to
      compute. Set `methods` to
      `all` to compute all
      post-training bias metrics. As an example, the array
      `["DPPL", "DI"]` computes the **Difference in Positive Proportions in
      Predicted Labels** and **Disparate Impact**. The
      available methods are as follows.
      - `DPPL` for [Difference in Positive
        Proportions in Predicted Labels (DPPL)](clarify-post-training-bias-metric-dppl.md "clarify-post-training-bias-metric-dppl.md")
      - `DI`for [Disparate Impact (DI)](clarify-post-training-bias-metric-di.md "clarify-post-training-bias-metric-di.md")
      - `DCA` for [Difference in Conditional
        Acceptance (DCAcc)](clarify-post-training-bias-metric-dcacc.md "clarify-post-training-bias-metric-dcacc.md")
      - `DCR` for [Difference in Conditional
        Rejection (DCR)](clarify-post-training-bias-metric-dcr.md "clarify-post-training-bias-metric-dcr.md")
      - `SD` for [Specificity difference
        (SD)](clarify-post-training-bias-metric-sd.md "clarify-post-training-bias-metric-sd.md")
      - `RD` for [Recall Difference (RD)](clarify-post-training-bias-metric-rd.md "clarify-post-training-bias-metric-rd.md")
      - `DAR` for [Difference in Acceptance Rates
        (DAR)](clarify-post-training-bias-metric-dar.md "clarify-post-training-bias-metric-dar.md")
      - `DRR` for [Difference in Rejection Rates
        (DRR)](clarify-post-training-bias-metric-drr.md "clarify-post-training-bias-metric-drr.md")
      - `AD` for [Accuracy Difference (AD)](clarify-post-training-bias-metric-ad.md "clarify-post-training-bias-metric-ad.md")
      - `TE` for [Treatment Equality (TE)](clarify-post-training-bias-metric-te.md "clarify-post-training-bias-metric-te.md")
      - `CDDPL` for [Conditional Demographic
        Disparity in Predicted Labels (CDDPL)](clarify-post-training-bias-metric-cddpl.md "clarify-post-training-bias-metric-cddpl.md")
      - `FT` for [Counterfactual Fliptest
        (FT)](clarify-post-training-bias-metric-ft.md "clarify-post-training-bias-metric-ft.md")
      - `GE` for [Generalized entropy (GE)](clarify-post-training-bias-metric-ge.md "clarify-post-training-bias-metric-ge.md")

  - shap – Include this
    method if you want to compute SHAP values. The SageMaker Clarify processing
    job supports the Kernel SHAP algorithm. The `shap`
    object has the following parameters.
    - baseline –
      (Optional) The SHAP baseline dataset, also known as the
      background dataset. Additional requirements for the
      baseline dataset in a tabular dataset or computer vision
      problem are as follows. For more information about SHAP
      Baselines, see [SHAP Baselines for
      Explainability](clarify-feature-attribute-shap-baselines.md "clarify-feature-attribute-shap-baselines.md")
      - For a **tabular**
        dataset, `baseline` can be either the
        in-place baseline data or the S3 URI of a baseline
        file. If `baseline` is not provided,
        the SageMaker Clarify processing job computes a baseline by
        clustering the input dataset. The following are
        required of the baseline:

            + The format must be the same as the dataset
             format specified by
             `dataset_type`.
            + The baseline can only contain features that
             the model can accept as input.
            + The baseline dataset can have one or more
             instances. The number of baseline instances
             directly affects the synthetic dataset size and
             job runtime.
            + If `text_config` is specified,
             then the baseline value of a text column is a
             string used to replace the unit of text specified
             by `granularity`. For example, one
             common placeholder is "[MASK]", which is used to
             represent a missing or unknown word or piece of
             text.

        The following examples show how to set
        in-place baseline data for different
        `dataset_type` parameters:

            + If `dataset_type` is either
             `text/csv` or
             `application/x-parquet`, the model
             accepts four numeric features, and the baseline
             has two instances. In this example, if one record
             has all zero feature values and the other record
             has all one feature values, then baseline should
             be set to `[[0,0,0,0],[1,1,1,1]]`,
             without any header.
            + If `dataset_type` is
             `application/jsonlines`, and
             `features` is the key to a list of four
             numeric feature values. In addition, in this
             example, if the baseline has one record of all
             zero values, then `baseline` should be
             `[{"features":[0,0,0,0]}]`.
            + If `dataset_type` is
             `application/json`, the
             `baseline` dataset should have the same
             structure and format as the input dataset.

      - For **computer
        vision** problems, `baseline`
        can be the S3 URI of an image that is used to mask
        out features (segments) from the input image. The
        SageMaker Clarify processing job loads the mask image and
        resizes it to the same resolution as the input
        image. If baseline is not provided, the SageMaker Clarify
        processing job generates a mask image of [white noise](https://en.wikipedia.org/wiki/White_noise "https://en.wikipedia.org/wiki/White_noise") at the same resolution as the
        input image.

    - features_to_explain
      – (Optional) An array of strings or zero-based
      indices of feature columns to compute SHAP values for.
      If `features_to_explain` is not provided,
      SHAP values are computed for all feature columns. These
      feature columns cannot include the label column or
      predicted label column. The
      `features_to_explain` parameter is only
      supported for tabular datasets with numeric and
      categorical columns.
    - num_clusters –
      (Optional) The number of clusters that the dataset is
      divided into to compute the baseline dataset. Each
      cluster is used to compute one baseline instance. If
      `baseline` is not specified, the SageMaker Clarify
      processing job attempts to compute the baseline dataset
      by dividing the tabular dataset into an optimal number
      of clusters between `1` and `12`.
      The number of baseline instances directly affects the
      runtime of SHAP analysis.
    - num_samples –
      (Optional) The number of samples to be used in the
      Kernel SHAP algorithm. If `num_samples` is
      not provided, the SageMaker Clarify processing job chooses the
      number for you. The number of samples directly affects
      both the synthetic dataset size and job runtime.
    - seed –(Optional)
      An integer used to initialize the pseudo random number
      generator in the SHAP explainer to generate consistent
      SHAP values for the same job. If seed is not specified,
      then each time that the same job runs, the model may
      output slightly different SHAP values.
    - use_logit –
      (Optional) A Boolean value that indicates that you want
      the logit function to be applied to the model
      predictions. Defaults to `false`. If
      `use_logit` is `true`, then
      the SHAP values are calculated using the logistic
      regression coefficients, which can be interpreted as
      log-odds ratios.
    - save_local_shap_values
      – (Optional) A Boolean value that indicates that
      you want the local SHAP values of each record in the
      dataset to be included in the analysis result. Defaults
      to `false`.

    If the main dataset is split across multiple files or
    distributed processing is activated, also specify an
    identifier column using the parameter
    `joinsource_name_or_index`. The
    identifier column and the local SHAP values are saved in
    the analysis result. This way, you can map each record
    to its local SHAP values.
    - agg_method –
      (Optional) The method used to aggregate the local SHAP
      values (the SHAP values for each instance) of all
      instances to the global SHAP values (the SHAP values for
      the entire dataset). Defaults to `mean_abs`.
      The following methods can be used to aggregate SHAP
      values.
      - mean_abs
        – The mean of absolute local SHAP values of
        all instances.
      - mean_sq
        – The mean of squared local SHAP values of
        all instances.
      - median –
        The median of local SHAP values of all
        instances.

    - text_config –
      Required for natural language processing explainability.
      Include this configuration if you want to treat text
      columns as text and explanations should be provided for
      individual units of text. For an example of an analysis
      configuration for natural language processing
      explainability, see [Analysis configuration
      for natural language processing explainability](#clarify-analysis-configure-nlp-example "#clarify-analysis-configure-nlp-example")
      - granularity
        – The unit of granularity for the analysis
        of text columns. Valid values are
        `token`, `sentence`, or
        `paragraph`. **Each
        unit of text is considered a feature**,
        and local SHAP values are computed for each
        unit.
      - language
        – The language of the text columns. Valid
        values are `chinese`,
        `danish`,
        `dutch`,
        `english`,
        `french`,
        `german`,
        `greek`,
        `italian`,
        `japanese`,
        `lithuanian`,
        `multi-language`,
        `norwegian bokmål`,
        `polish`,
        `portuguese`,
        `romanian`,
        `russian`,
        `spanish`,
        `afrikaans`,
        `albanian`,
        `arabic`,
        `armenian`,
        `basque`,
        `bengali`,
        `bulgarian`,
        `catalan`,
        `croatian`,
        `czech`,
        `estonian`,
        `finnish`,
        `gujarati`,
        `hebrew`,
        `hindi`,
        `hungarian`,
        `icelandic`,
        `indonesian`,
        `irish`,
        `kannada`,
        `kyrgyz`,
        `latvian`,
        `ligurian`,
        `luxembourgish`,
        `macedonian`,
        `malayalam`,
        `marathi`,
        `nepali`,
        `persian`,
        `sanskrit`,
        `serbian`,
        `setswana`,
        `sinhala`,
        `slovak`,
        `slovenian`,
        `swedish`,
        `tagalog`,
        `tamil`,
        `tatar`,
        `telugu`,
        `thai`,
        `turkish`,
        `ukrainian`,
        `urdu`,
        `vietnamese`,
        `yoruba`. Enter
        `multi-language` for a mix of multiple
        languages.
      - max_top_tokens
        – (Optional) The maximum number of top
        tokens, based on global SHAP values. Defaults to
        `50`. It is possible for a token to
        appear multiple times in the dataset. The SageMaker Clarify
        processing job aggregates the SHAP values of each
        token, and then selects the top tokens based on
        their global SHAP values. The global SHAP values
        of the selected top tokens are included in the
        `global_top_shap_text` section of the
        analysis.json file.
      - The local SHAP value of aggregation.

    - image_config –
      Required for computer vision explainability. Include
      this configuration if you have an input dataset
      consisting of images and you want to analyze them for
      explainability in a computer vision problem.
      - model_type
        – The type of the model. Valid values
        include:
        - `IMAGE_CLASSIFICATION` for an
          image classification model.
        - `OBJECT_DETECTION` for an object
          detection model.

      - max_objects
        – Applicable only when model_type is
        `OBJECT_DETECTION`.The max
        number of objects, ordered by confidence score,
        detected by the computer vision model. Any objects
        ranked lower than the top max_objects by
        confidence score are filtered out. Defaults to
        `3`.
      - context
        – Applicable only when model_type is
        `OBJECT_DETECTION`. It
        indicates if the area around the bounding box of
        the detected object is masked by the baseline
        image or not. Valid values are `0` to
        mask everything, or `1` to mask
        nothing. Defaults to 1.
      - iou_threshold
        – Applicable only when
        `model_type` is
        `OBJECT_DETECTION`.The
        minimum intersection over union (IOU) metric for
        evaluating predictions against the original
        detection. A high IOU metric corresponds to a
        large overlap between the predicted and ground
        truth detection box. Defaults to
        `0.5`.
      - num_segments
        – (Optional) An integer that determines the
        approximate number of segments to be labeled in
        the input image. Each segment of the image is
        considered a feature, and local SHAP values are
        computed for each segment. Defaults to
        `20`.
      - segment_compactness – (Optional)
        An integer that determines the shape and size of
        the image segments generated by the [scikit-image slic](https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.slic "https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.slic") method. Defaults to
        `5`.

  - pdp – Include this
    method to compute partial dependence plots (PDPs). For an
    example of an analysis configuration to generate PDPs, see [Compute partial
    dependence plots (PDPs)](#clarify-analysis-configure-csv-example-pdp "#clarify-analysis-configure-csv-example-pdp")
    - features –
      Mandatory if the `shap` method is not
      requested. An array of feature names or indices to
      compute and plot PDP plots.
    - top_k_features –
      (Optional) Specifies the number of top features used to
      generate PDP plots. If `features` is not
      provided, but the `shap` method is requested,
      then the SageMaker Clarify processing job chooses the top features
      based on their SHAP attributions. Defaults to
      `10`.
    - grid_resolution
      – The number of buckets to divide the range of
      numeric values into. This specifies the granularity of
      the grid for the PDP plots.

  - asymmetric_shapley_value –
    Include this method if you want to compute explainability metrics
    for time-series forecasting models. The SageMaker Clarify processing job
    supports the asymmetric Shapley values algorithm. Asymmetric
    Shapley values are a variant of the Shapley value that drop
    the symmetry axiom. For more information, see [Asymmetric Shapley
    values: incorporating causal knowledge into model-agnostic
    explainability](https://arxiv.org/abs/1910.06358 "https://arxiv.org/abs/1910.06358"). Use these values to determine how features
    contribute to the forecasting outcome. Asymmetric Shapley values take
    into account the temporal dependencies of the time series data that
    forecasting models take as input.

  The algorithm includes the following parameters:

      - direction –
       Available types are `chronological`,
       `anti_chronological`, and `bidirectional`. The temporal
       structure can be navigated in chronological or anti-chronological
       order or both. Chronological explanations are built by iteratively
       adding information from the first time step onward. Anti-chronological
       explanations add information starting from the last step and moving
       backward. The latter order may be more appropriate in the presence
       of recency bias, such as for forecasting stock prices.
      - granularity – The explanation
       granularity to be used. The available granularity options are shown as
       follows:




      	* timewise – `timewise`
      	 explanations are inexpensive and provide information about specific
      	 time steps only, such as figuring out how much the information of the
      	 nth day in
      	 the past contributed to the forecasting of the mth day in the future.
      	 The resulting attributions do not explain individually static covariates
      	 and do not differentiate between target and related time series.
      	* fine\_grained – `fine_grained`
      	 explanations are computationally more intensive but provide a full
      	 breakdown of all attributions of the input variables. The method
      	 computes approximate explanations to reduce runtime. For more information,
      	 see the following parameter `num_samples`.


      	###### Note

      	`fine_grained` explanations only support
      	 `chronological` order.
      - num\_samples – (Optional)
       This argument is required for `fine_grained` explanations. The higher
       the number, the more precise the approximation. This number should scale with the
       dimensionality of the input features. A rule of thumb is to set this variable to *(1 + max(number
       of related time series, number of static covariates))^2* if the result is not
       too big.
      - baseline – (Optional)
       The baseline config to replace out-of-coalition values for the corresponding
       datasets (also known as background data). The following snippet shows an
       example of a baseline config:



      ```
      {
          "related_time_series": "zero",
          "static_covariates": {
              `<item_id_1>`: [0, 2],
              `<item_id_2>`: [-1, 1]
          },
          "target_time_series": "zero"
      }
      ```



      	* For temporal data such as target time series or related time series, the
      	 baseline value types can be one of the following values:




      		+ `zero` — All out-of-coalition values
      		 are replaced with 0.0.
      		+ `mean` — All out-of-coalition values
      		 are replaced with the average of a time series.
      	* For static covariates, a baseline entry should only be provided when
      	 the model request takes static covariate values, in which case this field
      	 is required. The baseline should be provided for every item as a list. For example,
      	 if you have a dataset with two static covariates, your baseline config could be
      	 the following:



      	```
      	"static_covariates": {
      	    `<item_id_1>`: [1, 1],
      	    `<item_id_2>`: [0, 1]
      	}
      	```

      	In the preceding example, `<item_id_1>`
      	 and `<item_id_2>` are the item ids from the dataset.

  - report – (Optional) Use
    this object to customize the analysis report. This parameter is
    not supported for time series explanation jobs. There are three
    copies of the same report as part of the analysis result:
    Jupyter Notebook report, HTML report, and PDF report. The object
    has the following parameters:
    - name – File name
      of the report files. For example, if `name`
      is `MyReport`, then the report
      files are `MyReport.ipynb`,
      `MyReport.html`, and
      `MyReport.pdf`. Defaults to
      `report`.
    - title –
      (Optional) Title string for the report. Defaults to
      `SageMaker AI Analysis Report`.

- predictor – Required if the
  analysis requires predictions from the model. For example, when the
  `shap`, `asymmetric_shapley_value`, `pdp`, or
  `post_training_bias` method is requested, but predicted
  labels are not provided as part of the input dataset. The following are
  parameters to be used in conjunction with `predictor`:
  - model_name – The name of
    your SageMaker AI model created by the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API. If you specify
    `model_name` instead of endpoint_name, the SageMaker Clarify
    processing job creates an ephemeral endpoint with the model
    name, known as a **shadow
    endpoint**, and gets predictions from the endpoint.
    The job deletes the shadow endpoint after the computations are
    completed. If the model is multi-model, then the
    `target_model` parameter must be specified. For
    more information about multi-model endpoints, see [Multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md").
  - endpoint_name_prefix –
    (Optional) A custom name prefix for the shadow endpoint.
    Applicable if you provide `model_name` instead of
    `endpoint_name`. For example, provide
    `endpoint_name_prefix` if you want to restrict
    access to the endpoint by endpoint name. The prefix must match
    the [EndpointName](../APIReference/API_CreateEndpoint.md#sagemaker-CreateEndpoint-request-EndpointName "../APIReference/API_CreateEndpoint.md#sagemaker-CreateEndpoint-request-EndpointName") pattern, and its maximum length is
    `23`. Defaults to `sm-clarify`.
  - initial_instance_count –
    Specifies the number of instances for the shadow endpoint.
    Required if you provide model_name instead of endpoint_name. The
    value for `initial_instance_count` can be different
    from the [InstanceCount](../APIReference/API_ProcessingClusterConfig.md#sagemaker-Type-ProcessingClusterConfig-InstanceCount "../APIReference/API_ProcessingClusterConfig.md#sagemaker-Type-ProcessingClusterConfig-InstanceCount") of the job, but we recommend a 1:1
    ratio.
  - instance_type –
    Specifies the instance type for the shadow endpoint. Required if
    you provide `model_name` instead of
    `endpoint_name`. As an example,
    `instance_type` can be set to "ml.m5.large". In
    some cases, the value specified for `instance_type`
    can help reduce model inference time. For example, to run
    efficiently, natural language processing models and computer
    vision models typically require a graphics processing unit (GPU)
    instance type.
  - endpoint_name – The name
    of your SageMaker AI endpoint created by the [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API. If provided,
    `endpoint_name` takes precedence over the
    `model_name` parameter. Using an existing
    endpoint reduces the shadow endpoint bootstrap time, but it can
    also cause a significant increase in load for that endpoint.
    Additionally, some analysis methods (such as `shap`
    and `pdp`) generate synthetic datasets that are sent
    to the endpoint. This can cause the endpoint's metrics or
    captured data to be contaminated by synthetic data, which may
    not accurately reflect real-world usage. For these reasons, it's
    generally not recommended to use an existing production endpoint
    for SageMaker Clarify analysis.
  - target_model – The
    string value that is passed on to the TargetModel parameter of
    the SageMaker AI [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax "../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax") API. Required if your model
    (specified by the model_name parameter) or endpoint (specified
    by the endpoint_name parameter) is multi-model. For more
    information about multi-model endpoints, see [Multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md").
  - custom_attributes –
    (Optional) A string that allows you to provide additional
    information about a request for an inference that is submitted
    to the endpoint. The string value is passed to the
    `CustomAttributes` parameter of the SageMaker AI [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax "../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax") API.
  - content_type –
    content_type – The model input format to be used for getting
    predictions from the endpoint. If provided, it is passed to the
    `ContentType` parameter of the SageMaker AI [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax "../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax") API.
    - For computer vision explainability, the valid values
      are `image/jpeg`,
      `image/png` or
      `application/x-npy`. If
      `content_type` is not provided, the
      default value is
      `image/jpeg`.
    - For time series forecasting explainability, the valid value is
      `application/json`.
    - For other types of explainability, the valid values
      are `text/csv`,
      `application/jsonlines,` and
      `application/json`. A value for
      `content_type` is required if the
      `dataset_type` is
      `application/x-parquet`. Otherwise
      `content_type` defaults to the value of
      the `dataset_type` parameter.

  - accept_type – The model
    output format to be used for getting predictions from the
    endpoint. The value for `accept_type` is passed to
    the `Accept` parameter of the SageMaker AI [InvokeEndpoint](../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax "../APIReference/API_runtime_InvokeEndpoint.md#RequestSyntax") API.
    - For computer vision explainability, if
      `model_type` is "OBJECT_DETECTION" then
      `accept_type` defaults to
      `application/json`.
    - For time series forecasting explainability, the valid value is
      `application/json`.
    - For other types of explainability, the valid values
      are `text/csv`,
      `application/jsonlines`, and
      `application/json`. If a value
      for `accept_type` is not provided,
      `accept_type` defaults to the value of
      the `content_type` parameter.

  - content_template – A
    template string used to construct the model input from dataset
    records. The parameter `content_template` is only
    used and required if the value of the `content_type`
    parameter is either `application/jsonlines` or
    `application/json`.

  When the `content_type` parameter is
  `application/jsonlines`, the template should have
  only one placeholder, `$features`, which is replaced
  by a features list at runtime. For example, if the template is
  `"{\"myfeatures\":$features}"`, and if a record
  has three numeric feature values: `1`, `2`
  and `3`, then the record will be sent to the model as
  JSON Line `{"myfeatures":[1,2,3]}`.

  When the `content_type` is
  `application/json`, the template can have either
  placeholder `$record` or `records`. If the
  placeholder is `record`, a single record is replaced
  with a record that has the template in
  `record_template` applied to it. In this case,
  only a single record will be sent to the model at a time. If the
  placeholder is `$records`, the records are replaced
  by a list of records, each with a template supplied by
  `record_template`.
  - record_template – A
    template string to be used to construct each record of the model
    input from dataset instances. It is only used and required when
    `content_type` is `application/json`.
    The template string may contain one of the following:

        - A placeholder `$features` parameter that is
         substituted by an array of feature values. An additional
         optional placeholder can substitute feature column
         header names in `$feature_names`. This
         optional placeholder will be substituted by an array of
         feature names.
        - Exactly one placeholder `$features_kvp`
         that is substituted by the key-value pairs, feature name
         and feature value.
        - A feature in the `headers` configuration.
         As an example, a feature name `A`, notated by
         the placeholder syntax `"${A}"` will be
         substituted by the feature value for
         `A`.

    The value for `record_template` is used with
    `content_template` to construct the model input.
    A configuration example showing how to construct a model input
    using a content and record template follows.

  In the following code example, the headers and features are
  defined as follows.

      - ``headers`:["A", "B"]`
      - ``features`:[[0,1], [3,4]]`

  The example model input is as follows.

  ```
  {
      "instances": [[0, 1], [3, 4]],
      "feature_names": ["A", "B"]
  }
  ```

  The example `content_template` and
  `record_template` parameter values to construct
  the previous example model input follows.

      - `content_template: "{\"instances\": $records,
       \"feature_names\": $feature_names}"`
      - `record_template: "$features"`

  In the following code example, the headers and features are
  defined as follows.

  ```
  [
      { "A": 0, "B": 1 },
      { "A": 3, "B": 4 },
  ]
  ```

  The example `content_template` and
  `record_template` parameter values to construct
  the previous example model input follows.

      - `content_template: "$records"`
      - `record_template: "$features_kvp"`

  An alternate code example to construct the previous example
  model input follows.

      - `content_template: "$records"`
      - `record_template: "{\"A\": \"${A}\", \"B\":
       \"${B}\"}"`

  In the following code example, the headers and features are
  defined as follows.

  ```
  { "A": 0, "B": 1 }
  ```

  The example content_template and record_template parameters
  values to construct above: the previous example model input
  follows.

      - `content_template: "$record"`
      - `record_template: "$features_kvp"`

  For more examples, see [Endpoint requests for time series data](clarify-processing-job-data-format-time-series-request-jsonlines.md "clarify-processing-job-data-format-time-series-request-jsonlines.md").
  - label – (Optional) A zero-based
    integer index or JMESPath expression string used to extract
    predicted labels from the model output for bias analysis. If the
    model is multiclass and the `label` parameter
    extracts all of the predicted labels from the model output, then
    the following apply. This feature is not supported for time series.

        - The `probability` parameter is required to
         get the corresponding probabilities (or scores) from the
         model output.
        - The predicted label of the highest score is
         chosen.

    The value for `label` depends on the value of the
    accept_type parameter as follows.

        - If `accept_type` is
         `text/csv`, then
         `label` is the index of any predicted
         labels in the model output.
        - If `accept_type` is
         `application/jsonlines` or
         `application/json`, then
         `label` is a JMESPath expression that's
         applied to the model output to get the predicted
         labels.

  - label_headers – (Optional)
    An array
    of values that the label can take in the dataset. If bias
    analysis is requested, then the `probability`
    parameter is also required to get the corresponding probability
    values (scores) from model output, and the predicted label of
    the highest score is chosen. If explainability analysis is
    requested, the label headers are used to beautify the analysis
    report. A value for `label_headers` is required for
    computer vision explainability. For example, for a multiclass
    classification problem, if the label has three possible values,
    `bird`, `cat`, and
    `dog`, then `label_headers`
    should be set to `["bird","cat","dog"]`.
  - probability – (Optional)
    A zero-based integer index or a JMESPath expression string used
    to extract probabilities (scores) for explainability analysis
    (but not for time series explainability),
    or to choose the predicted label for bias analysis. The value of
    `probability` depends on the value of the
    `accept_type` parameter as follows.
    - If `accept_type` is
      `text/csv`,
      `probability` is the index of the
      probabilities (scores) in the model output. If
      `probability` is not provided, the entire
      model output is taken as the probabilities
      (scores).
    - If `accept_type` is JSON data (either
      `application/jsonlines` or
      `application/json`),
      `probability` should be a JMESPath
      expression that is used to extract the probabilities
      (scores) from the model output.

  - time_series_predictor_config – (Optional)
    Used only for time series explainability. Used to instruct the SageMaker Clarify processor how to
    parse data correctly from the data passed as an S3 URI in `dataset_uri`.
    - forecast – A JMESPath expression
      used to extract the forecast result.

## Example analysis

configuration files

The following sections contain example analysis configuration files for data in CSV
format, JSON Lines format, and for natural language processing (NLP), computer
vision (CV), and time series (TS) explainability.

The following examples show how to configure bias and explainability analysis
for a tabular dataset in CSV format. In these examples, the incoming dataset has
four feature columns, and one binary label column, `Target`. The
contents of the dataset are as follows. A label value of `1`
indicates a positive outcome. The dataset is provided to the SageMaker Clarify job by the
`dataset` processing input.

```
"Target","Age","Gender","Income","Occupation"
0,25,0,2850,2
1,36,0,6585,0
1,22,1,1759,1
0,48,0,3446,1
...
```

The following sections show how to compute pre-training and post-training bias
metrics, SHAP values, and partial dependence plots (PDPs) showing feature
importance for a dataset in CSV format.

#### Compute all

of the pre-training bias metrics

This example configuration shows how to measure if the previous sample
dataset is favorably biased towards samples with a
`Gender` value of `0`. The following
analysis configuration instructs the SageMaker Clarify processing job to compute all the
pre-training bias metrics for the dataset.

```
{
    "dataset_type": "text/csv",
    "label": "Target",
    "label_values_or_threshold": [1],
    "facet": [
        {
            "name_or_index": "Gender",
            "value_or_threshold": [0]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "all"
        }
    }
}

```

#### Compute

all of the post-training bias metrics

You can compute pre-training bias metrics prior to training. However, you
must have a trained model to compute post-training bias metrics. The
following example output is from a binary classification model that outputs
data in CSV format. In this example output, each row contains two columns.
The first column contains the predicted label, and the second column
contains the probability value for that label.

```
0,0.028986845165491
1,0.825382471084594
...
```

The following configuration example instructs the SageMaker Clarify processing job to
compute all possible bias metrics using the dataset and the predictions from
the model output. In the example, the model is deployed to a SageMaker AI endpoint
`your_endpoint`.

###### Note

In the following example code, the parameter `content_type`
and `accept_type` are not set. Therefore, they automatically
use the value of the parameter dataset_type, which is
`text/csv`.

```
{
    "dataset_type": "`text/csv`",
    "label": "`Target`",
    "label_values_or_threshold": `[1]`,
    "facet": [
        {
            "name_or_index": "`Gender`",
            "value_or_threshold": `[0]`
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "`all`"
        },
        "post_training_bias": {
            "methods": "`all`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "label": `0`
    }
}
```

#### Compute the

SHAP values

The following example analysis configuration instructs the job to compute
the SHAP values designating the `Target` column as labels and all
other columns as features.

```
{
    "dataset_type": "`text/csv`",
    "label": "`Target`",
    "methods": {
        "shap": {
            "num_clusters": `1`
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "probability": `1`
    }
}
```

In this example, the SHAP `baseline` parameter is omitted and
the value of the `num_clusters` parameter is `1`. This
instructs the SageMaker Clarify processor to compute one SHAP baseline sample. In this
example, probability is set to `1`. This instructs the SageMaker Clarify
processing job to extract the probability score from the second column of
the model output (using zero-based indexing).

#### Compute partial

dependence plots (PDPs)

The following example shows how to view the importance of the
`Income` feature on the analysis report using PDPs. The
report parameter instructs the SageMaker Clarify processing job to generate a report.
After the job completes, the generated report is saved as report.pdf to the
`analysis_result` location. The `grid_resolution`
parameter divides the range of the feature values into `10`
buckets. Together, the parameters specified in the following example
instruct the SageMaker Clarify processing job to generate a report containing a PDP
graph for `Income` with `10` segments on the x-axis.
The y-axis will show the marginal impact of `Income` on the
predictions.

```
{
    "dataset_type": "text/csv",
    "label": "Target",
    "methods": {
        "pdp": {
            "features": ["`Income`"],
            "grid_resolution": `10`
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "probability": `1`
    },
}
```

#### Compute both

bias metrics and feature importance

You can combine all the methods from the previous configuration examples
into a single analysis configuration file and compute them all by a single
job. The following example shows an analysis configuration with all steps
combined.

In this example, the `probability` parameter is set to
`1` to indicate that probabilities are contained in the
second column (using zero-based indexing). However, because bias analysis
needs a predicted label, the `probability_threshold` parameter is
set to `0.5` to convert the probability score into a binary
label. In this example, the `top_k_features` parameter of the
partials dependence plots `pdp` method is set to `2`.
This instructs the SageMaker Clarify processing job to compute partials dependence plots
(PDPs) for the top `2` features with the largest global SHAP
values.

```
{
    "dataset_type": "text/csv",
    "label": "`Target`",
    "probability_threshold": `0.5`,
    "label_values_or_threshold": [`1`],
    "facet": [
        {
            "name_or_index": "`Gender`",
            "value_or_threshold": [`0`]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "`all`"
        },
        "post_training_bias": {
            "methods": "`all`"
        },
        "shap": {
            "num_clusters": `1`
        },
        "pdp": {
            "top_k_features": `2`,
            "grid_resolution": `10`
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "probability": `1`
    }
}
```

Instead of deploying the model to an endpoint, you can provide the name of
your SageMaker AI model to the SageMaker Clarify processing job using the
`model_name` parameter. The following example shows how to
specify a model named `your_model`. The SageMaker Clarify
processing job will create a shadow endpoint using the configuration.

```
{
     ...
    "predictor": {
        "model_name": "`your_model`",
        "initial_instance_count": `1`,
        "instance_type": "`ml.m5.large`",
        "probability": `1`
    }
}
```

The following examples show how to configure bias analysis and explainability
analysis for a tabular dataset in JSON Lines format. In these examples, the
incoming dataset has the same data as the previous section but they are in the
SageMaker AI JSON Lines dense format. Each line is a valid JSON object. The key
"Features" points to an array of feature values, and the key "Label" points to
the ground truth label. The dataset is provided to the SageMaker Clarify job by the
"dataset" processing input. For more information about JSON Lines, see [JSONLINES request format](cdf-inference.md#cm-jsonlines "cdf-inference.md#cm-jsonlines").

```
{"Features":[25,0,2850,2],"Label":0}
{"Features":[36,0,6585,0],"Label":1}
{"Features":[22,1,1759,1],"Label":1}
{"Features":[48,0,3446,1],"Label":0}
...
```

The following sections show how to compute pre-training and post-training bias
metrics, SHAP values, and partial dependence plots (PDPs) showing feature
importance for a dataset in JSON Lines format.

#### Compute

pre-training bias metrics

Specify the label, features, format, and methods to measure pre-training
bias metrics for a `Gender` value of `0`. In the
following example, the `headers` parameter provides the feature
names first. The label name is provided last. By convention, the last header
is the label header.

The `features` parameter is set to the JMESPath expression
"Features" so that the SageMaker Clarify processing job can extract the array of
features from each record. The `label` parameter is set to
JMESPath expression "Label" so that the SageMaker Clarify processing job can extract the
ground truth label from each record. Use a facet name to specify the
sensitive attribute, as follows.

```
{
    "dataset_type": "`application/jsonlines`",
    "headers": [`"Age","Gender","Income","Occupation","Target"`],
    "label": "`Label`",
    "features": "`Features`",
    "label_values_or_threshold": [`1`],
    "facet": [
        {
            "name_or_index": "`Gender`",
            "value_or_threshold": [`0`]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "`all`"
        }
    }
}
```

#### Compute all the

bias metrics

You must have a trained model to compute post-training bias metrics. The
following example is from a binary classification model that outputs JSON
Lines data in the example's format. Each row of the model output is a valid
JSON object. The key `predicted_label` points to the predicted
label, and the key `probability` points to the probability
value.

```
{"predicted_label":0,"probability":0.028986845165491}
{"predicted_label":1,"probability":0.825382471084594}
...
```

You can deploy the model to a SageMaker AI endpoint named
`your_endpoint`. The following example analysis configuration
instructs the SageMaker Clarify processing job to compute all possible bias metrics for
both the dataset and the model. In this example, the parameter
`content_type` and `accept_type` are not set.
Therefore, they are automatically set to use the value of the parameter
dataset_type, which is `application/jsonlines`. The SageMaker Clarify
processing job uses the `content_template` parameter to compose
the model input, by replacing the `$features` placeholder by an
array of features.

```
{
    "dataset_type": "`application/jsonlines`",
    "headers": [`"Age","Gender","Income","Occupation","Target"`],
    "label": "`Label`",
    "features": "`Features`",
    "label_values_or_threshold": [`1`],
    "facet": [
        {
            "name_or_index": "`Gender`",
            "value_or_threshold": [`0`]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "`all`"
        },
        "post_training_bias": {
            "methods": "`all`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "content_template": "{`\"Features\":$features`}",
        "label": "`predicted_label`"
    }
}
```

#### Compute the SHAP

values

Because SHAP analysis doesn’t need a ground truth label, the
`label` parameter is omitted. In this example, the
`headers` parameter is also omitted. Therefore, the SageMaker Clarify
processing job must generate placeholders using generic names like
`column_0` or `column_1` for feature headers, and
`label0` for a label header. You can specify values for
`headers` and for a `label` to improve the
readability of the analysis result. Because the probability parameter is set
to JMESPath expression `probability`, the probability value will
be extracted from the model output. The following is an example to calculate
SHAP values.

```
{
    "dataset_type": "`application/jsonlines`",
    "features": "`Features`",
    "methods": {
        "shap": {
            "`num_clusters`": 1
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "content_template": "`{\"Features\":$features}`",
        "probability": "`probability`"
    }
}
```

#### Compute partials

dependence plots (PDPs)

The following example shows how to view the importance of "Income" on PDP.
In this example, the feature headers are not provided. Therefore, the
`features` parameter of the `pdp` method must use
zero-based index to refer to location of the feature column. The
`grid_resolution` parameter divides the range of the feature
values into `10` buckets. Together, the parameters in the example
instruct the SageMaker Clarify processing job to generate a report containing a PDP
graph for `Income` with `10` segments on the x-axis.
The y-axis will show the marginal impact of `Income` on the
predictions.

```
{
    "dataset_type": "`application/jsonlines`",
    "features": "`Features`",
    "methods": {
        "pdp": {
            "features": [`2`],
            "grid_resolution": `10`
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "content_template": "`{\"Features\":$features}`",
        "probability": "`probability`"
    }
}
```

#### Compute

both bias metrics and feature importance

You can combine all previous methods into a single analysis configuration
file and compute them all by a single job. The following example shows an
analysis configuration with all steps combined. In this example, the
`probability` parameter is set. But because bias analysis
needs a predicted label, the `probability_threshold` parameter is
set to `0.5` to convert the probability score into a binary
label. In this example, the `top_k_features` parameter of the
`pdp` method is set to `2`. This instructs the
SageMaker Clarify processing job to compute PDPs for the top `2` features
with the largest global SHAP values.

```
{
    "dataset_type": "`application/jsonlines`",
    "headers": [`"Age","Gender","Income","Occupation","Target"`],
    "label": "`Label`",
    "features": "`Features`",
    "probability_threshold": `0.5`,
    "label_values_or_threshold": [`1`],
    "facet": [
        {
            "name_or_index": "`Gender`",
            "value_or_threshold": [`0`]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "`all`"
        },
        "post_training_bias": {
            "methods": "`all`"
        },
        "shap": {
            "num_clusters": `1`
        },
        "pdp": {
            "top_k_features": `2`,
            "grid_resolution": `10`
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "endpoint_name": "`your_endpoint`",
        "content_template": "`{\"Features\":$features}`",
        "probability": "`probability`"
    }
}
```

The following examples show how to configure bias and explainability analysis
for a tabular dataset in JSON format. In these examples, the incoming dataset
has the same data as the previous section but they are in the SageMaker AI JSON dense
format. For more information about JSON Lines, see [JSONLINES request format](cdf-inference.md#cm-jsonlines "cdf-inference.md#cm-jsonlines").

The whole input request is valid JSON where the outer structure is a list and
each element is the data for a record. Within each record, the key
`Features` points to an array of feature values, and the key
`Label` points to the ground truth label. The dataset is provided
to the SageMaker Clarify job by the `dataset` processing input.

```
[
    {"Features":[25,0,2850,2],"Label":0},
    {"Features":[36,0,6585,0],"Label":1},
    {"Features":[22,1,1759,1],"Label":1},
    {"Features":[48,0,3446,1],"Label":0},
    ...
]
```

The following sections show how to compute pre-training and post-training bias
metrics, SHAP values, and partial dependence plots (PDPs) that show feature
importance for a dataset in JSON Lines format.

#### Compute pre-training bias metrics

Specify the label, features, format, and methods to measure pre-training
bias metrics for a `Gender` value of `0`. In the
following example, the `headers` parameter provides the feature
names first. The label name is provided last. For JSON datasets, the last
header is the label header.

The `features` parameter is set to the JMESPath expression that
extracts a 2D array or matrix. Each row in this matrix must contain the list
of `Features` for each record. The `label` parameter
is set to JMESPath expression that extracts a list of ground truth labels.
Each element in this list must contain the label for a record.

Use a facet name to specify the sensitive attribute, as follows.

```
{
    "dataset_type": "application/json",
    "headers": ["Age","Gender","Income","Occupation","Target"],
    "label": "[*].Label",
    "features": "[*].Features",
    "label_values_or_threshold": [1],
    "facet": [
        {
            "name_or_index": "Gender",
            "value_or_threshold": [0]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "all"
        }
    }
}
```

#### Compute all

the bias metrics

You must have a trained model to compute post-training bias metrics. The
following code example is from a binary classification model that outputs
JSON data in the example's format. In the example, each element under
`predictions` is the prediction output for a record. The
example code contains the key `predicted_label`, that points to
the predicted label, and the key `probability` points to the
probability value.

```
{
    "predictions": [
        {"predicted_label":0,"probability":0.028986845165491},
        {"predicted_label":1,"probability":0.825382471084594},
        ...
    ]
}
```

You can deploy the model to a SageMaker AI endpoint named
`your_endpoint`.

In the following example, the parameter `content_type` and
`accept_type` are not set. Therefore,
`content_type` and `accept_type` are automatically
set to use the value of the parameter `dataset_type`, which is
`application/json`. The SageMaker Clarify processing job then uses the
`content_template` parameter to compose the model input.

In the following example, the model input is composed by replacing the
`$records` placeholder by an array of records. Then, the
`record_template` parameter composes each record’s JSON
structure and replaces the `$features` placeholder with each
record’s array of features.

The following example analysis configuration instructs the SageMaker Clarify
processing job to compute all possible bias metrics for both the dataset and
the model.

```
{
    "dataset_type": "application/json",
    "headers": ["Age","Gender","Income","Occupation","Target"],
    "label": "[*].Label",
    "features": "[*].Features",
    "label_values_or_threshold": [1],
    "facet": [
        {
            "name_or_index": "Gender",
            "value_or_threshold": [0]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "all"
        },
        "post_training_bias": {
            "methods": "all"
        }
    },
    "predictor": {
        "endpoint_name": "your_endpoint",
        "content_template": "$records",
        "record_template": "{\"Features\":$features}",
        "label": "predictions[*].predicted_label"
    }
}
```

#### Compute the

SHAP values

You don’t need to specify a label for SHAP analysis. In the following
example, the `headers` parameter is not specified. Therefore, the
SageMaker Clarify processing job will generate placeholders using generic names like
`column_0` or `column_1` for feature headers, and
`label0` for a label header. You can specify values for
`headers` and for a `label` to improve the
readability of the analysis result.

In the following configuration example, the probability parameter is set
to a JMESPath expression that extracts the probabilities from each
prediction for each record. The following is an example to calculate SHAP
values.

```
{
    "dataset_type": "application/json",
    "features": "[*].Features",
    "methods": {
        "shap": {
            "num_clusters": 1
        }
    },
    "predictor": {
        "endpoint_name": "your_endpoint",
        "content_template": "$records",
        "record_template": "{\"Features\":$features}",
        "probability": "predictions[*].probability"
    }
}
```

#### Compute

partial dependence plots (PDPs)

The following example shows you how to view a feature importance in PDPs.
In the example, the feature headers are not provided. Therefore, the
`features` parameter of the `pdp` method must use
zero-based index to refer to location of the feature column. The
`grid_resolution` parameter divides the range of the feature
values into `10` buckets.

Together, the parameters in the following example instruct the SageMaker Clarify
processing job to generate a report containing a PDP graph for
`Income` with `10` segments on the x-axis. The
y-axis shows the marginal impact of `Income` on the
predictions.

The following configuration example shows how to view the importance of
`Income` on PDPs.

```
{
    "dataset_type": "application/json",
    "features": "[*].Features",
    "methods": {
        "pdp": {
            "features": [2],
            "grid_resolution": 10
        },
        "report": {
            "name": "report"
        }
    },
    "predictor": {
        "endpoint_name": "your_endpoint",
        "content_template": "$records",
        "record_template": "{\"Features\":$features}",
        "probability": "predictions[*].probability"
    }
}
```

#### Compute

both bias metrics and feature importance

You can combine all previous configuration methods into a single analysis
configuration file and compute them all with a single job. The following
example shows an analysis configuration with all steps combined.

In this example, the `probability` parameter is set. Because
bias analysis needs a predicted label, the
`probability_threshold` parameter is set to `0.5`,
which is used to convert the probability score into a binary label. In this
example, the `top_k_features` parameter of the `pdp`
method is set to `2`. This instructs the SageMaker Clarify processing job to
compute PDPs for the top `2` features with the largest global
SHAP values.

```
{
    "dataset_type": "application/json",
    "headers": ["Age","Gender","Income","Occupation","Target"],
    "label": "[*].Label",
    "features": "[*].Features",
    "probability_threshold": 0.5,
    "label_values_or_threshold": [1],
    "facet": [
        {
            "name_or_index": "Gender",
            "value_or_threshold": [0]
        }
    ],
    "methods": {
        "pre_training_bias": {
            "methods": "all"
        },
        "post_training_bias": {
            "methods": "all"
        },
        "shap": {
            "num_clusters": 1
        },
        "pdp": {
            "top_k_features": 2,
            "grid_resolution": 10
        },
        "report": {
            "name": "report"
        }
    },
    "predictor": {
        "endpoint_name": "your_endpoint",
        "content_template": "$records",
        "record_template": "{\"Features\":$features}",
        "probability": "predictions[*].probability"
    }
}
```

The following example shows an analysis configuration file for computing
feature importance for natural language processing (NLP). In this example, the
incoming dataset is a tabular dataset in CSV format, with one binary label
column and two feature columns, as follows. The dataset is provided to the SageMaker Clarify
job by the `dataset` processing input parameter.

```
0,2,"They taste gross"
1,3,"Flavor needs work"
1,5,"Taste is awful"
0,1,"The worst"
...
```

In this example, a binary classification model was trained on the previous
dataset. The model accepts CSV data, and it outputs a single score between
`0` and `1`, as follows.

```
0.491656005382537
0.569582343101501
...
```

The model is used to create a SageMaker AI model named “your_model". The following
analysis configuration shows how to run a token-wise explainability analysis
using the model and dataset. The `text_config` parameter activates
the NLP explainability analysis. The `granularity` parameter
indicates that the analysis should parse tokens.

In English, each token is a word. The following example also shows how to
provide an in-place SHAP "baseline" instance using an average "Rating" of 4. A
special mask token "[MASK]" is used to replace a token (word) in "Comments".
This example also uses a GPU endpoint instance type to speed up
inferencing.

```
{
    "dataset_type": "`text/csv`",
    "headers": [`"Target","Rating","Comments"`]
    "label": "`Target`",
    "methods": {
        "shap": {
            "text_config": {
                "granularity": "`token`",
                "language": "`english`"
            }
            "baseline": [[`4,"[MASK]"`]],
        }
    },
    "predictor": {
        "model_name": "`your_nlp_model`",
        "initial_instance_count": `1`,
        "instance_type": "`ml.g4dn.xlarge`"
    }
}
```

The following example shows an analysis configuration file computing feature
importance for computer vision. In this example, the input dataset consists of
JPEG images. The dataset is provided to the SageMaker Clarify job by the
`dataset` processing input parameter. The example shows how to
configure an explainability analysis using a SageMaker image classification model. In
the example, a model named `your_cv_ic_model`, has been trained to
classify the animals on the input JPEG images.

```
{
    "dataset_type": "`application/x-image`",
    "methods": {
        "shap": {
             "image_config": {
                "model_type": "`IMAGE_CLASSIFICATION`",
                 "num_segments": `20`,
                "segment_compactness": `10`
             }
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "model_name": "`your_cv_ic_model`",
        "initial_instance_count": `1`,
        "instance_type": "`ml.p2.xlarge`",
        "label_headers": [`"bird","cat","dog"`]
    }
}
```

For more information about image classification, see [Image Classification - MXNet](image-classification.md "image-classification.md").

In this example, a [SageMaker AI object detection
model](object-detection.md "object-detection.md"), `your_cv_od_model` is trained on the same JPEG
images to identify the animals on them. The following example shows how to
configure an explainability analysis for the object detection model.

```
{
    "dataset_type": "`application/x-image`",
    "probability_threshold": `0.5`,
    "methods": {
        "`shap`": {
             "image_config": {
                "model_type": "`OBJECT_DETECTION`",
                 "max_objects": `3`,
                "context": `1.0`,
                "iou_threshold": `0.5`,
                 "num_segments": `20`,
                "segment_compactness": `10`
             }
        },
        "report": {
            "name": "`report`"
        }
    },
    "predictor": {
        "model_name": "`your_cv_od_model`",
        "initial_instance_count": `1`,
        "instance_type": "`ml.p2.xlarge`",
        "label_headers": [`"bird","cat","dog"`]
    }
}
```

The following example shows an analysis configuration file for computing feature
importance for a time series (TS). In this example, the incoming dataset is a time series
dataset in JSON format with a set of dynamic and static covariate features.
The dataset is provided to the SageMaker Clarify job by the dataset processing
input parameter `dataset_uri`.

```
[
    {
        "item_id": "item1",
        "timestamp": "2019-09-11",
        "target_value": 47650.3,
        "dynamic_feature_1": 0.4576,
        "dynamic_feature_2": 0.2164,
        "dynamic_feature_3": 0.1906,
        "static_feature_1": 3,
        "static_feature_2": 4
    },
    {
        "item_id": "item1",
        "timestamp": "2019-09-12",
        "target_value": 47380.3,
        "dynamic_feature_1": 0.4839,
        "dynamic_feature_2": 0.2274,
        "dynamic_feature_3": 0.1889,
        "static_feature_1": 3,
        "static_feature_2": 4
    },
    {
        "item_id": "item2",
        "timestamp": "2020-04-23",
        "target_value": 35601.4,
        "dynamic_feature_1": 0.5264,
        "dynamic_feature_2": 0.3838,
        "dynamic_feature_3": 0.4604,
        "static_feature_1": 1,
        "static_feature_2": 2
    },
]
```

The following sections explain how to compute feature attributions for a forecasting
model with the asymmetric Shapley values algorithm for a JSON dataset.

#### Compute

the explanations for time series forecasting models

The following example analysis configuration displays the options used by
the job to compute the explanations for time series forecasting models.

```
{
    'dataset_type': 'application/json',
    'dataset_uri': 'DATASET_URI',
    'methods': {
        'asymmetric_shapley_value': {
            'baseline': {
                "related_time_series": "zero",
                "static_covariates": {
                    "item1": [0, 0], "item2": [0, 0]
                },
                "target_time_series": "zero"
            },
            'direction': 'chronological',
            'granularity': 'fine_grained',
            'num_samples': 10
        },
        'report': {'name': 'report', 'title': 'Analysis Report'}
    },
    'predictor': {
        'accept_type': 'application/json',
        'content_template': '{"instances": $records}',
        'endpoint_name': 'ENDPOINT_NAME',
        'content_type': 'application/json',
        'record_template': '{
            "start": $start_time,
            "target": $target_time_series,
            "dynamic_feat": $related_time_series,
            "cat": $static_covariates
        }',
        'time_series_predictor_config': {'forecast': 'predictions[*].mean[:2]'}
    },
    'time_series_data_config': {
        'dataset_format': 'timestamp_records',
        'item_id': '[].item_id',
        'related_time_series': ['[].dynamic_feature_1', '[].dynamic_feature_2', '[].dynamic_feature_3'],
        'static_covariates': ['[].static_feature_1', '[].static_feature_2'],
        'target_time_series': '[].target_value',
        'timestamp': '[].timestamp'
    }
}
```

##### Time

series explainability configuration

The preceding example uses `asymmetric_shapley_value` in `methods` to define
the time series explainability arguments like baseline, direction, granularity,
and number of samples. The baseline values are set for all three types of data:
related time series, static covariates, and target time series.
These fields instruct the SageMaker Clarify
processor to compute feature attributions for one item at a time.

#####

Predictor configuration

You can fully control the payload structure that the SageMaker Clarify processor sends using JMESPath
syntax. In the preceding example, the `predictor` config instructs Clarify
to aggregate records into `'{"instances": $records}'` , where each record is
defined with the arguments given for `record_template` in the example.
Note that `$start_time`, `$target_time_series`, `$related_time_series`,
and `$static_covariates` are internal tokens used to map dataset values to
endpoint request values.

Similarly, the attribute `forecast` in `time_series_predictor_config`
is used to extract the model forecast from the endpoint response.
For example, your endpoint batch response could be the following:

```
{
    "predictions": [
        {"mean": [13.4, 3.6, 1.0]},
        {"mean": [23.0, 4.7, 3.0]},
        {"mean": [3.4, 5.6, 2.0]}
    ]
}
```

Suppose you specify the following time series predictor configuration:

```
'time_series_predictor_config': {'forecast': 'predictions[*].mean[:2]'}
```

The forecast value is parsed as the following:

```
[
    [13.4, 3.6],
    [23.0, 4.7],
    [3.4, 5.6]
]
```

#####

Data configuration

Use the `time_series_data_config` attribute to instruct the
SageMaker Clarify processor to parse data correctly from the data passed as an S3 URI in
`dataset_uri`.
