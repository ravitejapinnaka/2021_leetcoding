"""
Ref: https://leetcode.com/problems/subdomain-visit-count/

A website domain like "discuss.leetcode.com" consists of various subdomains.
At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level,
"discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains
 "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
 followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains.
 We would like a list of count-paired domains, (in the same format as the input, and in any order),
  that explicitly counts the number of visits to each subdomain.

Example:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

"""
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    # def subdomainVisits(self, cpdomains):
        freq = {}
        for domain in cpdomains:
            num, dom = domain.split(' ')

            while dom:
                freq[dom] = freq.get(dom, 0) + int(num)
                dom = '.'.join(dom.split('.')[1:])
        print(freq)
        output = [str(value) + ' ' + key for key, value in freq.items()]
        return output

Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])


