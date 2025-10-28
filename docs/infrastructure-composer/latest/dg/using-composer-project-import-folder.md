# Import an existing project folder in the Infrastructure Composer console

Using local sync mode, you can import the parent folder of an existing project. If your project contains multiple
templates, you can choose the template to load.

###### To import an existing project from the Home page

1. Sign in to the [Infrastructure Composer
   console](https://console.aws.amazon.com/composer/home "https://console.aws.amazon.com/composer/home").
2. On the **Home** page, choose **Load a CloudFormation template**.
3. For **Project location**, choose **Select folder**. Select your project’s parent
   folder and choose **Select**.

###### Note

If you do not receive this prompt, your browser may not support the File System Access API, which is required
for local sync mode. For more information, see [Allow web page access to local files in Infrastructure Composer](reference-fsa.md "reference-fsa.md"). 4. When prompted by your browser, select **View files**. 5. For **Template file**, choose your template from the dropdown list. If your project contains a
single template, Infrastructure Composer automatically selects it for you. 6. Choose **Create**.

###### To import an existing project from the canvas

1. From the canvas, choose **Menu** to open the menu.
2. In the **Open** section, choose **Project folder**.

###### Note

If the **Project folder** option is unavailable, your browser may not support the File System
Access API, which is required for local sync mode. For more information, see [Allow web page access to local files in Infrastructure Composer](reference-fsa.md "reference-fsa.md"). 3. For **Project location**, choose **Select folder**. Select your project’s parent
folder and choose **Select**. 4. When prompted by your browser, select **View files**. 5. For **Template file**, choose your template from the dropdown list. If your project contains a
single template, Infrastructure Composer automatically selects it for you. 6. Choose **Create**.
When you import an existing project folder, Infrastructure Composer activates **local sync mode**. Changes
made to your project’s template or files are automatically saved to your local machine.
