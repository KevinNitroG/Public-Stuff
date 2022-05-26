### Cloudflare Workers Reverse Proxy

   **alternating use of different dynos to bypass Heroku's 550-hour monthly limit for non-credit card verified account**

- Need to deploy two dynos via two Heroku accounts with the same variable settings
- Log in to your cloudflare account
- Click Workers in the left navigation bar and select Create a Service
- After creating the service, click Quick Edit
- Paste the following code into editor

 ```
const SingleDay = 'cloud1.herokuapp.com'
const DoubleDay = 'cloud2.herokuapp.com'
const timezone = 'Etc/GMT+2'; 

addEventListener(
    "fetch",event => { 

        let localized_date = new Date(new Date().toLocaleString('en-US', { timeZone: timezone }));
        if (localized_date.getDate()%2) {
            host = SingleDay
        } else {
            host = DoubleDay
        }

        let url=new URL(event.request.url);
        url.hostname=host;
        let request=new Request(url,event.request);
        event. respondWith(
            fetch(request)
        )
    }
)
```

- Fill in Heroku dyno domain names at line 1 & 2. Set timezone at line 3 to control time of switching dyno, ranging from Etc/GMT-12 to Etc/GMT+12.
- Click Save and Deploy.
