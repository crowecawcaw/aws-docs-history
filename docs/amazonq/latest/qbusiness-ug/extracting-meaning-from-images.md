# Extracting semantic meaning from embedded

visual content with Amazon Q Business

When Amazon Q Business processes your input files from a data source, it uses advanced image
understanding capabilities to extract semantic information and insights from images and
other visuals. For example, it can extract insights from bar charts, technical
illustrations, or hierarchical organizational structures.

By extracting semantic meaning from embedded images, Amazon Q Business makes the visual
information in your data sources queryable. This makes relevant information easier to find,
even if it's conveyed in embedded diagrams or charts. This data provides additional context
and nuance to the information in your data sources and builds a more complete knowledge base
from your enterprise data.

You can enable content extraction when you add or update a data connector, or when you
import a file directly. You can enable it by using the Amazon Q Business console or by using API
operations. Processing documents that contain images and visuals takes more time than
processing text-only documents.

When you enable content extraction for a connector, we recommend that you use incremental
sync mode. If you enable full-sync for your connector, or if you import the same files
individually, Amazon Q Business processes the file and corresponding images again. For more
information about sync modes in Amazon Q Business, see [Sync mode](connector-concepts.md#connector-sync-mode "connector-concepts.md#connector-sync-mode").

Extracting semantic meaning from embedded images and visuals incurs additional costs. For
more information, see [Amazon Q Business
pricing.](https://aws.amazon.com/q/business/pricing/ "https://aws.amazon.com/q/business/pricing/")

When Amazon Q Business processes your input files from a data source, it uses advanced image
understanding capabilities to extract semantic information and insights from images and
other visuals. For example, it can extract insights from bar charts, technical
illustrations, or hierarchical organizational structures. This capability now extends to
images embedded in web pages, in addition to images in documents like PDFs and
presentations.

###### Note

For data sources using web-crawler as the connector, only data sources created after
06/13/2025 will process images both in web-pages and attachments/linked-documents. Data
sources created before 06/13/2025, will continue to process images only in
attachments/linked-documents (pdf, ppt, word). Please reach out to AWS support for
enabling for existing datasources.

###### Topics

- [End user experience](#semantic-meaning-user-experience "#semantic-meaning-user-experience")
- [Guidelines and
  requirements](semantic-meaning-guidelines-and-requirements.md "semantic-meaning-guidelines-and-requirements.md")
- [Extracting content from visuals
  with data connectors](enable-semantic-meanining-data-source.md "enable-semantic-meanining-data-source.md")
- [Extracting semantic meaning from audio and
  video content](Audio-video-extraction.md "Audio-video-extraction.md")
- [Extracting content from visuals
  in a file](enable-semantic-meanining-file-upload.md "enable-semantic-meanining-file-upload.md")
- [Downloading images to add to
  responses (API operations)](semantic-meaning-adding-img-response.md "semantic-meaning-adding-img-response.md")

## End user experience

After Amazon Q Business extracts semantic meaning from images and visuals, your end users can
ask questions and get answers related to the images. When an end user asks a question,
Amazon Q Business retrieves relevant answers from the text and the images. Answers include the
images and links for the documents that contain them.

For example, your user might ask, "Can you walk me through the process of enrolling in
a health plan on the employee benefits site?" Amazon Q Business would then analyze the
company's internal knowledge base, including detailed guides, process documentation, and
screen shots showing the step-by-step enrollment process. It would synthesize this
information into a clear, easy-to-follow response that outlined each stage of the
enrollment journey.
