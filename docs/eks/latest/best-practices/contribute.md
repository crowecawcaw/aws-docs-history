

# Contribute to this guide
<a name="contribute"></a>

Anyone can contribute to the best practices guide. The EKS Best Practices Guide is written in the AsciiDoc format on GitHub.

## Summary for existing contributors
<a name="_summary_for_existing_contributors"></a>
+ Open the [`bpg-docs.code-workspace`](https://github.com/aws/aws-eks-best-practices/blob/master/bpg-docs.code-workspace) with VS Code to automatically install the AsciiDoc extension.
  + Learn more about the [AsciiDoc Extension](https://marketplace.visualstudio.com/items?itemName=asciidoctor.asciidoctor-vscode) on the Visual Studio Marketplace.
+ The source files for the AWS Docs website are stored in [`latest/bpg`](https://github.com/aws/aws-eks-best-practices/tree/master/latest/bpg) 
+ The syntax is highly similar to markdown.
  + Review the [Syntax Reference](https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/) in the AsciiDoctor docs.
+ The docs platform only deploys `latest/bpg/images`. Each of the guide sections has a symbolic link back to this directory. For example, `latest/bpg/networking/images` points to `latest/bpg/images`.

## Setup a local editing environment
<a name="_setup_a_local_editing_environment"></a>

If you plan to edit the guide frequently, setup a local editing environment.

### Fork and clone the repo
<a name="_fork_and_clone_the_repo"></a>

You need to be familiar with `git`, `github`, and text editors. For information on getting started with `git` and `github`, see [Getting started with your GitHub account](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account) in the GitHub docs.

1. View the [EKS Best Practices Guide on GitHub](https://github.com/aws/aws-eks-best-practices).

1. Create a fork of the project repo. Learn how to [fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) in the GitHub docs.

1. Clone your fork of the project repo. Learn how to [clone your forked repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository).

### Open the VS Code Workspace
<a name="_open_the_vs_code_workspace"></a>

AWS recommends using Visual Studio Code from Microsoft to edit the guide. For more information about VS Code, see [Download Visual Studio Code](https://code.visualstudio.com/download) and [Get started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started) in the Visual Studio Code Documentation.

1. Open VS Code.

1. Open the `bpg-docs.code-workspace` file from the cloned repo.

1. If this is your first time opening this workspace, accept the prompt to install the AsciiDoc extension. This extension checks the syntax of AsciiDoc files and generates a live preview.

1. Browse to the `latest/bpg` directory. This directory holds the source files that deploy to the AWS documentation site. The source files are organized by guide section, such as "security" or "networking".

### Edit a file
<a name="_edit_a_file"></a>

1. Open a file in the editor.
   + View the AsciiDoc Syntax to learn how to create headings, links, and lists.
   + You can use Markdown syntax to format text, create lists, and headings. You cannot use Markdown syntax to create links.

1. Open a live preview of the page.
   + First, press `ctrl-k` or `cmd-k` (depending on keyboard). Second, press `v`. This opens a preview in split view.

AWS suggests using feature branches to organize your changes. Learn how to create branches with git.

### Submit a Pull Request
<a name="_submit_a_pull_request"></a>

You can create a pull request from the GitHub website or the GitHub cli.

Learn how to [create a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) by using the GitHub Website.

Learn how to [create a pull request](https://cli.github.com/manual/gh_pr_create) by using the GitHub cli.

## Use the github.dev web-based editor
<a name="_use_the_github_dev_web_based_editor"></a>

The `github.dev` web-based editor is based on VS Code. This is a great way to edit multiple files and preview content without any setup.

It has support for the AsciiDoc extension. You can do git operations by using the GUI. The web-based editor does not have a shell or terminal for running commands.

You must have a GitHub account. You will be prompted to login if required.

 [🚀 Launch the GitHub web-based editor.](https://github.dev/aws/aws-eks-best-practices/blob/master/bpg-docs.code-workspace?workspace=true) 

## Edit a single page
<a name="_edit_a_single_page"></a>

You can rapidly update individual pages by using GitHub. Each page contains an "📝 Edit this page on GitHub" link at the bottom.

1. Navigate to the page in this guide you want to edit

1. Click the "Edit this page on GitHub" link at the bottom

1. Click the edit pencil icon on the top right of the GitHub file viewer, or press `e` 

1. Edit the file

1. Submit your changes using the "Commit changes…​" button. This button creates a GitHub pull request. The guide maintainers will review this pull request. A reviewer will approve the pull request, or request changes.

## View and set the ID for a page
<a name="_view_and_set_the_id_for_a_page"></a>

This page explains how to view and set page ID.

The page ID is a unique string that identifies each page on the documentation site. You can view the page ID in the address bar of your browser when you’re on a specific page. The page ID is used for the URL, the filename, and to create cross-reference links.

For example, if you’re viewing this page, the URL in your browser’s address bar will look similar to:

```
https://docs.aws.amazon.com/view-set-page-id.html
```

The last part of the URL (`view-set-page-id`) is the page ID.

### Set the page ID
<a name="_set_the_page_id"></a>

When creating a new page, you need to set the page ID in the source file. The page ID should be a concise, hyphenated string that describes the page content.

1. Open the source file for your new page in a text editor.

1. At the top of the file, add the following line. It should be above the first heading.

   ```
   [#my-new-page]
   ```

   Replace `my-new-page` with the page ID for your new page.

1. Save the file.

**Note**  
Page IDs must be unique across the entire documentation site. If you try to use an existing page ID, you’ll get a build error.

## Create a new page
<a name="_create_a_new_page"></a>

Learn how create a new page and update the guide table of contents.

### Create page metadata
<a name="_create_page_metadata"></a>

1. Determine the page title, and page short title. The page short title is optional, but recommended if the page title is more than a few words.

1. Determine the ID of the page. This must be unique within the EKS Best Practices Guide. The convention is to use all lowercase, and separate words with `-`.

1. Create a new asciidoc file, in a folder if needed, and add the following text to the file:  
**Example**  

   [."topic"] [\#<page-id>] = <page-title> :info\_titleabbrev: <page-short-title>

   For example,  
**Example**  

   [."topic"] [\#scalability] = EKS Scalability best practices :info\_titleabbrev: Scalability

### Add to table of contents
<a name="_add_to_table_of_contents"></a>

1. Open the file for the parent page in the table of contents. For new top level guide sections, the parent file is `book.adoc`.

1. At the bottom of the parent file, update and insert the following directive:  
**Example**  

   include::<new-filename>[leveloffset=\+1]

   For Example,  
**Example**  

   include::dataplane.adoc[leveloffset=\+1]

## Insert an image
<a name="_insert_an_image"></a>

1. Find the image prefix for the page you are editing. Review the `:imagesdir:` property in the heading of the file. For examples, ``:imagesdir: images/reliability/` 

1. Place your image in this path, such as `latest/bpg/images/reliability` 

1. Determine appropriate alt-text for you image. Write a short high-level description of the image. For example, "diagram of VPC with three availability zones" is appropriate alt-text.

1. Update the following example with the alt-text and image filename. Insert at the desired location.  
**Example**  

   image::<image-filename>[<image-alt-text>]

   For example,  
**Example**  

   image::eks-data-plane-connectivity.jpeg[Network diagram]

## Check style with Vale
<a name="_check_style_with_vale"></a>

1.  [Install the Vale CLI.](https://vale.sh/docs/vale-cli/installation/) 

1. Run `vale sync` 

1. Install the [Vale Extension](https://marketplace.visualstudio.com/items?itemName=ChrisChinchilla.vale-vscode) from the Visual Studio Marketplace.

1. Restart VS Code, and open an AsciiDoc file

1. VS Code underlines problematic text. Learn how to work with [Errors and Warnings](https://code.visualstudio.com/docs/editor/editingevolved#_errors-warnings) in the VS Code docs.

## Build a local preview
<a name="_build_a_local_preview"></a>

1. Install the `asciidoctor` tool using `brew` on Linux or MacOS
   + Learn how to [install asciidoctor cli](https://docs.asciidoctor.org/asciidoctor/latest/install/) in the AsciiDoctor docs.
   + Learn how [install the brew package manager](https://brew.sh/index.html).

1. Open a terminal, and navigate to `latest/bpg/` 

1. Run `asciidoctor book.adoc` 
   + Review any syntax warnings and errors

1. Open the `book.html` output file.
   + On MacOS, you can run `open book.html` to open the preview in your default browser.

## AsciiDoc Cheat Sheet
<a name="_asciidoc_cheat_sheet"></a>

### Basic Formatting
<a name="_basic_formatting"></a>

```
*bold text*
_italic text_
`monospace text`
```

### Headers
<a name="_headers"></a>

```
= Document Title (Header 1)
== Header 2
=== Header 3
==== Header 4
===== Header 5
====== Header 6
```

### Lists
<a name="_lists"></a>

Unordered Lists:

```
- Item 1
- Item 2
-- Subitem 2.1
-- Subitem 2.2
- Item 3
```

Ordered Lists:

```
. First item
. Second item
.. Subitem 2.1
.. Subitem 2.2
. Third item
```

### Links
<a name="_links"></a>

```
External link:  https://example.com[Link text]
Internal link: <<page-id>>
Internal link: xref:page-id[Link text]
```

### Images
<a name="_images"></a>

```
image::image-file.jpg[Alt text]
```

### Code Blocks
<a name="_code_blocks"></a>

```
 [source,python]
 ----
 def hello_world():
     print("Hello, World!")
 ----
```

### Tables
<a name="_tables"></a>

 [Learn how to build a basic table.](https://docs.asciidoctor.org/asciidoc/latest/tables/build-a-basic-table/) 

```
[cols="1,1"]
|===
|Cell in column 1, row 1
|Cell in column 2, row 1

|Cell in column 1, row 2
|Cell in column 2, row 2

|Cell in column 1, row 3
|Cell in column 2, row 3
|===
```

### Admonitions
<a name="_admonitions"></a>

```
NOTE: This is a note admonition.

WARNING: This is a warning admonition.

TIP: This is a tip admonition.

IMPORTANT: This is an important admonition.

CAUTION: This is a caution admonition.
```

Preview:

**Note**  
This is a note admonition.

### Includes
<a name="_includes"></a>

```
 include::filename.adoc[]
```