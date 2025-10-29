# Monitorização de Sistema Windows com Prometheus, Grafana e Docker

<p align="center">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/a7089567-5cb3-4b66-8c4b-2051ea784b09" />
</p>

Este projeto surge com o principal objetivo de explorar ferramentas com grande relevancia no mundo tecnologico, Prometheus, Grafana e Docker. Através da integração destas três tecnologias, é possível observar em tempo real o desempenho do sistema.

* **Prometheus** — Ferramenta open source para recolha, armazenamento e consulta de métricas em séries temporais (*time-series database*), muito usada para monitorizar sistemas e aplicações. 
* **Grafana** — Plataforma de visualização e análise de métricas, que permite construir dashboards interativos para transformar dados em informação visual e útil.
* **Docker** — Tecnologia de containerização que simplifica a implementação e gestão de serviços, garantindo portabilidade e facilidade de execução com um único comando.

Neste sentido idealizei um projeto que pudesse combinar stas ferramentas de forma poderosa e relevante e assim surgiu o conceito de criar um projeto que visa implementar um sistema de **monitorização do Windows**. O projeto demonstra de forma prática os conceitos de **observabilidade**, **monitorização de infraestrutura** e **automação de ambientes com containers**.


## Tecnologias Utilizadas

* **Docker & Docker Compose** → Docker desktop to containerização e orquestração dos serviços. O docker-compose.yml que specifies which images to use , the ports to expose, volumes to mount, networks to connect, environment variables. 
* **Prometheus** → Recolha e armazenamento das métricas dos exporters (ex: Windows Exporter). O Ficheiro prometheus.yml é o ficheiro de configuração principal do Prometheus, definindo quais endpoints o Prometheus deve monitorar, ajustar intervalos de scraping (de quanto em quanto tempo coleta métricas), adiciona rótulos, targets e jobs. Este serviço é acedido por: http://localhost:9090
* **Grafana** → Visualização de métricas, criação de dashboards, alert rules, definição de contact points. Este serviço é acedido por: http://localhost:3000 ( Login padrão: admin / admin )
* **Windows Exporter** → Ferramenta para expor métricas do sistema Windows. utilizando o **Windows Exporter** como fonte de métricas. Windows Exporter (em host.docker.internal:9182), significa que o foco é monitorizar o sistema Windows do host. Descarregar e instalar a ferramenta: https://github.com/prometheus-community/windows_exporter

## Estrutura de Diretórios

```
/monitoring-windows/
│
├── docker-compose.yml
│
├── prometheus/
    └── prometheus.yml
```

## Metricas

Neste projeto foi desenvolvido um dashboard no Grafana que inclui diferentes metricas de desempenho do sistema, desde CPU Usage, Memory Usage, Disk IO, Network Throughput entre outros.

<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

Foram estabelecidas alert rules para diferentes metricas sendo despoletado uma notificação que é recebida no webhook ( https://webhook.site/#!/view/2f7264ff-34ca-4d25-bfea-c60a5e0b8370/ ) sendo este o contact point criado para o efeito. Em cada alert rule, de acordo com o valor obtido no na condição de alerta tem atribuida um nivel de severidade( Critical, Warning, Normal ) na label serevity , a qual é calculada automaticamente. Alert rules com condições complexas foram desenvolvidas como é o caso do: Sistema sobrecarregado, que corresponde a combinação de tres requesitos ( CPU >80% + RAM >85% + Disco >80% ) e o alert rule Leak ou processo zombie
com dois requesitos ( RAM >85% + CPU <30% )




canal do youtube: https://www.youtube.com/watch?v=h4Sl21AKiDg&list=PLy7NrYWoggjxCF3av5JKwyG7FFF9eLeL4

Udemy:
https://www.udemy.com/course/prometheus-and-grafana-learn-monitoring-alerting-today/?utm_source=bing&utm_medium=udemyads&utm_campaign=BG-Search_DSA_Beta_Prof_la.EN_cc.ROW-English&campaigntype=Search&portfolio=Bing-ROW-English&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&utm_content=deal4584&utm_term=_._ag_1326013411676364_._ad__._kw_IT+en_._de_c_._dm__._pl__._ti_dat-2334675503276564%3Aloc-152_._li_136968_._pd__._&matchtype=b&msclkid=867563032908100915820be5a09e823d&couponCode=PMNVD3025

Parametros windows
<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

