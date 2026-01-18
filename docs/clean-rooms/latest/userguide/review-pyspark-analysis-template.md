# Reviewing a PySpark analysis

template

When another member creates an analysis template in your collaboration, you must review
and approve it before it can be used.

The following procedure shows you how to review a PySpark analysis template, including
its rules, parameters, and referenced tables. As a collaboration member, you'll assess
whether the template aligns with your data sharing agreements and security
requirements.

After the analysis template and approved, it can be used in a job in AWS Clean Rooms.

###### Note

When you bring your analysis code into a collaboration, be aware of the following:

- AWS Clean Rooms doesn't validate or guarantee the behavior of the analysis code.
  - If you need to ensure certain behavior, review the code of your collaboration
    partner directly or work with a trusted third-party auditor to review it.

- AWS Clean Rooms guarantees that the SHA-256 hashes of the code listed in the PySpark
  analysis template matches the code running in the PySpark analysis environment.
- AWS Clean Rooms doesn't perform any auditing or security analysis of additional libraries
  you bring into the environment.
- In the shared security model:

      + You (the customer) are responsible for the security of the code running in the
       environment.
      + You (the customer) are responsible for setting the appropriate error message
       configuration for the environment.
      + AWS Clean Rooms is responsible for the security of the environment, ensuring that




      	- only the approved code runs
      	- only specified configured tables are accessible
      	- the only output destination is the result receiver's S3 bucket.

  AWS Clean Rooms generates SHA-256 hashes of the user script and virtual environment for your
  review. However, the actual user script and libraries aren't directly accessible within
  AWS Clean Rooms.

To validate that the user script and libraries shared are the same as those referenced
in the analysis template, you can create a SHA-256 hash of the files shared and compare it
to the analysis template hash created by AWS Clean Rooms. The hashes of the code run will also be in
the job logs.

**Prerequisites**

- Linux/Unix operating system or Windows Subsystem for Linux (WSL)
- User script file you want to hash
  - Request that the analysis template creator share the file through a secure
    channel.

- The analysis template hash created by AWS Clean Rooms

###### To review a PySpark analysis template using the AWS Clean Rooms console

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
   collaboration creator.
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Templates** tab, go to the **Analysis templates
   created by other members** section.
5. Choose the analysis template that has the **Can run status** of
   **No requires your review**.
6. Choose **Review**.
7. Review the analysis rule **Overview**,
   **Definition**, and **Parameters** (if any).

###### Note

Parameters allow analysis runners to submit different values at submission time. If an analysis template supports parameters, review how the parameter values are used in the code of your collaboration partner to ensure it meets your requirements. 8. Validate that the shared user script and libraries are the same as those referenced
in the analysis template.

    1. Create a SHA-256 hash of the files shared and compare it to the analysis
     template hash created by AWS Clean Rooms.


    You can generate a hash by navigating to the directory containing your user
     script file and then running the following command:



    ```
    sha256sum your_script_filename.py
    ```

    Example output:



    ```
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 my_analysis.py
    ```
    2. Alternatively, you can use Amazon S3 checksum features. For more information, see
     [Checking object integrity in Amazon
     S3](../../../AmazonS3/latest/userguide/checking-object-integrity.md "../../../AmazonS3/latest/userguide/checking-object-integrity.md") in the *Amazon S3 User
     Guide*.
    3. Another alternative is to view the hashes of the executed code in the job
     logs.

9. Review the configured tables listed under **Tables referenced in
   definition**.

The **Status** next to each table will read **Template not
allowed**. 10. Choose a table.

    1. To approve the analysis template, choose **Allow template on
     table**. Confirm your approval by choosing
     **Allow**.
    2. To decline approval, choose **Disallow**.

If you have chosen to approve the analysis template, the member who can run jobs can now
run a PySpark job on a configured table using a PySpark analysis template. For more
information, see [Running PySpark jobs](run-jobs.md "run-jobs.md").
