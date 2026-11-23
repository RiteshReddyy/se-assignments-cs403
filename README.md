# Software Engineering Labs

Ritesh Babu Reddy · PES2UG24CS403 · Section 5G

| Lab | Assignment | Report |
| --- | --- | --- |
| 1 | Digital gift card and loyalty point exchange requirements | [PDF](Lab-1/PES2UG24CS403_Lab1_Report.pdf) |
| 2 | Agile backlog and two simulated sprints | [PDF](Lab-2/PES2UG24CS403_Lab2_Report.pdf) |
| 3 | Gift card exchange architecture | [PDF](Lab-3/PES2UG24CS403_Lab3_Report.pdf) |
| 4 | Pac-Man repair and feature implementation | [PDF](Lab-4/PES2UG24CS403_Lab4_Report.pdf) |
| 5 | Static analysis of a movie review board | [PDF](Lab-5/PES2UG24CS403_Lab5_Report.pdf) |
| 6 | Statement and branch coverage of a spam scorer | [PDF](Lab-6/PES2UG24CS403_Lab6_Report.pdf) |
| 7 | Property-based testing of message and address helpers | [PDF](Lab-7/PES2UG24CS403_Lab7_Report.pdf) |

## Lab evidence

Lab 1 includes the editable requirements table and use-case flow. Peer critique remains pending.

Lab 2 includes three epics, six stories, two closed sprints and screenshots from Jira. The report explains the difference between the second sprint's board estimates and its burndown chart. Open Reports and select either sprint for the instructor demonstration. [WALLET burndown charts](https://se-assignments-cs403.atlassian.net/jira/software/c/projects/WALLET/boards/2/reports/burndown-chart)

Lab 4 includes two ten-second game recordings and the [full four-turn programming conversation](Lab-4/Chat%20history.md). Install the dependencies in that folder and run `python game.py`. Use the arrow keys to move and R to restart.

For Labs 5–7, use Python 3.12. From the selected lab folder, install its dependencies with `python -m pip install -r requirements.txt`. Run `python movie_reviews.py` in Lab 5. In Lab 6, run `python -m coverage run --branch --source=spam_scoring -m pytest -q` followed by `python -m coverage report -m`. In Lab 7, run `python -m pytest --hypothesis-seed=403 -q`.
