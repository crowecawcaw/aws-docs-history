

# Creating an ETL job using notebooks in AWS Glue Studio
<a name="create-notebook-job"></a>

**To start using notebooks in the AWS Glue Studio console**

1.  Attach AWS Identity and Access Management policies to the AWS Glue Studio user and create an IAM role for your ETL job and notebook. 

1.  Configure additional IAM security for notebooks, as described in [Granting permissions for the IAM role](notebook-getting-started.md#studio-notebook-permissions). 

1.  Open the AWS Glue Studio console at [https://console.aws.amazon.com/gluestudio/](https://console.aws.amazon.com/gluestudio/). 
**Note**  
Check that your browser does not block third-party cookies. Any browser that blocks third party cookies either by default or as a user-enabled setting will prevent notebooks from launching. For more information on managing cookies, see:
   + [Chrome](https://support.alertlogic.com/hc/en-us/articles/360018127132-Turn-Off-Block-Third-Party-Cookies-in-Chrome-for-Windows)
   + [Firefox](https://support.mozilla.org/en-US/kb/third-party-cookies-firefox-tracking-protection)
   + [Safari](https://support.apple.com/guide/safari/manage-cookies-sfri11471/mac)

1. Choose the **Jobs** link in the left-side navigation menu. 

1.  Choose **Jupyter notebook** and then choose **Create** to start a new notebook session. 

1.  On the **Create job in Jupyter notebook** page, provide the job name, and choose the IAM role to use. Choose **Create job**. 

    After a short time period, the notebook editor appears. 

1.  After you add the code you must execute the cell to initiate a session. There are multiple ways to execute the cell: 
   + Press the play button.
   +  Use a keyboard shortcut: 
     +  On MacOS, **Command** \+ **Enter** to run the cell. 
     +  On Windows, **Shift** \+ **Enter** to run the cell. 

    For information about writing code using a Jupyter notebook interface, see * [The Jupyter Notebook User Documentation ](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) *. 

1.  To test your script, run the entire script, or individual cells. Any command output will be displayed in the area beneath the cell. 

1.  After you have finished developing your notebook, you can save the job and then run it. You can find the script in the **Script** tab. Any magics you added to the notebook will be stripped away and won't be saved as part of the script of the generated AWS Glue job. AWS Glue Studio will auto-add a `job.commit()` to the end of your generated script from the notebook contents.

   For more information about running jobs, see [Start a job run](managing-jobs-chapter.md#start-jobs). 

   