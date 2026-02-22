# Web Crawler integration

With Web Crawler integration in Amazon Quick, you can create knowledge bases from
website content by crawling and indexing web pages. This integration supports data
ingestion capabilities with different authentication options based on your user tier.

## What you can do

Web Crawler users can ask questions about content stored on websites and web pages.
For example, users can inquire about documentation sites, knowledge bases, or search
for specific information across multiple web pages. The integration enables users to
quickly access and understand information from web content, regardless of location or
type, while providing contextual details such as publication dates, modification
history, and page ownership—all contributing to more efficient information discovery
and better-informed decision making.

###### Note

Web Crawler integration supports data ingestion only. It doesn't provide action
capabilities for managing websites or web services.

## Before you begin

Before you set up Web Crawler integration, make sure you have the following:

- Website URLs to crawl and index.
- Amazon Quick Enterprise subscription
- The website you want to crawl needs to be public and can't be behind a
  firewall or require special browser plugins to connect.

## Prepare website access and authentication

Before setting up the integration in Amazon Quick, prepare your website access credentials. Web Crawler integration supports different authentication methods based on your user role:

**No authentication**

Available for all users. Use for crawling public websites that don't require authentication.

**Basic authentication**

Standard HTTP Basic Authentication for secured websites. HTTP Basic
Authentication is a simple way to protect web resources by requiring a
username and password. When you visit a protected site using Basic
Authentication, your browser will show a pop-up dialog box asking for your
credentials.

**Required credentials:**

- Login page URL - The URL of the login page
- **Username** - Basic auth username
- **Password** - Basic auth password

**Form authentication**

For websites that use HTML form-based login pages.

The formis set up to for you to sepecify XPath. XPath (XML Path Language)
is a query language used to navigate through elements and attributes in an
HTML or XML document. To identify an XPath for a web page element, a user
can utilize their browser's developer tools, typically accessed by
right-clicking on the desired element and selecting "Inspect" or pressing
F12. Once the element is highlighted in the developer tools, the user can
right-click on the corresponding HTML code, select "Copy," and then choose
"Copy XPath" from the submenu. This generates a unique path that identifies
the element's exact location in the document structure. The resulting XPath
might look something like //input[@id='username'] or
//button[@type='submit'], where the double forward slashes (//) indicate the
path can start anywhere in the document, and the square brackets contain
attributes that help identify the specific element.

**Required information:**

- **Login page URL** - URL of the login form (e.g., `https://example.com/login`)
- **Username** - Login username
- **Password** - Login password
- **Username field XPath** - XPath to username input field (e.g., `//input[@id='username']`)
- **Username button XPath** (Optional) - XPath to
  username button field (e.g.,
  `//input[@id='username_button']`)
- **Password field XPath** - XPath to password input field (e.g., `//input[@id='password']`)
- **Password button XPath** - XPath to password button (e.g.,
  `//button[@type='password']`)

**SAML authentication**

For websites that use SAML-based single sign-on authentication.

SAML (Security Assertion Markup Language) authentication is a federated
identity standard that enables single sign-on (SSO) by allowing users to
authenticate through a centralized identity provider rather than entering
credentials directly into each application. Unlike traditional form
authentication where users type their username and password into fields on
the application's login page, SAML redirects users to their organization's
identity provider (like Microsoft Azure AD or Okta) to authenticate, then
passes a secure token back to the application to grant access. This approach
provides a seamless user experience across multiple applications,
centralized user management for IT administrators, and enhanced security
through features like multi-factor authentication, while form authentication
requires separate credential management for each individual
application

**Required information:**

- **Login page URL** - URL of the SAML login page
- **Username** - SAML username
- **Password** - SAML password
- **Username field XPath** - XPath to username
  input field (e.g., `//input[@id='username']`)
- **Username button XPath** (Optional) - XPath to
  username button field (e.g.,
  `//input[@id='username_button']`)
- **Password field XPath** - XPath to password
  input field (e.g., `//input[@id='password']`)
- **Password button XPath** - XPath to password
  button (e.g., `//button[@type='password']`)

### XPath configuration examples

Use these XPath examples to configure form and SAML authentication:

```

Username field examples:
//input[@id='username']
//input[@name='user']
//input[@class='username-field']

Password field examples:
//input[@id='password']
//input[@name='pass']
//input[@type='password']

Submit button examples:
//button[@type='submit']
//input[@type='submit']
//button[contains(text(), 'Login')]

```

## Set up Web Crawler integration

After preparing your website access requirements, create the Web Crawler integration in Amazon Quick.

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **Web Crawler** from the integration options, and
   click the **Add** button (plus "+" button).
3. Choose **Access data from Web Crawler**. Web Crawler integration supports data access only - action execution is not available for web crawling.
4. Configure integration details and authentication method, then create
   knowledge bases as needed.
   1. Select the authentication type for your web crawler
      integration.
   2. Fill in the required details based on your selected
      authentication method.
   3. Select **Create and continue**.
   4. Fill in the Name and description for your knowledge
      base.
   5. Add the content URLs you want to crawl.
   6. Select **Create**.

After clicking create, the data sync is started automatically.

## Configure crawling

You can configure which websites and pages to crawl and how to filter the content.

### Configure URLs and content sources

Configure which websites and pages to crawl:

#### Direct URLs

Specify individual URLs to crawl:

```

https://example.com/docs
https://example.com/blog
https://example.com/support

```

**Limit:** Maximum 10 URLs per dataset

### Content filters and crawl settings

#### Crawl scope settings

