# Sharing Quick Sight Topics

|                                           |
| ----------------------------------------- |
| **Applies<br>to:*<br>• Enterprise Edition |

|                                                               |
| ------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick administrators and authors |

After you create and publish a Topic, share it with others in your organization.
Sharing a Topic allows your users to ask questions in Amazon Quick chat and use the
Topic as a data model in analysis sheets.

###### To share a Topic

1. From the Topic page, select the ellipsis menu and choose
   **Share**.
2. Search for and add specific users or groups.
3. Set permission levels (**Owner** or
   **Viewer**) and choose **Done**.

| Permission Level | Can Ask Questions | Can Modify Topic | Can Use in Analysis |
| ---------------- | ----------------- | ---------------- | ------------------- |
| Owner            | Yes               | Yes              | Yes                 |
| Viewer           | Yes               | No               | Yes                 |

Quick Sight enforces row-level security (RLS) and column-level security (CLS) at
the dataset level. Access controls are preserved through the Topic's semantic layer,
regardless of how users access the Topic.
