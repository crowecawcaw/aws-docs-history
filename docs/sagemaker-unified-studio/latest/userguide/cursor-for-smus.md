# Cursor in Amazon SageMaker Unified Studio

Cursor is a VS Code-based AI-powered IDE that you can use as a local IDE to connect to
your Amazon SageMaker Unified Studio Spaces and resources.

###### Important

Cursor is currently verified only for Spaces with public internet access.

These instructions assume you already have an Amazon SageMaker Unified Studio domain, project, and Space set
up.

###### To set up Cursor

1. Download and install Cursor from [cursor.com/download](https://cursor.com/download "https://cursor.com/download")
   (minimum version v2.6.18 or later).
2. Open the AWS Toolkit panel in Cursor and navigate to the Amazon SageMaker Unified Studio
   section.
3. Choose **Sign in to get started**, and then choose
   **IAM Credentials**. You can also use IAM Identity
   Center.
4. Create or choose a credential profile using the same IAM role you use to
   access your project in the AWS Management Console. Choose the Region your
   project is in, and then sign in. Your Amazon SageMaker Unified Studio resources (Data, Compute,
   Spaces) appear in the panel.
5. Under your project, choose **Compute**, and then choose
   **Spaces**. Hover over the Space you want to connect to and
   choose the **Connect** button.
6. When prompted to install the Remote SSH Plugin for Cursor, choose
   **Install**. This enables remote access, starts the Space,
   and connects to it.
7. Sign in to Cursor on the Space when prompted. After you connect, all project
   files are available in your remote workspace.

###### Note

Instances must have a minimum of 8 GB RAM. The following instance types are not
supported: `ml.t3.medium`, `ml.c7i.large`,
`ml.c6i.large`, `ml.c6id.large`,
`ml.c5.large`.
