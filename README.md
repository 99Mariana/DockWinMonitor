# Monitorização de Sistema Windows com Prometheus, Grafana e Docker

<p align="center">
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/a7089567-5cb3-4b66-8c4b-2051ea784b09" />
</p>

Este projeto surge com o principal objetivo de explorar ferramentas com grande relevancia no mundo tecnologico, Prometheus, Grafana e Docker.

* 🟦 **Prometheus** — Ferramenta open source para recolha, armazenamento e consulta de métricas em séries temporais (*time-series database*), muito usada para monitorizar sistemas e aplicações.
* 🟨 **Grafana** — Plataforma de visualização e análise de métricas, que permite construir dashboards interativos para transformar dados em informação visual e útil.
* 🐳 **Docker** — Tecnologia de containerização que simplifica a implementação e gestão de serviços, garantindo portabilidade e facilidade de execução com um único comando.

Neste sentido idealizei um projeto que pudesse combinar stas ferramentas de forma poderosa e relevante e assim surgiu o conceito de criar um projeto que visa implementar um sistema de **monitorização do Windows**. O projeto demonstra de forma prática os conceitos de **observabilidade**, **monitorização de infraestrutura** e **automação de ambientes com containers**.

Através da integração destas três tecnologias, é possível observar em tempo real o desempenho do sistema, utilizando o **Windows Exporter** como fonte de métricas. Windows Exporter (em host.docker.internal:9182), significa que o foco é monitorizar o sistema Windows do host.


## Metricas

Neste projeto foi desenvolvido um dashboard no Grafana que inclui diferentes metricas de desempenho do sistema, desde CPU Usage, Memory Usage, Disk IO, Network Throughput entre outros.

<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

