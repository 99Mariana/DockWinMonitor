from flask import Flask, request
import json
import re

app = Flask(__name__)

@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        return "Webhook Flask ativo! Use POST com JSON para alertas.", 200

    # Recebe JSON do Grafana
    data = request.get_json()
    if not data:
        return "No JSON received", 400

    print("=== JSON recebido do Grafana ===")
    print(json.dumps(data, indent=2))

    alerts = data.get("alerts", [])
    message_lines = [f"{len(alerts)} alerta(s) recebido(s)\n"]

    for alert in alerts:
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})
        values = alert.get("values", {})

        summary = annotations.get("summary", "Sem resumo")
        description = annotations.get("description", "Sem descrição")
        status = alert.get("status", "Sem status")
        alertname = labels.get("alertname", "Sem nome")
        instance = labels.get("instance", "Sem instância")

        # --- Substituir placeholders Grafana nos textos ---
        def substituir_variaveis(texto):
            # Substitui {{ index $labels "X" }}
            texto = re.sub(
                r'\{\{\s*index\s*\$labels\s*"([^"]+)"\s*\}\}',
                lambda m: str(labels.get(m.group(1), f"<sem {m.group(1)}>")),
                texto,
            )
            # Substitui {{ index $values "A" }}
            texto = re.sub(
                r'\{\{\s*index\s*\$values\s*"([^"]+)"\s*\}\}',
                lambda m: str(values.get(m.group(1), f"<sem {m.group(1)}>")),
                texto,
            )
            return texto

        summary_real = substituir_variaveis(summary)
        description_real = substituir_variaveis(description)

        message_lines.append(f"Alerta: {alertname}")
        message_lines.append(f"Instância: {instance}")
        message_lines.append(f"Status: {status}")
        message_lines.append(f"Resumo: {summary_real}")
        message_lines.append(f"Descrição: {description_real}")
        message_lines.append("-" * 60)

    message_text = "\n".join(message_lines)
    print(message_text)

    return {"message": message_text}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




