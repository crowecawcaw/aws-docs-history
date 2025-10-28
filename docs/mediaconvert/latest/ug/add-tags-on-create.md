# Adding tags when you create an AWS Elemental MediaConvert

resource

The following procedures show you how to add tags to your MediaConvert queues, job
templates, and output presets when you create them.

**Topics**

## Adding tags when creating a resource

(console)

You can add tags when you create a queue, job template, or output preset.

###### To add tags when you create a queue, job template, or output preset

(console)

1. Follow the steps in one of the following procedures to begin creating the
   resource, but don't save the resource:
   - [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md")
   - [Creating a queue](creating-queues.md "creating-queues.md")
   - [Creating a template](creating-template-from-scratch.md "creating-template-from-scratch.md")
   - [Creating a preset](creating-preset-from-scratch.md "creating-preset-from-scratch.md")
   - [Creating a preset, based on a system preset](create-custom-preset-from-system-preset.md "create-custom-preset-from-system-preset.md")

2. Find the **Tags** section in the relevant
   location:
   - For jobs – on the **Create job** page,
     after you choose **Settings** from the
     **Job** section on the left
   - For queues – at the bottom of the **Create
     queue** page
   - For output presets – at the bottom of the **Create
     preset** page
   - For job templates – at the bottom of the **Create
     job template** page, after you choose
     **Settings** from the **Job**
     section on the left

3. In the **Tags** section, choose
   **Add**.
4. For **Tag key**, enter a name for the tag. For
   **Tag value**, enter a value for the tag.
5. Choose **Create** to save the new resource with its
   tags.

## Adding tags when creating a resource (API

and AWS CLI)

When you create a job, job template, output preset, or queue using the
AWS Elemental MediaConvert API or the AWS CLI, submit your JSON specification for the resource
as usual. Include tags as shown in the following JSON example, in
`tags`:

```
{
	"name": "Job Template Test with Resource Tags",
	"description": "Job Template Test",
	"tags":{
		"Company": "Banana",
		"Stage": "Production"
	},
	"settings":{
```
