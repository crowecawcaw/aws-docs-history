

# Customize views by using HTML and JSX
<a name="customize-views-jsx-sg"></a>

You can customize view layouts by using HTML or JSX in the input parameters of the [Show view](show-view-block.md) block.

**Custom views only**  
Only custom views support HTML and JSX in the `TemplateString` input. Views built in the UI builder don't.

The following example uses HTML or JSX in a [Show view](show-view-block.md) block.

1. Create a flow with a [Show view](show-view-block.md) block.

1. Open the properties of the [Show view](show-view-block.md) block.

1. Under **View**, choose **Detail**.

1.  In the **Sections** section, choose **Set JSON**. 

1. Paste one of the following samples.

   To use HTML:

   ```
   {
   "TemplateString": "<TextContent>Steps:<ol><li>Customer provides incident information</li><li>Customer provides receipts and agrees with amount</li> <li>Customer receives reimbursement</li></ol></TextContent>"
   }
   ```

   To use JSX:

   ```
   {
   "TemplateString":
   "Please provide an introduction to the customers. Ask them how their day is going.
   Things to say:
   Hello, how are you today? My name is Bob, who am I speaking to?"
   }
   ```