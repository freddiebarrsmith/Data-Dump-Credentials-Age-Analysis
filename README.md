# Data-Dump-Credentials-Age-Analysis
Takes in data breaches, maybe even grepped down to a specific organisation in the following format.

A .csv file, containing all of the users and passwords in the following format:

username:password
username2:password2
username3:password3
username4:password4

It will then output, after execution, as fast as the 1.5 second api rate limiting will allow:

username:password:2018
username2:password2:2017
username3:password3:2017
username4:password4:2018

The year being the date at which that email address last was recorded to have been subject to a data breach.
