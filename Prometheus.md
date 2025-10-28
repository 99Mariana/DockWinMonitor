# [Prometheus](#prometheus)

## [Content](#content)

- [Prometheus](Prometheus.md):
    - [Introduction](#introduction)
    - [Architecture](#architecture)
    - [Prometheus Configuration](#configuration)
    - [Exploring Prometheus browser](#browser)


### Introduction
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#introduction)

Prometheus is an open-source systems monitoring and alerting toolkit designed for reliability and scalability. It helps you collect and analyze metrics from various systems and applications to understand their performance and health.

Prometheus collects and stores its metrics as time series data, meaning each metric is recorded along with the timestamp of when it was captured. Additionally, metrics can include **labels**, optional key-value pairs that provide more context, such as the source, service, or instance of the data.

In simple terms, Prometheus lets you track how systems behave over time and trigger alerts when something goes wrong, making it a powerful tool for monitoring modern infrastructure.

To learn more about Prometheus, visit the official documentation at: https://prometheus.io/docs/introduction/first_steps/


### Architecture
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#Architecture)

As shown on the official website, the architecture of Prometheus and some of its ecosystem components is illustrated below:

<p align="center">
    <img width="80%"  alt="" src="https://github.com/user-attachments/assets/fb0c34ea-c913-4aae-8e93-9c9ad552117d" />
</p>
In this image, we can see the Prometheus server, which is responsible for scraping and storing time series data. It also shows the client libraries used to instrument application code, the Pushgateway that supports short-lived jobs, and various exporters designed for specific services such as HAProxy, StatsD, and Graphite. Additionally, it includes the Alertmanager, which manages alerts, and several supporting tools.

These components work together to form the Prometheus ecosystem: the server continuously collects metrics from different sources, the exporters expose metrics from third-party systems, and the Alertmanager handles notifications based on alerting rules. This architecture enables Prometheus to provide a flexible, reliable, and scalable monitoring solution for dynamic and distributed environments.

### Configuration
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#Configuration)

The `prometheus.yml` file is essential, as it is the main configuration file for Prometheus. It defines which endpoints Prometheus should monitor, such as `windows_exporter` or other services, sets the scraping intervals (how often metrics are collected), configures alerts if needed, and allows you to add labels, targets, and jobs. Without this file, Prometheus won’t know where to collect metrics; it may start successfully, but it won’t gather any useful data. Check the example below:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'windows_exporter'
    static_configs:
      - targets: ['host.docker.internal:9182']
```

A Prometheus configuration file consists of three main sections: global, rule_files, and scrape_configs.

**Global** - defines settings that apply to the entire Prometheus server. This includes parameters such as the default time interval for scraping targets (scrape_interval), how often rules are evaluated (evaluation_interval), and any external labels that help identify this Prometheus instance in federated setups or alerts. These configurations act as defaults for all jobs unless they are specifically overridden later in the file.

**Rule_files** lists the locations of files containing alerting and recording rules. Alerting rules trigger notifications when certain conditions are met, while recording rules create new time series based on existing metrics for easier querying and analysis.

**Scrape_configs** specifies the targets that Prometheus should monitor. Each job includes information about how to discover the targets, where to scrape metrics from, and any additional processing like relabeling or authentication. This section determines what data Prometheus actually collects.


### Exploring Prometheus browser

> [Prometheus](#Prometheus) > [Content](#content) > [This section](#browser)

Since Prometheus also exposes data about itself as an HTTP endpoint it can scrape and monitor its own health. In the default configuration there is a single job, called prometheus, which scrapes the time series data exposed by the Prometheus server. The job contains a single, statically configured, target, the localhost on port 9090. Prometheus expects metrics to be available on targets on a path of /metrics. So this default job is scraping via the URL: http://localhost:9090/metrics.

The endpoint http://localhost:9090/query allows you to run instant queries in Prometheus. This means you can ask Prometheus for the current metric values or the values at a specific point in time. You send a PromQL (Prometheus Query Language) expression to this endpoint, and it returns the results in JSON format. You can view the results in a table or use the Graph tab to visualize them.

To get CPU usage for user processes over the last  minute we can introduze the code:

````rate(node_cpu_seconds_total{mode="user"}[1m]) ````
<p align="center">
    <img width="85%" align="center" alt="" src="https://github.com/user-attachments/assets/437889bb-ca28-4cb8-8805-1663e6884c15" />
<p >

In the http://localhost:9090/alerts is shows all the alerting rules that are currently loaded into Prometheus. This are define in the rule_files section of the configuration file., Each alerting rule checks some condition based on metric data (using PromQL), When the condition becomes true, the alert fires.

<p align="center">
<img width="85%" alt="" src="https://github.com/user-attachments/assets/2e81cbfe-b9ec-4189-970b-70048c9345a1" />
<p >



