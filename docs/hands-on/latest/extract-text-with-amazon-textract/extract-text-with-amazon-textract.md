

# Extract information from unstructured documents with Amazon Bedrock and Amazon Textract
<a name="extract-text-with-amazon-textract"></a>


|  |  | 
| --- |--- |
| **AWS experience** | Beginner  | 
| **Time to complete** | 20 minutes  | 
| **Cost to complete** | Less than USD 0.15 if completed within 2 hours and the notebook is deleted at the end of the tutorial.  | 
| **Get help** | [Troubleshooting Amazon Bedrock models](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-troubleshooting.html) <br />[Debugging training issues](https://docs.aws.amazon.com/textract/latest/dg/textract-debugging-failures-adapters.html)  | 
| **Last update** | August 31, 2026  | 

## Overview
<a name="overview"></a>

In this tutorial, you will learn how to use Amazon Bedrock and Amazon Textract to extract and process information from unstructured documents. 

Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. 

Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, layout elements, and data from scanned documents. 

In this tutorial, you provide each document as a single-page image in JPG or PNG format, such as a scanned form, receipt, or ID card. This is the input that the Amazon Textract **DetectDocumentText** operation reads. Multi-page PDF documents require a different, asynchronous Amazon Textract workflow that is outside the scope of this tutorial. 

## What you will accomplish
<a name="what-you-will-accomplish"></a>

In this tutorial, you will: 
+ Enable access to a foundation model on your AWS account 
+ Create a new Jupyter notebook to write test code and run tests 
+ Generate code 
+ Clean up your resources 

## Prerequisites
<a name="prerequisites"></a>

Before starting this tutorial, you will need: 
+ An AWS account: if you don't already have one follow the [Setting Up Your Environment](https://docs.aws.amazon.com/hands-on/latest/setup-environment/) tutorial. 

## Implementation
<a name="implementation"></a>

### Step 1: Set up access to an Anthropic model
<a name="enable-anthropic-fm"></a>

Amazon Bedrock enables serverless foundation models automatically the first time you invoke them in a commercial AWS Region. Anthropic models have one additional one-time requirement: before you can use a Claude model, you must submit use case details for your AWS account. In this step, you submit those details from the Amazon Bedrock model catalog. 

**Note**  
**Already submitted Anthropic use case details for this account?** Skip to [Step 2: Create a Jupyter notebook](#create-a-jupyter-notebook).

1. Open the model catalog

   1. Sign in to the AWS Management Console, and open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home). 

   1. In the left navigation pane, under **Discover**, choose **Model catalog**. 

1. Choose an Anthropic model

   1. In the model catalog, filter by the **Anthropic** provider, and then choose a current Claude model, such as **Claude Sonnet 4.5**. 
**Note**  
Any current Claude text model works for this tutorial. To choose a model for your own use case, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html).

1. Submit use case details

   1. If this is the first time your account requests access to an Anthropic model, choose **Submit use case details**, complete the form (a description of your intended use and a website URL), and then choose **Submit**. Access is granted immediately. If your account already has access, the model opens directly. 
**Note**  
If you don't see the form, your account already has access to Anthropic models. The use case form is required only once per account, or once for the management account of an AWS organization. You can now create a Jupyter notebook.

### Step 2: Create a Jupyter notebook
<a name="create-a-jupyter-notebook"></a>

In this step, you will create a Jupyter notebook to write your proof of concept code and test it out with real documents. 

1. Open Amazon SageMaker AI

   1. Open the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home). 

   1. In the left navigation pane, under **Applications and IDEs**, choose **Notebooks**. 

1. Create a notebook instance

   1. On the **Notebooks and Git repos** page, choose **Create notebook instance**. 

1. Configure notebook instance settings

   On the **Create notebook instance** page, fill out the following configuration settings: 

   1. For **Notebook instance name**, enter a name for your Jupyter instance. 

   1. For **Notebook instance type**, verify **ml.t3.medium** is selected. 

   1. Keep all other default settings. 

1. Configure permissions and encryption

   In the **Permissions and encryption** section: 

   1. For **IAM role**, choose **Create a new role** from the list. 

   1. On the **Create an IAM role** dialog box, for **S3 buckets you specify** - **optional**, choose **None**, and then choose **Create role**. 

   Then, choose **Create notebook instance**. 
