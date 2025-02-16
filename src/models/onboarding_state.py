from typing import TypedDict, List, Optional

class EmployeeState(TypedDict):
    name: str
    role: str
    department: str
    start_date: str
    access_levels: List[str]
    skills: List[str]
    welcome_package: Optional[str]
    training_materials: Optional[str]
    final_package: Optional[str]