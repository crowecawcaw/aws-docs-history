

# Customize views for the Connect Customer agent workspace by using HTML and JSX
<a name="customize-views-jsx-sg"></a>

You can customize the look and feel of the layouts of View resources. You do this by using HTML or JSX when you pass in input parameters to the [Show view](show-view-block.md) block.

**Custom Views only**  
The TemplateString input for HTML and JSX content is supported only with Custom Views. It is not supported with views built using the No-Code UI Builder.

Complete the following steps for a simple example of how you can use HTML or JSX with a [Show view](show-view-block.md) block.

1. Create a flow with a [Show view](show-view-block.md) block.

1. Open the Properties page of [Show view](show-view-block.md) block. 

1. Under **View**, select **Detail** from the dropdown list. 

1.  In the **Sections** section, choose **Set JSON**. 

1. Copy and paste the following JSON code. This code shows how HTML or JSX expressions get processed.

   **HTML example**

   ```
   {
   "TemplateString": 
        "<TextContent>Steps:<ol><li>Customer provides incident information</li><li>Customer provides receipts and agrees with 
            amount</li> <li>Customer receives reimbursement</li></ol></TextContent>"
   }
   ```

   **JSX example**

   ```
   {
   "TemplateString":
   "Please provide an introduction to the customers. Ask them how their day is going
   Things to say:
   Hello, how are you today? My name is Bob, who am I speaking to?"
   }
   ```