**Note**  
It can take a few minutes for the notebook instance to be created. Wait until its **Status** shows **InService** before you continue.  
![The Create notebook instance page in the Amazon SageMaker AI console, showing the Notebook instance settings section with the instance name and type, and the Permissions and encryption section with a successfully created IAM role and the Create notebook instance button.](http://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/images/create-notebook-instance-config.png)

### Step 3: Generate code to process your documents
<a name="generate-code-to-process-your-documents"></a>

In this step, you use the Amazon Bedrock playground to generate the Python code for your notebook, and then you run that code in the Jupyter notebook you created. First, you open your notebook. Next, you switch to the Amazon Bedrock playground and prompt a model to write the code that calls Amazon Textract. Finally, you return to your notebook, add a document image, grant the required permissions, and run the code. 

1. Open JupyterLab

   1. On the **Notebook instances** page, in the **Actions** column, choose **Open JupyterLab** for the notebook instance you created.
**Note**  
JupyterLab opens in a separate browser tab.

1. Create a new notebook

   1. In the **JupyterLab** Launcher, under **Notebook**, choose **conda\_python3** to create a notebook that uses that kernel. 

1. Open the chat playground

   1. In a new tab, open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home). 

   1. In the left navigation pane, under **Test**, choose **Playground**. 

1. Select the model

   1. To get started, choose **Select model**. 

1. Specify the model details

   In the **Select model** dialog box: 

   1. For **Categories**, choose **Anthropic**. 

   1. For **Models with access**, choose the Claude model you set up in Step 1 (for example, Claude Sonnet 4.5). 

   1. Then, choose **Apply**. 
**Note**  
The **Models with access** list shows the models your account can use. Choose the same Claude model you set up in Step 1.

1. Generate code

   1. In the **Chat playground**, you can now ask the model to write sample code. The following is an example prompt that you can use to extract information from an unstructured document. 

      ```
      I am writing a Jupyter notebook with a proof of concept python code snippets to perform a few tasks. 
      To start, write a snippet to iterate the current folder and read all the jpg/png files and for each file call textract DetectDocumentText API to extract all the text on the image.
      Re-save the result with the same file name and txt extension.
      Also make sure to: 
      - Not reprocess any files that already have the txt file existing in the directory 
      - Print a progress bar output using tqdm 
      - Keep everything readable and properly componentized in methods 
      - No need for __main__ implementations as it's a snippet to run on Jupyter notebook.
      ```

   1. After you enter your prompt and choose **Run**, the response includes the generated code in a code block, along with an explanation of what it does. 

1. Check the output

   1. Your generated code should look similar to the following example. To get a clean, ready-to-run copy, use this example rather than the playground output. The code finds the JPG and PNG files in the notebook directory, sends each one to the Amazon Textract **DetectDocumentText** operation, and saves the extracted text to a matching **.txt** file. Copy the following code, return to the JupyterLab notebook you created, and paste it into a cell. You run this code in a later step, after you add a document image and grant the required permissions. 
**Note**  
This example uses the US East (N. Virginia) (**us-east-1**) Region. If you are working in a different Region, change the **aws\_region** value in the code to match.

     ```
     import boto3
     import os
     from pathlib import Path
     from tqdm import tqdm
     import json
     
     def get_image_files(directory='.'):
         """
         Get all jpg and png files from the specified directory.
     
         Args:
             directory (str): Path to directory to scan. Defaults to current directory.
     
         Returns:
             list: List of Path objects for image files
         """
         image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
         image_files = []
     
         for ext in image_extensions:
             image_files.extend(Path(directory).glob(ext))
     
         return sorted(image_files)
     
     
     def filter_unprocessed_files(image_files):
         """
         Filter out images that already have corresponding txt files.
     
         Args:
             image_files (list): List of Path objects for image files
     
         Returns:
             list: List of Path objects for unprocessed images
         """
         unprocessed = []
     
         for image_path in image_files:
             txt_path = image_path.with_suffix('.txt')
             if not txt_path.exists():
                 unprocessed.append(image_path)
     
         return unprocessed
     
     
     def extract_text_from_image(image_path, textract_client):
         """
         Extract text from an image using AWS Textract DetectDocumentText API.
     
         Args:
             image_path (Path): Path to the image file
             textract_client: Boto3 Textract client
     
         Returns:
             str: Extracted text from the image
         """
         with open(image_path, 'rb') as image_file:
             image_bytes = image_file.read()
     
         response = textract_client.detect_document_text(
             Document={'Bytes': image_bytes}
         )
     
         # Extract text from blocks
         extracted_text_lines = []
         for block in response['Blocks']:
             if block['BlockType'] == 'LINE':
                 extracted_text_lines.append(block['Text'])
     
         return '\n'.join(extracted_text_lines)
     
     
     def save_extracted_text(image_path, extracted_text):
         """
         Save extracted text to a txt file with the same name as the image.
     
         Args:
             image_path (Path): Path to the original image file
             extracted_text (str): Text to save
         """
         txt_path = image_path.with_suffix('.txt')
     
         with open(txt_path, 'w', encoding='utf-8') as txt_file:
             txt_file.write(extracted_text)
     
     
     def process_images_with_textract(directory='.', aws_region='us-east-1'):
         """
         Process all images in directory with AWS Textract and save results as txt files.
     
         Args:
             directory (str): Path to directory containing images. Defaults to current directory.
             aws_region (str): AWS region for Textract client. Defaults to 'us-east-1'.
         """
         # Initialize Textract client
         textract_client = boto3.client('textract', region_name=aws_region)
     
         # Get all image files
         print("Scanning for image files...")
         image_files = get_image_files(directory)
         print(f"Found {len(image_files)} image file(s)")
     
         # Filter out already processed files
         unprocessed_files = filter_unprocessed_files(image_files)
         print(f"{len(unprocessed_files)} file(s) need processing")
     
         if not unprocessed_files:
             print("No files to process!")
             return
     
         # Process each image with progress bar
         print("\nProcessing images...")
         for image_path in tqdm(unprocessed_files, desc="Extracting text", unit="file"):
             try:
                 # Extract text using Textract
                 extracted_text = extract_text_from_image(image_path, textract_client)
     
                 # Save to txt file
                 save_extracted_text(image_path, extracted_text)
     
             except Exception as e:
                 tqdm.write(f"Error processing {image_path.name}: {str(e)}")
     
         print("\nProcessing complete!")
     
     
     # Run the processing
     process_images_with_textract(directory='.', aws_region='us-east-1')
     ```

