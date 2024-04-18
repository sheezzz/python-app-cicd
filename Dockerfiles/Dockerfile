# final stage
ARG BASE_IMAGE
FROM $BASE_IMAGE

WORKDIR /api

COPY . /api

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5000

CMD ["python", "-u", "app.py"]
