# 0x18. Webstack monitoring

This project involves using Datadog to measure what's going on with my server.

## Resources

* [Configuring NGINX Logging](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
* [Why monitor servers](http://www.monitance.com/en/product-news/what-is-server-monitoring-and-why-is-it-important/)
* [Application Performance Management](https://en.wikipedia.org/wiki/Application_performance_management)
* [How to get Sumo Logic Access Keys](https://help.sumologic.com/Manage/Security/Access-Keys)
* [Google SRE book - Monitoring Distributed Systems](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html)

## Tasks :page_with_curl

* **0. Sign up for Datadog and install datadog-agent**
  * [Datadog](https://www.datadoghq.com/): Signed up, installed `datadog-agent` on my server.
  * Created `application key`

* **1. Monitor some metrics**
  System metrics were setup using using [System Check](https://docs.datadoghq.com/integrations/system/)
  * Setup system metrics to monitor  the number of read requests issued to the device per second.
  * Setup system metrics to monitor  the number of write requests issued to the device per second.

* **2. Create a dashboard**
  * Created a new dashboard on Datadog
  * Added 4 widgets to the dashboard
  * retrieved `dashboard_id` using [Datadog's API](https://docs.datadoghq.com/api/latest/dashboards/?code-lang=curl). The id can be found at [2-setup_datadog](./2-setup_datadog)
