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

## Contributing

Contributions are always welcome! If you have any ideas or suggestions, please create a pull request.

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->
