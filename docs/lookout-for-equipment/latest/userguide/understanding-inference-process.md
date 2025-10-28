On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Understanding the inference process

When you're planning your use of Lookout for Equipment, it may be useful to understand exactly what happens at each step of the inference process.

![Inference steps](images/inference-steps.png)

1. Lookout for Equipment looks for the component name (which can be the name of an asset or a sensor,
   depending on how your data was ingested).
2. Once the component name is found in the file name, Lookout for Equipment looks at the time stamp in the CSV file name.
3. The timestamp in the file name must be within the range of time that your scheduler is
   running. For example, if the scheduler is running every 5 minutes, then at 9:05,
   Lookout for Equipment will look for any files that have a timestamp from 9:00 to 9:05. Any files
   with timestamps outside this range will be ignored for the inference run.
4. Lookout for Equipment automatically ingests the files with the right component name, and within the right time range.
5. Lookout for Equipment opens the CSV file and runs inference on any rows in the CSV file with timestamps that
   fit within the scheduler window. For example, if the scheduler is running every 5
   minutes, and the current time is 9:05, then Lookout for Equipment will grab any files with the
   timestamp in the file name from 9:00 to 9:05, and will then run inference on any
   rows in the CSV with timestamps between 9:00 to 9:05.
6. The inference results are placed into your designated output bucket in a JSON file.
7. The steps above are repeated in perpetuity until the scheduler is turned off.
