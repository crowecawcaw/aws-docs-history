# Create a design review

Assess your design documents against organization security requirements by uploading files for AWS Security Agent to review. Design reviews help identify security issues early in the development lifecycle, enabling you to address architectural concerns when they are most cost-effective to resolve.

AWS Security Agent analyzes your design documents against your organization’s security requirements, providing detailed security findings to improve security posture before implementation begins.

In this procedure, you’ll create a design review by uploading design files for analysis.

## Prerequisites

Before you begin, ensure you have:

- Access to the AWS Security Agent web application
- Design documents ready for upload (DOC, DOCX, JPEG, MD, PDF, PNG and TXT)
- Each file must be 2MB or smaller, with a combined total of 6MB across all files
- Understanding of which security requirements are enabled for your organization

## Step 1: Start creating a design review

Navigate to the design review creation page in the Agent Web App.

1. Log in to the AWS Security Agent web application.
2. Navigate to the **Design reviews** section.
3. Click **Create Design Review**.

###### Tip

You can view your organization’s enabled security requirements by navigating to the **Security requirements** page in the AWS Security Agent console. Click on any enabled requirement to view its details. These requirements are used to analyze your design files.

## Step 2: Name your design review

Provide a descriptive name that helps identify the purpose and scope of this design review.

1. In the **Design review name** section, locate the **Name** field.
2. Enter a descriptive name for your design review.

###### Note

The name should clearly identify the project, feature, or component being reviewed. Maximum 80 characters.

## Step 3: Upload design files

Upload the design documents you want AWS Security Agent to analyze for security compliance.

1. In the **Files to review** section, review the file requirements:

###### Important

A maximum of 5 files may be uploaded per design review. Each file must be 2MB or smaller, with a combined total of 6MB across all files. Supported formats: DOC, DOCX, JPEG, MD, PDF, PNG and TXT. 2. Upload your files using one of these methods:

    1. **Drag and drop** – Drag files directly into the file dropzone area
    2. **Browse** – Click **Choose files** to browse and select files from your computer

3. Verify that all required files are uploaded.

###### Tip

For best results, include architecture diagrams, design specifications, and technical documentation that describe your system’s security-relevant components and data flows.

## Step 4: Initiate the design review

After configuring all required information, initiate the security analysis of your design documents.

1. Review all uploaded files and settings to ensure accuracy.
2. Click **Start design review** at the bottom of the page.
3. AWS Security Agent will analyze your design documents against enabled security requirements.

###### Note

The design review process typically completes within minutes, depending on the number and size of files uploaded. You’ll receive security findings based on your organization’s security requirements.

## Next steps

After starting your design review:

- Monitor the review progress in the Agent Web App
- Review security findings
- Share findings with your development team
- Address identified security findings in your design
- Update design documents and resubmit if needed
