# Submit a job requiring limits

You apply a limit by specifying it as a host requirement for the job or job step. If you
 don't specify a limit in a step and that step uses an associated resource, the step's usage
 isn't counted against the limit when jobs are scheduled..

Some Deadline Cloud submitters enable you to set a host requirement. You can specify the limit's
 amount requirement name in the submitter to apply the limit.

If your submitter doesn't support adding host requirements, you can also apply a limit
 by editing the job template for the job.

###### To apply a limit to a job step in the job bundle

1. Open the job template for the job using a text editor. The job template is located
 in the job bundle directory for the job. For more information, see [Job bundles](build-job-bundle.md "build-job-bundle.md") in the *Deadline Cloud Developer Guide*.
2. Find the step definition for the step to apply the limit to.
3. Add the following to the step definition. Replace
 `amount.name` with the amount requirement name of your limit.
 For typical use, you should set the `min` value to 1.



YAML

```
  hostRequirements:
    amounts:
    - name: amount.`name`
      min: 1
```


JSON

```
"hostRequirements": {
    "amounts": [
        {
            "name": "`amount.name`",
            "min": "1"
        }
    }
}
```



You can add multiple limits to a job step as follows. Replace
 `amount.name_1` and `amount.name_2`
 with the amount requirement names of your limits.



YAML

```
  hostRequirements:
    amounts:
    - name: `amount.name_1`
      min: 1
    - name: `amount.name_2`
      min: 1
```


JSON

```
"hostRequirements": {
    "amounts": [
        {
            "name": "amount.`name_1`",
            "min": "1"
        },
        {
            "name": "amount.`name_2`",
            "min": "1"
        }
    }
}
```
4. Save the changes to the job template.
