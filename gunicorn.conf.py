# Configuração do Gunicorn

# Configurações do servidor
bind = '0.0.0.0:8000'
workers = 4
worker_class = 'sync'
timeout = 120

# Configurações de logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Configuração da aplicação
wsgi_app = 'run:app'

# Configurações de desenvolvimento
reload = True