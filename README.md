## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment support (`venv`)

### Setup Instructions

1. **Get API Keys**

   Obtain API keys from:
   - [OpenAI](https://www.openai.com/)
   - [Exa](https://www.exa.com/)

2. **Add API Keys to `.env`**

   Create a `.env` file in the root directory and add your API keys. You can use the provided `.env.sample` file as a reference:

   ```env
   OPENAI_MODEL_NAME=gpt-4o
   OPENAI_API_KEY=your_openai_api_key
   EXA_API_KEY=your_exa_api_key

   # If using Azure OpenAI
   # USE_AZURE=1
   # AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
   # AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   # AZURE_OPENAI_DEPLOYMENT=your_azure_openai_deployment
   # OPENAI_API_VERSION=2024-02-01
   ```

3. **Create a Virtual Environment**

    Create a virtual environment and activate it:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. **Install Dependencies**

    Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

5. **Run the Application**

    Run the main application:

    ```
    python main.py
    ```


### Additional Notes
Ensure that your `.env` file contains all the necessary keys and configurations.

If you're using Azure OpenAI, uncomment the relevant lines in the `.env` file and fill in your Azure-specific details.

The Agents will write an output report that can be found under `outputs/`.