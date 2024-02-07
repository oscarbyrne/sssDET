
# BL SDET Tech Test

## Background

There are two parts to this exercise. First we want to test your manual QA abilities. Second, we want to test your automation skills. Please commit (and push) your responses to this test into the git repository we have shared with yu. 


## Part 1 - QA Scenarios


1. Write a test case for successfully sending an email in Gmail.

Document your test case in a file called testcase1.txt. Commit (and push)  this file to this git repo.


2. Consider the following screenshot. Write a bug report for the exception that occurs on the Login page during the login process. 

Screenshot: https://www.evernote.com/shard/s365/sh/d01105e9-699d-94d2-149a-7c5deff79348/RMQlTCliUgVP6pjFwgQL5Ug5tkRKZFwiYVDDeP4W_hWdRL8gc1QrjR-QuQ

Write your bug report in a text document called bugreport1.txt. Include all important information. Commit (and push) this file to this git repo.


3. Consider the following video. What potential issues (if any) do you see with this password reset scenario?

Video: https://drive.google.com/file/d/1hhjKcmv0RDUJNLNXST2FPxXBKYVJBG-7/view?pli=1

The scenario includes steps to specifying a wrong email address, getting the “reset password” email for the correct email address, trying to change password to the one that’s used previously, and successfully setting a new password.

Write the summary of any issues you see in text document called issues1.txt. Commit (and push) this file to this git repo.


## Part 2 - Programming Exercise

Using the demonstration application found here: https://github.com/juice-shop/juice-shop, we want you to demonstrate how you would setup a test automation framework to test this site. To get started, follow the instructions at the bottom of this link to get the application running locally. We recommend using the instructions for Docker, but you are free to follow alternate instructions. Once you have it running, we want you to write an automated test using Playwright + Python (or alternative testing framework that is Python based) to perform the following test scenario:

1. Log in
2. Add a carrot juice to your basket
3. Verify that the item is in your basket
4. Remove item from your basked
5. Verify that item is removed from basket
6. Log out

Please create a screen recording of your automation test in action and include this in your submission.

When you have this working, commit (and push) your files you created and instructions on how to run your test to a directory called testapp in this git repo.


## Check

At the end of this, you should have committed (and pushed) the following to the git repo we shared with you:

testcase1.txt
bugreport1.txt
issues1.txt
testapp\ -- directory for your test automation scripts including screen recording


## Tech Interview

In the techincal interview, be prepared to discuss your responses and solution to the programming exercise.
