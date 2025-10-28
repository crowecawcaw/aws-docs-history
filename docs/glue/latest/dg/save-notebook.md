# Saving your notebook and job script

You can save your notebook and the job script you are creating at any time. Simply
choose the **Save** button in the upper right corner, the same as if you
were using the visual or script editor.

When you choose **Save**, the notebook file is saved in
the default locations:

- By default, the job script is saved to the Amazon S3 location indicated in the **Job Details**
  tab, under **Advanced properties**, in the Job details
  property **Script path**. Job scripts are saved in a subfolder named `Scripts`.
- By default, the notebook file (`.ipynb`) is saved to the Amazon S3 location
  indicated in the **Job Details** tab, under **Advanced properties**, in the Job details
  **Script path**. Notebook files are saved in a subfolder named
  `Notebooks`.

###### Note

When you save the job, the job script contains only the code cells from the notebook.
The Markdown cells and magics aren't included in the job script. However, the `.ipynb` file
will contain any markdown and magics.

After you save the job, you can then run the job using the script that you created in the
notebook.
