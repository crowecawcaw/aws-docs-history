AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Previewing files in the AWS Cloud9 IDE

You can use the AWS Cloud9 IDE to preview the files in a AWS Cloud9 development environment from within the IDE.


* [Open a file for preview](#file-preview-file-open "#file-preview-file-open")
* [Reload a file preview](#file-preview-file-reload "#file-preview-file-reload")
* [Change the file preview type](#file-preview-file-preview-type "#file-preview-file-preview-type")
* [Open a file preview in a separate web browser
 tab](#file-preview-file-open-tab "#file-preview-file-open-tab")
* [Switch to a different file preview](#file-preview-file-switch "#file-preview-file-switch")

## Open a file for preview


Choose one of the following options in the AWS Cloud9 IDE to open a file preview tab within
 the environment:



* In the **Environment** window, open the context (right-click)
 menu for the file you want to preview, and then choose
 **Preview**.


###### Note

Although you can use this approach to preview any file, preview works best with
 files that have the following file extensions:



	+ `.htm`
	+ `.html`
	+ `.pdf`
	+ `.svg`
	+ `.xhtml`
	+ Any file containing content in Markdown format.
* Open a file with one of the following file extensions:




	+ `.pdf`
	+ `.svg`
* With the file you want to preview already open and active, on the menu bar, choose
 **Preview, Preview File FILE\_NAME**. Or choose **Tools,
 Preview, Preview File FILE\_NAME**, where **FILE\_NAME**
 is the name of the file you want to preview.


###### Note

These commands only work with the following file types:



	+ `.htm`
	+ `.html`
	+ `.markdown`
	+ `.md`
	+ `.pdf`
	+ `.svg`
	+ `.txt`: Preview works best if the file's content is in
	 Markdown format.
	+ `.xhtml`: Preview works best if the file contains or
	 references content presentation information.

###### Note

The **Preview Settings** menu in the file preview tab is currently
 not functional and choosing any of its menu commands will have no effect.


## Reload a file preview


On the file preview tab, choose the **Refresh** button (the circular
 arrow).


## Change the file preview type


On the file preview tab, choose one of the following from the preview type list:



* **Browser**: Previews the file in a web browser format, for the
 following file types only:




	+ `.htm`
	+ `.html`
	+ `.pdf`
	+ `.svg`
	+ `.xhtml`: Preview works best if the file contains or
	 references content presentation information.
* **Raw Content (UTF-8)**: Previews the file's original contents in
 Unicode Transformation Format 8-bit (UTF-8) format. This might display unexpected
 content for some file types.
* **Markdown**: Previews any file containing Markdown format. Attempts
 to preview any other file type, but might display unexpected content.

## Open a file preview in a separate web browser
 tab


On the file preview tab, choose **Pop Out Into New Window**.


## Switch to a different file preview


On the file preview tab, type the path to a different file path in the address bar. The
 address bar is located between the **Refresh** button and the preview type
 list.
