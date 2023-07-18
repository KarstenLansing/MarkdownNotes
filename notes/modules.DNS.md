---
id: ss8bxpot0dy27btxxfklp7p
title: DNS
desc: ''
updated: 1668803026067
created: 1668803021618
---

~Domain Name System~ (DNS) is a hierarchical distributed naming system for computers, services, or any resource connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying ~Internet Protocol~ (IP) network. By providing a worldwide, distributed directory service, the Domain Name System is an essential component of the functionality of the ~Internet~.

- Resolves domain names to IP addresses
- When you type in a domain name, your browser sends a DNS request to a DNS server (resolver server) to find that domain name in their database and return the IP address of the domain name.
    - 13 sets of these roots servers strategically placed around the world.
    - Operated by 12 different organizations.
    - Each set has thier own unique IP address.
    - Works like a phone book
- In DNS database, a domain name is mapped or joined with an I.P address.
- Must (should) be a static IP address.
- It could take up to 24 hours to update the DNS database for a domain name to be mapped to a new IP address.
- DNS is used with static IP addresses

### Process of the DNS Lookup Process (DNS Resolution)
  > 1. If the resolver server cant find the corresponding IP address, it will ask the root server (top of the DNS hierarchy).
2. **Catch 1** The root server doesn't know IP address, but it will direct the resolver server to ask the TLD server (top level domain server) of that '.com/edu/org' etc. domain name.
3. **Catch 2** (if it doesn't know) The TLD server will direct the resolver server to ask the authoritative name server of that domain name.
    - The authoritative name server is the last authority and will respond with the IP address of the domain name.
4. The resolver server will return the IP address to the browser.
5. The resolver server stores the queried domain name and its corresponding IP address in its cache for a certain period of time (usually 24 hours) so that it can answer the same request without asking the root server again.



## DDNS (Dynamic DNS)
- Dynamic DNS is used with dynamic IP addresses.
- Dynamic IP addresses are assigned by a DHCP server, the IP changes periodically.
- DDNS allows you to access devices on your network from the internet even if your IP address changes (homes)
> 1.  Custom hostname created with DDNS is mapped to your dynamic IP address.
  2. DNS updates and maps it to your custom hostname every time your IP address changes.