To view these settings, you must first set up a knowledge base and then examine the advanced settings option.

**Crawl depth**

- Range: 0-10 (default: 1)
- 0 = crawl only specified URLs
- 1 = include linked pages one level deep
- Higher values follow links deeper into the site

**Maximum links per page**

- Default: 1000
- Maximum: 1,000
- Controls how many links to follow from each page

**Wait time**

- Default: 1
- The amount of time the web crawler will wait for each page
  after the page reaches "page ready" state. This is useful for pages that have dynamic javascript load characteristics where the page has content
  blocks that loads after the main template is loaded.Increase wait time if
  you have visually rich content or anticipate high load
  times.

## Manage knowledge bases

After setting up your Web Crawler integration, you can create and manage knowledge bases from your crawled website content.

### Edit existing knowledge bases

You can modify your existing Web Crawler knowledge bases:

1. In the Amazon Quick console, choose **Knowledge bases**.
2. Select your Web Crawler knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then choose **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same Web Crawler integration:

1. In the Amazon Quick console, choose **Integrations**, and then select the **Data** tab.
2. Choose your existing Web Crawler integration from the list.
3. Choose the three-dot icon under **Actions**, then choose **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

### Attachments and file crawling

Control whether the system processes files and attachments linked from web
pages:

- Enable file attachment crawling - Select this option to crawl and index
  files and attachments found on web pages, such as PDFs, documents, and media
  files.

### Crawling behavior and sync configuration

Your Web Crawler integration follows these crawling practices:

- **Incremental sync model:** First sync performs full crawl, subsequent syncs capture changes only
- **Automatic retry:** Built-in retry logic for failed requests
- **Duplicate handling:** Automatic detection and handling of
  URLs
- **Crawler identification:** Identifies itself with user-agent string "aws-quick-on-behalf-of-<UUID>" in request headers

#### Robots.txt compliance

Web Crawler respects the robots.txt protocol and honors user-agent and allow/disallow directives. This enables you to control how the crawler accesses your site.

##### How robots.txt checking works

- **Host-level checking:** Web Crawler reads robots.txt files at the host level (for example, example.com/robots.txt)
- **Multiple host support:** For domains with multiple hosts, Web Crawler honors robots rules for each host separately
- **Fallback behavior:** If Web Crawler cannot fetch robots.txt due to blocking, parsing errors, or timeouts, it will behave as if robots.txt does not exist and will crawl the site

##### Supported robots.txt fields

Web Crawler recognizes these robots.txt fields (field names are case-insensitive, values are case-sensitive):

`user-agent`
Identifies which crawler the rules apply to

`allow`
A URL path that may be crawled

`disallow`
A URL path that may not be crawled

`sitemap`
The complete URL of a sitemap

`crawl-delay`
Specified amount of time (in seconds) to wait between requests to your website

#### Meta tag support

Web Crawler supports page-level robots meta tags that you can use to control how your data is used. You can specify page-level settings by including a meta tag on HTML pages or in an HTTP header.

##### Supported meta tags

`noindex`
Do not index the page. If you don't specify this rule, the page may be indexed and eligible to appear in experiences

`nofollow`
Do not follow the links on this page. If you don't specify this rule, Web Crawler may use the links on the page to discover those linked pages

You can combine multiple values using a comma (for example, "noindex, nofollow").

###### Note

To detect meta tags, Web Crawler needs to access your page, so do not block your page with robots.txt which will prevent it from being recrawled.

## Troubleshooting

Use this section to resolve common issues with Web Crawler integration.

### Authentication failures

**Symptoms:**

- "Unable to authenticate" error messages
- 401/403 HTTP responses
- Login page redirect loops
- Session timeout errors

**Resolution steps:**

1. Verify the site is reachable from the AWS region the Amazon Quick instance is setu
2. Verify credentials accuracy and ensure they haven't expired
3. Check authentication endpoint availability and accessibility
4. Validate XPath configurations by testing them in browser developer tools
5. Review browser network logs to understand the authentication flow
6. Ensure login page URL is correct and accessible
7. Test authentication manually using the same credentials

### Access and connectivity issues

**Symptoms:**

- Connection timeouts and network errors
- Network unreachable errors
- DNS resolution failures

**Resolution steps:**

1. Verify network connectivity to target websites
2. Validate site accessibility:
   - Check DNS resolution for target domains
   - Verify SSL/TLS configuration and certificates
   - Test access from different networks if possible

### Crawl and content issues

**Symptoms:**

- Missing or incomplete content
- Incomplete crawls or early termination
- Rate limiting errors (429 responses)
- Content not being indexed properly

**Resolution steps:**

1. Review robots.txt restrictions:
   - Check robots.txt file for crawl restrictions
   - Verify crawler is allowed to access target paths
   - Ensure robots.txt compliance isn't blocking content

2. Check rate limiting and throttling:
   - Monitor response headers for rate limit information
   - Implement appropriate crawl delays

3. Verify URL patterns and filters:
   - Test regex patterns for accuracy
   - Check URL formatting and structure
   - Validate include/exclude pattern logic

4. Review content restrictions:
   - Check for noindex meta tags on pages
   - Verify content type support
   - Ensure content size is within limits

5. Update the Wait time to an appropriate value so the content loads on the page before the cralwer tries crawling

### Known limitations

Web Crawler integration has the following limitations:

- **URL limits:** Maximum of 10 URLs, sitemap not supported
- **Crawl depth:** Maximum crawl depth of 10 levels
- **Security requirements:** HTTPS required for web proxy configurations
