#!/bin/bash
# REQUISITO: Generar Dockerfile dinámicamente
cat <<EOF > Dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install shodan
COPY app.py .
CMD ["python", "app.py"]
EOF

# REQUISITO: Construir y ejecutar
podman build -t shodan-image .
podman run --rm --name shodan-container -e SHODAN_API_KEY=\${SHODAN_API_KEY} shodan-image
