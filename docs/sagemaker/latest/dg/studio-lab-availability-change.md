

# Studio Lab availability change
<a name="studio-lab-availability-change"></a>

**Note**  
Amazon SageMaker Studio Lab is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Studio Lab, but we do not plan to introduce new features.

## Amazon SageMaker Studio
<a name="studio-lab-replacement-studio"></a>

Amazon SageMaker Studio serves as a complete replacement for SageMaker Studio Lab by providing the same JupyterLab-based notebook environment with additional access to AWS services, scalable compute resources, and integrated ML tools. SageMaker Studio supports the same notebook runtime, conda environments, and file management workflows that Studio Lab users are familiar with.

For compute, SageMaker Studio provides access to a range of instance types from free tier (ml.t3.medium) to GPU-accelerated instances like G6, G6e etc., enabling users to scale beyond Studio Lab's fixed 12 GB RAM and 15 GB storage limits. For collaboration and MLOps, SageMaker Studio integrates with AWS services such as Amazon S3, SageMaker Pipelines, and Managed MLflow for experiment tracking. Refer to [SageMaker AI Free Tier](https://aws.amazon.com/sagemaker/ai/pricing/) for details.

Together, these capabilities provide a scalable, production-ready alternative to SageMaker Studio Lab's free-tier notebook environment.

## Replacing Amazon SageMaker Studio Lab with Amazon SageMaker Studio
<a name="studio-lab-replacing"></a>

This section guides you through migrating your existing Amazon SageMaker Studio Lab data to Amazon SageMaker Studio. This solution supports equivalent functionality for running JupyterLab notebooks, managing conda environments, and storing project files during development on Amazon SageMaker AI.

### Exporting from Studio Lab
<a name="studio-lab-exporting"></a>

1. **Export Conda Environment Configurations.** Activate the conda environment you want to migrate and export it to a YAML file. Do not export the `studiolab`, `studiolab-safemode`, or `base` environments, as these are incompatible with SageMaker Studio.

1. **Save Notebooks and Data Files.** Download your JupyterLab notebooks (.ipynb files), Python scripts, and any associated data from your Studio Lab environment. You can export files to your local machine using the Studio Lab File Browser, or push them to a Git repository using the Studio Lab terminal.

1. **Copy Large Datasets to Amazon S3 (If Applicable).** For large files or directories that are difficult to download locally, copy them to an S3 bucket using the Studio Lab terminal. Refer to [Uploading objects to Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) for the detailed steps.

1. **Delete Your Studio Lab Project (Optional).** Once migration is confirmed, delete your Studio Lab project files to free up storage.

### Configuring replacements
<a name="studio-lab-configuring-replacements"></a>

1. **Create an AWS Account.** If you do not already have an AWS account, create one at [aws.amazon.com/free](https://aws.amazon.com/free/).

1. **Set Up a SageMaker Studio Domain and Space.** Create a SageMaker Studio domain and user profile, then create a JupyterLab Space. Each Space gets its own Amazon EBS volume for persistent storage. Refer to [SageMaker AI domain overview](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html) for the detailed steps.

1. **Upload Notebooks and Files to SageMaker Studio.** Open your JupyterLab Space and upload your exported files using the File Browser upload icon, or clone your Git repository directly from the JupyterLab terminal.

1. **Recreate Conda Environments in SageMaker Studio.** Open a terminal in your JupyterLab Space and use your exported YAML file to recreate your conda environment. After installation, the environment will be available as a kernel for your notebooks. Refer to [JupyterLab environment customization](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide-customize-package-manager.html) in SageMaker Studio for the detailed steps.

Migrating to SageMaker Studio only migrates your notebooks, files, and environment configurations. Historical compute usage or session logs from Studio Lab are not transferred. Future development, experimentation, and compute management will happen within SageMaker Studio.