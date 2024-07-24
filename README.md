## requestReflector

Very simple Python Flask app that just reflects the request it receives, and that's pretty much all it does. Intended to assist with debugging other web related tools and utilities when the use of a proxy is not an option.

```
$ docker build -t requestreflector .
$ docker run -p 1234:1234 requestreflector
```

Live version at https://requestreflector.evilpony.win/
