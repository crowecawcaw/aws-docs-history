**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a new page

Learn how to create a new documentation page. This topic includes instructions for creating the initial page metadata and adding the page to the guide table of contents.

## Create page

1. Navigate to the chapter directory. For example, if you want to create a new page in the "Security" section, navigate to the `latest/ug/security` directory.
2. Determine the page ID. By convention, the page ID is all lowercase and segmented with `-`. The ID of this page is `create-page`.
3. Create a new file with the page ID and the `adoc` extension. For example, `create-page.adoc`.
4. Insert the page metadata using this template:

```
 include::../attributes.txt[]

 [.topic]
 [#unique-page-id]
 = Page title
 :info_titleabbrev: Short title

 [abstract]
 --
 Brief summary of the page's content.
 --

 Introduction paragraph goes here.
```

## Add page to navigation

1. Navigate to the parent page. The parent page of top level sections is `book.adoc`.
2. At the bottom of the parent page, include the child page.

`include::${filename}[leveloffset=+1]`

_For example:_

`include::create-page.adoc[leveloffset=+1]`
