

# Troubleshooting PySpark analysis templates
<a name="troubleshooting-pyspark-analysis-templates"></a>

When running jobs using PySpark analysis templates, you might encounter failures during job initialization or execution. These failures typically relate to script configuration, data access permissions, or environment setup.

For more information about PySpark limitations, see [PySpark limitations in AWS Clean Rooms](pyspark-analysis-templates.md#pyspark-limitations).

**Topics**
+ [Troubleshooting your code](#troubleshoot-your-code)
+ [Analysis template job doesn't start](#troubleshooting_analysis_template_job_fails_to_start)
+ [Analysis template job starts but fails during processing](#analysis-template-job-failes-to-run)
+ [Virtual environment setup fails](#virtual-environment-setup-fails)

## Troubleshooting your code
<a name="troubleshoot-your-code"></a>



To help you develop and troubleshoot your code, we suggest you simulate AWS Clean Rooms in your own AWS account by enabling **Detailed error messages** and running jobs using your own test data. 

You can also simulate PySpark in AWS Clean Rooms in Amazon EMR Serverless with the following steps. It will have small differences with PySpark in AWS Clean Rooms but mostly covers how your code can be run. 

**To simulate PySpark in AWS Clean Rooms in EMR Serverless**

1. Create a dataset in Amazon S3, catalog it in the AWS Glue Data Catalog, and set up Lake Formation permissions.

1. Register the S3 location with Lake Formation using a custom role.

1. Create an Amazon EMR Studio instance if you don’t already have one (Amazon EMR Studio is needed to use Amazon EMR Serverless).

1. Create an EMR Serverless app
   + Select release version emr-7.7.0.
   + Select ARM64 architecture.
   + Opt for **Use custom settings**.
   + Disable preinitialized capacity.
   + If you plan to do interactive work, select **Interactive endpoint** > **Enable endpoint for EMR studio**.
   + Select **Additional configurations** > **Use Lake Formation for fine-grained access control**.
   + Create the application.

1. Use EMR-S either via EMR-Studio notebooks or the `StartJobRun` API.

## Analysis template job doesn't start
<a name="troubleshooting_analysis_template_job_fails_to_start"></a>

### Common causes
<a name="troubleshooting_common_cause"></a>

Analysis template jobs can fail immediately at startup due to three main configuration issues: 
+ Incorrect script naming that doesn't match the required format 
+ Missing or incorrectly formatted entrypoint function in the user script 
+ Incompatible Python version in the virtual environment

### Resolution
<a name="troubleshooting_resolution"></a>

**To resolve:**

1. Verify your user script: 

   1. Check that your user script has a valid Python filename.

     Valid Python filenames use lowercase letters, underscores to separate words, and the .py extension.

1. Verify the entrypoint function. If your user script doesn't have an entrypoint function, add one. 

   1. Open your user script.

   1. Add this entrypoint function:

      ```
      def entrypoint(context):
          # Your analysis code here
      ```

   1. Ensure the function name is spelled exactly as `entrypoint`. 

   1. Verify the function accepts the `context` parameter.

1. Check Python version compatibility: 

   1. Verify your virtual environment uses Python 3.9 or 3.11.

   1. To check your version, run: `python --version` 

   1. If needed, update your virtual environment: 

      ```
      conda create -n analysis-env python=3.9
      conda activate analysis-env
      ```

### Prevention
<a name="troubleshooting_prevention"></a>
+ Use the provided analysis template starter code that includes the correct file structure.
+ Set up a dedicated virtual environment with Python 3.9 or 3.11 for all analysis templates. 
+ Test your analysis template locally using the template validation tool before submitting jobs. 
+ Implement CI/CD checks to verify script naming and entrypoint function requirements.

## Analysis template job starts but fails during processing
<a name="analysis-template-job-failes-to-run"></a>

### Common causes
<a name="troubleshooting_common_cause"></a>

Analysis jobs can fail during execution for these security and formatting reasons:
+ Unauthorized direct access attempts to AWS services like Amazon S3 or AWS Glue 
+ Returning output in incorrect formats that don't match required DataFrame specifications 
+ Blocked network calls due to security restrictions in the execution environment 

### Resolution
<a name="troubleshooting_resolution"></a>

**To resolve**

1. Remove direct AWS service access: 

   1. Search your code for direct AWS service imports and calls. 

   1. Replace direct S3 access with provided Spark session methods. 

   1. Use only pre-configured tables through the collaboration interface. 

1. Format outputs correctly: 

   1. Verify all outputs are Spark DataFrames. 

   1. Update your return statement to match this format: 

      ```
      return {
          "results": {
              "output1": dataframe1
          }
      }
      ```

   1. Remove any non-DataFrame return objects. 

1. Remove network calls: 

   1. Identify and remove any external API calls. 

   1. Remove any urllib, requests, or similar network libraries. 

   1. Remove any socket connections or HTTP client code. 

### Prevention
<a name="troubleshooting_prevention"></a>
+ Use the provided code linter to check for unauthorized AWS imports and network calls. 
+ Test jobs in the development environment where security restrictions match production. 
+ Follow the output schema validation process before deploying jobs. 
+ Review the security guidelines for approved service access patterns.

## Virtual environment setup fails
<a name="virtual-environment-setup-fails"></a>

### Common causes
<a name="virtual-env-fails-cause"></a>

Virtual environment configuration failures commonly occur due to: 
+ Mismatched CPU architecture between development and execution environments 
+ Python code formatting issues that prevent proper environment initialization 
+ Incorrect base image configuration in container settings 

### Resolution
<a name="virtual-env-fails-resolution"></a>

**To resolve**

1. Configure the correct architecture: 

   1. Check your current architecture with `uname -m. `

   1. Update your Dockerfile to specify ARM64: 

      ```
      FROM --platform=linux/arm64 public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
      ```

   1. Rebuild your container with `docker build --platform=linux/arm64.` 

1. Fix Python indentation: 

   1. Run a Python code formatter like `black` on your code files. 

   1. Verify consistent use of spaces or tabs (not both). 

   1. Check indentation of all code blocks: 

      ```
      def my_function():
          if condition:
              do_something()
          return result
      ```

   1. Use an IDE with Python indentation highlighting. 

1. Validate environment configuration: 

   1. Run `python -m py_compile your_script.py` to check for syntax errors. 

   1. Test the environment locally before deployment. 

   1. Verify all dependencies are listed in `requirements.txt`. 

### Prevention
<a name="virtual-env-fails-prevention"></a>
+ Use Visual Studio Code or PyCharm with Python formatting plugins 
+ Configure pre-commit hooks to run code formatters automatically 
+ Build and test environments locally using the provided ARM64 base image 
+ Implement automated code style checking in your CI/CD pipeline 