# QA Automation Exercise

## Preparation:

1. Create a new Gmail user or use an existing user for this exercise
2. Install/configure a test automation tool such as Selenium, Cypress or equivalent

## Exercise 1: New Email

Write a script that performs the following automated test:

1) Log in to Gmail
2) Compose and send a new email to the same user logged in
3) When the new email arrives, move it to a newly created folder called "test1". Be sure to account for a delay in case Gmail is slow for some reason.
4) Delete the folder "test1"
5) Log out of Gmail

Note: The test can be initiated manually from the command line or testing IDE but should execute without human 
interaction. If the test ran a million times would you run out of space in your gmail account? (We do not recommend 
you run it a million times, although you should be able to now that your test is automated!)

Submit a screen recording (video) of the test operating, along with your code.

## Exercise 2: Labels

What is the difference between a label and a folder in Gmail?

Can you find an example somewhere in Gmail where the UI for labels starts to break down when the nesting is more than 
4 or 5 levels deep? What have the Gmail developers done to accommodate that situation?

* Create a nested label 'test1/test2/test3'.
* Describe the first list entry in the 'Label as:' dialog for an email that already has the label test1/test2/test3.
* Describe the resulting behaviour when you select 'test1/test2' in the 'Label as:' dialog for an email that already has the label test1/test2/test3?

## Exercise 3: Personal Story

Explain a real-life situation that you recently found yourself in where you stopped yourself and questioned 
'the quality of that'. 

For example, you make a pizza and quickly cut it into 6 pieces. You find yourself asking if you cut it fairly by 
starting to calculate the volume of each piece for each millimetre off with your cuts. Then you shake your head, 
return to reality, and make a mental note to cut pizza into 8 pieces next time because you can do it more accurately :)

## Bonus question

Why do you think pizza is usually round?

## Anything Web Can Improve?

Let us know if you think we can improve anything in this exercise!