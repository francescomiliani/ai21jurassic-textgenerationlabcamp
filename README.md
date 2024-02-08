# ai21jurassic-textgenerationlabcamp

AI21 Jurassic 2 LLM in Text Generation Labcamp

## Setup

### 1. Virtual Enviroment creation

1. **Open a terminal or command prompt:**
   - On Windows, you can use Command Prompt or PowerShell.
   - On macOS or Linux, you can use the terminal.

2. **Navigate to your project directory:**
   ```bash
   cd path/to/your/project
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
   This command uses the `venv` module to create a virtual environment named "venv" in your project directory. Replace `python` with `python3` on some systems.

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

   Once activated, your terminal prompt will change to indicate that you are now working within the virtual environment.

5. **Install packages as needed:**
   Now you can use `pip` to install Python packages, and they will be isolated within your virtual environment.
   ```bash
   pip install package_name
   ```

6. **Deactivate the virtual environment:**
   When you're done working in the virtual environment, you can deactivate it.
   ```bash
   deactivate
   ```

### 2. Packages installation

Run the following command to install all packages needed:
```bash
pip install -r requirements.txt
```

### 3. API KEY and go!

1. Rename the file `.env.example` to `.env`
2. Place inside the API KEY got from AI21 Studio website.
3. Run the code
```bash
python main.py
```

### Examples

#### 1. Tokenization (token counting)

Example of output: 'some text' => 2

#### 2. Chat completion

Example of input: 'What are my favorite'
Example of output: 'books?'

#### 3. Chat

Example of input: 'These are a few of my favorite'
Example of output: '1. "The Shawshank Redemption"
2. "The Godfather"
3. "The Dark Knight"
4. "Goodfellas"
5. "The Lord of the Rings: The Return of the King"
6. "Schindler's List"
7. "The Prestige"
8. "The Dark Knight"
9. "The Matrix"
10. "Fight Club"'
