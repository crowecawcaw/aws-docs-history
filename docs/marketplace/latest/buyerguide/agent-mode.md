

# Agent mode for AWS Marketplace

Agent mode is a conversational interface purpose-built for software procurement on AWS Marketplace. It is powered by a set of specialized capabilities to help you discover, evaluate, and select software solutions through natural conversation. You describe your needs in plain language and receive personalized recommendations, comparisons, and evaluation reports, and you can buy and deploy the software. Agent mode combines the AWS Marketplace product catalog with specialized knowledge from trusted third parties.

Agent mode uses six specialized capabilities that work together to guide you through your software procurement journey. The capabilities that power agent mode include the following:
+ **Search capability** – Translates your requirements into relevant recommendations from the AWS Marketplace catalog. When you describe a business problem or use case, the Search capability shows options across software, professional services, AI agents and tools, and multi-product solutions. The results become more specific as you add context.
+ **Comparison capability** – Creates side-by-side comparisons of products with reviews, features, and key differentiators.
+ **Evaluation capability** – Generates detailed reports and purchase proposals with insights gathered throughout your discovery process.
+ **Trust capability** – Retrieves a product's security and compliance profile for sellers whose trust center is hosted by a supported third-party provider (Drata or Vanta). It streamlines access to security evidence that requires a nondisclosure agreement (NDA), compares products on security and compliance, and runs Consensus Assessments Initiative Questionnaire (CAIQ) assessments against the seller's evidence or your own uploaded evidence.
+ **Checkout capability** – Helps you complete a purchase. After you sign in, you see the pricing available to you, including public pricing and any private offers extended to your AWS account. It helps you configure the offer (for example, selecting dimensions), summarizes the end user license agreement (EULA) and answers questions about it, and adds purchase order (PO) numbers.
+ **Deployment capability** – After you subscribe to a supported product, guides you from subscription to a running product in your AWS account. It reads the product's deployment requirements, analyzes your AWS environment, generates a tailored deployment plan, and runs it with your approval.

These capabilities operate over a shared working memory and track your evolving needs across interactions.