1. Prepare a document image

   1. Find a document image (JPG or PNG) on your local machine, such as a scanned form, receipt, or card. In JupyterLab, drag the file onto the file browser panel on the left side, not the code editor on the right. (You can also choose the **Upload** button in the file browser.) Confirm the file appears in the file browser next to your notebook. 

1. Configure permissions

   Before you can run the code in your JupyterLab, the IAM role that was created with your notebook instance needs permissions for the AWS services that your code uses. The example code uses Amazon Textract, so the role needs Amazon Textract permissions. 

   1. Open the [IAM console](https://console.aws.amazon.com/iam/home). 

   1. In the left navigation pane, under **Access management**, choose **Roles**. 

1. Search for the IAM role

   1. In the **search box**, find the **AmazonSageMaker-ExecutionRole-<timestamp>** role that was created with your notebook instance in Step 2, and then choose the role name to open it. 

1. Add permissions

   1. On the **AmazonSageMaker-ExecutionRole-<timestamp>** page, choose the **Add permissions** menu, and select **Attach policies**. 

1. Attach the policy

   1. On the **Attach policy to AmazonSageMaker-ExecutionRole-<timestamp>** page, in the **Other permissions policies** section search bar, enter **AmazonTextractFullAccess**. Then, select the check box next to the policy, and choose **Add permissions**. 

1. Run the notebook

   1. Return to your JupyterLab notebook, select the cell that contains your pasted code, and then choose the **Run** button to run the cell.   
![A Jupyter Notebook interface showing Python code for processing image files, including functions to list image files, check if a file should be processed, and extract text using Amazon Textract.](http://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/images/jupyter-notebook-interface-code-processing.png)

1. View the text file

   1. After your code runs, a **.txt file** with the same name as your image appears in the file browser on the left. Double-click the file to open it and view the extracted text.   
![A file explorer and text editor showing a health insurance card's redacted details, including member name, ID, plan type, and coverage information.](http://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/images/file-explorer-text-editor-health-insurance.png)

### Clean up resources
<a name="clean-up-resources"></a>

In this step, you will go through the steps to delete all the resources you created throughout this tutorial. We recommend that you stop the Jupyter notebook you created to prevent unexpected costs. 

1. Stop the notebook

   1. In the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home), in the left navigation pane, under **Applications and IDEs**, choose **Notebooks**, and select the notebook you created. Then, choose **Actions**, and select **Stop**. 

1. Delete the notebook

   1. After the notebook stops (this can take around 5 minutes), choose **Actions** again, and select **Delete** to remove the notebook instance so it no longer incurs charges. 

## Congratulations
<a name="congratulations"></a>

You have created a sample proof of concept to extract information from documents. 

Next steps: to learn more, see the [Amazon Textract Developer Guide](https://docs.aws.amazon.com/textract/latest/dg/what-is-textract.html) and the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).