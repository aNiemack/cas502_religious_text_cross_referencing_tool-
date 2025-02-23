# cas502_religious_text_cross_referencing_tool-
Team: Andrew Niemack and Joshua Carlin

## Project Description
This tool is for taking databases of words from several different religious texts for the purpose of cross-referencing use of words that are related to one another. This tool will draw on databases of both scriptural and extra-scriptural sources to compare and contrast usage of words to both inform and verify the reliability of the translation. Beyond translational use, it would also help inform any study in comparative religion to see how each culture and language treats similar and different concepts. The code for this project was written to facilitate searching for terms across multiple texts and solves the problem of having to coordinate many different databases in order to research a religion comparatively. While this is still feasible, and not necessarily a problem to be solved, it certainly can make the research easier for any would-be scholars of comparative religion.

## Anticipated Challenges
One of the technical challenges I anticipate is I’m not sure how much access I will have to databases, and how robust those databases might be. Furthermore, trying to balance translational software with dictionary software will likely require a degree of skill with coding that I do not yet have. It may happen that one or the other will have to be developed at some later stage, or one will be very basic and the other will be more fleshed out. The team consists of myself and Andrew Niemack and considering my being an absolute beginner in coding, I will say that there is a challenge in the team composition as a result of the large discrepancy in skills between myself and what the project might call for. Thankfully, this is an idealized theoretical final product, but the product at the end of this course will likely be a very rough prototype of this. Lastly, one challenge regarding the process that would make collaborating difficult in general is that because this works with a large array of languages, it may require collaboration with databases maintained by a diverse enough group of people that it would be difficult to do on one’s own. Beyond that, collaboration within the team itself could be complicated by differences in opinion of how to organize collation of data or even what data to include, as well as what functionalities to implement and in what order.

## Communication Plan
The plan is to talk regularly over slack about each week’s goals and what the assignments will require. When necessary, I would also like to meet over zoom. I assume we will work in a shared space, so we’ll be able to see what the other person is doing with the code. This could change depending on the availability and preferences of anybody I end up working with because of personal communication styles, work styles, or even time zones.

## Branching Strategy
For this project when each team member is working on a particular task or issue they will create a working branch off main for the task where they will do the primary work on that task. In cases where one member's work is dependent on the other teammate they can merge with the other working branch to get the necessary updates. When a task or issue is completed then the team member will create a pull request to merge the working branch back into main. This will allow everyone to review and approve the code before pushing to main.


## running code
Running these commands should start the site

1. python -m pip install -r requirements.txt
2. cd text_cross_reference
3. python manage.py runserver

Then go to localhost:8000 in browser to view.

## Collaboration Documentation
Should any bugs be found or features found to be needed an issue should be generated on GitHub for me to work on. This can include either features or bugs. Related to this, should anyone wish to contribute they can either send a request to merge, or create an issue detailing what they'd like to work on. Should further collaboration be pursued, the owner of the repository will reach out for further information. 

## User Documentation
This code is a word search function that will search textual databases for instances of string inputs. It's output should be one of two things; it will either be a word count or it will return the lines of data that include the string you search for depending on which iteration of the code you run. 

## License
I chose the  GNU GENERAL PUBLIC LICENSE, version 2 because it allowed for public use, but did not grant patent use rights, which is something I did not want on this software. 
