traces:
  otlp:
    http:
      enabled: true
    grpc:
      enabled: true

storage:
  trace:
    backend: azure
    azure:
      container_name: tempo
      storage_account_name: stdstoragelog01
      storage_account_key: ${STORAGE_ACCOUNT_ACCESS_KEY}

distributor:
  extraArgs:
  - "-config.expand-env=true"
  extraEnv:
  - name: STORAGE_ACCOUNT_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: stdstoragelog01-access-key
        key: accountKey

compactor:
  extraArgs:
  - "-config.expand-env=true"
  extraEnv:
  - name: STORAGE_ACCOUNT_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: stdstoragelog01-access-key
        key: accountKey

ingester:
  extraArgs:
  - "-config.expand-env=true"
  extraEnv:
  - name: STORAGE_ACCOUNT_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: stdstoragelog01-access-key
        key: accountKey

querier:
  extraArgs:
  - "-config.expand-env=true"
  extraEnv:
  - name: STORAGE_ACCOUNT_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: stdstoragelog01-access-key
        key: accountKey

queryFrontend:
  extraArgs:
  - "-config.expand-env=true"
  extraEnv:
  - name: STORAGE_ACCOUNT_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: stdstoragelog01-access-key
        key: accountKey

metaMonitoring:
  serviceMonitor:
    enabled: true
    labels:
      prometheus: system
