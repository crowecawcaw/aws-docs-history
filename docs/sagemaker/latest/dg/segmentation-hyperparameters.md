

# Semantic Segmentation Hyperparameters
<a name="segmentation-hyperparameters"></a>

The following tables list the hyperparameters supported by the Amazon SageMaker AI semantic segmentation algorithm for network architecture, data inputs, and training. You specify Semantic Segmentation for training in the `AlgorithmName` of the [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request.

**Network Architecture Hyperparameters**


| Parameter Name | Description | 
| --- | --- | 
| backbone | The backbone to use for the algorithm's encoder component.<br />**Optional**<br />Valid values: `resnet-50`, `resnet-101` <br />Default value: `resnet-50` | 
| use\_pretrained\_model | Whether a pretrained model is to be used for the backbone.<br />**Optional**<br />Valid values: `True`, `False`<br />Default value: `True` | 
| algorithm | The algorithm to use for semantic segmentation. <br />**Optional**<br />Valid values:+  `fcn`: [Fully-Convolutional Network (FCN) algorithm ](https://arxiv.org/abs/1605.06211)  <br />+  `psp`: [Pyramid Scene Parsing (PSP) algorithm](https://arxiv.org/abs/1612.01105) <br />+  `deeplab`: [DeepLab V3 algorithm](https://arxiv.org/abs/1706.05587) <br />Default value: `fcn` | 

**Data Hyperparameters**


| Parameter Name | Description | 
| --- | --- | 
| num\_classes | The number of classes to segment.<br />**Required**<br />Valid values: 2 ≤ positive integer ≤ 254 | 
| num\_training\_samples | The number of samples in the training data. The algorithm uses this value to set up the learning rate scheduler.<br />**Required**<br />Valid values: positive integer | 
| base\_size | Defines how images are rescaled before cropping. Images are rescaled such that the long size length is set to `base_size` multiplied by a random number from 0.5 to 2.0, and the short size is computed to preserve the aspect ratio.<br />**Optional**<br />Valid values: positive integer > 16<br />Default value: 520 | 
| crop\_size | The image size for input during training. We randomly rescale the input image based on `base_size`, and then take a random square crop with side length equal to `crop_size`. The `crop_size` will be automatically rounded up to multiples of 8.<br />**Optional**<br />Valid values: positive integer > 16<br />Default value: 240 | 

**Training Hyperparameters**


| Parameter Name | Description | 
| --- | --- | 
| early\_stopping | Whether to use early stopping logic during training.<br />**Optional**<br />Valid values: `True`, `False`<br />Default value: `False` | 
| early\_stopping\_min\_epochs | The minimum number of epochs that must be run.<br />**Optional**<br />Valid values: integer<br />Default value: 5 | 
| early\_stopping\_patience | The number of epochs that meet the tolerance for lower performance before the algorithm enforces an early stop.<br />**Optional**<br />Valid values: integer<br />Default value: 4 | 
| early\_stopping\_tolerance | If the relative improvement of the score of the training job, the mIOU, is smaller than this value, early stopping considers the epoch as not improved. This is used only when `early_stopping` = `True`.<br />**Optional**<br />Valid values: 0 ≤ float ≤ 1<br />Default value: 0.0 | 
| epochs | The number of epochs with which to train.<br />**Optional**<br />Valid values: positive integer<br />Default value: 10 | 
| gamma1 | The decay factor for the moving average of the squared gradient for `rmsprop`. Used only for `rmsprop`.<br />**Optional**<br />Valid values: 0 ≤ float ≤ 1<br />Default value: 0.9 | 
| gamma2 | The momentum factor for `rmsprop`.<br />**Optional**<br />Valid values: 0 ≤ float ≤ 1<br />Default value: 0.9 | 
| learning\_rate | The initial learning rate. <br />**Optional**<br />Valid values: 0 < float ≤ 1<br />Default value: 0.001 | 
| lr\_scheduler | The shape of the learning rate schedule that controls its decrease over time.<br />**Optional**<br />Valid values: +  `step`: A stepwise decay, where the learning rate is reduced (multiplied) by the `lr_scheduler_factor` after epochs specified by `lr_scheduler_step`. <br />+  `poly`: A smooth decay using a polynomial function.  <br />+  `cosine`: A smooth decay using a cosine function.  <br />Default value: `poly` | 
| lr\_scheduler\_factor | If `lr_scheduler` is set to `step`, the ratio by which to reduce (multipy) the `learning_rate` after each of the epochs specified by the `lr_scheduler_step`. Otherwise, ignored.<br />**Optional**<br />Valid values: 0 ≤ float ≤ 1<br />Default value: 0.1 | 
| lr\_scheduler\_step | A comma delimited list of the epochs after which the `learning_rate` is reduced (multiplied) by an `lr_scheduler_factor`. For example, if the value is set to `"10, 20"`, then the `learning-rate` is reduced by `lr_scheduler_factor` after the 10th epoch and again by this factor after 20th epoch.<br />**Conditionally Required** if `lr_scheduler` is set to `step`. Otherwise, ignored.<br />Valid values: string<br />Default value: (No default, as the value is required when used.) | 
| mini\_batch\_size | The batch size for training. Using a large `mini_batch_size` usually results in faster training, but it might cause you to run out of memory. Memory usage is affected by the values of the `mini_batch_size` and `image_shape` parameters, and the backbone architecture.<br />**Optional**<br />Valid values: positive integer <br />Default value: 16 | 
| momentum | The momentum for the `sgd` optimizer. When you use other optimizers, the semantic segmentation algorithm ignores this parameter.<br />**Optional**<br />Valid values: 0 < float ≤ 1<br />Default value: 0.9 | 
| optimizer | The type of optimizer. For more information about an optimizer, choose the appropriate link:+  `adam`: [Adaptive momentum estimation](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam) <br />+  `adagrad`: [Adaptive gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad) <br />+  `nag`: [Nesterov accelerated gradient](https://calculus.subwiki.org/wiki/Nesterov%27s_gradient_acceleration) <br />+  `rmsprop`: [Root mean square propagation](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#RMSProp) <br />+  `sgd`: [Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) <br />**Optional**<br />Valid values: `adam`, `adagrad`, `nag`, `rmsprop`, `sgd` <br />Default value: `sgd` | 
| syncbn | If set to `True`, the batch normalization mean and variance are computed over all the samples processed across the GPUs.<br />**Optional** <br />Valid values: `True`, `False` <br />Default value: `False` | 
| validation\_mini\_batch\_size | The batch size for validation. A large `mini_batch_size` usually results in faster training, but it might cause you to run out of memory. Memory usage is affected by the values of the `mini_batch_size` and `image_shape` parameters, and the backbone architecture. +  To score the validation on the entire image without cropping the images, set this parameter to 1. Use this option if you want to measure performance on the entire image as a whole.   Setting the `validation_mini_batch_size` parameter to 1 causes the algorithm to create a new network model for every image. This might slow validation and training.   <br />+  To crop images to the size specified in the `crop_size` parameter, even during evaluation, set this parameter to a value greater than 1.  <br />**Optional**<br />Valid values: positive integer<br />Default value: 16 | 
| weight\_decay | The weight decay coefficient for the `sgd` optimizer. When you use other optimizers, the algorithm ignores this parameter. <br />**Optional**<br />Valid values: 0 < float < 1<br />Default value: 0.0001 | 