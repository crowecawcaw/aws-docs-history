# Fixing training errors

You use the manifest summary to identify [List of terminal manifest
content errors](tm-debugging.md#tm-error-category-combined-terminal "tm-debugging.md#tm-error-category-combined-terminal") and
[List of non-terminal
JSON line validation errors](tm-debugging.md#tm-error-category-non-terminal-errors "tm-debugging.md#tm-error-category-non-terminal-errors") encountered during training.
You must fix manifest content errors. We recommend that you also fix non-terminal JSON Line errors.
For information about specific errors,
see [Non-Terminal JSON Line Validation Errors](tm-debugging-json-line-errors.md "tm-debugging-json-line-errors.md")
and [Terminal manifest content errors](tm-debugging-aggregate-errors.md "tm-debugging-aggregate-errors.md").

You can makes fixes to the training or testing dataset used for training. Alternatively, you can
make the fixes in the training and testing validation manifest files and use them to train the model.

After you make your fixes,
you need to import the updated manifests(s) and retrain the model. For more information, see [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

The following procedure shows you how to use the manifest summary to fix terminal manifest content errors. The procedure also shows you how
to locate and fix JSON Line errors in the training and testing validation manifests.

###### To fix Amazon Rekognition Custom Labels training errors

1. Download the validation results files. The file names are _training_manifest_with_validation.json_, _testing_manifest_with_validation.json_
   and _manifest_summary.json_. For more information, see
   [Getting the validation results](tm-debugging-getting-validation-data.md "tm-debugging-getting-validation-data.md").
2. Open the manifest summary file (_manifest_summary.json_).
3. Fix any errors in the manifest summary. For more information, see [Understanding the manifest summary](tm-debugging-summary.md "tm-debugging-summary.md").
4. In the manifest summary, iterate through the `error_line_indices` array in `training` and fix the errors in `training_manifest_with_validation.json` at
   the corresponding JSON Line numbers. For more information, see [Understanding training and testing validation result manifests](tm-debugging-scope-json-line.md "tm-debugging-scope-json-line.md").
5. Iterate through the `error_line_indices` array in `testing` and fix the errors in `testing_manifest_with_validation.json`
   at the corresponding JSON Line numbers.
6. Retrain the model using the validation manifest files as the training and testing datasets. For more information, see [Training an Amazon Rekognition Custom Labels model](training-model.md "training-model.md").
   If you are using the AWS SDK and choose to fix the errors in the training or the test validation data manifest files,
   use the location of the validation data manifest files in the [TrainingData](../APIReference/API_TrainingData.md "../APIReference/API_TrainingData.md") and
   [TestingData](../APIReference/API_TestingData.md "../APIReference/API_TestingData.md") input parameters to
   [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md"). For more information, see
   [Training a model (SDK)](training-model.md#tm-sdk "training-model.md#tm-sdk").

## JSON line error precedence

The following JSON Line errors are detected first. If any of these errors occur, validation of JSON Line
errors is stopped. You must fix these errors before you can fix any of the other JSON Line errors

- MISSING_SOURCE_REF
- ERROR_INVALID_SOURCE_REF_FORMAT
- ERROR_NO_LABEL_ATTRIBUTES
- ERROR_INVALID_LABEL_ATTRIBUTE_FORMAT
- ERROR_INVALID_LABEL_ATTRIBUTE_METADATA_FORMAT
- ERROR_MISSING_BOUNDING_BOX_CONFIDENCE
- ERROR_MISSING_CLASS_MAP_ID
- ERROR_INVALID_JSON_LINE
