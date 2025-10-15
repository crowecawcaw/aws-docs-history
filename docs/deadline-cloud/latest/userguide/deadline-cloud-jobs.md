# Deadline Cloud jobs

A *job* is a set of instructions that AWS Deadline Cloud uses to schedule and run
 work on available workers. When you create a job, you choose the farm and queue to send the job
 to. 

A *submitter* is a plugin for your digital content creation (DCC)
 application that manages creating a job in the interface of your DCC application. After you
 create the job, you use the submitter send it to Deadline Cloud for processing.

The submitter creates an [Open Job Specification
 (OpenJD)](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications") template that describes the job. At the same time it uploads your asset files
 to an Amazon Simple Storage Service (Amazon S3) bucket. To reduce upload time, the submitter only sends files that have
 changed since the last upload to Amazon S3

You can also create a job in the following ways.


* From a terminal â for users submitting a job that are comfortable using the
 command line.
* From a script â for customizing and automating workloads.
* From an application â for when the user's work is in an application, or when an
 application's context is important.
 For more information, see [How to submit a job to
 Deadline Cloud](../developerguide/submit-jobs-how.md "../developerguide/submit-jobs-how.md") in the *Deadline Cloud Developer Guide*.

A job consists of:


* *Priority* â The approximate order that Deadline Cloud processes a job
 in a queue. You can set the job priority between 0 and 100, jobs with a higher number
 priority are generally processed first. Jobs with the same priority are processed in the
 order received.
* *Steps* â Defines the script to run on workers. Steps can
 have requirements such as minimum worker memory or other steps that need to complete first.
 Each step has one or more tasks.
* *Tasks* â A unit of work sent to a worker to perform. A task
 is a combination of a step's script and parameters, such as a frame number, that are used in
 the script. The job is complete when all tasks are complete for all steps.
* *Environment* â Set up and tear down instructions shared by
 multiple steps or tasks.
