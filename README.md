# Data-Dump-Credentials-Age-Analysis
Takes in data breaches, maybe even grepped down to a specific organisation in the following format.

A .csv file, containing all of the users and passwords in the following format:

username:password
<br>
username2:password2
<br>
username3:password3
<br>
username4:password4
<br>
It will then output, after execution, as fast as the 1.5 second api rate limiting will allow:

username:password:2018
<br>
username2:password2:2017
<br>
username3:password3:2017
<br>
username4:password4:2018
<br>
The year being the date at which that email address last was recorded to have been subject to a data breach.
