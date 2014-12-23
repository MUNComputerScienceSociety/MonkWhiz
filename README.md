# MonkWhiz

A quiz system featuring automatic student evaluation, reporting, and problem generation

## Goal

**From the hackathon ideas list:**

>A lot of first year courses use quiz systems like LON-CAPA and Mastering Chemistry to automate student
>testing and grading either in place of or along with written assignments. Many students do not want to
>have to pay a fee for access to some of these services, but professors do not have the resources to grade
>hundreds of quizes every week. Building a quiz system that could replace such services which allows
>professors to write or generate their own questions is not unlikely to see adoption.

## Implementation

The entirety of this application will be written in 
[Python (version 2.7)](https://wiki.python.org/moin/BeginnersGuide/Programmers), and implemented as a
web application built on the [Flask microframework](http://flask.pocoo.org/).  The application should
primarily provide a quiz interface like that of LON-CAPA or Mastering Chemistry that presents questions,
accepts and evaluates answers, and produces an evaluation.  Another ideal feature for the application is
question and answer generation based on templates.  Professors would likely want to be able to create
their own sets of questions and provide a template from which sample questions can be generated.  This
task may be made easier with the use of libraries such as the symbolic computing library
[SymPy](http://www.sympy.org/en/index.html) and the scientific computing library
[SciPy](http://www.scipy.org/).

## Directory Structure

    MonkWhiz
    ├── app
    |   ├── app.py
    |   ├── static
    |   |   ├── css
    |   |   ├── js
    |   |   └── img
    |   └── templates
    ├── .gitignore
    ├── LICENSE
    └── README.md

The `app` directory contains the code and resources for the application. Clearly, stylesheets
belong in `static/css`, javascript files in `static/js`, and images in `static/img`.
When changes are made to the structure of the application or to the set of instructions required to
execute the application, the `README.md` file should be updated accordingly.

## Execution

To execute the application and start running the service on Flask's built-in web server, navigate to the
`app` directory and execute

    python app.py