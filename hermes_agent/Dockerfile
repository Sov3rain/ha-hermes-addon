ARG BUILD_VERSION=dev
ARG BUILD_ARCH=amd64
FROM nousresearch/hermes-agent:v0.23.0@sha256:adb7890916de63245523492be8f68f9d2095fecbec4e2a6dab7960381f0fc002

ARG BUILD_VERSION
ARG BUILD_ARCH

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl nginx \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/nginx

ARG TARGETARCH
RUN ARCH=$(echo ${TARGETARCH:-$(dpkg --print-architecture)} | sed 's|arm64|aarch64|;s|amd64|x86_64|') \
    && curl -fsSL "https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.${ARCH}" -o /usr/local/bin/ttyd \
    && chmod +x /usr/local/bin/ttyd

LABEL \
  io.hass.version="${BUILD_VERSION}" \
  io.hass.type="app" \
  io.hass.arch="${BUILD_ARCH}"

ENV HERMES_HOME=/data

COPY fix-web-prefix.py /tmp/fix-web-prefix.py
RUN /opt/hermes/.venv/bin/python /tmp/fix-web-prefix.py

COPY ingress.conf /etc/nginx/nginx.conf
COPY landing.html /usr/share/nginx/html/index.html
COPY services/ /etc/services.d/
COPY run.sh /run.sh
RUN chmod a+x /run.sh /etc/services.d/ha-*/run

ENTRYPOINT ["/run.sh"]
