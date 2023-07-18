---
id: wfh4afd5bt53f5avnb9323m
title: CORS
desc: ''
updated: 1668802893555
created: 1668802887088
---

#### Same-origin policy (ONLY FOR BROWSERS)
- Same-origin policy by default applies in browsers, you can only call from origin back to your web server
   - Helps mitigate cross-site scripting attacks
   - There are cases where want to relax this policy. Answer: CORS 

#### Cross origin resource sharing (Browser security feature)
- relaxes security of website or API
- CORS can specify certain origins that are allowed to access the resource/API
- By returning a CORS header in the response headers


### Example:
- `https://websecurity-academy.net:443/some-path`
   > -  https:// -> Scheme
    - websecurity-academy.net -> Domain
    - :443 -> Port
    - /some-path -> Path
- `https://websecurity-academy.net:443/some-other-path`
- Differnet origin if Scheme, Port, or Domain are different

The some orign policy (SoP) prevents a malicious site from reading sensitive data from another site