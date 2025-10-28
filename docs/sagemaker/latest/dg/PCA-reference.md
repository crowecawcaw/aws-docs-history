# PCA Hyperparameters

In the `CreateTrainingJob` request, you specify the training algorithm. You
can also specify algorithm-specific HyperParameters as string-to-string maps. The
following table lists the hyperparameters for the PCA training algorithm provided by
Amazon SageMaker AI. For more information about how PCA works, see [How PCA Works](how-pca-works.md "how-pca-works.md").

| Parameter Name     | Description                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_dim`      | Input dimension. **Required** Valid values: positive integer                                                                                                                                                                                                                                  |
| `mini_batch_size`  | Number of rows in a mini-batch. **Required** Valid values: positive integer                                                                                                                                                                                                                   |
| `num_components`   | The number of principal components to compute. **Required** Valid values: positive integer                                                                                                                                                                                                    |
| `algorithm_mode`   | Mode for computing the principal components. **Optional** Valid values: _regular_ or _randomized_ Default value: _regular_                                                                                                                                                                    |
| `extra_components` | As the value increases, the solution becomes more accurate but the runtime and memory consumption increase linearly. The default, -1, means the maximum of 10 and `num_components`. Valid for _randomized_ mode only. **Optional** Valid values: Non-negative integer or -1 Default value: -1 |
| `subtract_mean`    | Indicates whether the data should be unbiased both during training and at inference. **Optional** Valid values: One of _true_ or _false_ Default value: _true_                                                                                                                                |
