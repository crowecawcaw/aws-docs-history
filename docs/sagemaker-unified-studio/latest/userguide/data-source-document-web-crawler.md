# Use a web crawler as a data source

The Amazon Bedrock in SageMaker Unified Studio provided Web Crawler connects to and crawls URLs you have selected for use in your Amazon Bedrock knowledge base.
You can crawl website pages in accordance with your set scope or limits for your selected URLs.

The web brawler connects to and crawls HTML pages starting from the seed URL, traversing all child links under the same
top primary domain and path. If any of the HTML pages reference supported documents, the Web Crawler will
fetch these documents, regardless of if they are within the same top primary domain.

The web crawler lets you:

- Select multiple URLs to crawl
- Respect standard `robots.txt` directives like 'Allow' and 'Disallow'
- Limit the scope of the URLs to crawl and optionally exclude URLs that match a filter pattern
- Limit the rate of crawling URLs
  There are limits to how many web page content items and MB per content item that Amazon Bedrock in SageMaker Unified Studio can
  crawl. See [Quotas
  for knowledge bases](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md"). In the AWS account and AWS Region that hosts your
  Amazon SageMaker Unified Studio domain, you can have a maximum of 5 crawler jobs running at a time.

###### Topics

- [Web crawler behavior](#data-source-document-web-crawler-behavior "#data-source-document-web-crawler-behavior")
- [Create a knowledge base with a web crawler](#data-source-document-web-crawler-procedure "#data-source-document-web-crawler-procedure")

## Web crawler behavior

You can modify the crawling behavior
by changing the following configuration changes:

### Source URLs

You specify the source URLs that you want the Knowledge Base to crawl. Before you
add a source URL, check the following.

- Check that you are authorized to crawl your source URLs.
- Check the path to robots.txt corresponding to your source URLs doesn't
  block the URLs from being crawled. The web crawler adheres to the standards of
  robots.txt: `disallow` by default if robots.txt is not found
  for the website. The web crawler respects robots.txt in accordance with the
  [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html "https://www.rfc-editor.org/rfc/rfc9309.html").
- Check if your source URL pages are JavaScript dynamically generated,
  as crawling dynamically generated content is currently not supported.
  You can check this by entering this in your browser:
  `view-source:https://examplesite.com/site/`.
  If the `body` element contains only a `div` element
  and few or no `a href` elements, then the page is likely
  generated dynamically. You can disable JavaScript in your browser, reload
  the web page, and observe whether content is rendered properly and contains
  links to your web pages of interest.

###### Important

When selecting websites to crawl, you must adhere to the
[Amazon Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/")
and all other Amazon terms. Remember that you must only use the web crawler to
index your own web pages, or web pages that you have authorization to crawl.

Make sure you are not crawling potentially excessive web pages. We recommend that you don't
crawl large websites, such as wikipedia.org, without filters or scope limits. Crawling
large websites will take a very long time to crawl.

[Supported file types](../../../bedrock/latest/userguide/knowledge-base-ds.md "../../../bedrock/latest/userguide/knowledge-base-ds.md") are crawled regardless of scope and if there's
no exclusion pattern for the file type.

### Website domain range for crawling URLs

You can limit the scope of the URLs to crawl based on each page URL's specific relationship to the
seed URLs. For faster crawls, you can limit URLs to those with the same host and initial URL path
of the seed URL. For more broader crawls, you can choose to crawl URLs with the same host or
within any subdomain of the seed URL.

You can choose from the following options.

- Default: Limit crawling to web pages that belong to the same host and with the
  same initial URL path. For example, with a seed URL of
  "https://aws.amazon.com/bedrock/" then only this path and web pages that extend
  from this path will be crawled, like "https://aws.amazon.com/bedrock/agents/".
  Sibling URLs like "https://aws.amazon.com/ec2/" are not crawled, for example.
- Host only: Limit crawling to web pages that belong to the same host. For example, with a
  seed URL of "https://aws.amazon.com/bedrock/", then web pages with
  "https://aws.amazon.com" will also be crawled, like
  "https://aws.amazon.com/ec2".
- Subdomains: Include crawling of any web page that has the same primary domain as
  the seed URL. For example, with a seed URL of
  "https://aws.amazon.com/bedrock/" then any web page that
  contains "amazon.com" (subdomain) will be crawled, like "https://www.amazon.com".

###### Note

Make sure you are not crawling potentially excessive web pages. It's not recommended to
crawl large websites, such as wikipedia.org, without filters or scope limits. Crawling
large websites will take a very long time to crawl.

[Supported file types](../../../bedrock/latest/userguide/knowledge-base-ds.md "../../../bedrock/latest/userguide/knowledge-base-ds.md") are crawled regardless of scope and if there's
no exclusion pattern for the file type.

### Use a URL regex filter to include or exclude URLs

You can include or exclude certain URLs in accordance with your scope.
[Supported file types](../../../bedrock/latest/userguide/knowledge-base-ds.md "../../../bedrock/latest/userguide/knowledge-base-ds.md") are crawled regardless of scope and if there's
no exclusion pattern for the file type. If you specify an inclusion and exclusion
filter and both match a URL, the exclusion filter takes precedence and the
web content isn’t crawled.

###### Important

Problematic regular expression pattern filters that lead to [catastrophic backtracking](../../../codeguru/detector-library/python/catastrophic-backtracking-regex.md "../../../codeguru/detector-library/python/catastrophic-backtracking-regex.md")
and look ahead are rejected.

An example of a regular expression filter pattern to exclude URLs that end with ".pdf" or PDF
web page attachments: `.*\.pdf$`

### Throttle crawling speed

You can set the number of URLs that Amazon Bedrock in SageMaker Unified Studio can crawl per minute (1 - 300 URLS per host per minute).
Higher values decrease synchronization time but increase the load on the host.

### Incremental syncing

Each time the the web crawler runs, it retrieves content for all URLs that are reachable
from the source URLs and which match the scope and filters. For incremental syncs after the
first sync of all content, Amazon Bedrock will update your knowledge base with new and modified content,
and will remove old content that is no longer present. Occasionally, the crawler may not be able
to tell if content was removed from the website; and in this case it will err on the side of
preserving old content in your knowledge base.

To sync your data source with your knowledge base, see [Synchronize an Amazon Bedrock Knowledge Base](kb-sync.md "kb-sync.md").

## Create a knowledge base with a web crawler

###### To create a Knowledge Base with a web crawler

1.  Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2.  Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3.  Choose the **Build** menu at the top of the page.
4.  In the **MACHINE LEARNING & GENERATIVE AI** section, choose
    **My apps**.
5.  In the **Select or create a new project to continue** dialog box, select the project that you want to use.
6.  In the left pane, choose **Asset gallery**.
7.  Choose **My components**.
8.  In the **Components** section, choose **Create
    component** and then **Knowledge Base**. The **Create
    Knowledge Base** pane is shown.
9.  For **Name**, enter a name for the Knowledge Base.
10. For **Description**, enter a description for the Knowledge
    Base.
11. In **Select data source type**, do one of the following:
    - Use a document as a data source by doing the following:

          1. Select **Local file**.
          2. Choose **Click to upload** and upload the document that you want the
           Knowledge Base to use. Alternatively, add your source documents by dragging and dropping
           the document from your computer.

      For more information, see [Use a Local file as a data source](data-source-document.md "data-source-document.md").

    - Use a web crawler as a data source by doing the following:
      1. Select **Web crawler**.
      2. Provide the **Source URLs** of the URLs you want to crawl. You can
         add up to 9 additional URLs by selecting **Add Source URLs**. By
         providing a source URL, you are confirming that you are authorized to crawl its
         domain.
      3. (Optional) Choose **Edit advanced web crawler configs** to make the
         following optional configuration changes:
         - **Website domain range**. Set the domain that you want the
           Knowledge Base to crawl. For more information, see [Website domain range for crawling URLs](#ds-sync-scope "#ds-sync-scope").
         - **Maximum throttling of crawling speed**. Set the speed at which
           the Knowledge Base crawls through the source URLs. For more information, see [Throttle crawling speed](#ds-throttle-crawling "#ds-throttle-crawling").
         - **URL regex filter**. Set regex filters for including
           (**Include patterns**) or excluding **Exclude
           patterns** URLS from the web crawl. For more information, see [Use a URL regex filter to include or exclude URLs](#ds-inclusion-exclusion "#ds-inclusion-exclusion").
         - Choose **Back** to leave the web crawler configuration pane.

12. For **parsing** Choose either **default** parsing or
    choose **parsing with foundation model**.
13. If you choose **parsing with foundation model**, do the following:
    1. For **Choose a foundation model for parsing** select your preferred
       foundation model. You can only choose models that your administrator has enabled for
       parsing. If you don't see a suitable model, contact your administrator.
    2. (Optional) Overwrite the **Instructions for the parser** to suit your
       specific needs.

14. (Optional) For **Embeddings model**, choose a model for converting your
    data into vector embeddings, or use the default model.
15. Choose **Create** to create the Knowledge Base.
16. Use the Knowledge Base in an app, by doing one of the following:
    - If your app is a chat agent app, do [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md").
    - If your app is a flow app, do [Add a Knowledge Base component to a flow app](add-kb-component-prompt-flow-app.md "add-kb-component-prompt-flow-app.md").
