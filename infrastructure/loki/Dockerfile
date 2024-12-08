FROM grafana/loki:2.7.1

USER root  

RUN mkdir -p /var/loki/chunks && \
    mkdir -p /var/loki/index && \
    mkdir -p /var/loki/cache && \
    chown -R 10001:10001 /var/loki

USER 10001:10001 
