

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create docs content with Amazon Q
<a name="create-content-q"></a>

You can use Amazon Q to create and revise docs content. This is an easy way to get started on a new page. Amazon Q is available as an extension to Visual Studio (VS) Code.

In the following image, Amazon Q generated the lines marked with green.

![Amazon Q in VS Code](http://docs.aws.amazon.com/eks/latest/userguide/images/contribute-q.png)


## Install Amazon Q with VS Code
<a name="_install_amazon_q_with_vs_code"></a>

1. Open VS Code.

1. Go to the Extensions view (Ctrl\+Shift\+X or Cmd\+Shift\+X).

1. Search for "Amazon Q".

1. Choose Install on the Amazon Q extension.

1. Wait for installation to complete.

1. Restart VS Code when prompted.

## Log in to Amazon Q
<a name="_log_in_to_amazon_q"></a>

1. After installing, choose the Amazon Q icon in the VS Code activity bar.

1. Choose **Sign in to Amazon Q**.

1. Enter your AWS credentials when prompted.

1. After you authenticate, the Amazon Q chat interface appears.

## Use Amazon Q to create content
<a name="_use_amazon_q_to_create_content"></a>

1. Open the file you want to edit in VS Code.

1. Select the text you want to revise or the location for new content.

1. Press **Ctrl\+I** or **Cmd\+I**.

1. In the prompt, be specific about:
   + The type of content you need.
   + The target audience.
   + Key points to cover.
   + Desired tone and style.

1. Review the generated content in the inline preview.

1. Use **enter** to accept the changes, or **esc** to reject them.

1. Edit further as needed.

## Tips
<a name="_tips"></a>
+ Start with a simple request and iterate to get the content you want.
+ Create a first draft of the page headings, then ask Q to fill them in.
+ Amazon Q might output Markdown. This is fine. The AsciiDoc tooling can understand most markdown syntax.

To learn more about Amazon Q Developer, see [Using Amazon Q Developer in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html).