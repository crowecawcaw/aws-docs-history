

# Discovery, assessment, and planning

Migration jobs include discovery, assessment, and migration planning in one job step, **Assessments and Migration Planning**. Discovery imports your inventory. Assessment estimates your costs on AWS and builds a business case. Migration planning groups your servers into applications and plans migration waves.

Discovery comes first, because assessment and migration planning both need your inventory. If you ask for an assessment before you upload inventory data, AWS Transform asks you to upload your inventory first. For information about the data that you can upload, see [Discovery](transform-vmware-discover-source-data.md).

Assessment and migration planning are separate features. Running one doesn't change the results of the other. After discovery, you can assess, plan, or do both, in either order, and you can rerun either one. For example, you can build a business case first and add wave planning to the same job later.

The following topics describe each part in detail: [Discovery](transform-vmware-discover-source-data.md), [Migration assessments](transform-app-assessments.md), and [Migration planning](transform-vmware-review-groupings-and-waves.md).

Designing the target state architecture for an application is a separate step, **Application design**. For more information, see [Application design](transform-vmware-target-state-architecture.md).