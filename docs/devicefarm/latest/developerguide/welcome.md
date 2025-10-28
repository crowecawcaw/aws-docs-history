# What is AWS Device Farm?

Device Farm is an app testing service that you can use to test and interact with your Android,
iOS, and web apps on real, physical phones and tablets that are hosted by Amazon Web Services
(AWS).

There are two main ways to use Device Farm:

- Automated testing of apps using a variety of testing frameworks.
- Remote access of devices onto which you can load, run, and interact with apps in
  real time.

###### Note

Device Farm is only available in the `us-west-2` (Oregon) region.

## Automated app testing

Device Farm allows you to upload your own tests or use built-in, script-free compatibility
tests. Because testing is performed in parallel, tests on multiple devices begin in
minutes.

As tests are completed, a test report that contains high-level results, low-level
logs, pixel-to-pixel screenshots, and performance data is updated.

Device Farm supports testing of native and hybrid Android and iOS apps, including those
created with PhoneGap, Titanium, Xamarin, Unity, and other frameworks. It supports
remote access of Android and iOS apps for interactive testing. For more information
about supported test types, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

## Remote access interaction

Remote access allows you to swipe, gesture, and interact with a device through your
web browser in real time. There are a number of situations where real-time interaction
with a device is useful. For example, customer service representatives can guide
customers through the use or setup of their device. They can also walk customers through
the use of apps running on a specific device. You can install apps on a device running
in a remote access session and then reproduce customer problems or reported bugs.

During a remote access session, Device Farm collects details about actions that take place
as you interact with the device. Logs with these details and a video capture of the
session are produced at the end of the session.

## Terminology

Device Farm introduces the following terms that define the way information is
organized:

**device pool**

A collection of devices that typically share similar characteristics, such
as platform, manufacturer, or model.

**job**

A request for Device Farm to test a single app against a single device. A job
contains one or more suites.

**metering**

Refers to billing for devices. You might see references to metered devices
or unmetered devices in the documentation and API reference. For more
information about pricing, see [AWS Device Farm
Pricing](https://aws.amazon.com/device-farm/pricing/ "https://aws.amazon.com/device-farm/pricing/").

**project**

A logical workspace that contains runs, one run for each test of a single
app against one or more devices. You can use projects to organize workspaces
in whatever way you choose. For example, you can have one project per app
title or one project per platform. You can create as many projects as you
need.

**report**

Contains information about a run, which is a request for Device Farm to test a
single app against one or more devices. For more information, see [Reports in AWS Device Farm](reports.md "reports.md").

**run**

A specific build of your app, with a specific set of tests, to be run on a
specific set of devices. A run produces a report of the results. A run
contains one or more jobs. For more information, see [Runs](test-runs.md "test-runs.md").

**session**

A real-time interaction with an actual, physical device through your web
browser. For more information, see [Sessions](sessions.md "sessions.md").

**suite**

The hierarchical organization of tests in a test package. A suite contains
one or more tests.

**test**

An individual test case in a test package.

For more information about Device Farm, see [Concepts](concepts.md "concepts.md").

## Setting up

To use Device Farm, see [Setting up](setting-up.md "setting-up.md").
