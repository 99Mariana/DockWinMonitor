# [Grafana](#Grafana)

## [Content](#content)

- [Grafana](Grafana.md):
    - [Introduction](#introduction)
    - [Grafana Explore](#explore)
    - [Alert Rules](#alert)
    - [Annotations](#annotations)
    - [Exploring Existing Templates and Dashboards](#templates)
    - [Building Custom Dashboards](#building)



### Introduction
> [Grafana](#Grafana) > [Content](#content) > [This section](#introduction)

Managing software and complex systems is never simple, and unexpected issues are inevitable. **Observability** plays a key role in helping teams understand what is happening within a system, allowing them to identify, analyze, and resolve problems quickly. The three main pillars of observability are **metrics, logs, and traces**.

**Prometheus** focuses on the metrics pillar, collecting and storing time-series data about system performance. These metrics provide valuable insights, but they don’t tell the full story. This is where **Grafana** adds significant value.

**Grafana** is a powerful open-source platform designed for **data visualization and monitoring**. It helps users track, analyze, interact with, and understand data from multiple sources through dynamic, real-time dashboards. The platform can connect to numerous data sources, including Prometheus, MySQL, PostgreSQL, Loki, and others. Users can also configure alerting rules to notify teams when certain thresholds are exceeded.

Together, Grafana and Prometheus form a robust observability stack. Grafana serves as a visualization and analysis layer on top of Prometheus, transforming raw numerical data into clear, interactive dashboards. These dashboards enable teams to easily monitor system health, detect trends, and understand system behavior at a glance.


### Grafana Explore
> [Grafana](#Grafana) > [Content](#content) > [This section](#explore)

Grafana has available a interface that was designed for interative on-the-fly investigation of your data, this interface is called Grafana Explore. Unlike dashboards, which are more static and structured, Explore lets you dig into metrics, logs, and traces in real time to troubleshoot, analyze trends, and understand system behavior.

<img width="80%"  alt="" src="https://github.com/user-attachments/assets/80854f79-9502-481d-9d61-eadc029b6888" />

This interface allows you to choose the database you want to analyze. By selecting the metric and the label, Grafana Explore automatically generates the query code. Once executed, you can analyze the results.

<img width="80%"  alt="" src="https://github.com/user-attachments/assets/e06e6055-572e-4abf-8b63-547330ab9108" />

Watch this video for a more in-depth presentation of Grafana Explore and the official website:
-> https://www.youtube.com/watch?v=1q3YzX2DDM4&t=334s
-> https://grafana.com/docs/grafana/latest/explore/get-started-with-explore/

### Alert Rules
> [Grafana](#Grafana) > [Content](#content) > [This section](#alerts)

An alert rule defines the conditions under which specific metrics are monitored and alerts are triggered.
An alert rule typically includes:

* **Queries and expressions** that tell Grafana which data to analyze.
* **A condition** that specifies what must happen for the alert to trigger.
* **An evaluation interval** that determines how often the rule is checked.
* **Actions and notifications** that define what happens when the alert is triggered — for example, sending an email.


Grafana supports two types of alert rules, Grafana-managed alert rules and Data source-managed alert rules. 

| **Feature**                             | **Grafana-managed alert rules**   | **Data source-managed alert rules**                               |
| --------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| **Where alerts are created**            | In Grafana                                      | In the data source (e.g., Prometheus, Loki, Mimir)                |
| **Where alerts are stored**             | Grafana database                                | Data source configuration                                         |
| **Who evaluates the alert**             | Grafana                                         | The data source itself                                            |
| **Supported data sources**              | Any (Prometheus, Loki, InfluxDB, etc.)          | Mainly Prometheus-based sources                                   |
| **Integration with Grafana dashboards** | Full integration                                | Limited integration                                               |
| **Flexibility and features**            | High — advanced configuration and notifications | Basic — depends on the data source capabilities                   |
| **Best use case**                       | Centralized and unified alert management        | When you already manage alerts inside Prometheus or similar tools |

Grafana recommends using Grafana-managed alert rules, as they are more flexible and fully integrated. Data source-managed alert rules depend on the data source and offer limited integration. Both types of alert rules can be configured in Grafana under the Alerts & IRM tab:

<img width="80%"  alt="" alt="image" src="https://github.com/user-attachments/assets/f7702366-7555-40d4-be9c-da9672ca27e1" />


For more information about alert rules, check the official website: https://grafana.com/docs/grafana/latest/alerting/alerting-rules/

#### How to create a Grafana-managed alert rule

The first step to create a grafana-managed alert rule is to create a contact point. A contact point is a configured destination for alerts, it defines where and how notifications are sent when an alert triggers. Each contact point specifies the communication channel (such as email, Slack, Telegram, webhook, etc.), its settings, and message templates. It works together with alert rules (which define alert conditions) and notification policies (which route alerts to specific contact points), forming the core of Grafana’s alerting system.

In the left menu in grafana we have a tab to create the contact point. In this case, we use Webhook.site to get a unique URL that we can use for this test.

<img width="80%" alt="" src="https://github.com/user-attachments/assets/bb2aab05-956d-4eb1-815f-6bf83c824565" />

The next step is to set up an alert rule. To do this, we go to the Alert rules tab, define the query and alert condition, choose a folder to store the rule, and select the contact point for notifications. We can also add a summary and description. In this example, an alert rule for CPU utilization was created.


<img width="80%" alt="" src="https://github.com/user-attachments/assets/73cb8869-b10f-4ad3-8274-69b3fa20c2fe" />

With both the contact point and the alert rule configured, we will start receiving alert notifications through a public webhook. This setup allows us to monitor when an alert is triggered and when the issue has been resolved, providing a complete view of the alert lifecycle.


<img width="80%"  alt="image" src="https://github.com/user-attachments/assets/b58218d1-908b-4605-b645-740aa67b3e84" />

For a more detailed tutorial, check out: 
https://grafana.com/tutorials/alerting-get-started/
https://grafana.com/tutorials/alerting-get-started/#set-evaluation-behavior

To make the alert easier to read, we can create a template. In this example, I’ll use a Flask webhook to receive the notification as a test, but a similar approach could also be applied to email notifications. 

Using a template like this allows for a more consistent and readable alert format:

```
{{ len .Alerts }} alert(s)

{{ range .Alerts }}
Summary: {{ .Annotations.summary }}
Status: {{ .Status }}
Description: {{ .Annotations.description }}

{{ end }}
```

<img width="80%" alt="image" src="https://github.com/user-attachments/assets/f345d29b-fcf3-48e0-a26d-b26d1b30b179" />

Note that to be possible to extract the message sent by Grafana, it was necessary to develop the **`webhook_server.py`** file. Grafana sends alerts in raw JSON format through a Webhook, which by itself does not display the information in a readable or structured way. The script serves as a bridge between Grafana and the user, converting the JSON alert data into meaningful and readable information.

The Python file, built using Flask, acts as a lightweight web server that listens for these alerts via HTTP POST requests. When an alert is received, the script extracts the relevant data — such as labels, values, and descriptions — and replaces the dynamic variables in the alert template (for example, `{{ index $labels "instance" }}`) with their actual values. It then formats and prints a clear, human-readable message to the console.


### Annotations
> [Grafana](#Grafana) > [Content](#content) > [This section](#annotations)

Annotations allow you to mark specific points on a graph or visualization with rich events, making it easier to correlate data when something goes wrong. They appear as vertical lines or icons on graph panels. Hovering over an annotation shows the event description, tags, and can even include links to external systems for more details. Annotations can be created directly in the panel, automatically through the HTTP API, or by configuring annotation queries in the dashboard settings.

For more information about annotations, check the official website: https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/

### Exploring Existing Templates and Dashboards
> [Grafana](#Grafana) > [Content](#content) > [This section](#templates)

Grafana provides a wide range of dashboard templates that can be downloaded and imported for free into any Grafana instance:

https://grafana.com/grafana/dashboards/?plcmt=oss-nav

These templates have been developed by the community and industry experts for various software systems and monitoring tools, such as Prometheus, Elasticsearch, Kubernetes, Docker, MySQL, among others. Each template comes pre-configured with the most relevant metrics for each monitored software, offering a clear and immediate overview of system performance, resource usage, and key operational indicators. In addition, the dashboards include ready-to-use visualizations that help users quickly interpret data and identify potential issues. These templates are also highly customizable, allowing users to adapt them according to their specific needs or infrastructure — panels can be modified, new metrics added, and visual styles adjusted. As a result, Grafana templates not only provide an efficient starting point for building monitoring dashboards but also help accelerate the deployment of observability solutions and encourage the adoption of monitoring best practices grounded in community expertise and real-world use cases.

To import a template, navigate to the 'New Dashboard' option and upload the corresponding file:

<img width="80%" alt="" src="https://github.com/user-attachments/assets/fc6079a5-ca88-458e-bc7c-cf1254f8a8fe" />

It is also possible to create a dashboard from scratch. For a step-by-step introduction, watch the videos below:

https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/create-dashboard/
https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/
https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/







