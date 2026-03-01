# Configuring a `robots.txt` file for Amazon Q Business Web Crawler

The `robots.txt` file is a standard used to implement the Robots Exclusion
Protocol, allowing website owners to specify which parts of their site visiting web
crawlers and robots can access. Amazon Q Business Web Crawler adheres to the rules
set in your website’s `robots.txt` file, which determines the areas it is
allowed or not allowed to visit. Amazon Q Business Web Crawler respects standard
robots.txt directives like `Allow` and `Disallow`. To control how
Amazon Q Business Web Crawler interacts with your website, you can simply
adjust these rules in your robots.txt file.

###### Topics

- [Configuring how Amazon Q Web Crawler accesses your website](#configure-web-crawler-website-access "#configure-web-crawler-website-access")
- [Stopping Amazon Q Web Crawler from crawling your website](#stop-web-crawler-access "#stop-web-crawler-access")

## Configuring how Amazon Q Web Crawler accesses your website

You can control how the Amazon Q Web Crawler indexes your website using
`Allow` and `Disallow` directives. You can also control
which web pages are indexed and which web pages are not crawled.

**To allow Amazon Q Web Crawler to crawl all web
pages except disallowed web pages, use the following
directive:**

```
User-agent: amazon-QBusiness    # Amazon Q Web Crawler
Disallow: /credential-pages/ # disallow access to specific pages
```

**To allow Amazon Q Web Crawler to crawl only
specific web pages, use the following directive:**

```
User-agent: amazon-QBusiness   # Amazon Q Web Crawler
Allow: /pages/ # allow access to specific pages
```

**To allow Amazon Q Web Crawler to crawl all
website content and disallow crawling for any other robots, use the following
directive:**

```
User-agent: amazon-QBusiness # Amazon Q Web Crawler
Allow: / # allow access to all pages
User-agent: * # any (other) robot
Disallow: / # disallow access to any pages
```

## Stopping Amazon Q Web Crawler from crawling your website

You can stop Amazon Q Web Crawler from indexing your website using the
`Disallow` directive. You can also control which web pages are
crawled and which aren't.

**To stop Amazon Q Web Crawler from crawling the
website, use the following directive:**

```
User-agent: amazon-QBusiness # Amazon Q Web Crawler
Disallow: / # disallow access to any pages
```

If you have any questions or concerns about Amazon Q Web Crawler, you
can reach out to the [AWS support team](https://aws.amazon.com/contact-us/?nc1=f_m "https://aws.amazon.com/contact-us/?nc1=f_m").
