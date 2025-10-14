# [Prometheus](#prometheus)

## [Content](#content)

- [Prometheus](Prometheus.md):
    - [Introduction](#introduction)
    - [Architecture](#architecture)
    - [Configuration](#configuration)


### Introduction
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#introduction)

Prometheus is an open-source systems monitoring and alerting toolkit designed for reliability and scalability. It helps you collect and analyze metrics from various systems and applications to understand their performance and health.

Prometheus collects and stores its metrics as time series data, meaning each metric is recorded along with the timestamp of when it was captured. Additionally, metrics can include **labels**—optional key-value pairs that provide more context, such as the source, service, or instance of the data.

In simple terms, Prometheus lets you track how systems behave over time and trigger alerts when something goes wrong, making it a powerful tool for monitoring modern infrastructure.

### Architecture
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#Architecture)

As shown on the official website, the architecture of Prometheus and some of its ecosystem components is illustrated below:

<img width="80%" alt="image" src="https://github.com/user-attachments/assets/fb0c34ea-c913-4aae-8e93-9c9ad552117d" />

In this image, we can see the Prometheus server, which is responsible for scraping and storing time series data. It also shows the client libraries used to instrument application code, the Pushgateway that supports short-lived jobs, and various exporters designed for specific services such as HAProxy, StatsD, and Graphite. Additionally, it includes the Alertmanager, which manages alerts, and several supporting tools.

These components work together to form the Prometheus ecosystem: the server continuously collects metrics from different sources, the exporters expose metrics from third-party systems, and the Alertmanager handles notifications based on alerting rules. This architecture enables Prometheus to provide a flexible, reliable, and scalable monitoring solution for dynamic and distributed environments.

### Configuration
> [Prometheus](#Prometheus) > [Content](#content) > [This section](#Configuration)

A Prometheus configuration file consists of three main sections: global, rule_files, and scrape_configs.

**Global** - defines settings that apply to the entire Prometheus server. This includes parameters such as the default time interval for scraping targets (scrape_interval), how often rules are evaluated (evaluation_interval), and any external labels that help identify this Prometheus instance in federated setups or alerts. These configurations act as defaults for all jobs unless they are specifically overridden later in the file.

**Rule_files** lists the locations of files containing alerting and recording rules. Alerting rules trigger notifications when certain conditions are met, while recording rules create new time series based on existing metrics for easier querying and analysis.

**Scrape_configs** specifies the targets that Prometheus should monitor. Each job includes information about how to discover the targets, where to scrape metrics from, and any additional processing like relabeling or authentication. This section determines what data Prometheus actually collects.

Since Prometheus also exposes data about itself as an HTTP endpoint it can scrape and monitor its own health. In the default configuration there is a single job, called prometheus, which scrapes the time series data exposed by the Prometheus server. The job contains a single, statically configured, target, the localhost on port 9090. Prometheus expects metrics to be available on targets on a path of /metrics. So this default job is scraping via the URL: http://localhost:9090/metrics.

https://prometheus.io/docs/introduction/first_steps/


