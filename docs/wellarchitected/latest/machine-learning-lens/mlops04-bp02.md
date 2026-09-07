

# MLOPS04-BP02 Establish reliable packaging patterns to access approved public libraries
<a name="mlops04-bp02"></a>

 Establishing reliable packaging patterns enables data scientists to access approved public libraries efficiently and consistently. By implementing structured access to public libraries and creating separate kernels for common ML frameworks, organizations can have both flexibility and security in their machine learning development environments. 

 **Desired outcome:** You create a streamlined workflow where your data scientists have reliable access to approved libraries through internal repositories. You maintain separate kernels for common ML frameworks like TensorFlow, PyTorch, Scikit-learn, and Keras. This approach improves development productivity while improving security and adherence with organizational requirements. 

 **Common anti-patterns:** 
+  Allowing uncontrolled direct downloads from public repositories. 
+  Using inconsistent or undocumented container configurations. 
+  Maintaining duplicate library versions across different environments. 
+  Not having a centralized strategy for package management. 
+  Failing to version control dependencies. 

 **Benefits of establishing this best practice:** 
+  Better security through controlled library usage. 
+  Improved reproducibility of ML workloads. 
+  Reduced dependency conflicts. 
+  Simplified adherence with organizational security policies. 
+  Faster onboarding of new data scientists. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Creating reliable packaging patterns is essential for maintaining consistent, secure, and efficient machine learning workflows. You need to establish infrastructure that gives data scientists access to the libraries they need while maintaining organizational control over those dependencies. Container technologies provide a portable, consistent way to package ML environments with required dependencies, making them ideal for this purpose. Internal artifact repositories allow for centralized management of approved packages so that team members use consistent, vetted versions. 

 Your packaging strategy should balance flexibility for data scientists with security and regulatory requirements. This means establishing both infrastructure (containers, repositories) and processes (approval workflows, versioning policies) that work together to create a streamlined experience. The use of standardized environments with separate kernels for different ML frameworks enables isolation when needed while providing the specific tools required for different types of projects. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up container infrastructure for ML workloads**. Create a container strategy using [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) (Amazon ECR) to store and manage your ML container images. Containers provide consistent environments that package dependencies, libraries, and runtime components needed for ML workloads. 

1.  **Create base container images for common ML frameworks**. Build and maintain separate base container images for frameworks like TensorFlow, PyTorch, Scikit-learn, and Keras using [optimized foundation model containers](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference.html) for efficient training and inference. These images should include standard configurations and commonly used libraries for each framework, with support for frameworks like Hugging Face Transformers and quantization techniques, providing consistency across your organization. 

1.  **Implement versioning and tagging policies**. Establish clear policies for versioning containers and artifacts for reproducibility of ML experiments and models. Use semantic versioning and proper tagging to track container image changes and library updates. 

1.  **Develop automation for container builds and updates**. Implement CI/CD pipelines using [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to automatically build, test, and deploy updated container images when dependencies need to be updated or security patches are required. 

1.  **Document usage patterns and onboarding procedures**. Create comprehensive documentation that explains how data scientists should use the established packaging patterns, including how to access approved libraries and work with containerized environments. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [What is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) 
+  [What are AWS Deep Learning Containers?](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html) 
+  [Docker containers for training and deploying models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html) 
+  [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) 
+  ["Publish Docker image to an Amazon ECR image repository" sample for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html) 

 **Related examples:** 
+  [SageMaker AI Custom Container Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/custom-training-containers) 
+  [Deep Learning Container Examples](https://github.com/aws/deep-learning-containers/tree/master/examples) 