# Introduction to Amazon Mechanical Turk

The following topics provide a high-level overview of the Amazon Mechanical Turk web service. After
reading these topics, you should understand the basics you need to work through the examples in this guide.

###### Topics

- [Overview of Amazon Mechanical Turk](#overview "#overview")
- [Key Amazon Mechanical Turk Concepts](#concepts "#concepts")
- [What's Next?](#examples "#examples")

## Overview of Amazon Mechanical Turk

Amazon Mechanical Turk provides an on-demand, scalable, human workforce to complete jobs that humans
can do better than computers. Amazon Mechanical Turk software formalizes job offers to the thousands of
Workers willing to do piecemeal work at their convenience. The software also retrieves
work performed and compiles it for you, the Requester, who pays the Workers for
satisfactory work (only). Optional qualification tests enable you to select competent
Workers.

The kinds of tasks humans can complete better than computers includes finding objects
in photos, writing reviews of restaurants, movies, or businesses, translating text
passages into foreign languages, getting the hours of operation of the business center
within a hotel, determining if a hotel is family-friendly, or telling you the most
relevant search results for a given phrase.

This guide presents a very slim slice of the Amazon Mechanical Turk API. For a complete description
of the entire API, go to the [Amazon Mechanical Turk API Reference](../AWSMturkAPI.md "../AWSMturkAPI.md").
For more information about using the API, go to the [Amazon Mechanical Turk Developer Guide](../AWSMechanicalTurkRequester.md "../AWSMechanicalTurkRequester.md").

### Features

The following list describes the features of Amazon Mechanical Turk highlighted by the tutorial
in this guide.

- On-demand workforce—Amazon Mechanical
  Turk provides access to a virtual community of Workers.
- Create jobs that Workers perform over the
  Internet—Advertise your job to the thousands of
  Amazon Mechanical TurkWorkers around the world

You prescribe the job (HIT) that Workers complete using their computer,
and pay them for their work.

- Test and publish your jobs—Test your jobs in the Amazon Mechanical Turk sandbox and publish the revised jobs to
  the outside world.

Amazon Mechanical Turk provides SDKs and command line tools to make it easier to build solutions
leveraging Amazon Mechanical Turk.

## Key Amazon Mechanical Turk Concepts

This section describes the concepts and terminology you need to understand to use Amazon Mechanical Turk effectively.

### Requester

A _Requester_ is a company, organization, or person that
creates and submits tasks (HITs) to Amazon Mechanical Turk for Workers to perform. As a Requester,
you can use a software application to interact with Amazon Mechanical Turk to submit
tasks, retrieve results, and perform other automated tasks. You can use the [Requester website](http://requester.mturk.amazon.com/ "http://requester.mturk.amazon.com/") to check
the status of your HITs, and manage your account.

### Human Intelligence Task

A _Human Intelligence Task (HIT)_ is a task that a Requester
submits to Amazon Mechanical Turk for Workers to perform. A HIT represents a single, self-contained
task, for example, "Identify the car color in the photo." Workers can find HITs
listed on the Amazon Mechanical Turk website. For more information, go to the [Amazon Mechanical Turk website](http://mturk.amazon.com "http://mturk.amazon.com").

Each HIT has a lifetime, specified by the Requester, that determines how long the
HIT is available to Workers. A HIT also has an assignment duration, which is the
amount of time a Worker has to complete a HIT after accepting it.

### Worker

A _Worker_ is a person who performs the tasks specified by a
Requester in a HIT. Workers use the [Amazon Mechanical Turk
website](http://mturk.amazon.com "http://mturk.amazon.com") to find and accept assignments, enter values into the question
form, and submit the results. The Requester specifies how many Workers can work on a
task. Amazon Mechanical Turk guarantees that a Worker can work on each task only one time.

### Assignment

An _assignment_ specifies how many people can submit completed
work for your HIT. When a Worker accepts a HIT, Amazon Mechanical Turk creates an assignment to
track the work to completion. The assignment belongs exclusively to the Worker and
guarantees that the Worker can submit results and be eligible for a reward until the
time the HIT or assignment expires.

### Reward

A _reward_ is the money you, as a Requester, pay Workers for
satisfactory work they do on your HITs.

## What's Next?

The next section explains how to sign up for AWS and for Amazon Mechanical Turk, and how to set up your development
environment.
