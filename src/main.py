# Standard library imports
import asyncio

# Local application imports
from src.config.settings import ollama_config
from src.llm.router_client import LLMRouter
from src.chains.onboarding_chain import OnboardingChain

async def main():
    """
    Main application entry point demonstrating the onboarding chain workflow.
    Handles the complete process of generating onboarding documentation for new employees.
    """
    # Initialize LLM router and onboarding chain components
    router = LLMRouter(ollama_config)  # Router handles communication with the LLM
    chain = OnboardingChain(router)    # Chain manages the sequence of onboarding steps
    
    # Define sample employee data structure with required fields and access information
    employee_data = {
        "name": "Alice Smith",
        "role": "Full Stack Developer",
        "department": "Engineering",
        "start_date": "2024-03-15",
        # List of required system access for the role
        "access_levels": ["github", "jira", "aws", "slack"],
        # Technical skills relevant to the position
        "skills": ["python", "javascript", "react", "docker"]
    }
    
    try:
        print("Starting onboarding process...")
        
        # Validate that all required employee information is present
        if chain.validate_requirements(employee_data) == "Pass":
            # Step 1: Generate initial welcome package with basic information
            print("\n1. Generating welcome package...")
            welcome_result = await chain.generate_welcome_package(employee_data)
            employee_data.update(welcome_result)  # Update state with welcome package
            
            # Step 2: Create role-specific training materials based on skills
            print("\n2. Creating training materials...")
            training_result = await chain.generate_training_materials(employee_data)
            employee_data.update(training_result)  # Update state with training materials
            
            # Step 3: Combine welcome package and training into final document
            print("\n3. Assembling final package...")
            final_result = await chain.generate_final_package(employee_data)
            employee_data.update(final_result)  # Update state with final package
            
            # Output the complete onboarding package
            print("\nFinal Onboarding Package:")
            print("=" * 50)
            print(employee_data["final_package"])
            
        else:
            print("Error: Missing required employee information")
            
    except Exception as e:
        # Handle any errors that occur during the process
        print(f"Error during onboarding process: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    # Run the async main function in the event loop
    asyncio.run(main())