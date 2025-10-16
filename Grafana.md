# [Grafana](#Grafana)

## [Content](#content)

- [Grafana](Grafana.md):
    - [Introduction](#introduction)
    - [Grafana Features and Capabilities](#features)
    - [Exploring Existing Templates and Dashboards](#templates)
    - [Building Custom Dashboards](#building)
    - [Configuring Alerts and Notifications](#alerts)


### Introduction
> [Grafana](#Grafana) > [Content](#content) > [This section](#introduction)

Managing software and complex systems is never simple, and unexpected issues are inevitable. **Observability** plays a key role in helping teams understand what is happening within a system, allowing them to identify, analyze, and resolve problems quickly. The three main pillars of observability are **metrics, logs, and traces**.

**Prometheus** focuses on the metrics pillar, collecting and storing time-series data about system performance. These metrics provide valuable insights, but they don’t tell the full story. This is where **Grafana** adds significant value.

**Grafana** is a powerful open-source platform designed for **data visualization and monitoring**. It helps users track, analyze, interact with, and understand data from multiple sources through dynamic, real-time dashboards. The platform can connect to numerous data sources, including Prometheus, MySQL, PostgreSQL, Loki, and others. Users can also configure alerting rules to notify teams when certain thresholds are exceeded.

Together, Grafana and Prometheus form a robust observability stack. Grafana serves as a visualization and analysis layer on top of Prometheus, transforming raw numerical data into clear, interactive dashboards. These dashboards enable teams to easily monitor system health, detect trends, and understand system behavior at a glance.

### Grafana Features and Capabilities
> [Grafana](#Grafana) > [Content](#content) > [This section](#features)


#### Explore metrics, logs, and traces 

Grafana has available a interface that was designed for interative on-the-fly investigation of your data, this interface is called Grafana Explore. Unlike dashboards, which are more static and structured, Explore lets you dig into metrics, logs, and traces in real time to troubleshoot, analyze trends, and understand system behavior.

<img width="80%"  alt="" src="https://github.com/user-attachments/assets/80854f79-9502-481d-9d61-eadc029b6888" />

This interface allows you to choose the database you want to analyze. By selecting the metric and the label, Grafana Explore automatically generates the query code. Once executed, you can analyze the results.

<img width="80%"  alt="" src="https://github.com/user-attachments/assets/e06e6055-572e-4abf-8b63-547330ab9108" />

Watch this video for a more in-depth presentation of Grafana Explore and the official website:
-> https://www.youtube.com/watch?v=1q3YzX2DDM4&t=334s
-> https://grafana.com/docs/grafana/latest/explore/get-started-with-explore/

#### Alerts

An alert rule defines the conditions under which specific metrics are monitored and alerts are triggered.
An alert rule typically includes:

* **Queries and expressions** that tell Grafana which data to analyze.
* **A condition** that specifies what must happen for the alert to trigger.
* **An evaluation interval** that determines how often the rule is checked.
* **Actions and notifications** that define what happens when the alert is triggered — for example, sending an email.


Grafana supports two types of alert rules, Grafana-managed alert rules and Data source-managed alert rules. 

| **Feature**                             | **Grafana-managed alert rules **   | **Data source-managed alert rules**                               |
| --------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| **Where alerts are created**            | In Grafana                                      | In the data source (e.g., Prometheus, Loki, Mimir)                |
| **Where alerts are stored**             | Grafana database                                | Data source configuration                                         |
| **Who evaluates the alert**             | Grafana                                         | The data source itself                                            |
| **Supported data sources**              | Any (Prometheus, Loki, InfluxDB, etc.)          | Mainly Prometheus-based sources                                   |
| **Integration with Grafana dashboards** | Full integration                                | Limited integration                                               |
| **Flexibility and features**            | High — advanced configuration and notifications | Basic — depends on the data source capabilities                   |
| **Best use case**                       | Centralized and unified alert management        | When you already manage alerts inside Prometheus or similar tools |

Grafana recommends using Grafana-managed alert rules, as they are more flexible and fully integrated. Data source-managed alert rules depend on the data source and offer limited integration. Both types of alert rules can be configured in Grafana under the Alerts & IRM tab:

<img width="1855" height="667" alt="image" src="https://github.com/user-attachments/assets/f7702366-7555-40d4-be9c-da9672ca27e1" />


#### Annotations

#### Dashboards variables

#### Configure Grafana

#### Import Dashboards and plugins

#### Authentication

#### Provision

#### Premissions

