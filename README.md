# amfoss-tasks (Gokul Krishnan G CSE19321)
These are the tasks I was able to complete till now, 14 out of 15.

0. Install Ubuntu 18.04:

  Installing ubuntu was way easier than I thought. I downloaded ubuntu 18.04 and created a bootable usb drive for installing. Then it was just a matter of following the on screen instructions and making partitions. I did run into an error though, the installer was not detecting my hard drive. I got round this by changing the SATA operation mode in the bios from RAID to AHCI.

1. Star all the amFOSS repositories:

  This was pretty straight forward, just had to follow all the instructions in the mentioned repository. Copy the script into the developer console of the browser and run.
  
2. Programming:

  I used python 3 to complete all the questions. I had no prior experience in computer science and I learned python during the first semester of college.
  
3. Google Scraping using Ruby

  Here I used the inspector window of the browser to find the HTML class of the title and url of the search results. Using Nokogiri I parsed two consecutive search results page and displays the first ten results in text format.


5.Get it using javascript:

I designed a basic webpage using html. I went through github's grapql api's documentation and watched several youtube videos to make the queries. I also had to get a personal access token from github so that I can authorize my requests. My webpage shows the usernam, name, bio and avatarlink of the given user, If no person exists it displays an alert box saying no person exists. Also, github has revoked my access token when i uploaded the program.
  
6. CLI App using Go:

  I went through the resources provided with the task and learned more about Go. The idea was to access the Users/show endpoint of the twitter API by sending a GET request. In order to do that I had to apply for a twitter developer account to recieve the consumer keys and access tokens. I used "Twitter API" which is a Go package for accessing version 1.1 of the Twitter API (https://github.com/amit-lulla/twitterapi). There were several resources online explaining the process of writing output to text file in Go.
  
7. Rusted Email:

  The general pattern for e-mail adress is a username followed by an @ symbol followed by domain. I found the regular expression for an e-mail id online ( "[a-z0-9_+]([a-z0-9_+.]*[a-z0-9_+])?)@([a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6}" ) and used the regex crate in rust to validate the input email-id.

8. Captcha Breaking:

  For this task I made a black and white png image with a simple arithmetic expression. The program I wrote is very basic. I used PIL and pytesseract ocr to extract the text from image as a string. I came across the built in eval() function in python which evaluates a string like a python expression and returns the result as an integer.
 
9. Setup a Simple Personal Website:

  I used the repository mentioned in the task and the followed the instructions to set up my website.
 link: https://gokulkrh.github.io/2020/01/04/amfoss-tasks/

10. CS50:

  I watched all the lectures till week 5 and completed the problemsets as much as I could.
  
Additional Tasks

11. A Pong game:

  I found several online tutorials and resources for building the game. I followed this tutorial on youtube (https://www.youtube.com/watch?v=KApAJhkkqkA) and made an offline multiplayer version of it.
 
12. Python Source:

  For this task I first converted the individual hexadecimal values to decimal and checked which ascii value when xored according to the program gives the decimal in the ciphertext. Then I reversed the shift function in the program to extract a list containing the flag. It took me a long time as I did most of the process on paper, I don't know if I'm supposed to do it like this but still I was able to solve the task.
  
13. Project Euler (for math freaks):

  I used python 3 and was able complete all the questions but it showed runtime errors and time limit exceeded errors in some test cases.
  
14. Bandit:
  
  completed bandit till level 10.
