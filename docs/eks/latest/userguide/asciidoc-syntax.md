

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# AsciiDoc syntax reference
<a name="asciidoc-syntax"></a>

AsciiDoc is the preferred markup language for AWS documentation. While the tooling has partial support for Markdown syntax (such as headings and lists), we recommend using AsciiDoc syntax for all content to ensure consistency and proper rendering.

This guide covers common syntax elements you’ll need when contributing to Amazon EKS documentation. For more advanced syntax and detailed information, refer to the [AsciiDoc documentation](https://docs.asciidoctor.org/asciidoc/latest/).

## New page
<a name="_new_page"></a>

Every new AsciiDoc document should begin with the structure defined in [Create a new page](create-page.md).

## Headings
<a name="_headings"></a>

Use headings to organize your content hierarchically:

```
= Page/topic title (level 1)
== Section title (level 2)
=== Level 3 heading
==== Level 4 heading
===== Level 5 heading
====== Level 6 heading
```

Note: Always use sentence case for headings in AWS documentation.

## Text formatting
<a name="_text_formatting"></a>

Format text to emphasize important information:

```
Use *bold text* for UI labels.
Use _italic text_ for introducing terms or light emphasis.
Use `monospace text` for code, file names, and commands.
```

## Lists
<a name="_lists"></a>

### Unordered lists
<a name="_unordered_lists"></a>

Create bulleted lists for items without a specific sequence:

```
* First item
* Second item
** Nested item
** Another nested item
* Third item
```

### Ordered lists
<a name="_ordered_lists"></a>

Create numbered lists for sequential steps or prioritized items:

```
. First step
. Second step
.. Substep 1
.. Substep 2
. Third step
```

## Links
<a name="_links"></a>

See [Insert a link](insert-link.md) for details on how to properly format links. Markdown-style links are not supported.

## Code examples
<a name="_code_examples"></a>

### Inline code
<a name="_inline_code"></a>

Use backticks for inline code:

```
Use the `kubectl get pods` command to list all pods.
```

### Code blocks
<a name="_code_blocks"></a>

Create code blocks with syntax highlighting and support for attributes (similar to entities):

```
 [source,python,subs="verbatim,attributes"]
 ----
 def hello_world():
     print("Hello, World!")
 ----
```

## Images
<a name="_images"></a>

Insert images with alt text for accessibility:

```
image::images/image-file.png[Alt text description]
```

## Tables
<a name="_tables"></a>

Create tables to organize information:

```
[%header,cols="2"]
|===
|Header 1
|Header 2

|Cell 1,1
|Cell 1,2

|Cell 2,1
|Cell 2,2
|===
```

For more complex tables, see the [AsciiDoc table documentation](https://docs.asciidoctor.org/asciidoc/latest/tables/build-a-basic-table/).

## Callouts
<a name="_callouts"></a>

Use callouts to highlight important information and admonitions:

```
NOTE: This is a note callout for general information.

TIP: This is a tip callout for helpful advice.

IMPORTANT: This is an important callout for critical information.
```

Preview:

**Note**  
This is a note callout.

## Including other files
<a name="_including_other_files"></a>

Include content from other files:

```
 include::filename.adoc[]
```

## Attributes (similar to entities)
<a name="_attributes_similar_to_entities"></a>

Use predefined attributes to maintain consistency. In particular, you MUST use attributes for AWS and ` arn:aws: `.

```
{aws} provides Amazon EKS as a managed Kubernetes service.
```

```
 [source,bash,subs="verbatim,attributes"]
 ----
 aws iam attach-role-policy \
     --role-name AmazonEKSAutoClusterRole \
     --policy-arn {arn-aws}iam::aws:policy/AmazonEKSClusterPolicy
 ----
```

For a list of attributes, look in the `../attributes.txt` file.

## Procedures
<a name="_procedures"></a>

Format step-by-step procedures:

```
To create an Amazon EKS cluster, do the following steps.

. Sign in to the {aws} Management Console.
. Open the Amazon EKS console.
. Choose *Create cluster*.

...
```