Foram estabelecidas alert rules para diferentes metricas sendo despoletado uma notificação que é recebida no webhook ( https://webhook.site/#!/view/2f7264ff-34ca-4d25-bfea-c60a5e0b8370/ ) sendo este o contact point criado para o efeito. Em cada alert rule, de acordo com o valor obtido no na condição de alerta tem atribuida um nivel de severidade( Critical, Warning, Normal ) na label serevity , a qual é calculada automaticamente. Alert rules com condições complexas foram desenvolvidas como é o caso do: Sistema sobrecarregado, que corresponde a combinação de tres requesitos ( CPU >80% + RAM >85% + Disco >80% ) e o alert rule Leak ou processo zombie
com dois requesitos ( RAM >85% + CPU <30% )

## ⚙️ Tecnologias Utilizadas

* **Docker & Docker Compose** → Containerização e orquestração dos serviços
* **Prometheus** → Recolha e armazenamento de métricas
* **Grafana** → Visualização de métricas e criação de dashboards
* **Windows Exporter** → Ferramenta para expor métricas do sistema Windows
* **Python (WebHook customizado)** → Endpoint adicional (exemplo de integração futura com alertas ou automações)



## 🧩 Arquitetura do Projeto

```plaintext
+---------------------------+
|   Windows Exporter        |
|  (host.docker.internal)   |
|  Porta: 9182              |
+-------------+-------------+
              |
              v
+-------------+-------------+
|          Prometheus        |
|  (Container: prometheus)   |
|  Porta: 9090               |
+-------------+-------------+
              |
              v
+-------------+-------------+
|            Grafana         |
|  (Container: grafana)      |
|  Porta: 3000               |
+-------------+-------------+
              |
              v
+-------------+-------------+
|            Webhook         |
|  (Container: webhook)      |
|  Porta: 5000               |
+----------------------------+
```

---

## 📂 Estrutura de Diretórios

```
/monitoring-windows/
│
├── docker-compose.yml
│
├── prometheus/
│   └── prometheus.yml
│
├── webhook/
│   └── Dockerfile
│   └── app.py
│
└── README.md
```

---

## 🧾 Ficheiros Principais

### 🧱 `docker-compose.yml`

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus:/etc/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    restart: unless-stopped

  grafana:
    image: grafana/grafana:10.4.3
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_FEATURE_TOGGLES_ALERTINGTEMPLATESINLABELSANNOTATIONS=true
    restart: unless-stopped
    depends_on:
      - prometheus

  webhook:
    build: ./webhook
    container_name: webhook
    ports:
      - "5000:5000"

volumes:
  grafana-data:
```

### 📊 `prometheus.yml`

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'windows_exporter'
    static_configs:
      - targets: ['host.docker.internal:9182']
```

👉 Este ficheiro define o **intervalo de recolha (15 segundos)** e o **target** — neste caso, o **Windows Exporter** que corre diretamente no sistema Windows, acessível a partir dos containers através de `host.docker.internal`.

---

## 🚀 Como Executar

### 1. Instalar o Windows Exporter

Descarregar e instalar a ferramenta [windows_exporter](https://github.com/prometheus-community/windows_exporter).
Por padrão, ela expõe as métricas na porta `9182`.

### 2. Clonar o repositório

```bash
git clone https://github.com/teu-utilizador/monitoring-windows.git
cd monitoring-windows
```

### 3. Subir os containers

```bash
docker-compose up -d
```

### 4. Aceder aos serviços

* **Prometheus:** [http://localhost:9090](http://localhost:9090)
* **Grafana:** [http://localhost:3000](http://localhost:3000)

  * *Login padrão:* `admin / admin`
* **Webhook:** [http://localhost:5000](http://localhost:5000)

---

## 📈 Visualização no Grafana

Após iniciar o ambiente:

1. Abrir o Grafana e configurar o **Prometheus como fonte de dados** (`http://prometheus:9090`).
2. Importar um dashboard JSON para visualizar as métricas do Windows Exporter.
3. Explorar gráficos de:

   * CPU Usage
   * Memory Usage
   * Disk IO
   * Network Throughput


*(Podes incluir screenshots ou links para dashboards aqui.)*

---

## 🎯 Objetivos e Relevância

Este projeto demonstra:

* A integração entre **Prometheus**, **Grafana** e **Docker** para criar uma pipeline de monitorização.
* O uso do **Windows Exporter** como fonte de métricas em ambiente Windows.
* A importância da **observabilidade** e da **automação de infraestrutura** para análise de desempenho.
* A possibilidade de estender o sistema com **alertas via webhook**.

É um exemplo prático e educativo de como implementar um **sistema de monitorização moderno e portátil**.

---

## 🔮 Melhorias Futuras

* Adicionar **Prometheus Alertmanager** e integração real com o **Webhook**
* Configurar alertas para CPU, memória e disco
* Criar dashboards customizados no Grafana
* Expandir para monitorizar múltiplos hosts ou containers

---

## 👨‍💻 Autor

**[Teu Nome]**
📎 [teu perfil GitHub](https://github.com/teu-utilizador)
💡 Projeto desenvolvido para explorar ferramentas de monitorização e observabilidade em ambiente Windows.

---

Queres que eu agora personalize este README com o **teu nome** e o **link exato do teu repositório GitHub** (para já poder colar direto no ficheiro `README.md`)?


canal do youtube: https://www.youtube.com/watch?v=h4Sl21AKiDg&list=PLy7NrYWoggjxCF3av5JKwyG7FFF9eLeL4

Udemy:
https://www.udemy.com/course/prometheus-and-grafana-learn-monitoring-alerting-today/?utm_source=bing&utm_medium=udemyads&utm_campaign=BG-Search_DSA_Beta_Prof_la.EN_cc.ROW-English&campaigntype=Search&portfolio=Bing-ROW-English&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&utm_content=deal4584&utm_term=_._ag_1326013411676364_._ad__._kw_IT+en_._de_c_._dm__._pl__._ti_dat-2334675503276564%3Aloc-152_._li_136968_._pd__._&matchtype=b&msclkid=867563032908100915820be5a09e823d&couponCode=PMNVD3025

Parametros windows
<img width="1895" height="894" alt="image" src="https://github.com/user-attachments/assets/3d2b1b87-5b31-4780-84d7-6e1f789130f3" />

