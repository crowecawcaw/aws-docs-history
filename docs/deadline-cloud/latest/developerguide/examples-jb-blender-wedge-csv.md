# Render Blender wedges from a CSV file on Deadline Cloud

The
[blender\_wedge\_from\_csv](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_wedge_from_csv "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_wedge_from_csv")
job bundle on the GitHub website renders a wedge from a CSV file. A
wedge is a set of look-development variations of the same Blender scene,
with one image for each variation. Choose the bundle when a spreadsheet
defines your job's task list: wedge variations and shot lists,
simulation parameter sweeps, per-asset QC checks, and similar structured
data that doesn't fit a numeric frame range.

The bundle includes a pre-submission hook that expands the CSV into
the job's task parameters at submission time, so each CSV row becomes
one task on the farm. The CSV is the artist-facing interface, and the
hook translates it into Open Job Description task parameters with no template
editing for each wedge. The hook is bundle-local: it travels with the job in
`hooks.yaml` and applies only to submissions of the
bundle.

The bundle requires the Deadline Cloud CLI version 0.58.0 or later with
PyYAML available to `python3`, a queue with a conda queue
environment that provides the `blender` package, and bundle
hooks enabled once per workstation:

```
deadline config set settings.allow_bundle_hooks true
```

Submit from the bundle directory. The CLI asks for confirmation
before running the bundle's hooks:

```
deadline bundle submit .
```

To wedge your own values, edit `wedges.csv`, or keep
multiple CSVs and pass one with
`-p WedgeCsvFile=`/path/to/my_wedges.csv``.
The README covers the combination expression that pairs CSV columns into
tasks, running the expansion locally, and the security model for bundle
hooks. For workstation-wide hooks, see
[Enforce fixed license limits with a Deadline Cloud submission hook](examples-license-limits-hook.md "examples-license-limits-hook.md"). For a frame-range
Blender render, see [Render Blender scenes on Deadline Cloud](examples-jb-blender-render.md "examples-jb-blender-render.md").
