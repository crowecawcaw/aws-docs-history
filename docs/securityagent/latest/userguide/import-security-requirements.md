

# Generate security requirements from documents
<a name="import-security-requirements"></a>

Generate the security requirements for a custom pack by uploading your existing security documentation. AWS Security Agent reads the documents you upload, identifies the security-relevant content, and generates structured security requirements with applicability, compliance criteria, and remediation guidance. You can review and edit the generated requirements before they are used in reviews.

Use this instead of writing each requirement by hand when you already have security policies, standards, or guidelines documented. For guidance on what to include in the documents you upload, see [Prepare documents for requirement generation](prepare-import-documents.md).

## Supported file formats
<a name="_supported_file_formats"></a>

You can upload the following file formats:
+ DOC
+ DOCX
+ MD
+ PDF
+ TXT

## Generate requirements
<a name="_generate_requirements"></a>

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab.

1. Create a pack, or choose an existing custom pack to generate requirements for.

1. Choose **Choose files**, or drag and drop your documents into the upload area.

1. Choose **Generate requirements**.

1. Wait for AWS Security Agent to process the documents. Generation runs in the background and can take a couple of minutes for large files. You cannot start another upload for the pack while generation is in progress.

1. Review the generated security requirements. Edit, delete, or add requirements as needed. Enable the pack when you want AWS Security Agent to evaluate its requirements during security reviews.

**Note**  
 AWS Security Agent generates requirements at the workload level and focuses on the security-relevant content in your documents. The number of requirements it generates depends on the content you provide. Review the generated requirements to confirm they reflect your intent.

## Replace requirements with a new upload
<a name="_replace_requirements_with_a_new_upload"></a>

Uploading new source documents regenerates the requirements for a pack.

**Important**  
When you upload new source documents to a pack, AWS Security Agent regenerates all requirements for that pack. Any existing requirements, including ones you added manually, are replaced. To keep your current requirements, do not upload new documents.

1. In the AWS console, navigate to AWS Security Agent.

1. In the navigation pane, choose **Security requirements**.

1. Choose the **Custom security requirements packs** tab, and then choose the pack.

1. Start a new upload, and acknowledge that uploading new source documents replaces the existing requirements.

1. Choose your files, and then choose **Generate requirements**.

## Next steps
<a name="_next_steps"></a>
+ Review and enable the generated requirements. See [Manage security requirements](security-requirements.md).
+ Create a design review or code review to evaluate your application against the pack.