AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with themes in the
 AWS Cloud9
 IDE

A *theme* defines your overall IDE colors. This applies across each
 AWS Cloud9 development environment associated with your IAM user. As you make changes to your theme, AWS Cloud9 pushes
 those changes to the cloud, and associates them with your IAM user. AWS Cloud9 also continually
 scans the cloud for changes to the theme that's associated with your IAM user. AWS Cloud9 applies
 those changes to your current environment.


* [View or change your theme](#settings-theme-view "#settings-theme-view")
* [Overall theme settings you can change](#settings-theme-change "#settings-theme-change")
* [Theme overrides](#settings-theme-code "#settings-theme-code")

## View or change your theme



1. On the menu bar, choose **AWS Cloud9**, **Preferences**.
2. To view your theme across each environment of yours, on the **Preferences** tab, in the
side navigation pane, choose **Themes**.
3. To change your theme across each environment of yours, in the **Themes** pane, change
the settings you want. To change portions of your theme by using code, choose the
**your stylesheet** link.
4. To apply your changes to any environment of yours, open that environment. If that environment is
 already open, refresh the web browser tab for that environment.

## Overall theme settings you can change


You can change the following kinds of overall theme settings on the **Preferences**
tab in the **Themes** pane.




****Flat Theme****

Applies the built-in flat theme across the AWS Cloud9 IDE.



****Classic Theme****

Applies the selected built-in classic theme across the AWS Cloud9 IDE.



****Syntax Theme****

Applies the selected theme to code files across the AWS Cloud9 IDE.




## Theme overrides


###### Important

AWS Cloud9 no longer supports the feature that allowed users to override IDE themes by
 updating the `styles.css` file. Users can continue to view, edit, and
 save the `styles.css` file using the editor. But, no theme overrides
 are applied when the AWS Cloud9 IDE loads. 

If AWS Cloud9 detects that the `styles.css` file has been modified, the
 following message is displayed in the IDE:

**`Support for theme overrides has been discontinued. The contents of this styles.css file will no longer be applied on loading the AWS Cloud9 IDE.`**

If you need to use style sheets to define themes for the IDE, please [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") directly.
