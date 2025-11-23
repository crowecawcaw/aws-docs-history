# MLCOST04-BP14 Select optimal algorithms

Selecting optimal algorithms for machine learning (ML) workloads is
crucial for balancing cost efficiency and performance. By
identifying appropriate ML paradigms and carefully evaluating
algorithmic choices, you can optimize both technical performance and
business outcomes while managing costs.

**Desired outcome:** You are able to
identify the most suitable ML algorithm for your specific use case
that balances accuracy, explainability, computational requirements,
and cost efficiency. You can conduct effective trade-off analyses
between different approaches and use AWS services to optimize
algorithm selection, training, and deployment.

**Common anti-patterns:**

- Using complex deep learning solutions without first exploring
  simpler algorithms.
- Ignoring the explainability requirements of the business use
  case.
- Failing to consider data constraints when selecting algorithms.
- Not evaluating computational and maintenance costs alongside
  accuracy metrics.

**Benefits of establishing this best
practice:**

- Reduced computational costs by using algorithms appropriate for
  the specific problem.
- Improved model performance through systematic comparison of
  algorithm options.
- Enhanced model explainability when required by business
  stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Selecting the optimal algorithm requires understanding your
specific ML problem type and the business constraints around it.
Begin by categorizing your problem into basic ML paradigms:
supervised learning (for labeled data), unsupervised learning (for
unlabeled data), or reinforcement learning (for sequential
decision problems). Consider what matters most for your use case,
whether it's prediction accuracy, model explainability, inference
speed, or a balance of these factors.

Algorithm selection significantly impacts both the performance and
cost efficiency of your ML solutions. A computationally expensive
algorithm might deliver marginally better accuracy but at
substantially higher operational costs. Similarly, a complex but
highly accurate algorithm might sacrifice the explainability
needed for regulatory adherence or business transparency. Finding
the right balance requires systematic experimentation and
evaluation against your business requirements.

AWS provides various services test, compare, and optimize
algorithms, allowing you to make data-driven decisions about which
approach delivers the best value for your specific use case.

### Implementation steps

1. **Define your machine learning problem
   type**. Categorize your problem as supervised
   learning (classification, regression), unsupervised learning
   (clustering, dimensionality reduction), or reinforcement
   learning. This initial classification narrows down the
   appropriate algorithms to consider.
2. **Determine business requirements and
   constraints**. Document specific accuracy targets,
   explainability needs, inference time requirements, and
   budget constraints. These requirements will serve as
   criteria for evaluating algorithm options.
3. **Start with simple algorithms
   first**. Begin experimentation with simpler
   algorithms like linear or logistic regression, decision
   trees, or k-means clustering before moving to more complex
   approaches. These algorithms are computationally efficient,
   simpler to interpret, and establish important baselines for
   performance comparison.
4. **Conduct structured
   experimentation**. Use
   [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to track different algorithm
   trials, hyperparameter configurations, and their results.
   This creates reproducibility and facilitates comparison
   between approaches.
5. **Perform comprehensive trade-off
   analysis**. When comparing algorithms, consider
   multiple dimensions beyond accuracy:
   - Data requirements (amount needed for training)
   - Computational resources required for training and
     inference
   - Model explainability and interpretability
   - Deployment complexity and operational overhead
   - Long-term maintenance costs

6. **Use AWS optimized algorithms and
   frameworks**. Use
   [Amazon SageMaker AI built-in algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") that are optimized for
   performance and cost-efficiency on AWS infrastructure. AWS
   also provides optimized versions of popular frameworks like
   TensorFlow, PyTorch, and MXNet that include performance
   enhancements for training across
   [Amazon EC2](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") instance families.
7. **Consider automated ML
   approaches**. For exploratory projects or when
   seeking optimal performance with minimal manual tuning, use
   SageMaker AI Canvas for rapid algorithm prototyping with the
   ability to export generated code to notebooks for further
   customization.
8. **Explore pre-trained
   models**. Search AWS Marketplace for pre-trained
   models that can accelerate development through transfer
   learning or direct deployment. Pre-trained models can
   significantly reduce computational costs and development
   time.
9. **Implement continuous
   evaluation**. As new algorithms and model versions
   emerge, periodically reassess whether your chosen approach
   remains optimal. Business requirements and available
   technologies evolve over time.
10. **Document algorithm selection
    rationale**. Create clear documentation explaining
    why specific algorithms were selected, what trade-offs were
    accepted, and how these decisions align with business
    requirements.
11. **For generative AI projects, consider
    foundation models from
    [Amazon
    Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") for natural language processing, image
    generation, and other tasks where these models can provide
    state-of-the-art performance with lower development
    costs.** Use techniques like prompt engineering and
    fine-tuning to adapt foundation models to your specific
    business needs while avoiding the computational expense of
    training from scratch.

## Resources

**Related documents:**

- [Built-in
  algorithms and pretrained models in Amazon SageMaker AI](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md#mlflow-tracking "../../../sagemaker/latest/dg/mlflow.md#mlflow-tracking")
- [How
  custom models work](../../../sagemaker/latest/dg/canvas-build-model.md "../../../sagemaker/latest/dg/canvas-build-model.md")
- [Types
  of Algorithms](../../../sagemaker/latest/dg/algorithms-choose.md "../../../sagemaker/latest/dg/algorithms-choose.md")
- [SageMaker AI
  JumpStart pretrained Models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
