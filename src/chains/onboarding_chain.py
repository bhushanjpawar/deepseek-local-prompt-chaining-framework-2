from typing import Dict
from src.models.onboarding_state import EmployeeState
from src.llm.router_client import LLMRouter

class OnboardingChain:
    """
    Manages the employee onboarding process through a series of LLM calls.
    Handles welcome package, training materials, and final package generation.
    """
    
    def __init__(self, llm_router: LLMRouter):
        """Initialize with LLM router for API communication"""
        self.llm = llm_router

    async def generate_welcome_package(self, state: EmployeeState) -> Dict:
        """
        Generates personalized welcome package for new employee.
        
        Args:
            state: Employee information including name, role, etc.
            
        Returns:
            Dict containing generated welcome package content
        """
        prompt = f"""Create a personalized welcome package for:
        Name: {state['name']}
        Role: {state['role']}
        Department: {state['department']}
        Start Date: {state['start_date']}
        
        Include: Welcome message, first-day schedule, and key contacts."""
        
        response = await self.llm.generate(prompt)
        return {"welcome_package": response["message"]["content"]}

    async def generate_training_materials(self, state: EmployeeState) -> Dict:
        """
        Creates role-specific training materials and learning path.
        
        Args:
            state: Employee information with skills and role details
            
        Returns:
            Dict containing generated training materials
        """
        prompt = f"""Create training materials for:
        Role: {state['role']}
        Skills: {', '.join(state['skills'])}
        Department: {state['department']}
        
        Include: Learning path, required training modules, and skill assessments."""
        
        response = await self.llm.generate(prompt)
        return {"training_materials": response["message"]["content"]}

    async def generate_final_package(self, state: EmployeeState) -> Dict:
        """
        Combines welcome package and training materials into final onboarding document.
        
        Args:
            state: Complete employee state with generated materials
            
        Returns:
            Dict containing final structured onboarding package
        """
        prompt = f"""Create a final onboarding package combining:
        Welcome Package: {state['welcome_package']}
        Training Materials: {state['training_materials']}
        Access Levels: {', '.join(state['access_levels'])}
        
        Format as a structured onboarding plan with timeline."""
        
        response = await self.llm.generate(prompt)
        return {"final_package": response["message"]["content"]}

    def validate_requirements(self, state: EmployeeState) -> str:
        """
        Validates that all required employee information is present.
        
        Args:
            state: Employee state to validate
            
        Returns:
            "Pass" if all required fields present, "Fail" otherwise
        """
        required_fields = ["name", "role", "department", "start_date"]
        if all(state.get(field) for field in required_fields):
            return "Pass"
        return "Fail"