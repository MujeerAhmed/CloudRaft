# CloudRaft

### Assumptions
- You have a K8s environment and deployed a functional nginx-ingress-controller
- If you have a registry then please push the image to the registry and add the name of the registry in manifest file

### Design decisions
- /key/set only accepts POST requests
- /search and /get/<key> accept both GET and POST requests

### Observability
- I would monitor the latency, uptime and performace of the api on uptime kuma
- Setup mail or push notification alerts for incidents of failure

### Testing before deployment
- Use a WSGI server like gunicorn or uwsgi
- Functional testing
