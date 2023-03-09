# Resume and Cover Letter Generator

This project is a software development project that utilizes web scraping, machine learning APIs, and HTML templates to generate a resume and cover letter based on a job posting. The purpose of this project is to automate the process of job application by generating a personalized resume and cover letter in a matter of seconds.

## Table of Contents

- [Resume and Cover Letter Generator](#resume-and-cover-letter-generator)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)

## Installation

1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Create a `.env.local` file and add the following variables:
   ```
   API_KEY=<your_api_key>
   ```
   Note: You will need to obtain an API key from the machine learning API provider.
4. Run `python main.py` to start the application.

## Usage

This project is currently limited to a command line tool. The program is controlled by a number of flags.

- `-h` or `--help`: Displays the help menu.
- `-o` or `--output`: Determines if files will be output.
- `-v` or `--verbose`: Determines if the program will print the output.
- `-r` or `--resume`: Determines if a resume will be generated.
- `-l` or `--letter`: Determines if a cover letter will be generated.
- `-p` or `--posting`: Determines if a job posting will be generated.

## Details

This application makes use of a number of core modules (resume, coverletter, posting) to generate a full job application for the user.
It is currently also dependant on a data file which should be stored in data/data.json. The data should have the format:

```json
{
    "resume": {
        "name": "your_name",
        "email": "your_email",
        "website": "your_website",
        "address": "your_address"
    },
    "projects": [
        {
            "title": "MyHealth",
            "description": "Full stack personal health records management application. Vue front end, FastAPI (Python) backend, postgres database, deployed on linux server using Docker containers. Features: login with OAuth2.0, REST API, CI/CD."
        },
    ],
    "skills": {
        "ci/cd": 0.4,
        "docker": 0.6,
        "fastapi": 0.2,
        "git": 0.6,
    },
    "skills_relatedness": {
        "ci/cd": {
            "docker": 0.7,
            "git": 0.8,
            "github": 0.8
        },
        "docker": {
            "ci/cd": 0.7
        },
        "git": {
            "github": 0.2,
        },
    }
}
```

### Posting Module

The Posting class takes some posting name and the job description text. It is used to generate the resume and cover letter.

### Resume Module

The Resume class uses the BeautifulSoup package to generate an HTML representation of the resume.

## Contributing

Contributions are always welcome! If you have any ideas or suggestions, please create a pull request.

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->
