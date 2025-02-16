# Employee Onboarding Chain Framework

A powerful framework for automating employee onboarding documentation using local LLM models through Ollama. This framework generates personalized onboarding packages, training materials, and comprehensive documentation while maintaining data privacy.

## Features

- 🚀 Automated Onboarding Document Generation
- 📚 Personalized Training Materials
- 🔄 Multi-step Processing Chain
- 🔒 Local Processing with Ollama
- ⚡ Async Processing Support
- 🎯 Role-specific Content Generation

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- DeepSeek-r1:7b model pulled via Ollama

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bhushanjpawar/deepseek-local-prompt-chaining-framework-2.git
cd deepseek-local-prompt-chaining-framework-2

python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate

pip install -e .

MODEL_NAME=deepseek-r1:7b
OLLAMA_BASE_URL=http://localhost:11434

from src.config.settings import ollama_config
from src.llm.router_client import LLMRouter
from src.chains.onboarding_chain import OnboardingChain

# Initialize components
router = LLMRouter(ollama_config)
chain = OnboardingChain(router)

# Define employee data
employee_data = {
    "name": "John Doe",
    "role": "Software Engineer",
    "department": "Engineering",
    "start_date": "2024-03-15",
    "access_levels": ["github", "jira"],
    "skills": ["python", "javascript"]
}

# Generate onboarding package
await chain.generate_welcome_package(employee_data)

deepseek-local-prompt-chaining-framework-2/
├── src/
│   ├── chains/           # Chain implementations
│   ├── config/           # Configuration management
│   ├── llm/             # LLM integration
│   ├── models/          # Data models
│   └── main.py          # Application entry point
├── tests/               # Test suite
├── .env                 # Environment variables
├── setup.py            # Package setup
└── README.md           # Documentation

## Output Format

The framework generates a structured onboarding document with the following layout:

```plaintext
### Onboarding Plan for [Employee Name]: [Role] Journey

#### 1. Welcome Package
- Personalized Welcome Message
- First-Day Schedule (Timeline)
- Key Contacts and Resources

#### 2. Training Materials
- Role-specific Learning Path
- Required Skills Development
- Assessment Milestones
- Resources and Documentation

#### 3. Final Package
##### Day 1: Arrival & Onboarding
- Morning Schedule
- Afternoon Activities
- Setup Requirements

##### Phase 1: Initial Training (Week 1-2)
- Core Skills Development
- Tool Familiarization
- Initial Assessments

##### Phase 2: Role-Specific Training (Week 3-4)
- Advanced Topics
- Project Introduction
- Team Integration

##### Access and Resources
- System Access Levels
- Documentation Links
- Support Contacts
- Learning Resources
```
## Contributing
1. Fork the repository
2. Create your feature branch ( git checkout -b feature/AmazingFeature )
3. Commit your changes ( git commit -m 'Add some AmazingFeature' )
4. Push to the branch ( git push origin feature/AmazingFeature )
5. Open a Pull Request
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For issues and feature requests, please create an issue in the GitHub repository.

