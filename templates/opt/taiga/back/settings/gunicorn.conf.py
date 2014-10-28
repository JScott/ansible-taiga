bind = "0.0.0.0:8001"
workers = 3
timeout = 60
pidfile = "{{ taiga_back_pidfile_path }}"
accesslog = "{{ taiga_back_access_log_path }}"
errorlog = "{{ taiga_back_error_log_path }}"
loglevel = 'info'
