# SageMaker JupyterLab

Create a JupyterLab space within Amazon SageMaker Studio to launch the JupyterLab
application. A JupyterLab space is a private or shared space within Studio that
manages the storage and compute resources needed to run the JupyterLab application. The
JupyterLab application is a web-based interactive development environment (IDE) for
notebooks, code, and data. Use the JupyterLab application's flexible and extensive
interface to configure and arrange machine learning (ML) workflows.

By default, the JupyterLab application comes with the SageMaker Distribution image. The
distribution image has popular packages, such as the following:

- PyTorch
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
  You can use shared spaces to collaborate on your Jupyter notebooks with other users in
  real time. For more information about shared spaces, see [Collaboration with shared spaces](domain-space.md "domain-space.md").

Within the JupyterLab application, you can use Amazon Q Developer, a generative AI
powered code companion to generate, debug, and explain your code. For information about
using Amazon Q Developer, see [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md"). For information about setting up Amazon Q Developer, see [JupyterLab administrator guide](studio-updated-jl-admin-guide.md "studio-updated-jl-admin-guide.md").

Build unified analytics and ML workflows in same Jupyter notebook. Run interactive
Spark jobs on Amazon EMR and AWS Glue serverless infrastructure, right from your
notebook. Monitor and debug jobs faster using the inline Spark UI. In a few
steps, you can automate your data prep by scheduling the notebook as a job.

The JupyterLab application helps you work collaboratively with your peers. Use the
built-in Git integration within the JupyterLab IDE to share and version code. Bring your
own file storage system if you have an Amazon EFS volume.

The JupyterLab application runs on a single Amazon Elastic Compute Cloud
(Amazon EC2)
instance and uses a single Amazon Elastic Block Store (Amazon EBS) volume for storage. You can switch faster
instances or increase the Amazon EBS volume size for your needs.

The JupyterLab 4 application runs in a JupyterLab space within Studio. Studio Classic
uses the JupyterLab 3 application. JupyterLab 4 provides the following benefits:

- A faster IDE than Amazon SageMaker Studio Classic, especially with large notebooks
- Improved
  document search
- A
  more
  performant and accessible text
  editor
  For more information about JupyterLab, see [JupyterLab
  Documentation](https://jupyterlab.readthedocs.io/en/stable/# "https://jupyterlab.readthedocs.io/en/stable/#").

###### Topics

- [JupyterLab user guide](studio-updated-jl-user-guide.md "studio-updated-jl-user-guide.md")
- [JupyterLab administrator guide](studio-updated-jl-admin-guide.md "studio-updated-jl-admin-guide.md")
