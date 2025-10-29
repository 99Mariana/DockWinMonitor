# Windows System Monitoring with Prometheus, Grafana and Docker

<p align="center">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/a7089567-5cb3-4b66-8c4b-2051ea784b09" />
</p>

This project was developed with the main goal of exploring widely used and relevant technologies: Prometheus, Grafana, and Docker, and demonstrating their combined power in a practical and meaningful way. With this goal in mind a have a ideia to integratethese three tools, and develop a project to become possible to monitor Windows system performance in real time, collecting and visualizing key metrics for resource analysis and optimization.

**Prometheus** : An open-source tool for collecting, storing, and querying time-series metrics, widely used for system and application monitoring in production environments.

**Grafana** : A powerful visualization platform that allows the creation of interactive dashboards, turning raw data into actionable insights.

**Docker** : A containerization technology that simplifies service deployment and management, ensuring portability and consistent execution across environments.

This project implements a Windows monitoring system using these technologies in a containerized environment, showcasing practical concepts of observability, infrastructure monitoring. It demonstrates how Prometheus, Grafana, and Docker can be combined to provide a robust and real-time monitoring solution, making it easier to understand system behavior and optimize resources efficiently.

In short, this project is designed to highlight the relevance and power of modern monitoring tools while providing a hands-on example of how containerized solutions can enhance system management and operational efficiency.

## Technologies Used

* **Docker & Docker Compose**:
    * Used for containerization and orchestration via *Docker Desktop*.
    * The `docker-compose.yml` file defines images, exposed ports, volumes, networks, and environment variables.

* **Prometheus**:
    * Responsible for collecting and storing metrics from exporters (e.g., Windows Exporter).
    * The `prometheus.yml` file specifies endpoints, scrape intervals, jobs, targets, and alert rules.
    * Access: **[http://localhost:9090](http://localhost:9090)**

* **Grafana**:
     * Used for metric visualization, dashboard creation, and alert rule management.
     * Access: **[http://localhost:3000](http://localhost:3000)**
     * Default login: `admin / admin`

* **Windows Exporter**:
     * Exposes system metrics from Windows (CPU, memory, disk, network, etc.).
     * Runs on the host and is accessed from containers via `host.docker.internal:9182`.
     * [Download Windows Exporter](https://github.com/prometheus-community/windows_exporter)

* **External Webhook Contact Point (Webhook.site)**:
     * A *Contact Point* was created in Grafana to send alerts to Webhook.site, an online webhook testing service.
     * This endpoint : **[https://webhook.site/#!/view/2f7264ff-34ca-4d25-bfea-c60a5e0b8370/](https://webhook.site/#!/view/2f7264ff-34ca-4d25-bfea-c60a5e0b8370/)**: was used to validate the correct delivery of alerts and verify their structure and formatting when received externally.
  
* **Webhook Service (Flask-based)**:
     * A custom webhook built with Flask, located in the `webhook` directory, created to test how alert messages could be received as formatted text.
     * This component includes:
          * a `Dockerfile` used to containerize the Flask webhook server, and
          * a `webhook_server.py` file responsible for handling incoming alert messages.

     * A custom alert message template was also created in Grafana and linked to this webhook through a dedicated Contact Point.
     * This setup allows alerts to be received by the Flask webhook (`webhook-flask`) in plain text, providing a readable and testable alert format.


## Project Structure

```
/monitoring-windows/
│
├── docker-compose.yml
│
├── prometheus/
│   └── prometheus.yml
|
└── webhook/
    ├── Dockerfile
    └── webhook_server.py

```

## Metrics and Dashboards

A dashboard was created to provide real-time visualization of key Windows system metrics, enabling easy monitoring and analysis of important performance indicators, including:

* **CPU Usage**
* **Memory Usage**
* **Disk I/O**
* **Network Throughput**
* **Active Processes**

<img width="80%"  alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

The dashboard allows users to quickly detect system bottlenecks, track resource usage, and gain actionable insights for infrastructure optimization and performance management.


**Alert Rules**

Custom alert rules were created in Grafana( Grafana-managed alert rules ), triggering automatic notifications to configured contact points, such as Webhook.site or a Flask webhook.
Several alerts were implemented, including: **CPU Utilization**, **RAM Utilization**, **Disk Utilization**, **Overloaded System**, and **Memory Leak/Zombie Process**. 

<img width="80%" alt="image" src="https://github.com/user-attachments/assets/04bbbcf1-f350-460f-b18a-df791ed770cc" />

For alert rules where the alert condition is based on a threshold, **severity levels** were defined using the **severity label**:

* 🟥 **Critical**
* 🟧 **Warning**
* 🟩 **Normal**

The label value is automatically assigned based on the value of the condition:
<img width="50%" height="346" alt="image" src="https://github.com/user-attachments/assets/719375e6-4061-4945-82a3-329d34cb03a6" /> 
<img width="80%" height="733" alt="image" src="https://github.com/user-attachments/assets/dd30c7a4-6328-4ba2-80ba-0b1237d54b91" />

**Complex alert rules** were also developed, that are the case of:
  * **Overloaded System** alert triggers when three conditions are met simultaneously (**CPU > 80%**, **RAM > 85%**, and **Disk > 80%**)
  * **Memory Leak/Zombie Process** alert triggers when two conditions are met (**RAM > 85%** and **CPU < 30%**).

canal do youtube: https://www.youtube.com/watch?v=h4Sl21AKiDg&list=PLy7NrYWoggjxCF3av5JKwyG7FFF9eLeL4

Udemy:
https://www.udemy.com/course/prometheus-and-grafana-learn-monitoring-alerting-today/?utm_source=bing&utm_medium=udemyads&utm_campaign=BG-Search_DSA_Beta_Prof_la.EN_cc.ROW-English&campaigntype=Search&portfolio=Bing-ROW-English&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&utm_content=deal4584&utm_term=_._ag_1326013411676364_._ad__._kw_IT+en_._de_c_._dm__._pl__._ti_dat-2334675503276564%3Aloc-152_._li_136968_._pd__._&matchtype=b&msclkid=867563032908100915820be5a09e823d&couponCode=PMNVD3025

Parametros windows
<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