**Topics**
+ [Using agent mode](#using-agent-mode)
+ [Getting started with agent mode](#getting-started-agent-mode)
+ [Security](#agent-mode-security)
+ [What agent mode can and can't do](#agent-mode-capabilities)
+ [Working with files](#agent-mode-working-with-files)
+ [Get the most out of agent mode](#agent-mode-best-practices)
+ [Use the authenticated experience in agent mode](agent-mode-authenticated-experience.md)
+ [Evaluating seller security and compliance in agent mode](agent-mode-security-compliance.md)

## Using agent mode
<a name="using-agent-mode"></a>

You can use agent mode from multiple locations across the AWS Marketplace website:
+ Home page entry point
+ Agent mode links in the site header
+ Search results when you need deeper evaluation
+ The search bar, when you enter a search phrase and choose agent mode
+ The Ask a question and Run risk assessment options on a product detail page (PDP)

## Getting started with agent mode
<a name="getting-started-agent-mode"></a>

**Topics**
+ [Step 1: Describe your needs](#get-started-agent-mode-describe-needs)
+ [Step 2: Receive recommendations](#get-started-agent-mode-receive-recommendations)
+ [Step 3: Explore and refine](#get-started-agent-mode-explore-refine)
+ [Step 4: Buy or subscribe](#get-started-agent-mode-purchase)
+ [Step 5: Deploy the product](#agent-mode-deploy)

### Step 1: Describe your needs
<a name="get-started-agent-mode-describe-needs"></a>

You start by describing what you're looking for in natural language. You can do the following:
+ Type your requirements directly, or describe a business problem or use case if you don't know which product or service you need.
+ Upload requirement documents as PDF, DOCX, or TXT files up to 1.5 MB.
+ Select from preset tasks, such as comparing specific products.

### Step 2: Receive recommendations
<a name="get-started-agent-mode-receive-recommendations"></a>

Agent mode provides instant recommendations across software, professional services, AI agents and tools, and multi-product solutions, followed by personalized insights. Each recommendation includes evidence that explains how it matches your requirements. As you answer follow-up questions, agent mode captures your requirements and narrows the results. You can act on the initial results at any time or continue refining.

### Step 3: Explore and refine
<a name="get-started-agent-mode-explore-refine"></a>

You can continue the conversation to do one or more of the following:
+ Ask questions about specific products.
+ Request comparisons between options.
+ Modify or add requirements.
+ Explore different evaluation criteria.
+ Review security certifications.
+ Request compliance, security, resilience, and AI governance documents.
+ Assess seller compliance against the CAIQ security framework.

### Step 4: Buy or subscribe
<a name="get-started-agent-mode-purchase"></a>

The purchase begins when you choose **Buy** after a search or comparison, or when you tell agent mode you want to buy a particular product. Agent mode walks you through the following:

1. Sign in to your AWS account.

1. Select an offer from those available to you, including private offers extended to your account.

1. Configure the offer, for example, selecting dimensions and adding a PO number.

1. Review the terms. Agent mode summarizes the EULA and answers questions about it.

1. Subscribe to complete the purchase.

Before you can buy or subscribe, you must sign in. For more information, see [Use the authenticated experience in agent mode](agent-mode-authenticated-experience.md).

Signing in lets agent mode enforce procurement controls your organization has in place, such as Private Marketplace and required purchase orders. If the product or its pricing model isn't supported in agent mode, agent mode redirects you to the standard purchase page. For details, see [Supported offers for purchase](#agent-mode-supported-offers).

#### Supported offers for purchase
<a name="agent-mode-supported-offers"></a>

You can purchase most products in agent mode, including software as a service (SaaS), Amazon Machine Image (AMI), container (including Helm charts and Amazon EKS add-ons), AWS CloudFormation template, SageMaker AI model and algorithm, and professional services products. This includes public offers, private offers, and most free trials.

For the following, agent mode shows a message and links you to a page where you can continue, such as the standard purchase page or the product page:
+ A new subscription to a product you already subscribe to.
+ AWS accounts that buy through a procurement system integration, such as SAP Ariba or Coupa.
+ Offers that include more than one product.
+ AMI, container, and other server-based products with annual pricing (usage pricing combined with a contract term). SaaS offers that combine a contract with usage pricing are supported.
+ SaaS free trials that also include usage-based pricing.
+ SaaS offers priced by AWS Region.
+ Contract offers that include variable payments.
+ Data-as-a-service products and AWS Data Exchange products.
+ Products that don't have an offer available to you. Agent mode links you to the product page.

If your organization requires approval before purchase, you can still configure the offer. When agent mode shows the price, it also shows a notice that approval is required and a link to the purchase page. Subscribe isn't available in agent mode for these offers.

If your organization uses a Private Marketplace and the product isn't approved, agent mode links you to a page where you can request it.

### Step 5: Deploy the product
<a name="agent-mode-deploy"></a>

After you subscribe to a supported product, agent mode automatically routes you to the Deployment capability. The Deployment capability reads the product's requirements, analyzes your AWS environment, and generates a deployment plan tailored to your setup and use case. If you prefer to deploy manually, you can dismiss the Deployment capability at any point and use the existing launch experience.

Deploying requires that you sign in. For more information, see [Use the authenticated experience in agent mode](agent-mode-authenticated-experience.md).

**Supported products for deployment**

The Deployment capability supports more than 100 AMI products, and AWS continues to add support for more products and delivery options. To check a specific product, go to the agent mode page and choose **Launch a product** to see your recent subscriptions with an indication of which ones support agent mode deployment.

#### Step a: Describe your use case
<a name="agent-mode-deploy-describe-use-case"></a>

Start from a recommended option with best-practice defaults, or give more detail about what you're trying to accomplish, such as team size, environment (dev, staging, or production), and Region. For example:
+ "I need a development environment for a three-person team."
+ "I want to run this in production in us-east-1."

#### Step b: Review your deployment plan
<a name="agent-mode-deploy-review-plan"></a>

The Deployment capability reads the product's deployment requirements and analyzes your AWS environment, including existing resources such as VPCs, IAM roles, subnet availability, and instance type constraints. It then generates a plan tailored to your environment and presents it for review before running anything. The plan includes estimated monthly costs.

**Note**  
Agent mode doesn't provision any resources until you approve the plan.  
Agent mode estimates AWS infrastructure costs from On-Demand pricing in the selected AWS Region, excluding taxes and AWS discounts. It estimates AWS Marketplace software usage costs from public pricing, excluding taxes, contract costs, and private offer pricing.

#### Step c: Approve and run
<a name="agent-mode-deploy-approve-execute"></a>

After you approve the configuration, the Deployment capability shows how it plans to run and the required AWS permissions. Choose **Execute** to begin provisioning in your account using AWS CloudFormation. If an error occurs, the Deployment capability surfaces it with a plain-language explanation and a suggested resolution.

#### Step d: Get started with the product
<a name="agent-mode-deploy-get-started"></a>

After deployment completes, the Deployment capability provides a personalized getting-started guide tailored to your configuration. It includes how to access the application, where to find the admin console, and what to configure first.

## Security
<a name="agent-mode-security"></a>

You can discover, compare, and evaluate products in agent mode without signing in. To view pricing and private offers for your account, purchase a product, or deploy it, you sign in to your AWS account, and agent mode acts only within that account's permissions.

When you use agent mode without signing in, agent mode stores all information you upload or enter without access restrictions, and unauthorized users might see it. On shared or public computers, other users who access the same system might see your uploaded information. Do not share confidential data, personally identifiable information (PII), or sensitive business information through this feature. Consider the public nature of any data you submit and make sure it doesn't contain proprietary, financial, or personal information that could cause harm if unauthorized parties access it.

Agent mode shows certification names as the seller entered them in their trust center, so similar certifications can appear with slightly different names. The seller and its trust center provider supply this information, and AWS doesn't verify it.

To request seller evidence, such as SOC 2 reports, or to run a security assessment, you complete a request form. The form asks for contact details, such as your name, business email, and company. Provide personal information only in this form, and enter only what the form asks for. AWS Marketplace shares this information with the seller and its trust center provider to process your request, and their terms and privacy policies apply.

For more information, see [Use the authenticated experience in agent mode](agent-mode-authenticated-experience.md).

## What agent mode can and can't do
<a name="agent-mode-capabilities"></a>

**Agent mode handles**
+ Discovering and evaluating software, professional services, AI agents and tools, and multi-product solutions, including when you start from a business problem or use case.
+ Comparing products and analyzing features.
+ Clarifying and refining requirements.
+ Generating purchase proposals and evaluation reports.
+ Answering questions about AWS Marketplace products.
+ Answering questions about integration and compatibility.
+ Reviewing compliance and assessing security. This includes reviewing SOC 2, ISO 27001, HIPAA, and similar certifications for participating products; comparing products on security and access control, certifications, security controls, and resiliency; and running CAIQ assessments against a seller's evidence or your own uploaded evidence.
+ Subscribing to AWS Marketplace products.
+ Summarizing an offer's EULA and answering questions about it.
+ Configuring an offer, including dimensions and PO numbers.
+ Deploying AWS Marketplace products.
+ Showing private pricing after you sign in.

**Agent mode doesn't handle**
+ Answering out-of-domain questions unrelated to software procurement, such as math problems or weather.
+ Answering questions about competitor cloud platforms.
+ Showing private pricing for products without public pricing.
+ Answering questions about non-AWS Marketplace products.
+ Running assessments against security questionnaires other than the CAIQ.
+ Assessing security and compliance for products whose seller's trust center isn't hosted by a supported third-party provider.
+ Completing a purchase without your confirmation. You always choose **Subscribe** yourself.
+ Changing, upgrading, or canceling an existing subscription.
+ Completing purchases for some offer types. For details, see [Supported offers for purchase](#agent-mode-supported-offers).

## Working with files
<a name="agent-mode-working-with-files"></a>

**Supported file types**
+ PDF documents
+ Microsoft Word documents (DOCX)
+ Plain text files (TXT)

**File size limit**

Up to 1.5 MB per file

**Security processing**

Agent mode processes all uploaded files securely. It does the following:

1. Scans files for malware using Amazon GuardDuty.

1. Validates file format and size.

1. Processes files in isolated environments with comprehensive logging.

1. Applies the same content guardrails as text conversations.

1. Encrypts files in transit and at rest, and automatically deletes them one day after upload.

## Get the most out of agent mode
<a name="agent-mode-best-practices"></a>
+ **Be specific**: Provide details about your use case, organization size, and technical requirements.
+ **Upload context**: Share RFPs or requirement documents to accelerate requirement gathering.
+ **Iterate freely**: Modify requirements and explore different angles without starting over.
+ **Ask follow-ups**: The capabilities adapt to your questions and learn from each interaction.
+ **Use comparisons**: Request side-by-side views when evaluating multiple options.
+ **Generate purchase proposals**: Create shareable artifacts for team collaboration and stakeholder approval.
+ **Refine with AI**: Provide additional instruction to specific sections of AI-generated content.
+ **Sign in when you are ready to buy**: Sign in to see the pricing and private offers available to your account before you make a final decision.