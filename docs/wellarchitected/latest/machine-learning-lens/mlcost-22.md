# MLCOST-22: Select optimal algorithms

Identify the basic machine learning paradigm that addresses your
ML problem type. Basic machine learning paradigms include:
supervised learning, unsupervised learning and reinforcement
learning. Identify the acceptable level of tradeoff between
explainability and success metrics per business requirements.
Run prototypes and experiments to explore high performing
algorithms. Select the optimal cost-efficient algorithms that
meet all the business requirements. Improved runtime performance
of a tuned algorithm within business requirements, is one step
towards optimizing the cost of ML.

## Implementation plan

- Adopt optimal practices
  - Start with simple algorithms, such as regression, and
    work towards more complex algorithms, such as deep
    learning, to compare the accuracy of the models.
    Optimize hyperparameters to determine which algorithm
    yields the best metrics for the business use case.
  - When selecting the optimal algorithm, run trade-off
    analysis between data constraints, computational
    performance, and maintenance efforts. For example, deep
    learning networks might produce more accurate results,
    but require more data than tree-based methods. Deep
    learning methods are also more difficult to maintain.

- Use AWS services
  - Use
    [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") with a suite of
    [built-in
    algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") to train and deploy machine learning
    models. AWS provides optimized versions of frameworks,
    such as TensorFlow, Chainer, Keras, and Theano. These
    frameworks include optimizations for high-performance
    training across
    [Amazon EC2](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") instance families.
  - Use
    [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to keep track of the
    models during testing.
  - Use
    [Amazon SageMaker AI Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development-get-started.md "../../../sagemaker/latest/dg/autopilot-automate-model-development-get-started.md") to select algorithms
    automatically.
  - Discover pre-trained ML models on AWS Marketplace -
    Pre-trained ML models are ready-to-use models that can
    be quickly deployed on _Amazon SageMaker AI_. By pre-training the models for
    you, solutions in AWS Marketplace take care of the
    heavy lifting, helping your team deliver ML powered
    features faster and at a lower cost.

## Documents

- [Choose
  an Algorithm](../../../sagemaker/latest/dg/algorithms-choose.md "../../../sagemaker/latest/dg/algorithms-choose.md")
- [Manage
  Machine Learning with Amazon SageMaker AIExperiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md")
- [Automate
  model development with Amazon SageMaker AIAutopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md")

## Blogs

- [Optimizing
  costs for machine learning with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/")
- [Amazon SageMaker AI Experiments – Organize, Track, and Compare Your
  Machine Learning Trainings](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/")
- [Amazon SageMaker AI Autopilot – Automatically Create High-Quality
  Machine Learning Models with Full](https://aws.amazon.com/blogs/aws/amazon-sagemaker-autopilot-fully-managed-automatic-machine-learning/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-autopilot-fully-managed-automatic-machine-learning/")
  [Control
  and Visibility](https://aws.amazon.com/blogs/aws/amazon-sagemaker-autopilot-fully-managed-automatic-machine-learning/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-autopilot-fully-managed-automatic-machine-learning/")
- [Streamline
  modeling with Amazon SageMaker AI Studio and the Amazon
  Experiments SDK](https://aws.amazon.com/blogs/machine-learning/streamline-modeling-with-amazon-sagemaker-studio-and-amazon-experiments-sdk/ "https://aws.amazon.com/blogs/machine-learning/streamline-modeling-with-amazon-sagemaker-studio-and-amazon-experiments-sdk/")

## Videos

- [Accelerate
  Machine Learning Projects with Hundreds of Algorithms and
  Models in AWS Marketplace](https://pages.awscloud.com/Accelerate-Machine-Learning-Projects-with-Hundreds-of-Algorithms-and-Models-in-AWS-Marketplace_2019_0422-MCL_OD.html "https://pages.awscloud.com/Accelerate-Machine-Learning-Projects-with-Hundreds-of-Algorithms-and-Models-in-AWS-Marketplace_2019_0422-MCL_OD.html")
- [Organize,
  Track, and Evaluate ML Training Runs with Amazon SageMaker AI
  Experiments](https://www.youtube.com/watch?v=zLOMYKZGxK0 "https://www.youtube.com/watch?v=zLOMYKZGxK0")
