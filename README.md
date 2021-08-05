# Instagram Follows Scrapper

*DISCLAIMER This script is for academic purposes only, run this script on your own responsibility*

The main motivation for this script is to get a list of relationships between users and who they follow to make a data visualization. 

Using selenium as a way to automatize Chrome browser, we achieve to use recursion to get the followed users of a single user, given a nested limit for the max number of recursion allowed.

Also, we store the obtained data on disk using shelve, so if the script fails, the script will rerun with cached values.